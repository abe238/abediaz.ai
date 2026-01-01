# Content Mapping Analysis: abe-diaz-profile.md → index.html

> Analysis Date: January 2026
>
> This document maps content from `docs/abe-diaz-profile.md` to `index.html`, identifies unused content, and documents discrepancies.

---

## Content Used in index.html

### Identity & Branding
| Profile Source | Used in index.html | Location |
|----------------|-------------------|----------|
| Name: "Abe Diaz" | ✅ "ABE DIAZ" | Header (line 551) |
| Tagline: "Seattle / Tech / Evangelist" | ✅ "Seattle/Tech/Evangelist" | Header tagline (line 552) |

### Professional Information
| Profile Source | Used in index.html | Location | Notes |
|----------------|-------------------|----------|-------|
| Current Title: "Sr. Manager - Disaster Relief at Amazon" | ⚠️ "Sr. Technical Program Manager on the Disaster Relief by Amazon team" | Meta description (line 7), Main content (line 576) | **DISCREPANCY - See below** |
| Education: MS Information Security, Lipscomb University | ✅ Full mention | Main content (line 576) | ✓ Matches |
| Education: BS Computer Engineering, UPR-Mayaguez | ✅ Full mention with link | Main content (line 576) | ✓ Matches |
| Hurricane Maria story (2017) | ✅ Narrative version with link | Main content (line 576) | Expanded with Seattle Times link |
| Disaster Relief team role | ✅ "joined the Disaster Relief by Amazon team permanently" | Main content (line 576) | With link to amazon.com/disasterrelief |

### Work History (Narrative Form)
| Profile Source | Used in index.html | Location |
|----------------|-------------------|----------|
| Deloitte: Enterprise app marketplace, C-Suite apps | ✅ "enterprise app marketplace with over 40 apps and iPad applications for the top leaders in the company including the CEO" | Main content (line 576) |
| NBCUniversal: Mobile Apps & Devices PM | ✅ "NBC News as the mobile program manager" | Main content (line 576) |
| Amazon Prime Video: Payments & revenue | ✅ "payments, royalties and revenue automation for Prime Video" | Main content (line 576) |
| Corporate in-kind donations program | ✅ "in charge of our corporate in-kind donations and mobile disaster pickup points program" | Main content (line 576) |

### Personal & Interests
| Profile Source | Used in index.html | Location |
|----------------|-------------------|----------|
| Personal philosophy statement | ✅ Full text | Main content (line 567) |
| Traveling interest | ✅ "Traveling" with link to stats | Main content (line 580) |
| Cider interest | ✅ "Cider" with link to Locust Cider | Main content (line 580) |
| Raspberry Pi interest | ✅ "RaspberryPis" with link | Main content (line 580) |
| Ice Baths interest | ✅ "Ice Baths" with link | Main content (line 580) |
| Contrast Showers interest | ✅ "Contrast Showers" with link | Main content (line 580) |
| Travel stats (visual) | ✅ Flight stats image displayed | Main content (lines 582-587) |

### Social Links
| Profile Source | Used in index.html | Location |
|----------------|-------------------|----------|
| LinkedIn: linkedin.com/in/abediaz | ✅ Two instances | Main content (line 578), Footer (line 596) |
| Twitter: twitter.com/abe238 | ✅ Multiple instances | Meta tags (lines 18-19), Main content (line 578), Footer (line 597) |
| Instagram: instagram.com/abe238 | ✅ One instance | Main content (line 578) |
| GitHub: github.com/abe238 | ❌ Not used | - |

---

## Content NOT Used in index.html

### Professional Details (Unused)
- ❌ **Impact & Achievements**: 200+ disaster relief efforts, 26+ million items delivered
- ❌ **Award**: "Seattle's 40 Under 40" (2023)
- ❌ **Proactive Supply Pre-positioning strategy**
- ❌ **AWS Disaster Response scope expansion**
- ❌ **Partner organizations**: Red Cross, WCK, WFP (mentioned but not featured)
- ❌ **Detailed work timeline**: Role dates and progression
- ❌ **Microsoft experience** (2013-2014)
- ❌ **AT&T Mobility experience** (2013)
- ❌ **Deloitte Software Engineer role** (2009-2011)

### Skills & Expertise (Unused)
- ❌ **Core Skills**: Disaster Relief, Philanthropy, Product Management, Technical Program Management
- ❌ **Technical Skills**: Mobile (iOS, Android, FireTV), Cloud/Logistics, .NET
- ❌ **Soft Skills**: Public Speaking, Developer Evangelism, Team Leadership, Process Automation

### Education Details (Unused)
- ❌ **Languages**: English (Native), Spanish (Native)
- ❌ **Activities**: IEEE, SHPE, ACM, ISACA
- ❌ **Graduation years**: 2009 (BS), 2012 (MS)

### Open Source Projects (Unused)
- ❌ **project-kickoff**: CLI scaffolding tool
- ❌ **aipm-resume-analyzer**: Resume analysis tool
- ❌ **yt-slides**: Video screenshot extractor
- ❌ **grandapi**: Raspberry Pi photo frame

### Volunteering (Unused)
- ❌ **Startup Weekend**: Event Organizer (2015-Present)
- ❌ **ALPFA, Inc (Seattle)**: VP of Technology (2015-2017)
- ❌ **Career Readiness Mentor**: Mentor Collective (2023)

