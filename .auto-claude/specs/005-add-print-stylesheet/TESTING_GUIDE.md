# Print Stylesheet Manual Testing Guide

## Overview
This guide provides step-by-step instructions for manually testing the print stylesheet implementation using browser print preview.

## Testing Instructions

### Step 1: Open the Page
1. Open `index.html` in your web browser
2. Ensure the page loads completely with all content visible

### Step 2: Access Print Preview
- **Chrome/Edge**: Press `Ctrl+P` (Windows) or `Cmd+P` (Mac)
- **Firefox**: Press `Ctrl+P` (Windows) or `Cmd+P` (Mac)
- **Safari**: Press `Cmd+P` (Mac)

### Step 3: Verify Print Settings
Ensure the following settings are configured:
- **Destination**: Save as PDF (or any printer)
- **Paper size**: Letter (8.5" x 11")
- **Margins**: Default
- **Scale**: 100%
- **Background graphics**: Optional (should work either way)

## Testing Checklist

### ✅ Layout & Structure
- [ ] Page displays in single-column layout (no side-by-side content)
- [ ] All content is within printable margins (0.75in on all sides)
- [ ] No horizontal scrolling or cut-off content
- [ ] Page breaks occur at natural section boundaries

### ✅ Hidden Elements (Should NOT be visible)
- [ ] Navigation menu (.site-nav) is hidden
- [ ] Share buttons (.share-section, .share-btn) are hidden
- [ ] Like buttons (.like-section, .like-btn) are hidden
- [ ] Email forms (.email-form) are hidden

### ✅ Typography
- [ ] Body text is in serif font (Georgia or Times New Roman)
- [ ] Font size is 12pt and readable
- [ ] Headings are properly sized and hierarchical:
  - H1 (name): 24pt
  - H2 tagline: 11pt
  - H2 section titles: 14pt
  - H3: 12pt
- [ ] Line height is comfortable (1.6 for paragraphs)
- [ ] All text is black (no colored text that might not print well)

### ✅ Links
- [ ] Links are underlined for visibility
- [ ] Important links show URLs in parentheses after link text
- [ ] Internal anchor links (#) do NOT show URLs
- [ ] Social media links format is appropriate

### ✅ Images
- [ ] Profile image prints at reasonable size (max 3 inches)
- [ ] Flight stats image is visible and properly sized
- [ ] Images do not split across pages
- [ ] Images maintain aspect ratio

### ✅ Contact Information
- [ ] Contact section is clearly visible
- [ ] LinkedIn link is visible and readable
- [ ] Twitter link is visible and readable
- [ ] Contact section appears on the printed output
- [ ] Contact information is not orphaned or split across pages

### ✅ Page Breaks
- [ ] No awkward breaks in the middle of sections
- [ ] Headings do not appear alone at bottom of page (orphaned)
- [ ] Widgets/sections are kept together
- [ ] No single lines at top/bottom of page (widows/orphans)
- [ ] Natural breaks occur after header and main content sections

### ✅ Overall Quality
- [ ] Print output looks professional
- [ ] Content is well-spaced and readable
- [ ] No overlapping elements
- [ ] No missing content
- [ ] Ready to be used as a resume/portfolio printout

## Browser-Specific Considerations

### Chrome/Edge
- Generally excellent print preview support
- Page break controls work well
- URL display via ::after works perfectly

### Firefox
- Good print preview support
- May handle page breaks slightly differently
- Test orphans/widows behavior

### Safari
- Print preview may differ slightly from final output
- Test on actual print or PDF export for accuracy
- Some CSS print features may have limited support

## Common Issues and Solutions

### Issue: URLs appear for social links
**Expected**: Social media URLs in contact section do NOT print (intentional to keep output clean)
**Actual**: If URLs do print, this is due to the CSS exclusion rule
**Note**: If you want social media URLs visible, remove or modify lines 679-682 in the print stylesheet

### Issue: Page breaks in wrong places
**Solution**: Adjust `break-after` and `break-inside` properties for affected elements

### Issue: Content too small/large
**Solution**: Adjust font-size values in pt units in the print stylesheet

### Issue: Margins too tight
**Solution**: Adjust @page margin value (currently 0.75in)

## Final Verification

After completing all checks, answer these questions:
1. Would you be comfortable handing this printout to a recruiter? ✅/❌
2. Is all important information visible and readable? ✅/❌
3. Does the layout look professional on paper? ✅/❌
4. Are there any awkward page breaks that need fixing? ✅/❌

If all answers are ✅, the print stylesheet is ready!

## Browser Testing Matrix

| Browser | Version | Tested | Status | Notes |
|---------|---------|--------|--------|-------|
| Chrome  | Latest  | ⬜     |        |       |
| Firefox | Latest  | ⬜     |        |       |
| Safari  | Latest  | ⬜     |        |       |
| Edge    | Latest  | ⬜     |        |       |

## Notes
Document any issues found during testing:
-
