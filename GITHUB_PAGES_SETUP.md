# GitHub Pages Setup Instructions

After merging this PR, you need to configure GitHub Pages to use GitHub Actions for deployment:

## Steps to Enable GitHub Pages with Hugo

1. Go to your repository on GitHub: `https://github.com/laurenceputra/laurenceputra.github.io`

2. Click on **Settings** (top navigation)

3. In the left sidebar, click on **Pages** (under "Code and automation")

4. Under **Build and deployment**:
   - **Source**: Select "GitHub Actions" (not "Deploy from a branch")
   
5. The workflow `.github/workflows/hugo.yml` will automatically:
   - Build the Hugo site when you push to the `main` branch
   - Deploy the built site to GitHub Pages
   - Make it available at `https://laurenceputra.github.io/`

## Workflow Triggers

The deployment workflow runs automatically on:
- Every push to the `main` branch
- Manual trigger from the Actions tab

## Verifying the Deployment

After pushing to `main`:
1. Go to the **Actions** tab in your repository
2. You should see the "Deploy Hugo site to GitHub Pages" workflow running
3. Once complete (green checkmark), your site will be live at `https://laurenceputra.github.io/`

## Local Preview Before Pushing

To preview changes locally before pushing:

```bash
hugo server -D
```

Visit `http://localhost:1313/` to see your changes.

## Troubleshooting

If the deployment fails:
1. Check the Actions tab for error messages
2. Ensure the workflow has the correct permissions (already configured in the workflow file)
3. Make sure GitHub Pages is enabled in Settings > Pages
4. Verify that the source is set to "GitHub Actions"

## Important Notes

- The old `index.html` has been moved to `index.html.bak` as a backup
- All content is now managed through Hugo (Markdown files in `content/` directory)
- Static assets (CSS, JS, images, PDF) remain in the `static/` directory
- The site will be built and deployed automatically - no manual HTML editing needed
