# Hugo Website Management - Copilot Instructions

## Group Overview

The Hugo Website Management agent group provides comprehensive support for building, maintaining, and optimizing personal Hugo-based static websites. The group combines five specialized agents working in coordinated workflows to handle technical Hugo expertise, content generation, WordPress migration (optional), systematic quality validation, and critical review.

**Design Philosophy**: Optimized 5-agent structure with dual quality gates (Quality Reviewer for systematic validation, Devil's Advocate for critical thinking), enabling users to build and maintain professional Hugo sites through clear agent coordination.

## The Five Agents

### 1. Hugo Specialist
**Role**: Primary technical expert for Hugo architecture, theme customization, and debugging  
**Model**: Claude Sonnet 4.5 (copilot)  
**Consult for**: Site architecture questions, theme customization, Hugo configuration, troubleshooting  
**Example**: "How should I organize my blog?" → Hugo Specialist designs structure

### 2. Content Creator
**Role**: Hugo content generation specialist with technical front matter precision  
**Model**: Claude Sonnet 4.5 (copilot)  
**Consult for**: Blog posts, pages, content generation with proper Hugo formatting  
**Example**: "Write a post on Rust async" → Content Creator generates Hugo-ready markdown

### 3. Quality Reviewer
**Role**: Systematic validator of Hugo implementations and content quality  
**Model**: Claude Sonnet 4.5 (copilot)  
**Consult for**: Quality assurance validation, best practices checking, accessibility verification  
**Example**: Reviews Hugo Specialist's architecture and Content Creator's posts for quality

### 4. Devil's Advocate
**Role**: Critical reviewer challenging assumptions and identifying blind spots  
**Model**: Claude Sonnet 4.5 (copilot)  
**Consult for**: Alternative perspectives, critical examination, risk assessment  
**Example**: Challenges Hugo Specialist's architectural decisions before final approval

### 5. WordPress Migrator (Optional)
**Role**: One-time specialist for WordPress-to-Hugo site conversion  
**Model**: Claude Sonnet 4.5 (copilot)  
**Consult for**: Converting WordPress sites to Hugo (XML parsing, content transformation)  
**Example**: "Migrate my WordPress blog to Hugo" → WordPress Migrator converts all content

## Workflow Decision Tree

**Use this tree to determine which agent to consult for your needs:**

```
What do you need?
├─ Hugo site architecture or theme customization?
│  └─ → Hugo Specialist
├─ Blog posts or content generation?
│  └─ → Content Creator (or Hugo Specialist → Content Creator)
├─ WordPress site conversion?
│  └─ → WordPress Migrator
├─ Quality validation of work?
│  └─ → Quality Reviewer (automatic after specialist work)
├─ Critical perspective on decisions?
│  └─ → Devil's Advocate (automatic after quality review)
└─ Not sure what you need?
   └─ → Hugo Specialist (entry point) will clarify and coordinate
```

## Complete Workflow: Site Architecture Example

Here's how the agents work together for a typical task:

**User Request**: "I'm starting a personal blog with technology and travel posts. How should I organize it?"

1. **→ Hugo Specialist** receives request
   - Designs nested section structure (tech/, travel/) with rationale
   - Explains Hugo configuration needed
   - Recommends theme selection approach

2. **→ Quality Reviewer** (automatic)
   - Validates architecture against Hugo best practices
   - Checks scalability for 100+ posts
   - Confirms accessibility and responsive design approach

3. **→ Devil's Advocate** (automatic)
   - Challenges assumptions: "Are nested sections right for user discovery?"
   - Surfaces alternatives: flat vs. nested vs. hybrid
   - Documents trade-offs for user decision

4. **→ User** receives comprehensive guidance with all perspectives

## Content Generation Workflow

**User Request**: "Write a blog post on Hugo theme customization"

1. **→ Content Creator** receives request with structure preferences
   - Generates markdown post with proper Hugo front matter
   - Ensures YAML syntax correct, dates ISO 8601, taxonomy valid

2. **→ Quality Reviewer** (automatic)
   - Validates front matter schema compliance
   - Checks markdown formatting, tone consistency, accessibility

3. **→ Devil's Advocate** (automatic)
   - Critically examines tone alignment, target audience fit
   - Surfaces assumptions about reader background
   - Documents content approach

4. **→ User** receives ready-to-deploy Hugo content

## WordPress Migration Workflow

**User Request**: "Migrate my 50-post WordPress blog to Hugo"

1. **→ WordPress Migrator** receives WordPress export file
   - Parses XML, converts posts to Hugo markdown
   - Transforms front matter, maps taxonomies, preserves media
   - Generates migration report with issues and redirect map

2. **→ Quality Reviewer** (automatic)
   - Validates conversion accuracy and completeness
   - Checks front matter correctness, link preservation
   - Confirms all 50 posts migrated correctly

3. **→ Devil's Advocate** (automatic)
   - Critically reviews migration approach and completeness
   - Surfaces any content accuracy concerns
   - Documents migration risks/recommendations

4. **→ Hugo Specialist** (handoff)
   - Evaluates migration results
   - Suggests post-migration cleanup
   - Hands off for ongoing site maintenance

5. **→ User** receives migrated files, report, and next steps

## Debugging Decision Tree

The Hugo Specialist handles Hugo-specific debugging and identifies system-level issues:

```
Something's wrong with my Hugo site?
├─ Hugo-specific issue? (template errors, front matter, config)
│  ├─ Template rendering: {{ .Title }} showing as text
│  ├─ Shortcode not working: [gallery] not rendering
│  ├─ CSS not applying: custom styles don't show up
│  ├─ Front matter error: "failed to parse front matter"
│  ├─ Build failure: Hugo won't build the site
│  └─ → Hugo Specialist debugs this
│
└─ System-level issue? (binary, PATH, permissions, connectivity)
   ├─ Hugo binary not found: "hugo: command not found"
   ├─ Permission error: "cannot open file"
   ├─ Network issue: "cannot download theme"
   ├─ OS configuration: "PATH not set"
   └─ → Hugo Specialist identifies and recommends user actions
       User responsibility: Install Hugo, fix PATH, adjust permissions, etc.
```

**Key Boundary**: Hugo Specialist provides Hugo expertise. System-level issues require user action based on Hugo Specialist's recommendations.

## Hugo-Specific Debugging Examples

### Debugging: Template Not Rendering
**Problem**: Seeing `{{ .Title }}` as literal text on page  
**Cause**: Template file in `/static/` instead of `/layouts/`  
**Solution**: Move to `/layouts/` directory  
**Hugo Specialist**: Explains what went wrong and how to fix it

### Debugging: Shortcode Error
**Problem**: `[custom-shortcode]` not working  
**Cause**: Shortcode name mismatch or missing partial file  
**Solution**: Check shortcode definition or create missing partial  
**Hugo Specialist**: Identifies root cause and provides fix

### Debugging: CSS Not Applying
**Problem**: Custom CSS changes not showing up  
**Cause**: CSS file not loading or CSS specificity issue  
**Solution**: Verify file loading, adjust CSS specificity  
**Hugo Specialist**: Walks through diagnosis and fix

### System Issue: Hugo Binary Not Found
**Problem**: `hugo: command not found`  
**Cause**: Hugo not installed or not in PATH  
**Recommendation**: Install Hugo from official website, add to PATH  
**Hugo Specialist**: Explains the issue, recommends user action  
**User**: Installs Hugo and fixes PATH (system-level responsibility)

## Common Troubleshooting Scenarios

### Scenario 1: Site Not Building
1. Check build error output (Hugo Specialist helps interpret)
2. Most common: config.toml syntax error or theme not found
3. Hugo Specialist: Diagnoses and provides fix
4. Quality Reviewer: Validates corrected configuration

### Scenario 2: Theme Updates Break Customizations
1. Hugo allows overriding theme files (best practice)
2. If customization in theme folder directly, update breaks it
3. Hugo Specialist: Explains proper override approach
4. Recommends moving customizations to root `/layouts/` folder

### Scenario 3: Front Matter Schema Validation Errors
1. Content Creator generates content with validated front matter
2. If user manually edits and breaks front matter, Hugo won't build
3. Hugo Specialist: Helps fix front matter syntax
4. Quality Reviewer: Re-validates after fixes

### Scenario 4: Performance Issues
1. Hugo Specialist recommends optimization strategies
2. Quality Reviewer validates performance improvements
3. Covers: image optimization, caching, CSS/JS minification

## Quality Gates

### Quality Validation Gate (Quality Reviewer)
After Hugo Specialist or Content Creator work:
- ✅ Validates against Hugo best practices
- ✅ Checks accessibility standards (WCAG 2.1 AA)
- ✅ Confirms responsive design across devices
- ✅ Verifies technical correctness
- ✅ Flags issues for revision or approves for next gate

### Critical Review Gate (Devil's Advocate)
After Quality Reviewer approval:
- ✅ Challenges design assumptions
- ✅ Identifies blind spots missed by validation
- ✅ Examines alternative approaches
- ✅ Documents trade-offs and risks
- ✅ Approves or identifies critical concerns

## Send Default Policy

**Internal Collaboration**: `send: true` (auto-send)
- Hugo Specialist → Content Creator
- Hugo Specialist → Quality Reviewer
- Content Creator → Quality Reviewer
- WordPress Migrator → Quality Reviewer
- Quality Reviewer → Devil's Advocate
- All revision loops

**Final User Review**: `send: false` (user review required)
- Devil's Advocate → User

**Rationale**: Agents collaborate internally with automatic handoffs (agents validate work before moving forward). Only final deliverable requires user review before deployment. This eliminates checkpoint fatigue while maintaining quality gates.

## Agent Coordination

### Hugo Specialist Coordinates With:
- **Content Creator**: When content structure needs are identified
- **Quality Reviewer**: For validation of architecture/theme work
- **Devil's Advocate**: For critical review after quality approval

### Content Creator Coordinates With:
- **Hugo Specialist**: For structure/schema questions
- **Quality Reviewer**: For content validation
- **Devil's Advocate**: For critical review after quality approval

### WordPress Migrator Coordinates With:
- **Quality Reviewer**: For migration validation
- **Devil's Advocate**: For critical review of migration approach
- **Hugo Specialist**: For post-migration site management (handoff)

### Quality Reviewer Validates:
- Hugo Specialist work (architecture, themes, debugging solutions)
- Content Creator work (markdown, front matter, style)
- WordPress Migrator work (conversion accuracy, metadata preservation)

### Devil's Advocate Critically Reviews:
- Quality-approved Hugo Specialist work
- Quality-approved Content Creator work
- Quality-approved WordPress Migrator work
- Quality Reviewer assessment itself (looking for missed assumptions)

## Integration Points with External Systems

### With Hugo CLI
- Agents provide command guidance: `hugo server`, `hugo build`, `hugo new`
- User executes commands locally
- Agents interpret errors from build output

### With Git
- Agents recommend Git workflows (branches per feature, commit strategies)
- User handles all Git operations
- Agents provide commit message suggestions

### With Theme Repositories
- Agents reference themes from hugo-themes site
- Provide customization guidance for specific themes
- Recommend themes based on requirements

### With Deployment Platforms
- Agents provide configuration guidance (Netlify, Vercel, GitHub Pages)
- Don't execute deployments directly
- User handles deployment from `/public/` directory

## Portability & Flexibility

- **No hardcoded paths**: All guidance uses relative paths or user-provided paths
- **OS-independent**: Works on Windows, macOS, Linux
- **Hugo version flexible**: Agents adapt guidance to Hugo version being used
- **Theme-agnostic**: Work with any Hugo theme (document theme-specific customizations)

## Speed & Quality Trade-offs

The dual quality gate approach (Quality Reviewer + Devil's Advocate) adds one handoff per task:
- **Simple task** (e.g., customize colors): User → Specialist → Quality → Devil's Advocate → User (1 handoff)
- **Complex task** (e.g., site architecture): User → Specialist → Quality → Devil's Advocate → User (1 handoff)
- **Benefit**: High-quality output with critical thinking before user review
- **No user checkpoints**: Internal handoffs auto-send; only final work requires user review

## Hugo Domain Context

**Key Concepts for This Group**:
- Hugo generates static HTML from markdown + templates
- Configuration in config.toml or config.yaml
- Content in `/content/` directory (markdown files)
- Themes provide layouts/styling; customization via `/layouts/` overrides
- Front matter (YAML/TOML) provides post metadata
- Hugo CLI commands: `hugo new`, `hugo server`, `hugo build`
- No native comments, database, or dynamic content

## Workflow Iteration Scenarios

### Scenario 1: Quality Reviewer Finds Issues
1. Quality Reviewer returns work to Hugo Specialist with structured feedback
2. Hugo Specialist revises on same branch
3. Quality Reviewer re-reviews
4. If approved, goes to Devil's Advocate
5. If critical concerns, returns to Hugo Specialist

### Scenario 2: Devil's Advocate Surfaces Critical Concerns
1. Devil's Advocate returns work to Hugo Specialist for reconsideration
2. Hugo Specialist revises approach
3. Quality Reviewer re-reviews revised work
4. Devil's Advocate re-reviews after quality re-approval
5. Cycle continues until approved

### Scenario 3: Multiple Iterations Needed
- Quality issues → back to specialist
- Critical issues → back to specialist (Quality re-reviews)
- Both types → iterates until both gates satisfied
- Goal: Converge on quality solution, not checkpoint fatigue

## When to Use Each Agent

### Consult Hugo Specialist For:
- "How should I organize my blog?"
- "I want to customize my theme's colors"
- "My template is showing {{ .Title }} as text - what's wrong?"
- "What's the best Hugo configuration for performance?"
- "How do I create a custom shortcode?"

### Consult Content Creator For:
- "Write a blog post on X topic"
- "Generate content following this structure and tone"
- "Create pages for my site"
- "Generate content bundles with proper front matter"

### Consult WordPress Migrator For:
- "Convert my WordPress blog to Hugo"
- "Migrate 100+ posts from WordPress"
- "I have a WordPress export file and want Hugo content"

### Quality Reviewer Invoked Automatically For:
- Validating Hugo Specialist architectural guidance
- Validating Content Creator's generated posts
- Validating WordPress Migrator's conversion results

### Devil's Advocate Invoked Automatically For:
- Critical review after Quality Reviewer approval
- Challenging architectural assumptions
- Examining alternative approaches
- Documenting trade-offs and risks

## Summary: Dual Quality Gates

```
Specialist Work
      ↓
Quality Reviewer (systematic validation)
      ↓
Devil's Advocate (critical thinking)
      ↓
User Review (final decision)
```

Each gate has distinct responsibility:
- **Quality Reviewer**: "Does this meet standards?"
- **Devil's Advocate**: "Have we considered everything? Are assumptions correct?"
- **User**: "Does this work for my needs?"

This structure ensures both systematic validation and critical thinking are applied, improving final quality and user confidence in the output.
