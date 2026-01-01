# Quick Spec: Update GitHub Link

## Overview
This task involves updating all instances of an incorrect GitHub profile link across the entire codebase. The link `https://github.com/abediaz` must be changed to `https://github.com/abe238`. This is a straightforward find-and-replace operation that spans multiple files and file types, including HTML, React components, markdown files, configuration files, and meta tags.

## Workflow Type
Feature (correction/update)

## Task Scope
- **Old URL**: `https://github.com/abediaz`
- **New URL**: `https://github.com/abe238`
- **Coverage**: All files across the codebase containing the old GitHub URL
- **File Types to Search**: HTML, JSX/TSX, Markdown, JSON config files, and meta tags
- **Search Patterns**:
  - `https://github.com/abediaz` (full URL)
  - `github.com/abediaz` (protocol-agnostic)
  - `@abediaz` (GitHub handle references)

## Success Criteria
- ✅ All instances of `https://github.com/abediaz` are replaced with `https://github.com/abe238`
- ✅ All variations and references (github.com/abediaz, @abediaz) are updated where applicable
- ✅ No instances of the old GitHub handle remain in the codebase
- ✅ All updated links are functional and point to the correct GitHub profile
- ✅ No broken links or orphaned references are introduced
- ✅ Social/meta tags are updated if they contain the old URL

## Task
Update GitHub profile link from `https://github.com/abediaz` to `https://github.com/abe238` across all instances in the page/codebase.

## Files to Modify
- All files containing the old GitHub URL (to be identified via search)

## Change Details
Replace all instances of:
- `https://github.com/abediaz` → `https://github.com/abe238`
- Also replace variations: `github.com/abediaz`, `@abediaz` references (where applicable to GitHub handle)

Search comprehensively across HTML, React, markdown, config files, and meta tags.

## Verification
- [ ] All instances of old GitHub URL are updated
- [ ] New URL displays correctly on the page
- [ ] No broken links or orphaned references remain
- [ ] Social/meta tags updated if applicable

## Notes
- Use global search to find all instances
- Verify in browser that links work and point to correct profile
- Check footer, navigation, social links, and any about/contact sections
