# Document CI/CD workflow configuration and fix inconsistencies

## Overview

The GitHub Actions deploy.yml workflow references npm commands (npm ci, npm run build) but the project has no package.json. This workflow will fail on every push. The documentation should explain the intended deployment process.

## Rationale

The workflow configuration doesn't match the actual project structure (static HTML with no build step). This creates confusion and prevents automated deployments. Documentation should either explain the intended build setup or the workflow should be fixed for a static site deployment.

---
*This spec was created from ideation and is pending detailed specification.*
