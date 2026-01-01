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

**Quick Stats:**
- ✅ **Used on Website**: 12 content elements from `abe-diaz-profile.md`
- ❌ **Not Used**: 28+ content elements remain in profile only
- ⚠️ **Discrepancies**: 2 alignment issues (outdated job title)

---

## 📊 Complete Website-to-Docs Mapping Table

This comprehensive table maps every content element on the website to its source in the documentation, showing alignment status and notes.

| # | Website Section | Website Content | HTML Location | Docs Source | Profile Section | Alignment | Notes |
|---|----------------|-----------------|---------------|-------------|-----------------|-----------|-------|
| **HEADER & NAVIGATION** |
| 1 | Page Title | "Abe Diaz \| Seattle/Tech/Evangelist" | line 6 | abe-diaz-profile.md | Identity → Name + Tagline | ✅ Match | Used in browser tab |
| 2 | H1 Header | "ABE DIAZ" | line 551 | abe-diaz-profile.md | Identity → Name | ✅ Match | Site header, uppercase |
| 3 | Tagline | "Seattle/Tech/Evangelist" | line 552 | abe-diaz-profile.md | Identity → Tagline | ✅ Match | Subheader below name |
| 4 | Navigation | "HOME" link | line 556 | Custom | N/A | - | Static navigation element |
| **META & SEO** |
| 5 | Meta Description | "A passionate technologist. Sr. Technical Program Manager..." | line 7 | abe-diaz-profile.md | Professional Summary + Work Experience | ⚠️ **Outdated** | Shows old title, needs update to "Sr. Manager - Disaster Relief" |
| 6 | OG Title | "Abe Diaz" | line 10 | abe-diaz-profile.md | Identity → Name | ✅ Match | Open Graph for social sharing |
| 7 | OG Description | "Seattle/Tech/Evangelist" | line 11 | abe-diaz-profile.md | Identity → Tagline | ✅ Match | Social preview text |
| 8 | OG Image | profile.jpg | line 14 | Custom | N/A | ✅ Match | Profile photo (external asset) |
| 9 | Twitter Card | @abe238 | lines 17-19 | abe-diaz-profile.md | Social Links → Twitter | ✅ Match | Twitter handle for cards |
| **ABOUT ME SECTION** |
| 10 | Section Title | "ABOUT ME" | line 565 | Custom | N/A | - | Section header |
| 11 | Philosophy | "A passionate technologist. I attend as many conferences..." | line 567 | abe-diaz-profile.md | Personal → Philosophy | ✅ Match | Personal mission statement |
| 12 | Profile Image | profile.jpg | lines 569-574 | External Asset | N/A | ✅ Present | Photo hosted in /images/ |
| **MAIN BIO PARAGRAPH** |
| 13 | Current Role | "Sr. Technical Program Manager on the Disaster Relief by Amazon team" | line 576 | abe-diaz-profile.md | Work Experience → Amazon | ⚠️ **Outdated** | Should be "Sr. Manager - Disaster Relief" (as of Feb 2025) |
| 14 | Origin Story | "Born and raised in Puerto Rico" | line 576 | abe-diaz-profile.md | Professional Summary → The Pivot | ✅ Match | Geographic background |
| 15 | BS Degree | "BS in Computer Engineering from UPR-Mayaguez" | line 576 | abe-diaz-profile.md | Education → BS | ✅ Match | Includes university link |
| 16 | MS Degree | "MS in Information Security from Lipscomb University" | line 576 | abe-diaz-profile.md | Education → MS | ✅ Match | Graduate degree |
| 17 | Deloitte Experience | "mobile technologies...Deloitte...enterprise app marketplace, 40+ apps, iPad apps for CEO" | line 576 | abe-diaz-profile.md | Work Experience → Deloitte | ✅ Match | Narrative form, condensed timeline |
| 18 | NBC Experience | "NBC News as mobile program manager" | line 576 | abe-diaz-profile.md | Work Experience → NBCUniversal | ✅ Match | Company name simplified |
| 19 | Amazon PV Experience | "Prime Video...payments, royalties and revenue automation" | line 576 | abe-diaz-profile.md | Work Experience → Amazon | ✅ Match | Earlier Amazon role mentioned |
| 20 | Hurricane Maria Story | "2017...technical volunteer...plane with relief items for Puerto Rico after Hurricane Maria" | line 576 | abe-diaz-profile.md | Professional Summary → The Pivot | ✅ Match | Expanded narrative form with link |
| 21 | Disaster Relief Transition | "experience of a lifetime...decided to join the Disaster Relief by Amazon team permanently" | line 576 | abe-diaz-profile.md | Professional Summary → The Pivot | ✅ Match | Career turning point story |
| 22 | Current Responsibilities | "in charge of...corporate in-kind donations and mobile disaster pickup points program" | line 576 | abe-diaz-profile.md | Work Experience → Amazon | ⚠️ Partial | May be outdated based on current "Sr. Manager" role |
| **SOCIAL CTA PARAGRAPH** |
| 23 | LinkedIn CTA | "check out my LinkedIn page http://linkedin.com/in/abediaz" | line 578 | abe-diaz-profile.md | Social Links → LinkedIn | ✅ Match | Call-to-action with link |
| 24 | Instagram CTA | "follow me on Instagram http://instagram.com/abe238" | line 578 | abe-diaz-profile.md | Social Links → Instagram | ✅ Match | Social media invitation |
| 25 | Twitter CTA | "Twitter http://twitter.com/abe238" | line 578 | abe-diaz-profile.md | Social Links → Twitter | ✅ Match | Social media link |
| **LIKES/INTERESTS** |
| 26 | Likes - Traveling | "Traveling (see stats below)" | line 580 | abe-diaz-profile.md | Personal → Interests | ✅ Match | Links to jetitup.com stats |
| 27 | Likes - Cider | "Cider" (links to Locust Cider) | line 580 | abe-diaz-profile.md | Personal → Interests | ✅ Match | Enhanced with brand link |
| 28 | Likes - RaspberryPis | "RaspberryPis" (links to raspberrypi.org) | line 580 | abe-diaz-profile.md | Personal → Interests | ✅ Match | Tech hobby with link |
| 29 | Likes - Ice Baths | "Ice Baths" (links to Wikipedia) | line 580 | abe-diaz-profile.md | Personal → Interests | ✅ Match | Wellness interest with reference |
| 30 | Likes - Contrast Showers | "Contrast Showers" (links to contrastshowers.com) | line 580 | abe-diaz-profile.md | Personal → Interests | ✅ Match | Wellness practice with link |
| **FLIGHT STATS VISUAL** |
| 31 | Flight Stats Image | flight-stats.png infographic | lines 582-587 | abe-diaz-profile.md | Personal → Travel Stats | ✅ Match | Visual representation of: 61 days in air, 626,410 miles, 25x around world |
| **CONTACT FOOTER** |
| 32 | Footer Title | "CONTACT ME:" | line 594 | Custom | N/A | - | Section header |
| 33 | Footer LinkedIn | "LinkedIn" link | line 596 | abe-diaz-profile.md | Social Links → LinkedIn | ✅ Match | Repeated from CTA section |
| 34 | Footer Twitter | "Twitter" link | line 597 | abe-diaz-profile.md | Social Links → Twitter | ✅ Match | Repeated from CTA section |

