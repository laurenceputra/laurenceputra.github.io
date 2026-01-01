# WordPress to Hugo Migration Guide
## Laurence Putra Franslay Personal Website

This guide provides comprehensive instructions for migrating content from WordPress to Hugo for laurenceputra.github.io.

---

## Table of Contents

1. [Overview](#overview)
2. [Prerequisites](#prerequisites)
3. [Migration Methods](#migration-methods)
4. [Automated Migration (Recommended)](#automated-migration-recommended)
5. [Manual Migration](#manual-migration)
6. [Image Migration](#image-migration)
7. [Post-Migration Tasks](#post-migration-tasks)
8. [Troubleshooting](#troubleshooting)

---

## Overview

**Current Status:**
- WordPress site: https://laurenceputra.com
- Hugo site (in development): https://laurenceputra.github.io
- Current Hugo content: 4 awards posts, 5 media posts

**Migration Goals:**
- Convert all WordPress posts to Hugo markdown format
- Preserve WordPress permalinks (already configured in `hugo.toml`)
- Maintain SEO metadata and taxonomy (categories/tags)
- Download and organize images appropriately
- Create redirect mappings if needed

---

## Prerequisites

### Required
- Access to WordPress admin dashboard at https://laurenceputra.com/wp-admin
- Python 3.6+ installed (for automated migration script)
- Hugo installed locally
- Git installed

### Optional
- `wget` or `curl` for downloading images
- Image optimization tools (ImageMagick, `imageoptim-cli`)

---

## Migration Methods

You have two options for migration:

| Method | Pros | Cons | Recommended For |
|--------|------|------|----------------|
| **Automated** | Fast, consistent, handles bulk conversion | Requires WordPress export file | Sites with 10+ posts |
| **Manual** | Full control, works without export file | Time-consuming, error-prone | Sites with <10 posts or export unavailable |

---

## Automated Migration (Recommended)

### Step 1: Export WordPress Content

1. **Log in to WordPress admin**: https://laurenceputra.com/wp-admin
2. **Navigate to**: Tools → Export
3. **Select**: "All content" (or choose specific post types)
4. **Click**: "Download Export File"
5. **Save**: The XML file (e.g., `laurenceputra.WordPress.2026-01-01.xml`)

**Alternative Export Method (if admin access unavailable):**
- Use WordPress WP All Export plugin (if installed)
- Contact hosting provider for database backup
- Use WordPress REST API (if enabled and accessible)

### Step 2: Install Python Dependencies

```bash
# Navigate to repository
cd /path/to/laurenceputra.github.io

# Install required Python packages
pip3 install html2text

# Or use requirements file (if created)
echo "html2text==2020.1.16" > requirements.txt
pip3 install -r requirements.txt
```

### Step 3: Run Migration Script

```bash
# Run the migration script
python3 wordpress-to-hugo-migration.py laurenceputra.WordPress.2026-01-01.xml
```

**Expected Output:**
```
=== WordPress to Hugo Migration ===
Input file: laurenceputra.WordPress.2026-01-01.xml

Found 50 items in WordPress export

✓ Migrated: People of Good Award → awards/people-of-good-award.md
✓ Migrated: PayPal Newsroom Feature → media-posts/paypal-newsroom-feature.md
✓ Migrated: My First Blog Post → posts/my-first-blog-post.md
...

=== Migration Complete ===
Posts migrated: 35
Pages migrated: 10
Drafts: 3
Skipped: 2
Issues logged: 5

Output directory: migrated-content
Migration report: migration-report.md
```

### Step 4: Review Migration Report

```bash
# Read the migration report
cat migration-report.md
```

The report includes:
- **Migration statistics**: Number of posts/pages converted
- **Issues log**: Shortcodes needing manual conversion, broken links, etc.
- **Next steps**: Specific actions needed for your content

### Step 5: Review Migrated Content

```bash
# List migrated posts
ls -la migrated-content/posts/

# Review a sample post
cat migrated-content/posts/sample-post.md
```

**Check for:**
- ✅ Front matter accuracy (title, date, categories, tags)
- ✅ Content formatting (headings, lists, emphasis)
- ✅ Image references (paths may need updating)
- ✅ Shortcode conversions (YouTube, galleries, etc.)
- ✅ Internal links (should use relative paths)

### Step 6: Move Content to Hugo Site

```bash
# Create necessary directories if they don't exist
mkdir -p content/posts content/pages

# Copy migrated content
cp -r migrated-content/posts/* content/posts/
cp -r migrated-content/pages/* content/pages/
cp -r migrated-content/awards/* content/awards/
cp -r migrated-content/media-posts/* content/media/

# Verify copy
ls -la content/posts/
ls -la content/awards/
```

### Step 7: Test Hugo Build

```bash
# Build and serve Hugo site
hugo server -D

# Open in browser
# http://localhost:1313
```

**Verify:**
- All posts display correctly
- Navigation works
- Categories and tags generate properly
- No build errors in terminal

---

## Manual Migration

Use this method if the WordPress export file is unavailable or for selectively migrating specific posts.

### Method 1: Copy from WordPress Admin

1. **Log in** to WordPress admin
2. **Navigate** to Posts → All Posts
3. **For each post:**
   - Click "Edit"
   - Switch to "Text" (HTML) editor mode
   - Copy the content
   - Note the metadata (date, categories, tags)
   - Create a new markdown file in Hugo

**Hugo File Template:**
```markdown
---
title: "Post Title from WordPress"
date: 2023-06-15T10:30:00Z
author: "laurence"
categories:
  - "Category Name"
tags:
  - "tag1"
  - "tag2"
draft: false
---

[Content goes here - convert HTML to Markdown]
```

### Method 2: Scrape from Live Site

Since https://laurenceputra.com is behind Cloudflare protection, scraping requires:

**Option A: Disable Cloudflare temporarily**
1. Log in to Cloudflare dashboard
2. Temporarily disable "I'm Under Attack" mode
3. Run scraping script
4. Re-enable protection

**Option B: Use WordPress REST API (if available)**
```bash
# Check if REST API is available
curl https://laurenceputra.com/wp-json/wp/v2/posts

# If successful, you can fetch posts programmatically
```

**Option C: Manual copy-paste**
1. Visit each post on live site
2. Copy content manually
3. Convert HTML to Markdown using tool like Pandoc

```bash
# Convert HTML to Markdown using Pandoc
echo '<h1>My Post</h1><p>Content here</p>' | pandoc -f html -t markdown
```

### Method 3: Database Export (if database access available)

If you have database access:

```sql
-- Export posts from WordPress database
SELECT 
    post_title,
    post_content,
    post_date,
    post_name,
    post_status
FROM wp_posts
WHERE post_type = 'post' 
  AND post_status = 'publish'
ORDER BY post_date DESC;
```

Then convert each row to Hugo markdown format.

---

## Image Migration

WordPress images need to be downloaded and organized in Hugo's static directory.

### Step 1: Identify Image Paths

WordPress typically stores images at:
```
https://laurenceputra.com/wp-content/uploads/YYYY/MM/filename.jpg
```

Hugo should store images at:
```
/static/img/filename.jpg  (accessible as /img/filename.jpg in markdown)
```

Or organized by section:
```
/static/img/awards/filename.jpg
/static/img/media/filename.jpg
/static/img/posts/filename.jpg
```

### Step 2: Download Images

**Option A: Manual Download (Small Number of Images)**
1. Visit WordPress Media Library
2. Download images individually
3. Organize in `/static/img/` directory

**Option B: Automated Download (Many Images)**

Create a script to download all images:

```bash
#!/bin/bash
# download-wordpress-images.sh

# Create image directories
mkdir -p static/img/awards static/img/media static/img/posts

# Extract image URLs from migrated content
grep -ohr 'https://laurenceputra.com/wp-content/uploads/[^)]*' migrated-content/ | sort -u > wordpress-images.txt

# Download each image
while IFS= read -r url; do
    filename=$(basename "$url")
    wget -q "$url" -O "static/img/$filename"
    echo "Downloaded: $filename"
done < wordpress-images.txt

echo "Image download complete"
```

Run the script:
```bash
chmod +x download-wordpress-images.sh
./download-wordpress-images.sh
```

**Option C: Use WordPress Plugin**

Install a plugin like "Export Media Library" to download all images as a zip file.

### Step 3: Update Image Paths in Markdown

Update all image references in migrated content:

```bash
# Replace WordPress image paths with Hugo paths
find content -name "*.md" -type f -exec sed -i 's|https://laurenceputra.com/wp-content/uploads/[0-9]*/[0-9]*/|/img/|g' {} +

# Or preserve year/month structure
find content -name "*.md" -type f -exec sed -i 's|https://laurenceputra.com/wp-content/uploads/|/img/|g' {} +
```

### Step 4: Optimize Images (Optional)

Reduce image sizes for better performance:

```bash
# Using ImageMagick
find static/img -name "*.jpg" -exec mogrify -resize 1920x1920\> -quality 85 {} \;
find static/img -name "*.png" -exec mogrify -resize 1920x1920\> {} \;

# Using imageoptim-cli (macOS)
imageoptim --imagealpha --jpeg-mini static/img/**/*
```

---

## Post-Migration Tasks

### 1. Update Internal Links

WordPress internal links need updating:

```bash
# Replace WordPress domain with relative paths
find content -name "*.md" -type f -exec sed -i 's|https://laurenceputra.com/|/|g' {} +
```

### 2. Convert Remaining Shortcodes

Check migration report for shortcodes needing manual conversion.

**Common Conversions:**

**YouTube:**
```
WordPress: [youtube https://www.youtube.com/watch?v=VIDEO_ID]
Hugo:      {{< youtube VIDEO_ID >}}
```

**Gallery:**
```
WordPress: [gallery ids="1,2,3"]
Hugo:      Create custom gallery shortcode or use multiple images
```

### 3. Verify Permalinks

Hugo is configured to match WordPress URL structure:

```toml
# In hugo.toml
[permalinks]
  posts = "/:year/:month/:day/:slug/"
```

Test that URLs match:
- WordPress: `https://laurenceputra.com/2020/10/16/people-of-good-award/`
- Hugo: `https://laurenceputra.github.io/2020/10/16/people-of-good-award/`

### 4. Set Up Redirects (if needed)

If any URLs change, create redirects:

**For Netlify** (create `/static/_redirects`):
```
/old-path  /new-path  301
```

**For GitHub Pages** (create HTML redirect pages):
```html
<!DOCTYPE html>
<meta charset="utf-8">
<title>Redirecting...</title>
<meta http-equiv="refresh" content="0; URL=/new-path">
<link rel="canonical" href="/new-path">
```

### 5. Test Everything

```bash
# Clean build
hugo --cleanDestinationDir

# Serve locally
hugo server

# Check for:
# - All posts load
# - Images display correctly
# - Categories and tags work
# - Internal links work
# - Shortcodes render properly
# - No 404 errors
```

### 6. Update Search Engines

After deployment, update search engines:

```bash
# Generate sitemap (Hugo does this automatically)
hugo

# Submit to Google Search Console
# Submit to Bing Webmaster Tools
```

---

## Troubleshooting

### Issue: Migration Script Fails

**Error: "ModuleNotFoundError: No module named 'html2text'"**
```bash
pip3 install html2text
```

**Error: "xml.etree.ElementTree.ParseError: not well-formed"**
- WordPress export file is corrupted
- Re-export from WordPress
- Try opening in text editor to check for issues

### Issue: Images Don't Load

**Check:**
1. Image files exist in `/static/img/` directory
2. Image paths in markdown are correct (start with `/img/`)
3. Filenames match exactly (case-sensitive)

**Fix:**
```bash
# List images in static directory
find static/img -type f

# Check image references in content
grep -r "!\[" content/

# Update paths if needed
find content -name "*.md" -exec sed -i 's|/old-path/|/img/|g' {} +
```

### Issue: Shortcodes Not Rendering

**Hugo shortcodes require specific syntax:**
```
Correct:   {{< youtube VIDEO_ID >}}
Incorrect: {{ youtube VIDEO_ID }}
Incorrect: {< youtube VIDEO_ID >}
```

**Check Hugo version:**
```bash
hugo version
# Should be v0.80.0 or higher for modern shortcodes
```

### Issue: Categories/Tags Not Working

**Verify hugo.toml has taxonomies configured:**
```toml
[taxonomies]
  category = "categories"
  tag = "tags"
```

**Check front matter format:**
```yaml
categories:
  - "Tech"
  - "Awards"
tags:
  - "hugo"
  - "wordpress"
```

### Issue: Dates Display Incorrectly

**Use ISO 8601 format in front matter:**
```yaml
date: 2023-06-15T10:30:00Z  # Correct
date: 15 Jun 2023           # Incorrect
```

### Issue: Build Errors

**Common errors:**

1. **"Error building site: failed to render pages"**
   - Check for syntax errors in markdown files
   - Look for unclosed shortcodes

2. **"Error: Unable to locate template"**
   - Theme not installed correctly
   - Template file missing in theme

3. **"Error: failed to parse front matter"**
   - YAML syntax error (indentation, quotes)
   - Missing `---` delimiters

**Debug tips:**
```bash
# Verbose build output
hugo -v

# Show warnings
hugo --log --verboseLog

# Build specific file to isolate issue
hugo --source . --destination public --contentDir content/posts/
```

---

## Migration Checklist

Use this checklist to track migration progress:

### Pre-Migration
- [ ] WordPress admin access confirmed
- [ ] WordPress export file obtained (or alternative method chosen)
- [ ] Python and dependencies installed
- [ ] Hugo site structure understood
- [ ] Backup current Hugo content

### Migration
- [ ] Migration script executed successfully
- [ ] Migration report reviewed
- [ ] All posts migrated (count verified)
- [ ] All pages migrated (count verified)
- [ ] Front matter validated on sample posts
- [ ] Content formatting looks correct

### Image Migration
- [ ] Image URLs identified
- [ ] Images downloaded from WordPress
- [ ] Images organized in `/static/img/`
- [ ] Image paths updated in markdown files
- [ ] Images optimized for web
- [ ] All images loading correctly in browser

### Content Review
- [ ] Shortcodes converted or marked for manual review
- [ ] Internal links updated
- [ ] Categories and tags preserved
- [ ] Author attribution correct
- [ ] Draft status preserved where appropriate
- [ ] SEO metadata preserved

### Testing
- [ ] Hugo build completes without errors
- [ ] Local server runs successfully
- [ ] All posts display correctly
- [ ] Images load properly
- [ ] Navigation works
- [ ] Categories and tags generate pages
- [ ] Search functionality works (if enabled)
- [ ] Responsive design verified on mobile

### Deployment
- [ ] Final build completed
- [ ] Redirects configured (if needed)
- [ ] Deployed to GitHub Pages
- [ ] DNS updated (if applicable)
- [ ] SSL certificate active
- [ ] Sitemap submitted to search engines

### Post-Deployment
- [ ] Verify live site matches local
- [ ] Check for 404 errors
- [ ] Test from multiple devices
- [ ] Monitor search console for issues
- [ ] Update social media links
- [ ] Archive or redirect old WordPress site

---

## Additional Resources

### Hugo Documentation
- Official Docs: https://gohugo.io/documentation/
- Migration Guide: https://gohugo.io/tools/migrations/
- Shortcodes: https://gohugo.io/content-management/shortcodes/
- Permalinks: https://gohugo.io/content-management/urls/

### WordPress Export
- Export Guide: https://wordpress.org/support/article/tools-export-screen/
- WXR Format: https://wordpress.org/support/article/tools-export-screen/#export-file-format

### Tools
- Pandoc (HTML to Markdown): https://pandoc.org/
- html2text (Python): https://pypi.org/project/html2text/
- ImageMagick (Image Optimization): https://imagemagick.org/

### Similar Migrations
- Jekyll to Hugo: https://gohugo.io/tools/migrations/#jekyll
- WordPress to Hugo Blog Posts: https://gohugo.io/tools/migrations/#wordpress

---

## Support

If you encounter issues during migration:

1. **Check this guide** for troubleshooting tips
2. **Review migration report** for specific issues with your content
3. **Consult Hugo documentation** for Hugo-specific questions
4. **Ask Hugo community** at https://discourse.gohugo.io/

---

## Migration Timeline Estimate

| Task | Time Estimate |
|------|---------------|
| Obtain WordPress export | 5-10 minutes |
| Install dependencies | 5 minutes |
| Run migration script | 5-15 minutes (depends on content volume) |
| Review migrated content | 30-60 minutes |
| Download and organize images | 30-90 minutes |
| Update image paths | 15-30 minutes |
| Convert remaining shortcodes | 30-60 minutes |
| Test Hugo build | 15-30 minutes |
| Final review and fixes | 60-120 minutes |
| **Total** | **3-6 hours** |

*Timeline assumes 30-50 posts with moderate complexity*

---

**Last Updated:** 2026-01-01
**Script Version:** 1.0
**Hugo Version:** v0.80.0+
