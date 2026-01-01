# Quick Start Guide: Adding Content to Your Hugo Site

## Adding a New Award

1. **Create the markdown file** in `content/awards/`:
   ```bash
   hugo new awards/my-new-award.md
   ```

2. **Edit the front matter**:
   ```yaml
   ---
   title: "My Amazing Award"
   date: 2025-06-15T10:00:00Z
   author: "laurence"
   categories:
     - "Awards"
   tags:
     - "awards"
     - "technology"
     - "leadership"
   featured_image: "/img/awards/my-award.jpg"  # Optional
   ---
   ```

3. **Write your content** in markdown below the front matter:
   ```markdown
   I'm honored to receive this award for...
   
   ![Award ceremony photo](/img/awards/ceremony.jpg)
   
   ## Background
   This award recognizes...
   ```

4. **Save and preview**:
   ```bash
   hugo server -D
   # Visit http://localhost:1313/awards/
   ```

5. **The award automatically appears as a card** on the `/awards/` page!

## Adding a New Media Mention

1. **Create the markdown file** in `content/media/`:
   ```bash
   hugo new media/my-media-feature.md
   ```

2. **Edit the front matter**:
   ```yaml
   ---
   title: "Featured in Tech Magazine"
   date: 2025-06-20T14:30:00Z
   author: "laurence"
   categories:
     - "Media"
   tags:
     - "video"          # Use "video" for video content
     - "technology"
     - "interview"
   outlet: "Tech Magazine"  # Optional: Publication name
   external_link: "https://example.com/article"  # Optional: Link to original
   featured_image: "/img/media/tech-mag.jpg"  # Optional
   ---
   ```

3. **Add content**:
   ```markdown
   {{< youtube VIDEO_ID_HERE >}}  # For YouTube videos
   
   Link to article: <https://example.com/my-article>
   
   ## Summary
   In this interview, I discussed...
   ```

4. **Save and preview**:
   ```bash
   hugo server -D
   # Visit http://localhost:1313/media/
   ```

5. **The media mention automatically appears as a card** on the `/media/` page!

## Front Matter Reference

### Required Fields
```yaml
title: "Your Title Here"        # REQUIRED
date: 2025-01-15T10:00:00Z      # REQUIRED (ISO 8601 format)
```

### Optional Fields
```yaml
author: "laurence"              # Author name
categories:                      # Section categories
  - "Awards"                    # or "Media"
tags:                            # Tags for filtering
  - "awards"
  - "technology"
  - "social"
  - "video"                     # For video content
  - "youtube"                   # For YouTube videos
featured_image: "/img/path.jpg"  # Card thumbnail
outlet: "Publication Name"       # Media outlet (media only)
external_link: "https://..."    # Link to original article (media only)
```

## Media Type Detection

The media cards automatically detect the type based on tags:
- **Video**: If tags include "video" or "youtube" → Red video badge with play icon
- **Article**: Otherwise → Green article badge with chart icon

## Image Management

### Adding Images to Posts

1. **Place image in static directory**:
   ```
   /static/img/awards/my-photo.jpg
   /static/img/media/screenshot.png
   ```

2. **Reference in markdown**:
   ```markdown
   ![Alt text description](/img/awards/my-photo.jpg)
   ```

3. **Set as featured image** (for card thumbnail):
   ```yaml
   featured_image: "/img/awards/my-photo.jpg"
   ```

### Image Best Practices
- Use descriptive alt text for accessibility
- Optimize images before uploading (compress, resize)
- Recommended size: 800px width for card images
- Use JPG for photos, PNG for graphics with transparency
- Name files descriptively: `award-ceremony-2025.jpg` not `IMG_1234.jpg`

## YouTube Videos

Embed YouTube videos using the shortcode:
```markdown
{{< youtube VIDEO_ID >}}
```

Example:
```markdown
{{< youtube ygvN5bSmwy4 >}}
```

## Building & Deploying

### Local Preview
```bash
hugo server -D  # -D includes draft posts
```

### Build for Production
```bash
hugo  # Generates static files in /public/
```

### Deploy
- **GitHub Pages**: Push to `gh-pages` branch or `main` (with GitHub Actions)
- **Netlify**: Connect repo, Netlify auto-builds on push
- **Vercel**: Import repo, auto-deploys on push

## File Naming Conventions

### Awards
```
content/awards/award-name-year.md
content/awards/people-of-good-award.md
content/awards/nus-outstanding-alumni-2021.md
```

### Media
```
content/media/publication-topic-year.md
content/media/paypal-newsroom-feature.md
content/media/2020-cna-interview-on-pss.md
```

### Images
```
static/img/awards/award-name-photo-number.jpg
static/img/media/outlet-name-screenshot.png
```

## Common Tasks

### Update Homepage
Edit `content/_index.md`

### Update Awards Section Description
Edit `content/awards/_index.md`

### Update Media Section Description
Edit `content/media/_index.md`

### Add New Section (Future)
```bash
mkdir content/blog
hugo new blog/_index.md
# Create layouts/blog/list.html and single.html
```

### Change Site Title or Settings
Edit `hugo.toml`

## Troubleshooting

### Card not appearing?
- Check front matter is valid YAML
- Ensure date is in ISO 8601 format
- Run `hugo` to check for build errors

### Image not showing?
- Verify path starts with `/img/`
- Check file exists in `/static/img/`
- Ensure no typos in filename

### Build error?
- Check YAML syntax in front matter
- Ensure all required fields present
- Look for unclosed shortcodes `{{<` must close with `>}}`

## Tips for Great Content

1. **Write compelling summaries** - First ~160 characters appear in card
2. **Use descriptive titles** - Clear, concise, searchable
3. **Tag appropriately** - Helps with filtering and discovery
4. **Add featured images** - Makes cards more visually appealing
5. **Include context** - Background, impact, significance
6. **Link to sources** - Use `external_link` for media articles
7. **Proofread** - Check spelling, grammar, formatting

## Next Steps

- Add your first award or media mention
- Upload and optimize images
- Preview locally with `hugo server`
- Build and deploy to production
- Share your new site!

---

For more details, see `IMPLEMENTATION_SUMMARY.md` in the repository root.
