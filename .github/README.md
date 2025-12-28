# Hugo Website Management Agent Group

Build and maintain professional personal Hugo websites with expert guidance through coordinated agent collaboration. This group provides technical Hugo expertise, content generation, WordPress migration support, and dual quality gates to ensure high-quality site management.

## Quick Start

### For Site Architecture or Theme Help
👉 **Start here**: @hugo-specialist

Examples:
- "How should I organize my blog?" → Architecture guidance
- "I want to customize my theme's colors" → Theme customization
- "My template isn't rendering - what's wrong?" → Hugo debugging

### For Content Generation
👉 **Consult**: @content-creator

Examples:
- "Write a blog post on Rust async patterns"
- "Generate content following my site's structure"
- "Create an about page with proper front matter"

### For WordPress Migration
👉 **Consult**: @wordpress-migrator (for one-time migrations)

Examples:
- "Convert my 50-post WordPress blog to Hugo"
- "I have a WordPress export file - migrate it to Hugo"

## The Five Agents

| Agent | Role | Best For | Model |
|-------|------|----------|-------|
| **Hugo Specialist** | Technical Hugo expert combining architecture, themes, and debugging | Site design, theme customization, troubleshooting | Sonnet 4.5 |
| **Content Creator** | Hugo content generation with technical front matter precision | Blog posts, pages, content generation | Sonnet 4.5 |
| **Quality Reviewer** | Systematic validator of Hugo work and content quality | Quality assurance, best practices validation (automatic) | Sonnet 4.5 |
| **Devil's Advocate** | Critical reviewer challenging assumptions and identifying blind spots | Risk assessment, alternative perspectives (automatic) | Sonnet 4.5 |
| **WordPress Migrator** | Optional specialist for WordPress-to-Hugo conversion | One-time site migrations (on-demand) | Sonnet 4.5 |

## Typical Workflows

### Workflow 1: Site Architecture
```
You: "How should I structure my blog?"
   ↓
Hugo Specialist → designs architecture
   ↓
Quality Reviewer → validates best practices
   ↓
Devil's Advocate → examines alternatives
   ↓
You: receive guidance with all perspectives
```

### Workflow 2: Content Generation
```
You: "Write a post on topic X"
   ↓
Content Creator → generates Hugo markdown
   ↓
Quality Reviewer → validates front matter & style
   ↓
Devil's Advocate → examines tone & approach
   ↓
You: receive ready-to-deploy Hugo content
```

### Workflow 3: WordPress Migration
```
You: "Migrate my WordPress site"
   ↓
WordPress Migrator → converts posts & metadata
   ↓
Quality Reviewer → validates conversion accuracy
   ↓
Devil's Advocate → examines migration completeness
   ↓
Hugo Specialist → prepares for ongoing maintenance
   ↓
You: receive Hugo-ready files
```

## Common Use Cases

### Case 1: Starting a New Hugo Blog
1. **Ask Hugo Specialist**: "I'm starting a blog covering tech and travel. How should I organize it?"
   - Receives: architecture recommendation, configuration guidance, theme suggestions
2. **Ask Content Creator**: "Generate my first 3 posts following this structure"
   - Receives: ready-to-deploy markdown files with proper front matter
3. **Result**: New Hugo blog ready to deploy

### Case 2: Customizing Your Theme
1. **Ask Hugo Specialist**: "I like my theme but want my brand colors. How do I customize it?"
   - Receives: CSS customization approach, specific file changes, accessibility verification
2. **Result**: Custom-branded theme ready to use

### Case 3: Troubleshooting Hugo Issues
1. **Ask Hugo Specialist**: "My custom CSS isn't showing up - what's wrong?"
   - Receives: diagnosis, explanation, fix with step-by-step guidance
2. **Result**: Issue resolved with understanding of the root cause

### Case 4: Migrating from WordPress
1. **Ask WordPress Migrator**: "Here's my WordPress export file - convert it to Hugo"
   - Receives: converted markdown files, front matter, media handling, migration report
2. **Ask Hugo Specialist**: "What cleanup do I need after migration?"
   - Receives: post-migration optimization, structure review, next steps
3. **Result**: Complete Hugo site ready for deployment

### Case 5: Generating Content Regularly
1. **Ask Content Creator**: "Write a post on [topic] for my blog"
   - Receives: complete markdown with proper front matter, ready to add to site
2. **Repeat**: For each new post
3. **Result**: Content generation that maintains site consistency

