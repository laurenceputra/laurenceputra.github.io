# AGENTS.md - Hugo Site Workflow

## Repository Structure

This repository contains Laurence Putra's personal website, built with Hugo.

### Branches

| Branch | Purpose | What it Contains |
|--------|---------|------------------|
| `hugo-source` | Hugo source files | Raw content, layouts, themes, config - edit here |
| `hugo-rebuild` | Built static site | Generated HTML/CSS/JS - GitHub Pages serves this |

## Workflow

### Making Changes

1. **Edit source files** in `hugo-source` branch:
   - Content: `content/` (Markdown files)
   - Layouts: `layouts/`
   - Styles: `static/css/`
   - Config: `hugo.toml`

2. **Build the site**:
   ```bash
   hugo --minify
   ```

3. **Push to hugo-rebuild**:
   ```bash
   # From hugo-source branch
   git checkout hugo-rebuild
   rm -rf *
   cp -r public/* ./
   git add .
   git commit -m "Update site"
   git push origin hugo-rebuild
   ```

### Automated Option

The subagent setup uses git worktrees to automate this:
- Source lives in `/home/node/.openclaw/workspace/laurence-profile/hugo-site`
- Built output goes to `/tmp/laurenceputra-site-main`
- Push both branches after rebuilding

## GitHub Pages

**Site URL:** https://laurenceputra.github.io

**Configuration:**
- Pages source: `hugo-rebuild` branch
- Custom domain: `laurenceputra.com` (via CNAME file)

## Commands

```bash
# Rebuild and push
cd /home/node/.openclaw/workspace/laurence-profile/hugo-site
hugo --minify
# ... then push as shown above

# Or use the worktree approach
cd /tmp/laurenceputra-site-main
git push origin hugo-rebuild
```

## Notes

- Source branch (`hugo-source`) is for development
- Rebuild branch (`hugo-rebuild`) is for deployment
- Never edit files directly in `hugo-rebuild`
- Always rebuild from source before pushing
