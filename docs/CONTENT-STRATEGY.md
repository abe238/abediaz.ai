# Content Strategy Documentation

> **Last Updated:** January 2026
> **Purpose:** This document defines the content strategy for abediaz.ai, mapping documentation sources to website sections and establishing maintenance guidelines.

---

## Table of Contents

1. [📌 Source of Truth: Quick Reference](#-source-of-truth-quick-reference)
2. [Overview](#overview)
3. [Content Sources](#content-sources)
4. [Version History](#version-history)
5. [Website Section Mapping](#website-section-mapping)
6. [Maintenance Guidelines](#maintenance-guidelines)

---

## 📌 Source of Truth: Quick Reference

> **IMPORTANT:** `docs/abe-diaz-profile.md` is the **single authoritative source** for all professional information, career history, achievements, and biographical data.

### The Relationship

```
┌─────────────────────────────────┐
│  abe-diaz-profile.md            │
│  (AUTHORITATIVE SOURCE)         │
│  ✓ Complete professional data   │
│  ✓ Source of truth for facts    │
│  ✓ Comprehensive timeline       │
└────────────┬────────────────────┘
             │
             │ curates & selects
             │ (~30% utilization)
             ↓
┌─────────────────────────────────┐
│  index.html                     │
│  (PUBLIC PRESENTATION)          │
│  ✓ Minimalist narrative         │
│  ✓ Story-focused content        │
│  ✓ Selective details            │
└─────────────────────────────────┘
```

### Key Principles

1. **abe-diaz-profile.md is the master record**
   - All dates, titles, companies, and achievements originate here
   - This document maintains complete historical accuracy
   - Updates to professional information START here

2. **index.html presents a curated selection**
   - Content is derived from abe-diaz-profile.md
   - Transforms data into personal narrative
   - Intentionally shows ~30% of available information
   - Emphasizes human story over resume details

3. **When information conflicts, abe-diaz-profile.md wins**
   - Profile document is the tiebreaker for factual disputes
   - Website should be updated to match profile document
   - Known discrepancies are documented in Version History below

---

## Overview

### Purpose

This content strategy documentation serves to:

- **Clarify the relationship** between documentation in `docs/` and the live website (`index.html`)
- **Establish a source of truth** for profile and professional information
- **Provide clear mapping** between content sources and website sections
- **Define maintenance workflows** for keeping content synchronized and up-to-date
- **Document content philosophy** for each format (comprehensive vs. minimalist)

### Content Philosophy

The abediaz.ai website follows a **dual-content strategy**:

1. **Website (index.html)**: Minimalist, personal narrative approach
   - Focus on human story and personality
   - Conversational tone and storytelling
   - Selective professional details
   - Emphasis on personal interests and philosophy

2. **Profile Documentation (docs/)**: Comprehensive professional reference
   - Complete work history and timeline
   - Quantified impact and achievements
   - Skills taxonomy and expertise areas
   - Awards, press coverage, and recognition

These two formats serve different purposes and intentionally maintain different levels of detail.

---

## Content Sources

### Primary Sources

#### 1. `docs/abe-diaz-profile.md` ⭐ AUTHORITATIVE SOURCE

- **Status:** ✅ **Single Source of Truth**
- **Purpose:** Master record for all professional and biographical information
- **Authority Level:** **PRIMARY** - All other sources derive from or defer to this document
- **Last Updated:** December 2025

**What This Means:**
- This document is the **official record** for Abe Diaz's professional profile
- All dates, job titles, company names, and achievements are authoritative here
- When information differs between sources, **this document is correct**
- Updates to professional information **must start here** before being reflected elsewhere

**Content Coverage:**
  - ✅ Identity and branding (name, title, location, tagline)
  - ✅ Professional summary with career narrative
  - ✅ Impact & achievements (quantified metrics)
  - ✅ Complete work experience timeline (2009-Present)
  - ✅ Education details (degrees, institutions, years)
  - ✅ Skills taxonomy (Core, Technical, Soft Skills)
  - ✅ Open source projects portfolio
  - ✅ Volunteering history
  - ✅ Press & publications
  - ✅ Personal interests and philosophy
  - ✅ Social links

**Relationship to Website:**
- `index.html` is a **derivative work** that curates content from this source
- Website shows ~30% of the information contained here
- Website transforms structured data into narrative storytelling
- Website intentionally omits detailed professional history for minimalist design

#### 2. `index.html` 🌐 PUBLIC PRESENTATION

- **Status:** ✅ Live Website
- **Purpose:** Public-facing personal brand homepage
- **Authority Level:** **SECONDARY** - Derives content from `abe-diaz-profile.md`
- **Content Strategy:** Minimalist, story-driven presentation

**What This Means:**
- This is a **curated view** of information from `abe-diaz-profile.md`
- Content here is **intentionally selective** (shows ~30% of available data)
- Focuses on personal narrative rather than comprehensive resume
- Should be **synchronized with** but not equal to the profile document

**Content Coverage:**
  - ✓ Name and tagline (from profile Identity section)
  - ✓ Personal philosophy statement (from profile Personal section)
  - ✓ Selected career narrative (from profile Work Experience, story-focused)
  - ✓ Hurricane Maria pivot story (from profile Professional Summary)
  - ✓ Personal interests with external links (from profile Personal section)
  - ✓ Travel statistics (from profile Personal section, visual representation)
  - ✓ Social media links (subset of profile Social Links)

**Relationship to Profile Document:**
- Every fact on the website **originates from** `abe-diaz-profile.md`
- Website does NOT introduce new biographical information
- Website transforms structured profile data into conversational narrative
- Updates to website content should **verify against** profile document for accuracy

#### 3. `docs/content-mapping-analysis.md`
- **Status:** ✅ Reference Document
- **Purpose:** Technical mapping between profile and website
- **Content Coverage:**
  - Line-by-line content mapping
  - Identification of used vs. unused content
  - Discrepancy documentation
  - Content utilization rates
  - Strategic recommendations
- **Usage:** Reference for understanding content relationships and identifying sync issues

### Supporting Resources

- **External Links:**
  - [amazon.com/disasterrelief](https://amazon.com/disasterrelief) - Disaster Relief program
  - [jetitup.com/MyStats](https://jetitup.com/MyStats) - Travel statistics
  - Social media profiles (LinkedIn, Twitter, Instagram, GitHub)

---

## Version History

### Current Version (January 2026)

**Active Documents:**
- `docs/abe-diaz-profile.md` - Comprehensive profile (Dec 2025)
- `index.html` - Live website
- `docs/content-mapping-analysis.md` - Content mapping (Jan 2026)
- `docs/CONTENT-STRATEGY.md` - This document (Jan 2026)

**Recent Changes:**
- January 2026: Created content strategy documentation
- January 2026: Performed comprehensive content mapping analysis
- December 2025: Updated abe-diaz-profile.md with current role information

### Known Issues

#### 🔴 CRITICAL: Job Title Discrepancy
- **Profile Document:** "Sr. Manager - Disaster Relief" (Feb 2025 - Present)
- **Website:** "Sr. Technical Program Manager on the Disaster Relief by Amazon team"
- **Status:** ⚠️ Requires immediate attention
- **Action Required:** Update index.html to reflect current title

#### ⚠️ MINOR: Missing GitHub Link
- **Profile Document:** ✅ github.com/abe238
- **Website:** ❌ Not included in social links section
- **Status:** Low priority
- **Action Required:** Consider adding to complete social media presence

### Historical Context

Prior to this documentation effort:
- Multiple content sources existed without clear relationships
- No formal mapping between docs/ and website sections
- Content synchronization happened ad-hoc
- No established source of truth for professional information

---

## Website Section Mapping

### Content Usage Overview

**Utilization Rate:** ~30% of profile content appears on website (12 of 40+ data points)

### Detailed Section Mapping

#### Header Section (index.html lines 551-552)
| Website Content | Source | Profile Location | Alignment |
|-----------------|--------|------------------|-----------|
| "ABE DIAZ" | abe-diaz-profile.md | Identity → Name | ✅ Match |
| "Seattle/Tech/Evangelist" | abe-diaz-profile.md | Identity → Tagline | ✅ Match |

#### Meta & SEO (index.html lines 5-7, 16-19)
| Website Content | Source | Profile Location | Alignment |
|-----------------|--------|------------------|-----------|
| Meta description | abe-diaz-profile.md | Professional Summary | ⚠️ Outdated title |
| Twitter meta tags | abe-diaz-profile.md | Social Links → Twitter | ✅ Match |
| Open Graph tags | Custom | N/A | - |

#### About Me Section (index.html line 567)
| Website Content | Source | Profile Location | Alignment |
|-----------------|--------|------------------|-----------|
| Personal philosophy | abe-diaz-profile.md | Personal → Philosophy | ✅ Match |

#### Main Bio (index.html line 576)
| Website Content | Source | Profile Location | Alignment |
|-----------------|--------|------------------|-----------|
| Current role description | abe-diaz-profile.md | Work Experience → Amazon | ⚠️ Outdated title |
| Hurricane Maria story | abe-diaz-profile.md | Professional Summary → The Pivot | ✅ Match (expanded) |
| Disaster Relief team mention | abe-diaz-profile.md | Professional Summary → Mission | ✅ Match |
| MS Information Security | abe-diaz-profile.md | Education | ✅ Match |
| BS Computer Engineering | abe-diaz-profile.md | Education | ✅ Match |
| Deloitte experience | abe-diaz-profile.md | Work Experience → Deloitte | ✅ Match (narrative form) |
| NBCUniversal experience | abe-diaz-profile.md | Work Experience → NBCUniversal | ✅ Match (narrative form) |
| Prime Video experience | abe-diaz-profile.md | Work Experience → Amazon | ✅ Match (narrative form) |

#### Social Links (index.html line 578)
| Website Content | Source | Profile Location | Alignment |
|-----------------|--------|------------------|-----------|
| LinkedIn | abe-diaz-profile.md | Social Links → LinkedIn | ✅ Match |
| Twitter | abe-diaz-profile.md | Social Links → Twitter | ✅ Match |
| Instagram | abe-diaz-profile.md | Social Links → Instagram | ✅ Match |
| GitHub | abe-diaz-profile.md | Social Links → GitHub | ❌ Missing |

#### Likes/Interests Section (index.html line 580)
| Website Content | Source | Profile Location | Alignment |
|-----------------|--------|------------------|-----------|
| Traveling (with link) | abe-diaz-profile.md | Personal → Interests | ✅ Match (enhanced) |
| Cider (with link) | abe-diaz-profile.md | Personal → Interests | ✅ Match (enhanced) |
| RaspberryPis (with link) | abe-diaz-profile.md | Personal → Interests | ✅ Match (enhanced) |
| Ice Baths (with link) | abe-diaz-profile.md | Personal → Interests | ✅ Match (enhanced) |
| Contrast Showers (with link) | abe-diaz-profile.md | Personal → Interests | ✅ Match (enhanced) |

#### Flight Stats Visual (index.html lines 582-587)
| Website Content | Source | Profile Location | Alignment |
|-----------------|--------|------------------|-----------|
| Travel stats image | abe-diaz-profile.md | Personal → Travel Stats | ✅ Match (visual representation) |

#### Footer (index.html lines 596-597)
| Website Content | Source | Profile Location | Alignment |
|-----------------|--------|------------------|-----------|
| LinkedIn link | abe-diaz-profile.md | Social Links → LinkedIn | ✅ Match |
| Twitter link | abe-diaz-profile.md | Social Links → Twitter | ✅ Match |

### Content NOT Used on Website

The following content exists in `abe-diaz-profile.md` but is intentionally not included on the website, following the minimalist philosophy:

#### Professional Details (70% of profile content)
- ❌ **Impact & Achievements**: 200+ disaster relief efforts, 26+ million items delivered
- ❌ **Award**: "Seattle's 40 Under 40" (Puget Sound Business Journal, 2023)
- ❌ **Proactive Supply Pre-positioning strategy**
- ❌ **AWS Disaster Response scope expansion**
- ❌ **Partner organizations**: Red Cross, WCK, WFP (detailed partnerships)
- ❌ **Detailed work timeline**: Specific role dates and progression
- ❌ **Microsoft experience** (2013-2014)
- ❌ **AT&T Mobility experience** (2013)
- ❌ **Deloitte Software Engineer role** (2009-2011)

#### Skills & Expertise
- ❌ **Core Skills**: Disaster Relief, Philanthropy, Product Management, Technical Program Management
- ❌ **Technical Skills**: Mobile (iOS, Android, FireTV), Cloud/Logistics, .NET
- ❌ **Soft Skills**: Public Speaking, Developer Evangelism, Team Leadership, Process Automation

#### Education Details
- ❌ **Languages**: English (Native), Spanish (Native)
- ❌ **Activities**: IEEE, SHPE, ACM, ISACA
- ❌ **Graduation years**: 2009 (BS), 2012 (MS)

#### Open Source Projects
- ❌ **project-kickoff**: CLI scaffolding tool with security best practices
- ❌ **aipm-resume-analyzer**: Resume analysis tool using AI frameworks
- ❌ **yt-slides**: Universal video screenshot extractor
- ❌ **grandapi**: Raspberry Pi photo frame powered by Google Drive

#### Volunteering
- ❌ **Startup Weekend**: Event Organizer (2015-Present)
- ❌ **ALPFA, Inc (Seattle)**: VP of Technology (2015-2017)
- ❌ **Career Readiness Mentor**: Mentor Collective (2023)

#### Press & Publications
- ❌ **Seattle Times article** (Sep 2023): "Amazon wants to bring its delivery efficiency to disaster relief"
- ❌ **KUOW (NPR) feature** (Sep 2023): "Disaster relief delivered by Amazon"
- ❌ **Puget Sound Business Journal** (Apr 2023): "40 Under 40" Feature

---

## Maintenance Guidelines

### Source of Truth Hierarchy

1. **For current role/title information:**
   - Primary: LinkedIn profile (most frequently updated)
   - Secondary: Update abe-diaz-profile.md
   - Tertiary: Update index.html

2. **For professional history:**
   - Primary: abe-diaz-profile.md (authoritative)
   - Reference: LinkedIn profile for verification

3. **For personal interests:**
   - Primary: index.html (curated public list)
   - Archive: abe-diaz-profile.md

### Update Workflow

#### When Professional Information Changes

**Example:** Job title, company, or role changes

1. **Update abe-diaz-profile.md**
   - Update Work Experience section with new role
   - Update Identity table if title changes
   - Update Professional Summary if mission changes
   - Add "Last updated" date at top

2. **Update index.html**
   - Update meta description (line 7)
   - Update main bio section (line 576)
   - Test Open Graph preview
   - Verify SEO tags

3. **Document the change**
   - Update this CONTENT-STRATEGY.md → Version History section
   - Note change date and what was updated
   - Remove from "Known Issues" if applicable

4. **Verify alignment**
   - Run content comparison check
   - Update content-mapping-analysis.md if major changes

#### When Adding New Achievements

**Example:** New award, press coverage, or major accomplishment

1. **Add to abe-diaz-profile.md**
   - Add to appropriate section (Impact & Achievements, Press & Publications, etc.)
   - Maintain chronological order
   - Include dates and links

2. **Evaluate for website inclusion**
   - Consider: Does this align with minimalist philosophy?
   - Consider: Is this a top-tier achievement worth featuring?
   - If YES: Update index.html strategically
   - If NO: Keep in profile.md only (still valuable for reference)

3. **Update this document**
   - Add to Version History
   - Update Website Section Mapping if added to site

#### When Personal Interests Change

**Example:** New hobby, interest, or passion

1. **Update index.html first** (public-facing)
   - Modify Likes section
   - Add relevant external links
   - Keep list concise (5-6 items max)

2. **Update abe-diaz-profile.md** (archive)
   - Update Personal → Interests section
   - Maintain comprehensive list

### Best Practices

#### Content Consistency
- ✅ **DO** use abe-diaz-profile.md as the authoritative reference for dates, titles, and facts
- ✅ **DO** keep index.html focused on storytelling and human connection
- ✅ **DO** verify LinkedIn profile matches before major updates
- ❌ **DON'T** add detailed professional achievements to index.html unless strategic
- ❌ **DON'T** remove content from abe-diaz-profile.md (it's an archive)
- ❌ **DON'T** update one source without considering the other

#### Timing & Frequency
- **Immediate updates required for:**
  - Job title or company changes
  - Critical factual corrections

- **Quarterly review recommended for:**
  - New achievements or awards
  - Press coverage or publications
  - Volunteer roles or open source projects

- **Annual review recommended for:**
  - Overall content strategy alignment
  - Website philosophy and messaging
  - Unused content evaluation (should anything be added?)

#### Quality Checks

Before finalizing any content update:

- [ ] Verify factual accuracy (dates, titles, companies)
- [ ] Check spelling and grammar
- [ ] Test all external links
- [ ] Verify social media links are current
- [ ] Test responsive design if HTML changed
- [ ] Preview Open Graph tags
- [ ] Update "Last Updated" dates
- [ ] Document change in Version History

### Emergency Corrections

If critical misinformation is discovered:

1. **Immediately update index.html** (highest visibility)
2. **Update abe-diaz-profile.md** (source of truth)
3. **Document in Known Issues** (this document)
4. **Create dated note in Version History**
5. **Review LinkedIn profile** for consistency

### Review Schedule

- **Weekly:** Monitor for LinkedIn profile changes
- **Monthly:** Review Known Issues section
- **Quarterly:** Content alignment audit
- **Annually:** Full content strategy review

---

## Appendix

### Related Documentation
- `docs/content-mapping-analysis.md` - Detailed technical mapping analysis
- `docs/abe-diaz-profile.md` - Comprehensive professional profile
- `.auto-claude/specs/013-create-content-strategy-documentation-linking-docs/` - Project specification

### Contact & Questions

For questions about this content strategy:
- Review the content-mapping-analysis.md for detailed technical mappings
- Check Version History for recent changes
- Consult abe-diaz-profile.md for authoritative professional information

---

*This document was created as part of Spec #013: Create content strategy documentation linking docs/ to website sections.*
