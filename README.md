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

- Start changes from `main` on a feature branch and open a PR against `main`.
- The workflow builds and deploys on pushes to `main` (or a manual workflow dispatch).
- Do not commit generated `public/` output.

The published site uses the custom domain `laurenceputra.com` via the generated `CNAME` file.
