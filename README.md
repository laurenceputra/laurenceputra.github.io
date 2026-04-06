# Laurence Putra Hugo Site

Rebuilt Hugo source for <https://laurenceputra.com/>.

## Local development

```bash
hugo server
```

## Production build

```bash
hugo --minify
```

## Deployment

GitHub Pages is deployed through `.github/workflows/hugo.yml`.

- The local working branch in this repo is `source`.
- That branch tracks `origin/hugo-source`.
- A push to `hugo-source` triggers the GitHub Pages build and deploy workflow.
- Deployment no longer depends on pushing built files to a separate `main` or `hugo-rebuild` branch.

The published site uses the custom domain `laurenceputra.com` via the generated `CNAME` file.
