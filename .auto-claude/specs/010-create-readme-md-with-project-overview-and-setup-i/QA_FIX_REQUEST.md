# QA Fix Request

**Status**: REJECTED
**Date**: 2026-01-01T09:55:00Z
**QA Session**: 1

## Critical Issues to Fix

### 1. Fix Deployment Workflow for Static Site

**Problem**: The `.github/workflows/deploy.yml` file contains Node.js build steps (npm ci, npm run build) that will fail because this is a static site with no package.json, no build process, and no dist/ directory.

**Location**: `.github/workflows/deploy.yml` lines 23-35

**Required Fix**: 
Remove the Node.js setup and build steps. Update the workflow to deploy static files directly from the repository root.

**Specific Changes**:
1. Remove lines 23-31 (Node.js setup, npm ci, npm run build steps)
2. Change line 35 from `path: ./dist` to `path: .`
3. Ensure the workflow checks out the repo and uploads the root directory to GitHub Pages

**Verification**: 
- Run the workflow and verify it completes without errors
- Confirm GitHub Pages deploys successfully
- Verify the live site at abediaz.ai loads correctly

---

### 2. Optimize Profile Image File Size

**Problem**: The `images/profile.jpg` file is 13 MB, causing slow page load times and poor user experience.

**Location**: `images/profile.jpg`

**Required Fix**:
Optimize the image to reduce file size while maintaining acceptable visual quality.

**Specific Changes**:
1. Resize image to appropriate display dimensions (500-800px wide is sufficient)
2. Compress with quality setting 80-85
3. Target file size: < 200 KB (ideally < 100 KB)

**Verification**:
- Check file size: `ls -lh images/profile.jpg`
- Visual inspection to confirm quality is acceptable
- Test page load time improvement

---

## After Fixes

Once fixes are complete:
1. Commit changes with message: "fix: update deployment workflow for static site and optimize profile image (qa-requested)"
2. QA will automatically re-run validation
3. Loop continues until approved

## Priority

**Issue 1 is CRITICAL** - must be fixed for production readiness. The deployment pipeline is currently broken.

**Issue 2 is MAJOR** - should be fixed for optimal user experience and performance.
