# abediaz.ai

> **Personal Portfolio Website** | Seattle/Tech/Evangelist

[![Live Site](https://img.shields.io/badge/Live%20Site-abediaz.ai-36BCAB?style=for-the-badge&logo=web&logoColor=white)](https://abediaz.ai)
[![GitHub Pages](https://img.shields.io/badge/Hosted%20on-GitHub%20Pages-222222?style=for-the-badge&logo=github&logoColor=white)](https://pages.github.com/)

---

## Tech Stack

This portfolio is intentionally minimalist, prioritizing **performance**, **maintainability**, and **simplicity** over framework complexity.

### Core Technologies

- **Static HTML/CSS** - Single-file architecture (`index.html`) with inline CSS for zero build overhead and maximum performance
- **Oswald Google Font** - Bold, modern typeface from Google Fonts for heading typography
- **Responsive Design** - Mobile-first CSS with media queries supporting desktop (768px+), tablet, and mobile (480px, 360px) breakpoints
- **CSS Custom Properties** - Design system variables for colors, typography, spacing, and layout consistency
- **Semantic HTML5** - Accessible markup with proper meta tags, Open Graph, and Twitter Card support

### Deployment & Infrastructure

- **GitHub Pages** - Static site hosting with custom domain support
- **GitHub Actions** - Automated CI/CD pipeline that builds and deploys on every push to `main`
- **Custom Domain** - Professional branding via `abediaz.ai` with DNS configuration through CNAME

### Design Philosophy

**Why static HTML?**
- ⚡ **Performance** - Near-instant page loads with no JavaScript framework overhead
- 🔒 **Security** - Minimal attack surface with no backend or database
- 💰 **Cost** - Free hosting via GitHub Pages
- 🛠️ **Simplicity** - Easy to maintain, update, and understand
- ♿ **Accessibility** - Works everywhere, including low-bandwidth connections and assistive technologies

This architecture demonstrates that not every project needs a complex framework—sometimes the simplest solution is the best solution.

---

## Local Development

Since this is a **static HTML site** with no build process, getting started is remarkably simple. No Node.js, npm, or build tools required!

### Prerequisites

- **Modern web browser** (Chrome, Firefox, Safari, Edge)
- **Git** (for cloning the repository)
- *(Optional)* **Local web server** for advanced testing

### Clone the Repository

```bash
# Clone via HTTPS
git clone https://github.com/abediaz/abediaz.ai.git

# Or clone via SSH
git clone git@github.com:abediaz/abediaz.ai.git

# Navigate to the project directory
cd abediaz.ai
```

### Running Locally

You have multiple options for viewing the site locally:

#### Option 1: Direct File Access (Simplest)

Simply open `index.html` in your browser:

```bash
# macOS
open index.html

# Linux
xdg-open index.html

# Windows
start index.html
```

Or double-click `index.html` in your file explorer.

**Note:** This method works perfectly for this static site, but some advanced features (like service workers or certain CORS-restricted resources) may require a local server.

#### Option 2: Python HTTP Server

If you have Python installed (most macOS/Linux systems do by default):

```bash
# Python 3
python -m http.server 8000

# Python 2
python -m SimpleHTTPServer 8000
```

Then visit: [http://localhost:8000](http://localhost:8000)

#### Option 3: Node.js HTTP Server

If you have Node.js installed:

```bash
# Using npx (no installation required)
npx serve

# Or install serve globally
npm install -g serve
serve
```

Then visit: [http://localhost:3000](http://localhost:3000) (or the port shown in the output)

#### Option 4: VS Code Live Server

If you use Visual Studio Code:

1. Install the "Live Server" extension by Ritwick Dey
2. Right-click `index.html` and select "Open with Live Server"
3. The site will open automatically in your browser with live reload

### Making Changes

Since all code is in `index.html` with inline CSS, you can edit directly:

1. Open `index.html` in your favorite editor
2. Make your changes
3. Refresh your browser to see updates (or use live reload with a local server)

**No build step, no bundlers, no transpilation—just edit and refresh!**

---

## Deployment

This site is automatically deployed to **GitHub Pages** via a **GitHub Actions** CI/CD pipeline. Every push to the `main` branch triggers a new deployment, ensuring the live site is always up to date.

### How It Works

The deployment process uses the [`.github/workflows/deploy.yml`](.github/workflows/deploy.yml) workflow, which consists of two main jobs:

#### 1. Build Job

```yaml
- Checkout code from repository
- Set up Node.js environment (v20)
- Install dependencies (npm ci)
- Build the project (npm run build)
- Upload build artifacts to GitHub Pages
```

The build job runs on `ubuntu-latest` and prepares the static site for deployment by:
- Installing all npm dependencies from `package-lock.json`
- Running the build script to generate production-ready files in the `./dist` directory
- Uploading the `./dist` folder as a Pages artifact

#### 2. Deploy Job

```yaml
- Deploy the uploaded artifact to GitHub Pages
- Output the deployment URL
```

The deploy job waits for the build job to complete (`needs: build`) and then publishes the artifact to GitHub Pages using the official `actions/deploy-pages@v4` action.

### Deployment Triggers

The workflow automatically runs when:

- **Push to `main`** - Any commit pushed to the main branch triggers a deployment
- **Manual trigger** - Can be manually triggered via the GitHub Actions UI (`workflow_dispatch`)

### Custom Domain Configuration

The site is accessible via the custom domain **[abediaz.ai](https://abediaz.ai)**, configured through:

1. **CNAME File** - The [`CNAME`](CNAME) file in the repository root contains `abediaz.ai`, which tells GitHub Pages to serve the site at this custom domain
2. **DNS Configuration** - The domain registrar's DNS is configured with:
   - An `A` record (or `ALIAS`/`ANAME`) pointing to GitHub Pages' IP addresses
   - Or a `CNAME` record pointing to `<username>.github.io`

This combination ensures visitors can access the site at the professional branded domain rather than the default `*.github.io` URL.

### Deployment Permissions

The workflow requires specific permissions to deploy to GitHub Pages:

```yaml
permissions:
  contents: read    # Read repository contents
  pages: write      # Deploy to GitHub Pages
  id-token: write   # Verify deployment identity
```

These permissions follow the principle of least privilege, granting only what's necessary for the deployment process.

### Concurrency Control

To prevent conflicts, the workflow uses concurrency control:

```yaml
concurrency:
  group: "pages"
  cancel-in-progress: true
```

This ensures that if multiple deployments are triggered simultaneously, only the most recent one proceeds, canceling any in-progress deployments to avoid race conditions.

### Monitoring Deployments

You can monitor deployment status:

- **GitHub Actions Tab** - View real-time logs and deployment history at `https://github.com/<username>/abediaz.ai/actions`
- **Environments Tab** - Check the `github-pages` environment for deployment URLs and status
- **Commit Status** - Each commit shows a green checkmark (✓) when deployment succeeds

### Manual Deployment

To manually trigger a deployment without pushing code:

1. Go to the **Actions** tab in the GitHub repository
2. Select the **"Deploy to GitHub Pages"** workflow
3. Click **"Run workflow"** and select the `main` branch
4. Click the green **"Run workflow"** button

This is useful for redeploying after configuration changes or troubleshooting deployment issues.

---

## Overview

This is the personal portfolio website for **Abe Diaz**, a passionate technologist and Sr. Technical Program Manager on the Disaster Relief by Amazon team. The site serves as a professional online presence showcasing technical expertise, leadership experience, and personal interests.

**Purpose:** This portfolio targets recruiters and hiring managers at leading AI companies including Anthropic, OpenAI, and DeepMind, demonstrating both technical capabilities and attention to detail through clean, purposeful design and implementation.

**Live Site:** [abediaz.ai](https://abediaz.ai)

### Key Highlights

- 🎨 **Clean, Professional Design** - Modern aesthetic with thoughtful typography and color system
- 📱 **Fully Responsive** - Optimized experience across desktop, tablet, and mobile devices
- ⚡ **Performance Focused** - Static HTML for fast loading and optimal user experience
- 🚀 **Modern Deployment** - Automated CI/CD pipeline via GitHub Actions
- 🌐 **Custom Domain** - Professional branding with custom domain configuration

---
