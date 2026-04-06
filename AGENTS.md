# AGENTS.md - Hugo Site Workflow

## Repository Structure

This repository contains Laurence Putra's personal website, built with Hugo.

### Branches

| Branch | Purpose | Notes |
|--------|---------|-------|
| `source` | Local working branch | Tracks `origin/hugo-source` |
| `hugo-source` | Remote source branch | Pushes here trigger GitHub Pages deployment |

## Workflow

### Making Changes

1. Edit Hugo source files in the working tree:
   - Content: `content/`
   - Layouts and shortcodes: `layouts/`
   - Styles: `static/css/`
   - Config: `hugo.toml`

2. Build the site locally:
   ```bash
   hugo --minify
   ```

3. Commit the source changes and push the local `source` branch to `origin/hugo-source`:
   ```bash
   git add .
   git commit -m "Update site"
   git push origin HEAD:hugo-source
   ```

## GitHub Pages

**Site URL:** https://laurenceputra.com

**Configuration:**
- Deployment workflow: `.github/workflows/hugo.yml`
- Trigger branch: `hugo-source`
- Custom domain: `laurenceputra.com` via `static/CNAME`

## Voice & Tone Principles

### First-Person Language
- Use "I" instead of "Laurence" or third-person pronouns
- Example: "I lead engineering teams" not "Laurence leads engineering teams"

### Direct, Authoritative Voice
- State achievements directly without attribution
- ❌ "Laurence's CV described him as..."
- ✅ "I am a versatile engineer with experience across..."

### Remove Soft Phrasing
- ❌ "helped launch", "was part of", "is known for"
- ✅ "launched", "led", "built"

## Content Structure Principles

### Hybrid Approach
- Individual post pages for each award/media item
- Summary `_index.md` pages that list all items
- Example:
  ```
  content/awards/
    ├── _index.md (list of all awards)
    ├── president-volunteerism-award.md (individual post)
    └── nus-computing-outstanding-young-alumni.md
  ```

### YouTube Videos
- Embed videos directly using shortcodes
- Don't just link to YouTube

### External Content
- Reference external sources (links to laurenceputra.com)
- Don't duplicate full content

## Role Information

### Current Roles
- **OSE Engineering Leader** - Operational Support and Efficiency
  - Platform Ownership
  - Operational Efficiency enhancement
  - AI-focused engineering/team work
- **Site Leader** - Server Architecture org at TikTok
- **eSRE function** - TikTok Singapore

## Notes

- GitHub Pages now deploys from Actions, not from a dedicated built-output branch.
- `public/` is generated output for local verification.
- Keep deployment guidance aligned with `hugo.yml` and remove stale references to older branch-based deploy flows.