## Hugo Prerequisites

Before using this group, ensure you have:
- ✅ Hugo installed locally ([install guide](https://gohugo.io/getting-started/installing/))
- ✅ A text editor for writing markdown
- ✅ Git for version control (recommended)
- ✅ Basic familiarity with markdown syntax
- ✅ Optional: GitHub/GitLab account for deployment

The agents handle Hugo expertise; you handle execution (running `hugo new`, `hugo server`, git commits, deployment).

## Hugo Fundamentals

**Quick Reference**:
- Hugo processes markdown from `/content/` directory
- Front matter (YAML/TOML) provides post metadata
- Themes provide layout/styling; override with `/layouts/` directory
- `hugo server` runs local dev server
- `hugo build` generates static files in `/public/`
- Deploy `/public/` directory to your hosting

**Directory Structure**:
```
my-hugo-site/
├── config.toml          # Site configuration
├── content/             # Your markdown posts
│   ├── posts/           # Blog posts
│   │   └── post.md
│   └── pages/           # Static pages
│       └── about.md
├── layouts/             # Theme overrides
├── static/              # Images, CSS, assets
├── themes/              # Hugo themes
└── public/              # Generated site (deploy this)
```

## Quality Validation Approach

This group uses **dual quality gates** for high-quality output:

1. **Quality Reviewer** (systematic validation)
   - Checks against Hugo best practices
   - Validates accessibility standards (WCAG 2.1 AA)
   - Confirms responsive design
   - Verifies technical correctness

2. **Devil's Advocate** (critical thinking)
   - Challenges design assumptions
   - Identifies blind spots
   - Examines alternative approaches
   - Documents trade-offs and risks

**Result**: You receive not just validated work, but thoroughly examined work with all perspectives documented.

## Hugo Specialist Responsibilities

- **Architecture & Structure**: Design how content is organized
- **Theme Customization**: Modify themes for your brand
- **Configuration**: Set up Hugo config.toml/yaml optimally
- **Debugging**: Solve Hugo-specific technical issues
- **Best Practices**: Guidance on Hugo conventions and patterns

**Hugo Debugging Scope**:
- ✅ Template rendering errors
- ✅ Front matter schema issues
- ✅ Shortcode problems
- ✅ CSS customization issues
- ✅ Build configuration errors
- ❌ Hugo binary installation (system-level)
- ❌ PATH environment variable (system-level)
- ❌ File permissions (system-level)

## Content Creator Responsibilities

- **Post Generation**: Create blog posts with proper front matter
- **Front Matter Precision**: YAML/TOML syntax, ISO 8601 dates, taxonomy accuracy
- **Markdown Quality**: Proper formatting, accessibility, readability
- **Style Consistency**: Match your site's tone and voice
- **Taxonomy Management**: Organize content with proper categories/tags

**Deployment**: Content is ready to deploy - copy to `/content/` directory and commit

## WordPress Migrator Responsibilities

- **Content Conversion**: Transform WordPress posts to Hugo markdown
- **Front Matter Mapping**: Convert post metadata to Hugo front matter
- **Taxonomy Mapping**: Map WordPress categories/tags to Hugo structure
- **Media Handling**: Preserve or reorganize image references
- **Redirect Mapping**: Generate redirects for SEO preservation
- **Migration Report**: Document conversion accuracy and issues

**Post-Migration**: Hugo Specialist handles site optimization and ongoing maintenance

## Example Interactions

### Example 1: Architecture Design
```
You: "I'm starting a tech blog. Should I use a flat structure (all posts in /posts/) 
     or nested structure (tech, tutorials, reviews folders)?"

Hugo Specialist: 
  - Flat works well for <30 posts
  - Nested works better for organized growth
  - Recommends nested with clear section organization
  - Explains Hugo configuration needed
  - Provides directory structure diagram

Quality Reviewer: Validates scalability, best practices ✓

Devil's Advocate: 
  - Challenges: "How do readers discover topics?"
  - Suggests: Also add recent-posts sidebar for time-based discovery
  - Documents: Trade-offs between organization and discoverability

You: Receive guidance + two perspectives to choose from
```

### Example 2: Content Generation
```
You: "Write a blog post on 'Hugo Theme Customization for Beginners' 
     targeting WordPress users, ~2000 words, beginner-friendly tone"

Content Creator:
  - Generates complete markdown with:
    - YAML front matter (title, date, categories, tags)
    - Proper heading hierarchy
    - Code examples
    - Resources section
  - Result: Ready to add to /content/posts/

Quality Reviewer: 
  - Validates front matter schema ✓
  - Checks markdown formatting ✓
  - Verifies tone matches site voice ✓
  - Confirms technical accuracy ✓

Devil's Advocate:
  - Examines: "Is tone actually accessible for WordPress users?"
  - Suggests: Add more step-by-step examples
  - Documents: Assumptions about reader background

You: Receive ready-to-use post with feedback for improvement
```

### Example 3: Theme Customization
```
You: "I want to change my theme's header colors to match my brand 
     (primary: #6366f1, secondary: #ec4899)"

Hugo Specialist:
  - Recommends: CSS override approach (don't modify theme directly)
  - Provides: /static/css/custom.css with color variables
  - Explains: How to integrate into theme layout
  - Verifies: Color contrast for accessibility (WCAG AA)
  - Suggests: Also consider dark mode

Quality Reviewer: 
  - Validates: Proper CSS, accessibility compliance ✓
  - Checks: Responsive design across devices ✓
  - Confirms: Contrast ratios meet WCAG standards ✓

Devil's Advocate:
  - Questions: "Are custom colors accessible for colorblind users?"
  - Suggests: Test with color blindness simulator
  - Documents: Trade-off between brand colors and accessibility

You: Receive complete customization with accessibility verified
```

## Troubleshooting

### "My CSS changes aren't showing up"
**Ask Hugo Specialist**:
- Check if CSS file is in `/static/` or `/layouts/` (matters for how it loads)
- Verify CSS specificity (theme styles might override)
- Clear cache and rebuild

### "Build error: 'failed to parse front matter'"
**Ask Hugo Specialist**:
- Likely YAML syntax error in front matter
- Common: Quotes needed for strings with special characters
- Can provide specific fix

### "Should I customize the theme or switch themes?"
**Ask Hugo Specialist**:
- Analyzes required changes vs. available themes
- Recommends based on time investment vs. outcome
- Provides both paths if applicable

### "How do I migrate my WordPress blog?"
**Ask WordPress Migrator**:
- Provide WordPress export file
- Specify target Hugo structure
- Receive converted files + migration report

## Tips for Best Results

1. **Be Specific**: "Change header color" vs. "Change header color from black to #6366f1 and adjust contrast"
2. **Provide Context**: Share your current Hugo structure, theme, or WordPress export details
3. **Define Requirements**: Content tone, audience level, target word count
4. **Ask Follow-ups**: "Why did you recommend this?" leads to better understanding
5. **Use Recommendations**: Quality Reviewer and Devil's Advocate provide perspectives - consider them

## Integration with Your Workflow

### Git Workflow
Agents recommend Git strategies but don't execute git commands:
- You create branches for new features
- You commit changes suggested by agents
- You push to GitHub/GitLab
- You deploy from main branch

### Hugo CLI Workflow
Agents provide command guidance but don't run commands:
- You run `hugo new content/posts/my-post.md`
- You run `hugo server` to preview locally
- You run `hugo build` to generate static files
- You deploy `/public/` directory

### Deployment Workflow
Agents provide deployment guidance but don't deploy:
- You configure Netlify/Vercel/GitHub Pages
- You push to main branch
- Your hosting provider builds and deploys automatically

## Portability & Flexibility

- Works with **any Hugo theme** (agents adapt guidance to your theme)
- Works with **any Hugo version** (agents adjust for version-specific features)
- Works on **Windows, macOS, Linux** (OS-independent guidance)
- Works with **any deployment platform** (Netlify, Vercel, GitHub Pages, custom)
- **No hardcoded paths**: All guidance uses relative paths

## Support & Documentation

For detailed Hugo documentation:
- [Hugo Official Docs](https://gohugo.io/documentation/)
- [Hugo Content Organization](https://gohugo.io/content-management/)
- [Hugo Templates](https://gohugo.io/templates/)

For guidance on using this agent group:
- Consult copilot-instructions.md for complete workflow documentation
- Review agent descriptions for specific responsibilities
- Use the decision tree to find the right agent for your need

## Version & Updates

**Current Version**: 1.0.0  
**Released**: January 2025

This group provides a complete Hugo website management system. Use copilot-instructions.md for workflow details and agent coordination guidance.

---

**Ready to start?** → Consult @hugo-specialist with your Hugo website question!
