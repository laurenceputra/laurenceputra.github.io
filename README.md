# Laurence Putra Franslay - Personal Website

This is the personal website of Laurence Putra Franslay, built with [Hugo](https://gohugo.io/) static site generator.

## About

This site serves as personal branding for a tech leader, philanthropist, and social fixer. It showcases work in software engineering, community building, photography, and social impact initiatives.

## Site Structure

- **Home Page**: Main landing page with sections on Software Engineering, Photography, Community, and Social initiatives
- **Awards Page**: Recognition and awards received for tech leadership and social impact
- **Media Mentions**: Coverage in various media outlets for work as a tech leader and social fixer

## Building the Site

### Prerequisites

- [Hugo Extended](https://gohugo.io/installation/) version 0.121.1 or later

### Local Development

To run the site locally:

```bash
hugo server -D
```

The site will be available at `http://localhost:1313/`

### Building for Production

To build the site for production:

```bash
hugo --minify
```

The built site will be in the `public/` directory.

## Deployment

This site is automatically deployed to GitHub Pages using GitHub Actions. The workflow is defined in `.github/workflows/hugo.yml`.

On every push to the `main` branch:
1. Hugo builds the site
2. The built site is deployed to GitHub Pages
3. The site becomes available at `https://laurenceputra.github.io/`

## Content Management

### Adding Content

Content files are in Markdown format in the `content/` directory:

- `content/_index.md` - Home page content
- `content/awards.md` - Awards page
- `content/media.md` - Media mentions page

To add a new page:

```bash
hugo new content/page-name.md
```

### Static Assets

Static assets (CSS, JavaScript, images, PDFs) are in the `static/` directory and are served from the root of the site.

## Theme

The site uses a custom Hugo theme located in `themes/laurenceputra/`. The theme is based on Pure.css and includes custom styling to match the original design.

## License

Content © Laurence Putra Franslay. All rights reserved.