---

## 📋 Content Available in Docs But NOT on Website

The following content exists in `abe-diaz-profile.md` but is **intentionally excluded** from the website, following the minimalist philosophy. This represents approximately **70% of the profile content**.

### Identity & Branding (Profile Section: Identity)
| Content | Profile Location | Reason for Exclusion |
|---------|------------------|---------------------|
| **Languages**: English (Native), Spanish (Native) | Identity table | Not essential for minimalist site |

### Professional Impact (Profile Section: Impact & Achievements)
| Content | Profile Location | Reason for Exclusion |
|---------|------------------|---------------------|
| **200+** disaster relief efforts worldwide | Impact & Achievements | Intentional - minimalist philosophy |
| **26+ million** relief items delivered | Impact & Achievements | Quantified metric, too resume-like |
| **"Seattle's 40 Under 40"** award (2023) | Impact & Achievements | Award not featured on minimalist site |
| Pioneered "Proactive Supply Pre-positioning" strategy | Impact & Achievements | Technical detail |
| Expanded scope to include AWS Disaster Response | Impact & Achievements | Professional detail |
| Partners: Red Cross, WCK, WFP | Impact & Achievements | Partnership details |

### Work Experience Timeline (Profile Section: Work Experience)
| Content | Profile Location | Reason for Exclusion |
|---------|------------------|---------------------|
| Specific role dates and progression at Amazon | Work Experience → Amazon table | Timeline details unnecessary for story |
| **Microsoft** (2013-2014): CS Program Manager | Work Experience → Microsoft | Older role, not core narrative |
| **AT&T Mobility** (2013): Developer Evangelist/Advocate | Work Experience → AT&T | Short tenure, less relevant |
| **Deloitte** Software Engineer role (2009-2011) | Work Experience → Deloitte | Entry-level role, included only Business Analyst role |
| NBCUniversal platforms: tvOS, FireTV, Roku details | Work Experience → NBCUniversal | Technical platform specifics |

