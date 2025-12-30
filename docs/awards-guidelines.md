# Awards editorial guidelines

This document describes how to add and maintain awards content and external links.

Fields to use in award post front matter:
- `external_url` (optional): External verification URL for the award (prefer HTTPS / canonical source)
- `external_url_label` (optional): Visible link text for the external URL (default: "Official announcement")
- `external_url_archive` (optional): Archive.org snapshot URL as a fallback
- `external_url_verified_date` (optional): ISO date when link was last verified (displayed as "Last verified" in the verification block)
- `external_url_status` (optional): `active` | `archived` | `dead`

Notes:
- The verification block appears on award posts when the post has `categories: ["Awards"]`. Use the `awards` archetype to create correctly categorized posts.

Best practices
- Add `url` only on award detail pages; homepage links should point to internal award pages.
- Prefer official organizational pages (university/award body/etc). Remove tracking params.
- Create an Archive.org snapshot when publishing and set `url_archive` where possible.
- Update `url_verified_date` after manual link checks; consider adding a CI link-checker that raises issues for dead links.

Maintenance
- Perform an annual link review: visit `external_url` for each award, update `external_url_verified_date` and `external_url_status`.
- For legacy awards (3+ years), prefer linking to `external_url_archive` instead of live sites where appropriate.

Accessibility
- External links on award pages must include an informative `aria-label` (the template sets this automatically).

CI Validation
- A GitHub Actions workflow runs on PRs and push to validate award posts. It checks:
  - Each file in `content/posts/awards/*.md` has a `categories` front matter and includes "Awards".
  - Each `external_url` (if present) uses `https://`.
  - The workflow will **warn** if `external_url` is missing or empty (the warning does not fail the build but surfaces on PRs for review).

Implementation notes
- Homepage shows compact award cards and links to internal post pages. External `external_url` fields are shown on the award detail page in the "Verification" section.