### Press & Publications (Unused)
- ❌ **Seattle Times article** (Sep 2023): "Amazon wants to bring its delivery efficiency to disaster relief"
- ❌ **KUOW (NPR) feature** (Sep 2023): "Disaster relief delivered by Amazon"
- ❌ **Puget Sound Business Journal** (Apr 2023): "40 Under 40" Feature

### Personal Details (Unused)
- ❌ **Detailed travel statistics**:
  - 61 days in the air
  - 626,410 total miles
  - 25x around the world
  - *(Note: Visual representation shown on site via flight-stats.png)*

---

## Discrepancies Between Sources

### 🔴 CRITICAL: Job Title Mismatch
| Source | Title | Date Context |
|--------|-------|--------------|
| **abe-diaz-profile.md** | "Sr. Manager - Disaster Relief" | "Feb 2025 - Present" |
| **index.html** | "Sr. Technical Program Manager on the Disaster Relief by Amazon team" | No date specified |

**Issue**: The profile document shows a promotion to Sr. Manager in February 2025, but the website still references the previous title (Sr. Technical Program Manager).

**Recommendation**: Update index.html to reflect current title "Sr. Manager - Disaster Relief at Amazon"

---

### ⚠️ MINOR: Date Inconsistency in Profile
| Issue | Details |
|-------|---------|
| **Profile header** | Says "Last updated: December 2025" |
| **Current role** | Says "Feb 2025 - Present" |

**Issue**: Profile references "Dec 2025" as last update but shows a role starting "Feb 2025 - Present", suggesting these are placeholder dates or the document was created speculatively.

**Recommendation**: Verify actual current title and update both documents accordingly.

---

### ⚠️ MINOR: Link Discrepancies
| Item | Profile | Index.html | Notes |
|------|---------|------------|-------|
| **Disaster Relief link** | Not specified | amazon.com/disasterrelief | Website adds this helpful link |
| **GitHub link** | ✅ github.com/abe238 | ❌ Not included | Profile has it, website doesn't |
| **JetItUp travel stats** | Not specified | ✅ jetitup.com/MyStats | Website links to external stats page |

---

## Content Strategy Observations

### Website Philosophy (index.html)
The current website follows a **minimalist, personal narrative** approach:
- ✅ Focus on human story (Hurricane Maria pivot)
- ✅ Personal philosophy statement front and center
- ✅ Conversational tone ("amazing wife", "amazing food")
- ✅ Links to external interests (cider, RaspberryPis)
- ❌ Limited professional achievements details
- ❌ No awards or recognition mentioned
- ❌ No press coverage highlighted

### Profile Philosophy (abe-diaz-profile.md)
The profile document follows a **comprehensive resume/LinkedIn** approach:
- ✅ Structured professional timeline
- ✅ Quantified impact (200+ efforts, 26M items)
- ✅ Awards and recognition
- ✅ Complete work history
- ✅ Skills taxonomy
- ✅ Open source portfolio

### Alignment Assessment
**Status**: ⚠️ **Partially Aligned**

The documents serve different purposes:
- **index.html**: Personal brand homepage (warm, inviting, storytelling)
- **abe-diaz-profile.md**: Professional reference document (comprehensive, achievement-focused)

---

## Recommendations

### 1. Fix Critical Discrepancy
- [ ] Update job title in index.html to match current role (Sr. Manager vs Sr. TPM)
- [ ] Verify actual current title with Abe

### 2. Consider Strategic Additions to Website
High-value content currently missing from index.html:
- [ ] **Seattle's 40 Under 40 award** - Prestigious recognition that strengthens credibility
- [ ] **Press mentions** - Seattle Times and KUOW links add third-party validation
- [ ] **Impact metrics** - "200+ disaster relief efforts, 26+ million items" is compelling
- [ ] **GitHub link** - Complements other social links for technical audience

### 3. Update Profile Document
- [ ] Clarify date references (Dec 2025 update date seems future-dated)
- [ ] Add amazon.com/disasterrelief link for consistency
- [ ] Add JetItUp travel stats link reference

### 4. Create Content Governance
- [ ] Establish index.html as "source of truth" for current role and public-facing content
- [ ] Use abe-diaz-profile.md as comprehensive reference/archive
- [ ] Define update process when professional details change

---

## Usage Summary

### Content Utilization Rate
- **Used from profile**: ~30% (12 of 40+ data points)
- **Primary usage categories**:
  - ✅ Identity & branding (100%)
  - ✅ Personal interests (100%)
  - ✅ Social links (75% - missing GitHub)
  - ✅ Work narrative (selective, story-focused)
  - ❌ Detailed achievements (0%)
  - ❌ Skills taxonomy (0%)
  - ❌ Open source (0%)
  - ❌ Press coverage (0%)

### Content Alignment
| Aspect | Aligned? | Notes |
|--------|----------|-------|
| **Name & branding** | ✅ Yes | Perfect match |
| **Current role** | ❌ No | Title discrepancy |
| **Story/narrative** | ✅ Yes | Consistent messaging |
| **Interests** | ✅ Yes | All represented |
| **Social presence** | ⚠️ Partial | Missing GitHub |
| **Professional depth** | ❌ No | Website much lighter |

---

## Document Metadata

- **Analysis performed**: January 2026
- **Sources analyzed**:
  - `docs/abe-diaz-profile.md` (Last updated: December 2025)
  - `index.html` (Current live site)
- **Discrepancies found**: 1 critical (job title), 2 minor (dates, links)
- **Unused content**: ~70% of profile data not present on website
- **Strategic assessment**: Documents serve different purposes; minimal alignment acceptable for current strategy

---

*This analysis supports the content strategy documentation initiative (Spec #013).*
