# WordPress to Hugo Migration - Quick Start

## 🚀 Quick Migration (If You Have WordPress Export File)

```bash
# 1. Install dependencies
pip3 install -r requirements.txt

# 2. Run migration
python3 wordpress-to-hugo-migration.py laurenceputra.WordPress.2026-01-01.xml

# 3. Review results
cat migration-report.md

# 4. Copy migrated content
cp -r migrated-content/posts/* content/posts/
cp -r migrated-content/pages/* content/pages/
cp -r migrated-content/awards/* content/awards/
cp -r migrated-content/media-posts/* content/media/

# 5. Test Hugo build
hugo server -D
```

---

## 📋 Migration Files Overview

| File | Purpose |
|------|---------|
| `wordpress-to-hugo-migration.py` | Main migration script (Python) |
| `requirements.txt` | Python dependencies |
| `WORDPRESS_MIGRATION_GUIDE.md` | Complete migration guide (30+ pages) |
| `HOW_TO_EXPORT_WORDPRESS.md` | How to obtain WordPress export file |
| `MIGRATION_README.md` | This quick reference file |

---

## 🎯 Migration Status

### ✅ Completed
- Migration script created and ready to use
- Comprehensive documentation written
- Export instructions provided
- Current Hugo content preserved (4 awards, 5 media posts)

### ⏳ Pending (User Action Required)
1. **Obtain WordPress export file** from https://laurenceputra.com
   - See: `HOW_TO_EXPORT_WORDPRESS.md` for detailed instructions
   - WordPress Admin → Tools → Export → Download Export File
   
2. **Upload export file** to this repository
   - Place in repository root as `laurenceputra.WordPress.2026-01-01.xml`
   
3. **Run migration script** (instructions above)

4. **Download images** from WordPress
   - Images need to be downloaded from WordPress media library
   - Organize in `/static/img/` directory
   - See migration guide for automated download script

5. **Review and test** migrated content
   - Check front matter accuracy
   - Verify image paths
   - Test Hugo build locally

---

## 📖 Documentation Guide

### Start Here
1. **Don't have WordPress export yet?**
   → Read: `HOW_TO_EXPORT_WORDPRESS.md`

2. **Have export file and want automated migration?**
   → Read: "Automated Migration" section in `WORDPRESS_MIGRATION_GUIDE.md`
   → Run: `python3 wordpress-to-hugo-migration.py <export-file.xml>`

3. **Prefer manual migration or export not available?**
   → Read: "Manual Migration" section in `WORDPRESS_MIGRATION_GUIDE.md`

4. **Issues during migration?**
   → Read: "Troubleshooting" section in `WORDPRESS_MIGRATION_GUIDE.md`

---

## 🛠️ Migration Script Features

The `wordpress-to-hugo-migration.py` script automatically:

✅ Parses WordPress WXR XML export files
✅ Converts posts/pages to Hugo markdown format
✅ Generates proper front matter (YAML)
✅ Maps categories and tags to Hugo taxonomies
✅ Converts HTML content to Markdown
✅ Converts WordPress shortcodes:
   - `[youtube]` → Hugo `{{< youtube >}}` shortcode
   - `[caption]` → Markdown image syntax
   - Marks others for manual review
✅ Preserves SEO metadata (Yoast descriptions, focus keywords)
✅ Maintains draft status
✅ Organizes posts into sections (posts, pages, awards, media)
✅ Generates comprehensive migration report
✅ Logs issues for manual review

---

## 🎨 Migration Output Structure

```
migrated-content/
├── posts/              # Regular blog posts
│   ├── post-1.md
│   ├── post-2.md
│   └── ...
├── pages/              # Static pages (About, Contact, CV, etc.)
│   ├── about.md
│   ├── cv.md
│   └── ...
├── awards/             # Awards section posts
│   └── ...
├── media-posts/        # Media mentions and interviews
│   └── ...
└── migration-report.md # Detailed report with statistics and issues
```

