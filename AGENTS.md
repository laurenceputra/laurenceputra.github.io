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

## Notes

- GitHub Pages now deploys from Actions, not from a dedicated built-output branch.
- `public/` is generated output for local verification.
- Keep deployment guidance aligned with `hugo.yml` and remove stale references to older branch-based deploy flows.
