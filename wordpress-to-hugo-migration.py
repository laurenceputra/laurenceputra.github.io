#!/usr/bin/env python3
"""
WordPress to Hugo Migration Script for laurenceputra.github.io

This script parses WordPress WXR (XML export) files and converts posts/pages
to Hugo-compatible markdown files with proper front matter.

Usage:
    python3 wordpress-to-hugo-migration.py <wordpress-export.xml>

Output:
    - Migrated content in migrated-content/
    - Migration report in migration-report.md
"""

import xml.etree.ElementTree as ET
import html
import re
import os
import sys
from datetime import datetime
from pathlib import Path
from urllib.parse import urlparse
import html2text

# WordPress XML namespace
WP_NS = {
    'content': 'http://purl.org/rss/1.0/modules/content/',
    'wp': 'http://wordpress.org/export/1.2/',
    'dc': 'http://purl.org/dc/elements/1.1/',
    'excerpt': 'http://wordpress.org/export/1.2/excerpt/'
}

class WordPressToHugoMigrator:
    def __init__(self, xml_file):
        self.xml_file = xml_file
        self.tree = ET.parse(xml_file)
        self.root = self.tree.getroot()
        self.channel = self.root.find('channel')
        
        # Statistics
        self.stats = {
            'posts': 0,
            'pages': 0,
            'media': 0,
            'drafts': 0,
            'skipped': 0
        }
        
        # Issues log
        self.issues = []
        
        # Output directories
        self.output_base = Path('migrated-content')
        self.posts_dir = self.output_base / 'posts'
        self.pages_dir = self.output_base / 'pages'
        self.awards_dir = self.output_base / 'awards'
        self.media_dir = self.output_base / 'media-posts'
        
        # Create directories
        for directory in [self.posts_dir, self.pages_dir, self.awards_dir, self.media_dir]:
            directory.mkdir(parents=True, exist_ok=True)
        
        # HTML to Markdown converter
        self.html_converter = html2text.HTML2Text()
        self.html_converter.body_width = 0  # Don't wrap lines
        self.html_converter.ignore_links = False
        self.html_converter.ignore_images = False
        self.html_converter.ignore_emphasis = False
        
    def get_text(self, element, path, namespaces=None):
        """Safely get text from XML element"""
        found = element.find(path, namespaces or {})
        return found.text if found is not None and found.text else ''
    
    def parse_post_meta(self, item):
        """Extract WordPress post meta (custom fields)"""
        meta = {}
        for postmeta in item.findall('wp:postmeta', WP_NS):
            key = self.get_text(postmeta, 'wp:meta_key', WP_NS)
            value = self.get_text(postmeta, 'wp:meta_value', WP_NS)
            if key and value:
                meta[key] = value
        return meta
    
    def extract_categories_tags(self, item):
        """Extract categories and tags from post"""
        categories = []
        tags = []
        
        for category in item.findall('category'):
            domain = category.get('domain', '')
            nicename = category.get('nicename', '')
            text = category.text or ''
            
            if domain == 'category':
                categories.append(text)
            elif domain == 'post_tag':
                tags.append(text)
        
        return categories, tags
    
    def convert_shortcodes(self, content):
        """Convert WordPress shortcodes to Hugo equivalents or mark for manual review"""
        issues = []
        
        # YouTube shortcode: [youtube URL] or [embed]URL[/embed]
        def replace_youtube(match):
            video_id = match.group(1)
            # Extract video ID from URL if needed
            if 'youtube.com' in video_id or 'youtu.be' in video_id:
                yt_match = re.search(r'(?:v=|youtu\.be/)([a-zA-Z0-9_-]{11})', video_id)
                if yt_match:
                    video_id = yt_match.group(1)
            return f'{{{{< youtube {video_id} >}}}}'
        
        # Extract video ID directly from YouTube shortcode
        content = re.sub(r'\[youtube\s+(?:https?://)?(?:www\.)?(?:youtube\.com/watch\?v=|youtu\.be/)([a-zA-Z0-9_-]+)\]', replace_youtube, content)
        # Extract video ID from embed shortcode (group 2 is the video ID)
        content = re.sub(r'\[embed\](https?://(?:www\.)?(?:youtube\.com/watch\?v=|youtu\.be/)([a-zA-Z0-9_-]+))\[/embed\]', lambda m: f'{{{{< youtube {m.group(2)} >}}}}', content)
        
        # Gallery shortcode - mark for manual review
        if '[gallery' in content:
            issues.append('Contains [gallery] shortcode - needs manual conversion')
            content = re.sub(r'\[gallery[^\]]*\]', '\n\n<!-- TODO: Convert gallery shortcode - see migration report -->\n\n', content)
        
        # Caption shortcode - convert to figure
        def replace_caption(match):
            caption_content = match.group(1)
            # Extract image URL and caption text
            img_match = re.search(r'<img[^>]+src="([^"]+)"[^>]*>', caption_content)
            caption_match = re.search(r'\](.+)$', caption_content)
            
            if img_match:
                img_url = img_match.group(1)
                caption = caption_match.group(1) if caption_match else ''
                return f'![{caption}]({img_url})'
            return match.group(0)
        
        content = re.sub(r'\[caption[^\]]*\](.*?)\[/caption\]', replace_caption, content, flags=re.DOTALL)
        
        # Check for remaining shortcodes
        remaining_shortcodes = re.findall(r'\[(\w+)[^\]]*\]', content)
        for shortcode in set(remaining_shortcodes):
            if shortcode not in ['youtube', 'embed', 'gallery', 'caption']:
                issues.append(f'Contains [{shortcode}] shortcode - needs manual conversion')
        
        return content, issues
    
    def convert_html_to_markdown(self, html_content):
        """Convert HTML content to Markdown"""
        if not html_content:
            return ''
        
        # Decode HTML entities
        html_content = html.unescape(html_content)
        
        # Convert to markdown
        markdown = self.html_converter.handle(html_content)
        
        # Clean up excessive newlines
        markdown = re.sub(r'\n{3,}', '\n\n', markdown)
        
        return markdown.strip()
    
    def determine_section(self, item, categories):
        """Determine which Hugo section this post belongs to"""
        post_type = self.get_text(item, 'wp:post_type', WP_NS)
        title_lower = self.get_text(item, 'title').lower()
        
        # Check categories
        categories_lower = [c.lower() for c in categories]
        
        if 'award' in categories_lower or 'awards' in title_lower:
            return 'awards'
        elif 'media' in categories_lower or 'press' in categories_lower or 'interview' in title_lower:
            return 'media-posts'
        elif post_type == 'page':
            return 'pages'
        else:
            return 'posts'
    
    def create_slug(self, title):
        """Create URL-friendly slug from title"""
        slug = title.lower()
        slug = re.sub(r'[^a-z0-9\s-]', '', slug)
        slug = re.sub(r'\s+', '-', slug)
        slug = re.sub(r'-+', '-', slug)
        return slug.strip('-')
    
    def format_date(self, date_string):
        """Convert WordPress date to ISO 8601 format"""
        try:
            # WordPress format: 2020-10-16 18:58:00
            dt = datetime.strptime(date_string, '%Y-%m-%d %H:%M:%S')
            return dt.strftime('%Y-%m-%dT%H:%M:%SZ')
        except:
            return date_string
    
    def migrate_item(self, item):
        """Migrate a single WordPress item (post/page)"""
        # Extract basic info
        title = self.get_text(item, 'title')
        post_type = self.get_text(item, 'wp:post_type', WP_NS)
        status = self.get_text(item, 'wp:status', WP_NS)
        post_date = self.get_text(item, 'wp:post_date', WP_NS)
        post_name = self.get_text(item, 'wp:post_name', WP_NS)
        author = self.get_text(item, 'dc:creator', WP_NS)
        
        # Skip attachments, revisions, nav_menu_items
        if post_type in ['attachment', 'revision', 'nav_menu_item']:
            self.stats['skipped'] += 1
            return
        
        # Skip posts without titles
        if not title:
            self.stats['skipped'] += 1
            return
        
        # Extract content
        content_html = self.get_text(item, 'content:encoded', WP_NS)
        excerpt_html = self.get_text(item, 'excerpt:encoded', WP_NS)
        
        # Extract categories and tags
        categories, tags = self.extract_categories_tags(item)
        
        # Extract post meta
        post_meta = self.parse_post_meta(item)
        
        # Determine section
        section = self.determine_section(item, categories)
        
        # Convert HTML to Markdown
        content_md = self.convert_html_to_markdown(content_html)
        
        # Convert shortcodes
        content_md, shortcode_issues = self.convert_shortcodes(content_md)
        
        # Create slug
        slug = post_name if post_name else self.create_slug(title)
        
        # Format date
        formatted_date = self.format_date(post_date)
        
        # Build front matter
        front_matter = {
            'title': title,
            'date': formatted_date,
            'author': author or 'laurence',
        }
        
        # Add categories if present
        if categories:
            front_matter['categories'] = categories
        
        # Add tags if present
        if tags:
            front_matter['tags'] = tags
        
        # Add draft status
        if status == 'draft':
            front_matter['draft'] = True
            self.stats['drafts'] += 1
        else:
            front_matter['draft'] = False
        
        # Add SEO metadata from Yoast if present
        if '_yoast_wpseo_metadesc' in post_meta:
            front_matter['description'] = post_meta['_yoast_wpseo_metadesc']
        
        if '_yoast_wpseo_focuskw' in post_meta:
            front_matter['yoast_focus_keyword'] = post_meta['_yoast_wpseo_focuskw']
        
        # Build markdown file
        markdown_content = '---\n'
        for key, value in front_matter.items():
            if isinstance(value, list):
                markdown_content += f'{key}:\n'
                for item_val in value:
                    markdown_content += f'  - "{item_val}"\n'
            elif isinstance(value, bool):
                markdown_content += f'{key}: {str(value).lower()}\n'
            else:
                # Escape quotes in string values
                value_str = str(value).replace('"', '\\"')
                markdown_content += f'{key}: "{value_str}"\n'
        markdown_content += '---\n\n'
        markdown_content += content_md
        
        # Determine output directory
        if section == 'awards':
            output_dir = self.awards_dir
        elif section == 'media-posts':
            output_dir = self.media_dir
        elif section == 'pages':
            output_dir = self.pages_dir
        else:
            output_dir = self.posts_dir
        
        # Write file
        output_file = output_dir / f'{slug}.md'
        output_file.write_text(markdown_content, encoding='utf-8')
        
        # Update statistics
        if post_type == 'page':
            self.stats['pages'] += 1
        else:
            self.stats['posts'] += 1
        
        # Log issues
        if shortcode_issues:
            for issue in shortcode_issues:
                self.issues.append(f'Post: "{title}" ({slug}.md) - {issue}')
        
        print(f'✓ Migrated: {title} → {section}/{slug}.md')
    
    def migrate(self):
        """Main migration function"""
        print(f'\n=== WordPress to Hugo Migration ===')
        print(f'Input file: {self.xml_file}\n')
        
        # Find all items
        items = self.channel.findall('item')
        print(f'Found {len(items)} items in WordPress export\n')
        
        # Migrate each item
        for item in items:
            try:
                self.migrate_item(item)
            except Exception as e:
                title = self.get_text(item, 'title')
                print(f'✗ Error migrating: {title} - {str(e)}')
                self.issues.append(f'Post: "{title}" - Migration error: {str(e)}')
        
        # Generate migration report
        self.generate_report()
        
        print(f'\n=== Migration Complete ===')
        print(f'Posts migrated: {self.stats["posts"]}')
        print(f'Pages migrated: {self.stats["pages"]}')
        print(f'Drafts: {self.stats["drafts"]}')
        print(f'Skipped: {self.stats["skipped"]}')
        print(f'Issues logged: {len(self.issues)}')
        print(f'\nOutput directory: {self.output_base}')
        print(f'Migration report: migration-report.md\n')
    
    def generate_report(self):
        """Generate comprehensive migration report"""
        report = f"""# WordPress to Hugo Migration Report

**Migration Date:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**Source File:** {self.xml_file}

## Migration Summary

- **Total Posts Converted:** {self.stats['posts']}
- **Total Pages Converted:** {self.stats['pages']}
- **Draft Posts:** {self.stats['drafts']}
- **Items Skipped:** {self.stats['skipped']} (attachments, revisions, nav items)
- **Issues Logged:** {len(self.issues)}

## Output Structure

```
migrated-content/
├── posts/          # Blog posts ({self.stats['posts']} files)
├── pages/          # Static pages ({self.stats['pages']} files)
├── awards/         # Awards section posts
└── media-posts/    # Media section posts
```

## Issues & Manual Review Required

"""
        if self.issues:
            for issue in self.issues:
                report += f'- {issue}\n'
        else:
            report += 'No issues found during migration.\n'
        
        report += """

## Next Steps

### 1. Review Migrated Content

Review all migrated files in `migrated-content/` directory:
- Check front matter accuracy
- Verify content formatting
- Review shortcode conversions
- Check image references

### 2. Move Content to Hugo Site

```bash
# Copy posts
cp -r migrated-content/posts/* content/posts/

# Copy pages
cp -r migrated-content/pages/* content/pages/

# Copy awards
cp -r migrated-content/awards/* content/awards/

# Copy media posts
cp -r migrated-content/media-posts/* content/media/
```

### 3. Download and Organize Images

WordPress images are typically at paths like:
- `/wp-content/uploads/YYYY/MM/filename.jpg`

You should:
1. Download images from WordPress site
2. Organize in Hugo's `/static/img/` directory
3. Update image paths in markdown files

Example image path conversion:
```
Before: /wp-content/uploads/2023/01/photo.jpg
After:  /img/photo.jpg
```

Use find/replace across all migrated files:
```bash
find migrated-content -name "*.md" -exec sed -i 's|/wp-content/uploads/[0-9]*/[0-9]*/|/img/|g' {} +
```

### 4. Set Up Redirects (Optional)

If your WordPress URLs differ from Hugo URLs, set up 301 redirects.

For Netlify, create `_redirects` file in `/static/`:
```
/old-wordpress-path  /new-hugo-path  301
```

For GitHub Pages with Jekyll, use `_config.yml` or HTML meta redirects.

### 5. Test Hugo Build

```bash
hugo server -D
```

Visit http://localhost:1313 and verify:
- All posts display correctly
- Images load properly
- Categories and tags work
- Shortcodes render correctly

### 6. Deploy

Once satisfied with migration:
```bash
hugo
# Deploy /public/ directory to hosting
```

## Common Issues and Solutions

### Shortcode Conversions

WordPress shortcodes that were marked for manual review:
- **[gallery]**: Convert to Hugo figure shortcodes or custom gallery partial
- **[caption]**: Already converted to markdown image syntax
- **Custom shortcodes**: Create Hugo equivalents in `/layouts/shortcodes/`

### Image Paths

All image references should be updated to match Hugo's static directory structure:
- WordPress: `/wp-content/uploads/2023/01/image.jpg`
- Hugo: `/img/image.jpg` or `/img/posts/post-name/image.jpg`

### Internal Links

Update internal links to match Hugo's URL structure:
- WordPress: `https://laurenceputra.com/2023/01/15/post-title/`
- Hugo: `/2023/01/15/post-title/` (configured in hugo.toml permalinks)

### Categories and Tags

- Categories are preserved in front matter
- Tags are preserved in front matter
- Hugo will automatically create taxonomy pages

## Migration Quality Checklist

- [ ] All posts extracted from WordPress XML
- [ ] Front matter complete (title, date, author, categories, tags)
- [ ] Dates in ISO 8601 format
- [ ] Categories/tags mapped correctly
- [ ] HTML converted to Markdown
- [ ] Shortcodes converted or marked for review
- [ ] SEO metadata preserved (descriptions, focus keywords)
- [ ] Draft status preserved
- [ ] Content readable and properly formatted

## Contact

For issues with this migration, review the specific error messages above and consult:
- Hugo documentation: https://gohugo.io/documentation/
- WordPress to Hugo migration guide: https://gohugo.io/tools/migrations/
"""
        
        # Write report
        report_file = Path('migration-report.md')
        report_file.write_text(report, encoding='utf-8')
        print(f'\n✓ Generated migration report: {report_file}')


def main():
    if len(sys.argv) < 2:
        print('Usage: python3 wordpress-to-hugo-migration.py <wordpress-export.xml>')
        print('\nExample:')
        print('  python3 wordpress-to-hugo-migration.py laurenceputra.WordPress.2026-01-01.xml')
        sys.exit(1)
    
    xml_file = sys.argv[1]
    
    if not os.path.exists(xml_file):
        print(f'Error: File not found: {xml_file}')
        sys.exit(1)
    
    try:
        migrator = WordPressToHugoMigrator(xml_file)
        migrator.migrate()
    except Exception as e:
        print(f'\nError during migration: {str(e)}')
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