### Education Details (Profile Section: Education)
| Content | Profile Location | Reason for Exclusion |
|---------|------------------|---------------------|
| Graduation years: 2009 (BS), 2012 (MS) | Education table | Dates not essential |
| **Activities**: IEEE, SHPE, ACM, ISACA | Education table | Professional organizations |

### Skills Taxonomy (Profile Section: Skills)
| Content | Profile Location | Reason for Exclusion |
|---------|------------------|---------------------|
| **Core Skills**: Disaster Relief, Philanthropy, Product Management, TPM | Skills → Core | Skills list feels resume-like |
| **Technical Skills**: Mobile (iOS, Android, FireTV), Cloud/Logistics, .NET | Skills → Technical | Technical details |
| **Soft Skills**: Public Speaking, Developer Evangelism, Team Leadership, Process Automation | Skills → Soft Skills | Soft skill enumeration |

### Open Source Portfolio (Profile Section: Open Source)
| Content | Profile Location | Reason for Exclusion |
|---------|------------------|---------------------|
| [project-kickoff](https://github.com/abe238/project-kickoff) - CLI scaffolding tool | Open Source table | Project portfolio not featured |
| [aipm-resume-analyzer](https://github.com/abe238/aipm-resume-analyzer) - Resume analysis with AI | Open Source table | Side project details |
| [yt-slides](https://github.com/abe238/yt-slides) - Video screenshot extractor | Open Source table | Tool description |
| [grandapi](https://github.com/abe238/grandapi) - Raspberry Pi photo frame | Open Source table | Personal project |

### Volunteering History (Profile Section: Volunteering)
| Content | Profile Location | Reason for Exclusion |
|---------|------------------|---------------------|
| **Startup Weekend**: Event Organizer (2015-Present) | Volunteering table | Volunteer roles not on site |
| **ALPFA, Inc (Seattle)**: VP of Technology (2015-2017) | Volunteering table | Leadership role detail |
| **Career Readiness Mentor**: Mentor Collective (2023) | Volunteering table | Recent mentoring |

### Press & Publications (Profile Section: Press & Publications)
| Content | Profile Location | Reason for Exclusion |
|---------|------------------|---------------------|
| **Seattle Times** article (Sep 2023): "Amazon wants to bring its delivery efficiency to disaster relief" | Press & Publications table | Press coverage not featured |
| **KUOW (NPR)** feature (Sep 2023): "Disaster relief delivered by Amazon" | Press & Publications table | Media appearance |
| **Puget Sound Business Journal** (Apr 2023): "40 Under 40" Feature | Press & Publications table | Award coverage |

### Social Media (Profile Section: Social Links)
| Content | Profile Location | Reason for Exclusion |
|---------|------------------|---------------------|
| **GitHub**: github.com/abe238 | Social Links table | ❌ **Missing** - should be added |
| **Website**: abediaz.ai (self-reference) | Social Links table | Circular reference |

---

### Summary Statistics

**Website Utilization:**
- ✅ **34 content elements** on website
- ✅ **32 elements** sourced from `abe-diaz-profile.md` (94%)
- ⚠️ **2 custom elements**: Navigation, section headers
- ⚠️ **2 outdated elements**: Job title in meta description and bio paragraph

**Profile Content NOT Used:**
- ❌ **1 identity detail** (languages)
- ❌ **6 impact metrics** (quantified achievements, awards, partnerships)
- ❌ **5 work experience details** (role dates, older positions, technical specifics)
- ❌ **2 education details** (graduation years, activities)
- ❌ **3 skills categories** (core, technical, soft skills taxonomy)
- ❌ **4 open source projects** (entire portfolio)
- ❌ **3 volunteering roles** (entire history)
- ❌ **3 press mentions** (all media coverage)
- ❌ **1 social link** (GitHub - should be considered for addition)

**Total Unused:** ~28 content elements (70% of profile content)

---

## Maintenance Guidelines

### Content Update Priority & Sequencing

> **TL;DR:** For factual updates → Update docs first. For creative/personal content → Update website first. Always sync both within 24 hours.

#### The Golden Rule: Update Order Matters

Different types of content have different update priorities. Follow this decision tree:

```
┌─────────────────────────────────────────┐
│   What type of content are you updating? │
└────────────┬────────────────────────────┘
             │
        ┌────┴────┐
        │         │
   FACTUAL    CREATIVE/PERSONAL
   UPDATES    UPDATES
        │         │
        ↓         ↓
   ┌────────┐  ┌────────┐
   │ DOCS   │  │WEBSITE │
   │ FIRST  │  │ FIRST  │
   └───┬────┘  └────┬───┘
       │            │
       ↓            ↓
   ┌────────┐  ┌────────┐
   │WEBSITE │  │  DOCS  │
   │ SECOND │  │ SECOND │
   └────────┘  └────────┘
```

---

#### Scenario 1: Factual/Professional Updates → **DOCS FIRST**

**Update Order:** `abe-diaz-profile.md` → `index.html` → Verify alignment

**When to use this workflow:**
- Job title, role, or company changes
- Work experience updates (dates, responsibilities)
- Education or certification additions
- Contact information changes
- Achievements, awards, or metrics
- Press coverage or publications
- Skills or expertise updates

**Why docs first?**
- `abe-diaz-profile.md` is the **authoritative source of truth**
- Establishes the factual record before public presentation
- Prevents discrepancies from being introduced
- Creates audit trail for professional history
- Enables verification before website publication

**Step-by-step process:**

1. **Update `abe-diaz-profile.md` FIRST** ⭐ PRIMARY SOURCE
   ```
   ✓ Update the relevant section (Work Experience, Education, etc.)
   ✓ Verify dates, titles, and facts are accurate
   ✓ Add "Last updated: [Month Year]" at top of document
   ✓ Save and commit changes with descriptive message
   ```

2. **Review and sync to `index.html` SECOND** 📝 DERIVATIVE
   ```
   ✓ Identify which website sections need updates (use mapping table)
   ✓ Update website content to match profile.md facts
   ✓ Transform data into narrative form (website is story-focused)
   ✓ Update meta description and SEO tags if needed
   ✓ Verify all changes align with minimalist philosophy
   ```

3. **Verify alignment THIRD** ✅ QUALITY CHECK
   ```
   ✓ Check that facts match between both sources
   ✓ Ensure dates, titles, companies are identical
   ✓ Test all links and references
   ✓ Preview website changes locally
   ✓ Update CONTENT-STRATEGY.md → Version History section
   ```

**Example:**
```
Change: Promotion to "Senior Manager - Disaster Relief"

Step 1: Update abe-diaz-profile.md
  → Work Experience table: Add new role with Feb 2025 date
  → Identity table: Update current title
  → Professional Summary: Update if mission changed

Step 2: Update index.html
  → Line 7 (meta description): Update title
  → Line 576 (main bio): Update role description
  → Verify Open Graph tags

Step 3: Verify
  → Confirm title matches across both files
  → Test website preview
  → Update CONTENT-STRATEGY.md Version History
```

---

#### Scenario 2: Creative/Personal Updates → **WEBSITE FIRST**

**Update Order:** `index.html` → `abe-diaz-profile.md` → Document change

**When to use this workflow:**
- Personal interests or hobbies (Likes section)
- Creative biography text or storytelling
- Website design or layout changes
- New external link curation
- Personal philosophy statements
- Narrative tone adjustments

**Why website first?**
- `index.html` is the **public presentation layer**
- Personal interests are curated for public consumption
- Creative content is written for the website context
- Profile.md serves as archive, not creative source
- Allows experimentation with public messaging

**Step-by-step process:**

1. **Update `index.html` FIRST** 🌐 PUBLIC FACING
   ```
   ✓ Modify the relevant section (Likes, About Me, etc.)
   ✓ Ensure new content fits minimalist philosophy
   ✓ Add/update external links if needed
   ✓ Test responsive design and mobile view
   ✓ Preview changes before publishing
   ```

2. **Archive to `abe-diaz-profile.md` SECOND** 📚 HISTORICAL RECORD
   ```
   ✓ Update Personal section to match website
   ✓ Maintain comprehensive list (profile can have more detail)
   ✓ Keep historical interests even if removed from website
   ✓ Add date note for when interest was added/changed
   ```

3. **Document the change THIRD** 📋 MAINTENANCE LOG
   ```
   ✓ Update CONTENT-STRATEGY.md → Version History
   ✓ Note what was changed and when
   ✓ Update mapping table if structure changed significantly
   ```

**Example:**
```
Change: Add new interest "Sailing" to Likes section

Step 1: Update index.html
  → Line 580: Add "Sailing" with link to sailing.org
  → Ensure list stays concise (5-6 items max)
  → Remove older interest if list gets too long

Step 2: Update abe-diaz-profile.md
  → Personal → Interests: Add "Sailing" with context
  → Keep removed interest in profile (archive purpose)

Step 3: Document
  → Update Version History with change date
```

---

#### Scenario 3: Critical Corrections → **WEBSITE IMMEDIATELY, DOCS NEXT**

**Update Order:** `index.html` (immediate) → `abe-diaz-profile.md` (within 1 hour) → Document issue

**When to use this workflow:**
- Factual errors discovered on live site
- Broken critical links
- Misinformation that could cause confusion
- Privacy or security concerns
- Legal or compliance issues

**Why website first in emergencies?**
- `index.html` has **highest visibility** (public facing)
- Minimize duration of incorrect information
- Fix public issue before updating internal docs
- Exception to normal "docs first" rule for factual updates

**Step-by-step process:**

1. **FIX `index.html` IMMEDIATELY** 🚨 EMERGENCY
   ```
   ✓ Correct the error or broken content
   ✓ Test fix works correctly
   ✓ Deploy/publish changes immediately
   ✓ Note what was changed and why
   ```

2. **UPDATE `abe-diaz-profile.md` WITHIN 1 HOUR** 📝 RESTORE ALIGNMENT
   ```
   ✓ Correct the same information in profile.md
   ✓ Ensure both sources now match
   ✓ Add note about when error was corrected
   ```

3. **DOCUMENT IN KNOWN ISSUES** ⚠️ TRANSPARENCY
   ```
   ✓ Add to CONTENT-STRATEGY.md → Known Issues (if needed)
   ✓ Add dated entry to Version History
   ✓ Note: Error, correction date, and what was fixed
   ✓ Review why error occurred (prevent future issues)
   ```

**Example:**
```
Issue: Website shows old employer name after acquisition

Step 1: Fix index.html immediately
  → Update company name throughout site
  → Test all references and links
  → Publish changes

Step 2: Update abe-diaz-profile.md within 1 hour
  → Correct Work Experience section
  → Ensure dates and facts align with website

Step 3: Document the correction
  → Add to Version History: "Corrected employer name [date]"
  → Review content sync process to prevent future drift
```

---

#### Keeping Content in Sync: Best Practices

##### Daily Habits
- ✅ **Make updates in pairs**: Never update one source without considering the other
- ✅ **Use the mapping table**: Reference Website Section Mapping to find related content
- ✅ **Commit with context**: Git commit messages should mention which sources were updated
- ✅ **Set reminders**: If you update one source, schedule the second update within 24 hours

##### Weekly Habits
- ✅ **Spot check alignment**: Compare 3-5 random facts between docs and website
- ✅ **Test all links**: Run link checker on both profile.md and index.html
- ✅ **Review Known Issues**: Check if any documented issues can be resolved

##### Monthly Habits
- ✅ **Full content audit**: Review all sections for alignment (use mapping table as checklist)
- ✅ **Update Version History**: Document all changes made during the month
- ✅ **Check external sources**: Verify LinkedIn profile matches docs/website

##### Quarterly Habits
- ✅ **Strategic review**: Evaluate if any unused profile content should be added to website
- ✅ **Philosophy check**: Ensure website still follows minimalist principles
- ✅ **Link rot scan**: Check all external links in both sources for broken URLs

##### Annual Habits
- ✅ **Complete overhaul review**: Full audit of content strategy effectiveness
- ✅ **Archive old content**: Move outdated information to archive section in profile.md
- ✅ **Redesign consideration**: Evaluate if website structure still serves goals

---

#### Content Synchronization Checklist

Use this checklist every time you make a content update:

**Before Making Changes:**
- [ ] Identify update type: Factual, Creative, or Emergency?
- [ ] Determine correct update order based on type
- [ ] Review mapping table to identify all affected sections
- [ ] Check if change affects SEO or meta tags

**During Updates:**
- [ ] Update primary source first (based on type)
- [ ] Transform content appropriately for each format
  - Docs: Structured, comprehensive, data-focused
  - Website: Narrative, minimalist, story-focused
- [ ] Maintain consistent facts across both sources
- [ ] Update "Last updated" dates

**After Updates:**
- [ ] Update secondary source within 24 hours
- [ ] Verify facts match between both sources
- [ ] Test all new/modified links
- [ ] Update CONTENT-STRATEGY.md → Version History
- [ ] Update mapping table if structure changed
- [ ] Commit changes with descriptive messages

**Quality Verification:**
- [ ] Spelling and grammar check
- [ ] Factual accuracy verification
- [ ] Link testing (internal and external)
- [ ] Mobile/responsive design check (if HTML changed)
- [ ] Open Graph preview (if meta tags changed)
- [ ] Alignment spot check (3-5 random facts)

---

#### Common Pitfalls to Avoid

❌ **DON'T:**
- Update website without planning to update docs (creates drift)
- Make factual changes to website before updating authoritative docs
- Skip documentation in Version History ("I'll remember" = you won't)
- Batch multiple unrelated updates without tracking each one
- Copy-paste between sources without transforming for context
- Leave one source outdated for more than 24 hours
- Update LinkedIn without syncing to internal docs

✅ **DO:**
- Follow the decision tree for every update
- Set calendar reminders to sync second source
- Use git commits to create audit trail
- Review mapping table before and after changes
- Transform content appropriately for each format
- Document reasons when deviating from guidelines
- Keep a update log (Version History serves this purpose)

---

#### Troubleshooting Common Sync Issues

**Issue: "I updated the website but forgot to update the docs"**
- ✅ Solution: Set a recurring calendar task "Sync website → docs" 24 hours after website update
- ✅ Prevention: Use a git pre-commit hook reminder to check if both sources need updates

**Issue: "The content drifted and now I don't know which is correct"**
- ✅ Solution: Check LinkedIn profile as tiebreaker for job titles/dates, use most recent update for other content
- ✅ Prevention: Update Version History immediately when making changes (creates timestamp trail)

**Issue: "I made a creative change to website bio and docs feel out of sync"**
- ✅ Solution: Creative/narrative changes don't need perfect sync—docs can remain factual while website is creative
- ✅ Prevention: Remember that website is story-focused, profile.md is data-focused. Identical facts ≠ identical text.

**Issue: "Too many discrepancies accumulated, where do I start?"**
- ✅ Solution:
  1. Fix critical factual errors first (job title, dates)
  2. Use mapping table to systematically check each section
  3. Document all found discrepancies in Known Issues
  4. Fix high-visibility website content before internal docs
  5. Update Version History with "Content sync audit completed [date]"

---

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