---

## 🔍 What Gets Migrated

### ✅ Automatically Migrated
- Post titles, content, dates
- Author attribution
- Categories and tags
- Draft status
- SEO metadata (if using Yoast)
- Custom fields / post meta
- YouTube video embeds
- Image references (paths need updating)

### ⚠️ Needs Manual Review
- Gallery shortcodes (no direct Hugo equivalent)
- Custom WordPress shortcodes
- Image paths (need updating to Hugo structure)
- Internal links (need updating)
- Comments (Hugo doesn't support native comments)

### ❌ Not Migrated
- WordPress themes/plugins
- Comments (consider Disqus, utterances, or similar)
- User accounts
- WordPress-specific features

---

## 📊 Expected Migration Timeline

| Phase | Time Estimate |
|-------|---------------|
| Obtain WordPress export | 5-10 minutes |
| Install Python dependencies | 5 minutes |
| Run migration script | 5-15 minutes |
| Review migrated content | 30-60 minutes |
| Download/organize images | 30-90 minutes |
| Update image paths | 15-30 minutes |
| Convert remaining shortcodes | 30-60 minutes |
| Test Hugo build | 15-30 minutes |
| Final review and fixes | 60-120 minutes |
| **TOTAL** | **3-6 hours** |

*Estimate assumes 30-50 posts with moderate complexity*

---

## 🎓 Migration Best Practices

1. **Backup everything first**
   - Keep original WordPress export file safe
   - Don't delete WordPress content until Hugo site is live

2. **Test thoroughly**
   - Run `hugo server -D` locally
   - Check all posts, images, links
   - Verify categories and tags

3. **Use version control**
   - Commit after each major migration step
   - Easy to revert if something goes wrong

4. **Don't rush**
   - Take time to review migrated content
   - Better to catch issues before deployment

5. **Keep documentation**
   - Save migration report
   - Document any custom conversions
   - Note any WordPress URLs that changed

---

## 🔧 Common Migration Issues

### Issue: WordPress export file not accessible
**Solution:** See `HOW_TO_EXPORT_WORDPRESS.md` for 7 different methods

### Issue: Images don't load after migration
**Solution:** 
- Download images from WordPress
- Update image paths in markdown files
- See "Image Migration" section in guide

### Issue: Shortcodes not converting
**Solution:**
- Check migration report for specific shortcodes
- Create custom Hugo shortcodes if needed
- See "Converting Shortcodes" section in guide

### Issue: Hugo build fails
**Solution:**
- Check error message carefully
- Common: Front matter YAML syntax errors
- See "Troubleshooting" section in guide

---

## 📞 Support Resources

### Migration Documentation
- **Full Guide:** `WORDPRESS_MIGRATION_GUIDE.md` (comprehensive, 400+ lines)
- **Export Guide:** `HOW_TO_EXPORT_WORDPRESS.md` (7 methods to get export file)
- **Quick Start:** This file

### Hugo Resources
- Hugo Documentation: https://gohugo.io/documentation/
- Hugo Forums: https://discourse.gohugo.io/
- Hugo Migration Tools: https://gohugo.io/tools/migrations/

### WordPress Resources
- WordPress Export: https://wordpress.org/support/article/tools-export-screen/
- WXR Format: https://wordpress.org/support/article/wordpress-export-tools/

---

## ✅ Pre-Migration Checklist

Before starting migration:

- [ ] WordPress admin access confirmed
- [ ] WordPress export file obtained (or know how to get it)
- [ ] Python 3.6+ installed (`python3 --version`)
- [ ] Hugo installed (`hugo version`)
- [ ] Git repository cloned locally
- [ ] Backed up current Hugo content
- [ ] Read at least "Quick Start" or "Automated Migration" section of guide
- [ ] Time allocated (3-6 hours for complete migration)

---

## 🚦 Migration Steps Summary

### Phase 1: Preparation (10-15 min)
1. Obtain WordPress export file
2. Install Python dependencies
3. Backup current content

### Phase 2: Automated Migration (10-20 min)
4. Run migration script
5. Review migration report
6. Move migrated files to content directory

### Phase 3: Manual Adjustments (60-120 min)
7. Download and organize images
8. Update image paths in markdown
9. Convert remaining shortcodes
10. Update internal links
11. Verify front matter

### Phase 4: Testing (30-45 min)
12. Test Hugo build locally
13. Check all posts display correctly
14. Verify images load
15. Test categories/tags
16. Check responsive design

### Phase 5: Deployment (15-30 min)
17. Final build
18. Deploy to GitHub Pages
19. Verify live site
20. Set up redirects if needed

---

## 📝 Migration Report

After running the migration script, you'll get `migration-report.md` with:

- **Statistics:** Posts/pages converted, drafts, issues
- **Output structure:** Where files were placed
- **Issues log:** Shortcodes needing attention, broken links, etc.
- **Next steps:** Specific actions for your content
- **Quality checklist:** Ensure nothing was missed

---

## 🎯 Current Site Context

### Existing Hugo Content
- **Homepage:** `content/_index.md`
- **Awards section:** 4 posts (People of Good Award, NUS Alumni Awards, SKM Award)
- **Media section:** 5 posts (PayPal feature, interviews, Project Lionheart)
- **Theme:** Custom `laurenceputra` theme with card layouts

### Configured Sections (in hugo.toml)
- Home
- Posts (not yet populated)
- Awards (has content)
- Media (has content)
- CV (needs creation)

### WordPress Site Details
- **Current site:** https://laurenceputra.com
- **Cloudflare protected:** Yes (may need to disable for scraping)
- **Expected content:** Blog posts, additional awards, media mentions
- **Permalink structure:** Already matched in Hugo config

---

## 💡 Pro Tips

1. **Start with a test run**
   - Migrate a few posts first
   - Verify the process works
   - Then migrate everything

2. **Use the migration report**
   - Don't skip reading it
   - Lists specific issues with your content
   - Saves debugging time later

3. **Keep WordPress running**
   - Don't shut down WordPress until Hugo site is live and tested
   - Easy to reference original content
   - Fallback if issues arise

4. **Optimize as you go**
   - Good time to improve image sizes
   - Update outdated content
   - Improve SEO metadata

5. **Document your changes**
   - Note any custom conversions
   - Keep list of URL changes
   - Helps with future maintenance

---

## 🎉 Migration Success Criteria

Migration is complete when:

- ✅ All WordPress posts migrated to Hugo
- ✅ All images downloaded and loading correctly
- ✅ Categories and tags working
- ✅ Hugo builds without errors
- ✅ Site looks correct on desktop and mobile
- ✅ SEO metadata preserved
- ✅ Redirects set up (if URLs changed)
- ✅ Live site deployed and tested

---

## 📌 Quick Commands Reference

```bash
# Install dependencies
pip3 install -r requirements.txt

# Run migration
python3 wordpress-to-hugo-migration.py <export-file.xml>

# View migration report
cat migration-report.md

# Copy migrated content
cp -r migrated-content/posts/* content/posts/
cp -r migrated-content/awards/* content/awards/
cp -r migrated-content/media-posts/* content/media/
cp -r migrated-content/pages/* content/pages/

# Test Hugo build
hugo server -D

# Production build
hugo

# Check Hugo version
hugo version

# Clean build directory
hugo --cleanDestinationDir

# Verbose build (for debugging)
hugo -v
```

---

**Ready to migrate?** Start with `HOW_TO_EXPORT_WORDPRESS.md` to get your export file!

**Have export file?** Run: `python3 wordpress-to-hugo-migration.py <your-file.xml>`

**Questions?** See: `WORDPRESS_MIGRATION_GUIDE.md` (comprehensive guide)

---

**Last Updated:** 2026-01-01
**Migration Script Version:** 1.0
**Minimum Hugo Version:** v0.80.0
