# Deployment Guide

## Overview

This repository uses **GitHub Actions** to automatically deploy a static HTML site to **GitHub Pages**. The site is hosted at [https://abediaz.ai](https://abediaz.ai) using a custom domain configuration.

## Site Structure

This is a **static site** with no build process required. All content is served directly from the repository root:

```
.
├── index.html          # Main landing page
├── CNAME              # Custom domain configuration (abediaz.ai)
├── images/            # Image assets
│   ├── profile.jpg    # Profile photo
│   └── flight-stats.png # Flight statistics infographic
├── docs/              # Additional documentation
│   └── abe-diaz-profile.md
└── .github/
    └── workflows/
        └── deploy.yml  # GitHub Actions deployment workflow
```

### Key Files

- **index.html**: Self-contained HTML file with embedded CSS (no external stylesheets)
- **CNAME**: Configures the custom domain `abediaz.ai` for GitHub Pages
- **images/**: Static image assets referenced by the site
- **docs/**: Additional Markdown documentation files

## Deployment Workflow

### Automatic Deployment

The site automatically deploys when changes are pushed to the `main` branch:

1. **Trigger**: Push to `main` branch or manual workflow dispatch
2. **Build Job**:
   - Checks out the repository code
   - Uploads the entire root directory (`.`) as a GitHub Pages artifact
3. **Deploy Job**:
   - Deploys the artifact to GitHub Pages
   - Updates the live site at `https://abediaz.ai`

### Workflow File: `.github/workflows/deploy.yml`

```yaml
name: Deploy to GitHub Pages

on:
  push:
    branches: [ main ]  # Auto-deploy on push to main
  workflow_dispatch:     # Allow manual deployment

permissions:
  contents: read         # Read repository contents
  pages: write          # Write to GitHub Pages
  id-token: write       # Required for GitHub Pages deployment

concurrency:
  group: "pages"
  cancel-in-progress: true  # Cancel any in-progress deployments

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4
      - name: Upload artifact
        uses: actions/upload-pages-artifact@v3
        with:
          path: .  # Upload entire root directory

  deploy:
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    needs: build
    runs-on: ubuntu-latest
    steps:
      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4
```

### Why No Build Step?

This site is **pure static HTML** with:
- ✅ Self-contained HTML with embedded CSS
- ✅ No JavaScript frameworks (React, Vue, etc.)
- ✅ No CSS preprocessors (Sass, Less)
- ✅ No package.json or npm dependencies
- ✅ No transpilation or bundling required

The workflow simply uploads the files as-is and deploys them directly to GitHub Pages.

## GitHub Pages Configuration

### Repository Settings

To configure GitHub Pages in your repository:

1. Navigate to **Settings** → **Pages**
2. Set **Source** to "GitHub Actions"
3. The custom domain `abediaz.ai` is configured via the `CNAME` file

### Custom Domain Setup

The site uses the custom domain **abediaz.ai**:

1. **CNAME File**: Contains the domain name `abediaz.ai`
2. **DNS Configuration**: The domain's DNS records must point to GitHub Pages:
   ```
   Type: A
   Name: @
   Value: 185.199.108.153
          185.199.109.153
          185.199.110.153
          185.199.111.153

   Type: CNAME
   Name: www
   Value: <username>.github.io
   ```
3. **GitHub Setting**: Custom domain is enforced in repository settings

## Manual Deployment

To manually trigger a deployment:

1. Go to **Actions** tab in the GitHub repository
2. Select **Deploy to GitHub Pages** workflow
3. Click **Run workflow** → **Run workflow**

## Monitoring Deployments

### View Deployment Status

1. **Actions Tab**: Shows all workflow runs and their status
2. **Environments**: Check the `github-pages` environment for deployment history
3. **Status Badge**: Add to README for at-a-glance status:
   ```markdown
   ![Deploy Status](https://github.com/<username>/<repo>/actions/workflows/deploy.yml/badge.svg)
   ```

### Deployment URL

After successful deployment, the site is available at:
- **Custom Domain**: https://abediaz.ai
- **GitHub Pages URL**: https://\<username\>.github.io/\<repository\>

## Troubleshooting

### Deployment Fails

**Check the Actions tab** for error details:

1. **Permissions Error**: Ensure repository settings have GitHub Pages enabled
2. **CNAME Issues**: Verify the CNAME file contains only the domain name (no protocol or path)
3. **File Not Found**: Check that all referenced assets exist (images, links)

### Common Issues

| Issue | Solution |
|-------|----------|
| 404 errors on assets | Verify file paths in index.html match repository structure |
| Custom domain not working | Check DNS configuration and wait for propagation (up to 24 hours) |
| Deployment stuck | Cancel in-progress runs and retry (concurrency control prevents conflicts) |
| Changes not appearing | Hard refresh browser (Ctrl+F5) to bypass cache |

### Workflow Validation

To validate the workflow syntax locally:

```bash
# Install actionlint (GitHub Actions linter)
brew install actionlint  # macOS
# or download from https://github.com/rhysd/actionlint

# Validate workflow
actionlint .github/workflows/deploy.yml
```

### Testing Locally

To preview the site locally before deploying:

```bash
# Option 1: Python's built-in server
python3 -m http.server 8000

# Option 2: Node.js http-server (if installed)
npx http-server

# Option 3: VS Code Live Server extension
# Install "Live Server" extension and click "Go Live"
```

Then open http://localhost:8000 in your browser.

## Making Changes

### Content Updates

1. **Edit index.html**: Update content, styling, or structure
2. **Add Images**: Place in `images/` directory and reference in HTML
3. **Update Docs**: Modify or add Markdown files in `docs/`

### Deployment Process

```bash
# 1. Make changes to files
git add .
git commit -m "Update site content"

# 2. Push to main branch (triggers auto-deployment)
git push origin main

# 3. Monitor deployment in Actions tab
# 4. Verify changes at https://abediaz.ai (allow 1-2 minutes)
```

## Security & Best Practices

### Workflow Security

- ✅ **Minimal Permissions**: Workflow uses least-privilege permissions
- ✅ **Pinned Actions**: Uses specific action versions (@v4, @v3)
- ✅ **Concurrency Control**: Prevents conflicting deployments
- ✅ **Environment Protection**: Uses `github-pages` environment

### Performance Optimization

- ✅ **Lazy Loading**: Images use `loading="lazy"` attribute
- ✅ **Efficient CSS**: Embedded CSS reduces HTTP requests
- ✅ **CDN Fonts**: Google Fonts loaded from CDN
- ✅ **Minimal Assets**: Only essential images included

## Additional Resources

- [GitHub Pages Documentation](https://docs.github.com/en/pages)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Custom Domains Guide](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site)
- [GitHub Actions Workflow Syntax](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions)

## Support

For issues or questions:
- **GitHub Issues**: Open an issue in this repository
- **GitHub Pages Status**: Check [GitHub Status](https://www.githubstatus.com/)
- **DNS Propagation**: Use [DNS Checker](https://dnschecker.org/) to verify DNS changes
