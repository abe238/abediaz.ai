# Quick Spec: Fix Missing Flight Statistics Image

## Overview
The flight statistics visualization showing 50+ countries visited is not displaying on the HTML page. This is likely due to a broken image reference - either an incorrect file path or a missing image file. The fix involves locating the HTML page, identifying the image reference, and correcting the path or restoring the missing file.

## Workflow Type
feature

## Task Scope
1. Find the HTML page with flight statistics visualization
2. Identify the broken image reference (img src, image URL, or asset path)
3. Fix the image path (relative vs absolute) or restore missing image file
4. Verify the flight statistics visualization displays correctly with all 50+ countries visible

## Success Criteria
- [ ] HTML page with flight statistics is located and accessible
- [ ] Broken image reference is identified in code or browser console
- [ ] Image displays correctly on the page without 404 errors
- [ ] Full 50+ countries visualization is visible and rendered
- [ ] No broken image errors in browser console
- [ ] Fix is applied and verified in browser

## Task Details

### Files to Modify
- HTML page containing flight statistics (location to be discovered)
- Image file reference in HTML or related component
- Possible: CSS or asset configuration if image path is incorrect

### Change Details
1. Find the HTML page with flight statistics visualization
2. Identify the broken image reference (img src, image URL, or asset path)
3. Fix the image path or restore missing image file
4. Common fixes:
   - Correct relative/absolute path to image file
   - Verify image file exists in correct location
   - Update asset bundling configuration if needed

### Verification
- [ ] Navigate to HTML page in browser
- [ ] Flight statistics image displays correctly
- [ ] All 50+ countries visualization is visible
- [ ] No 404 or broken image errors in console

### Notes
- Requirements phase didn't provide specific file paths - discovery step needed
- Image is likely a PNG/SVG visualization or chart
- Check both HTML src attributes and CSS background-image properties
