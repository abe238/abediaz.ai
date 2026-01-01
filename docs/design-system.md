# Abe Diaz Design System

> Comprehensive documentation of the CSS design system used throughout abediaz.ai

---

## Table of Contents

1. [Introduction](#introduction)
   - [Design Philosophy](#design-philosophy)
   - [Overview](#overview)
2. [Design Tokens](#design-tokens)
   - [Color Palette](#color-palette)
   - [Typography](#typography)
   - [Spacing & Layout](#spacing--layout)
3. [Components](#components)
   - [Layout Components](#layout-components)
   - [Typography Components](#typography-components)
   - [Interactive Components](#interactive-components)
   - [Content Components](#content-components)
4. [Responsive Design](#responsive-design)
   - [Breakpoints](#breakpoints)
   - [Mobile Adaptations](#mobile-adaptations)
5. [CSS Architecture](#css-architecture)
   - [Reset & Base Styles](#reset--base-styles)
   - [Browser Normalization](#browser-normalization)
6. [Quick Reference](#quick-reference)
   - [CSS Variables](#css-variables)
   - [Component Classes](#component-classes)
   - [Common Patterns](#common-patterns)
7. [Usage Examples](#usage-examples)
   - [Best Practices](#best-practices)
   - [Do's and Don'ts](#dos-and-donts)

---

## Introduction

### Design Philosophy

The Abe Diaz design system is built on principles of **clarity**, **simplicity**, and **intentional constraint**. Rather than offering unlimited flexibility, the system provides a curated set of design tokens and components that work harmoniously together.

**Core Principles:**

- **Minimalism First**: Every element serves a purpose. The design prioritizes content over decoration.
- **Systematic Consistency**: A 4px spacing scale and carefully chosen color palette ensure visual harmony across the entire site.
- **Performance-Conscious**: CSS-first approach with minimal JavaScript dependency for faster load times and better accessibility.
- **Responsive by Default**: Mobile-first thinking with thoughtful breakpoints that adapt to different screen sizes without compromising the design intent.
- **Accessibility Matters**: Color contrast ratios, semantic HTML, and keyboard navigation are first-class considerations.

**Design Ethos:**

This is a personal site for a technologist and evangelist. The design reflects the subject's personality: direct, authentic, and human. The teal accent color (#36BCAB) adds a touch of warmth to an otherwise neutral palette, while the Oswald typeface for headings provides strong visual hierarchy without being overly formal.

The design system embraces constraints as a feature, not a limitation. By providing exactly what's needed—no more, no less—it enables rapid development while maintaining consistency.

### Overview

This documentation covers approximately 520 lines of CSS organized into:

- **43 CSS Custom Properties** (Design Tokens)
  - 14 color primitives
  - 10 typography tokens (fonts, sizes, weights)
  - 11 spacing values (4px-based scale)
  - 4 layout dimensions
  - 2 border radii
  - 2 transition timings

- **15+ UI Components**
  - Layout structures (container, header, sidebar, footer)
  - Typography variants (headings, links, paragraphs)
  - Interactive elements (buttons, forms)
  - Content modules (widgets, profile, contact sections)

- **3 Responsive Breakpoints**
  - Desktop (default)
  - Tablet (≤768px)
  - Mobile (≤480px)
  - Small Mobile (≤360px)

The system is currently implemented as inline CSS in `index.html` and is designed to scale to a multi-page site with modular CSS architecture.

---

## Design Tokens

Design tokens are the fundamental building blocks of the design system—the named values that define colors, typography, spacing, and other visual properties.

### Color Palette

The color palette is intentionally minimal, favoring a neutral foundation with a single vibrant accent. This approach ensures the design feels clean and professional while allowing content to remain the primary focus.

#### Design Rationale

The palette is built around **three core color families**:
1. **Foundation Colors** (Black & White) - Maximum contrast and clarity
2. **Neutral Grays** - An 8-step scale for subtle variations and hierarchy
3. **Accent Colors** - Teal for warmth, Blue for external platforms

The teal accent (#36BCAB) was chosen to add personality and warmth to an otherwise neutral palette. It evokes approachability and energy without being overwhelming.

---

#### Foundation Colors

These provide the base contrast for the entire design system.

| Variable | Hex Code | Visual | Usage | Notes |
|----------|----------|--------|-------|-------|
| `--color-black` | `#000000` | ⬛ | Primary headings (h1, h2.section-title, h3), high-emphasis text | Highest contrast, used sparingly for maximum impact |
| `--color-white` | `#FFFFFF` | ⬜ | Page backgrounds, input fields, button text on colored backgrounds | Pure white for clean, modern aesthetic |

**Accessibility:**
- Black on white: **21:1** contrast ratio (WCAG AAA for all text sizes)
- White on black: **21:1** contrast ratio (WCAG AAA for all text sizes)

---

#### Neutral Grays

An 8-step gray scale provides nuanced hierarchy for text, borders, and backgrounds. The scale uses a non-linear progression optimized for readability and visual distinction.

| Variable | Hex Code | Visual | Usage | Status | Notes |
|----------|----------|--------|-------|--------|-------|
| `--color-gray-50` | `#F3F3F3` | ◻️ | *Reserved* | Unused | Lightest gray - available for subtle backgrounds |
| `--color-gray-100` | `#F1F1F1` | ◻️ | *Reserved* | Unused | Very light gray - available for hover states |
| `--color-gray-200` | `#DDDDDD` | ◻️ | Borders, dividers, widget outlines | **Active** | Subtle separation without harsh lines |
| `--color-gray-300` | `#AAAAAA` | ◻️ | *Reserved* | Unused | Mid-light gray - available for disabled states |
| `--color-gray-500` | `#767676` | ◼️ | Input borders, form element outlines | **Active** | Medium gray for interactive boundaries |
| `--color-gray-600` | `#666666` | ◼️ | Secondary text (taglines, footer, small text) | **Active** | Lower-emphasis text content |
| `--color-gray-700` | `#555555` | ◼️ | Body text, standard content | **Active** | Primary text color across the site |
| `--color-gray-800` | `#32373C` | ◼️ | *Reserved* | Unused | Dark gray - available for future use |
| `--color-gray-900` | `#222222` | ◼️ | *Reserved* | Unused | Near-black - available for future use |

**Accessibility (on white background):**
- gray-200: **1.7:1** - Decorative only, not for text
- gray-500: **4.6:1** - WCAG AA for large text (18px+)
- gray-600: **5.7:1** - WCAG AA for all text sizes
- gray-700: **7.4:1** - WCAG AAA for body text (13px+)

**Design Notes:**
- The active grays (200, 500, 600, 700) form a well-balanced hierarchy
- Reserved grays (50, 100, 300, 800, 900) are defined for future expansion
- All grays use pure neutral values (no color temperature bias)

---

#### Accent Colors

Accent colors provide visual interest and semantic meaning. The teal is the primary brand color, while blue is reserved for specific external platform integrations.

**Teal (Primary Accent)**

| Variable | Hex Code | Visual | Usage | Notes |
|----------|----------|--------|-------|-------|
| `--color-teal-500` | `#36BCAB` | 🟦 | Links, hover states, focus indicators, accent underlines | Primary interactive color throughout the site |

**Accessibility:**
- Teal on white: **3.3:1** - WCAG AA for large text only (18px+)
- **Important:** Teal should only be used for interactive elements (links, buttons) or large text (18px+)
- Never use teal for small body text - use gray-700 instead

**Design Notes:**
- The teal balances warmth and professionalism
- Creates clear affordance for interactive elements
- Adds personality without overwhelming the content

**Blue (Platform Integration)**

| Variable | Hex Code | Visual | Usage | Status | Notes |
|----------|----------|--------|-------|--------|-------|
| `--color-blue-500` | `#0073B1` | 🔵 | LinkedIn button background | **Active** | Matches LinkedIn brand color |
| `--color-blue-700` | `#2E4453` | 🔵 | *Reserved* | Unused | Darker blue - available for future platform integrations |

**Accessibility:**
- Blue-500 with white text: **4.6:1** - WCAG AA for large text (18px+)
- Blue-700 with white text: **9.3:1** - WCAG AAA for all text sizes

**Design Notes:**
- Blue is intentionally reserved for external platform colors (LinkedIn, etc.)
- Helps users distinguish between site actions and external links
- Blue-700 is available for darker platform color needs

---

#### Color Usage Guidelines

**When to use each color:**

1. **Black (`--color-black`)**
   - Main page headings (h1)
   - Section titles (h2.section-title)
   - Subsection headings (h3)
   - Use when maximum emphasis is needed

2. **White (`--color-white`)**
   - Page background
   - Input field backgrounds
   - Text on colored button backgrounds
   - Clean slate for content

3. **Gray-700 (`--color-gray-700`)**
   - Default for all body text
   - Paragraph content
   - Standard links (before hover)
   - Primary reading text

4. **Gray-600 (`--color-gray-600`)**
   - Taglines and subtitles
   - Footer text
   - Less prominent information
   - Meta information

5. **Gray-500 (`--color-gray-500`)**
   - Input borders (default state)
   - Form field outlines
   - Interactive element boundaries

6. **Gray-200 (`--color-gray-200`)**
   - Section dividers
   - Widget borders
   - Subtle separators
   - Visual rhythm elements

7. **Teal-500 (`--color-teal-500`)**
   - All link hover states
   - Focus indicators
   - Accent links (`.accent-link`)
   - Interactive element feedback
   - Primary call-to-action affordance

8. **Blue-500 (`--color-blue-500`)**
   - LinkedIn button background
   - External platform integrations only

**Best Practices:**

- ✅ **Do:** Use gray-700 for all standard body text
- ✅ **Do:** Reserve teal for interactive elements to create clear affordance
- ✅ **Do:** Use black sparingly for maximum impact
- ✅ **Do:** Maintain consistent color usage across similar components
- ❌ **Don't:** Use teal for small body text (fails accessibility)
- ❌ **Don't:** Mix gray levels inconsistently within the same component
- ❌ **Don't:** Use blue for internal site actions (reserve for platforms)
- ❌ **Don't:** Add colors outside the defined palette without documentation

---

#### Accessibility Summary

All color combinations in active use meet or exceed **WCAG 2.1 Level AA** standards:

| Foreground | Background | Ratio | WCAG Level | Use Case |
|------------|------------|-------|------------|----------|
| Black | White | 21:1 | AAA | Headings (all sizes) |
| Gray-700 | White | 7.4:1 | AAA | Body text (13px+) |
| Gray-600 | White | 5.7:1 | AA | Secondary text (12px+) |
| Teal-500 | White | 3.3:1 | AA (Large) | Links, interactive (18px+) |
| White | Blue-500 | 4.6:1 | AA (Large) | LinkedIn button (16px+) |

**Note:** Teal links in body text rely on underlines and context (not color alone) to meet accessibility requirements for users with color vision deficiencies.

---

#### Visual Palette Reference

```
FOUNDATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
■ Black    #000000  --color-black
□ White    #FFFFFF  --color-white

NEUTRALS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
▢ Gray 50  #F3F3F3  --color-gray-50   [Reserved]
▢ Gray 100 #F1F1F1  --color-gray-100  [Reserved]
▢ Gray 200 #DDDDDD  --color-gray-200  ✓ Active
▢ Gray 300 #AAAAAA  --color-gray-300  [Reserved]
▪ Gray 500 #767676  --color-gray-500  ✓ Active
▪ Gray 600 #666666  --color-gray-600  ✓ Active
▪ Gray 700 #555555  --color-gray-700  ✓ Active
▪ Gray 800 #32373C  --color-gray-800  [Reserved]
▪ Gray 900 #222222  --color-gray-900  [Reserved]

ACCENTS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
● Teal 500 #36BCAB  --color-teal-500  ✓ Active (Primary)
● Blue 500 #0073B1  --color-blue-500  ✓ Active (LinkedIn)
● Blue 700 #2E4453  --color-blue-700  [Reserved]
```

---

### Typography

The typography system is built on a simple yet powerful combination of two carefully chosen typefaces: **Oswald** for headings and **Helvetica Neue** for body text. This pairing creates a strong visual hierarchy while maintaining exceptional readability.

#### Design Rationale

Typography serves as the primary tool for establishing hierarchy and guiding attention throughout the site. The system is designed around these principles:

1. **Clear Hierarchy** - Oswald's bold, uppercase headings create immediate visual anchors
2. **Exceptional Readability** - Helvetica Neue provides clean, comfortable reading for body text
3. **Systematic Scaling** - A limited set of font sizes prevents inconsistency
4. **Performance-Conscious** - Only Oswald is loaded from Google Fonts; everything else uses system fonts
5. **Responsive Typography** - Font sizes adapt to screen size for optimal readability

The Oswald + Helvetica pairing balances personality with professionalism. Oswald adds character without being decorative, while Helvetica Neue provides the neutral, highly readable foundation that body text requires.

---

#### Font Families

Three font stacks provide coverage for different use cases. Each stack includes fallbacks to ensure graceful degradation across all platforms.

**Heading Font Stack**

| Variable | Font Stack | Source | Usage |
|----------|-----------|--------|-------|
| `--font-heading` | `"Oswald", Helvetica, Arial, sans-serif` | Google Fonts | All headings (h1, h2.section-title, h3), widget headings, navigation, buttons, labels |

**Details:**
- **Oswald** is loaded from Google Fonts with weights 400 and 700
- Falls back to Helvetica on systems where web fonts fail to load
- Arial provides universal support as the final fallback
- Designed for high-impact, uppercase headings
- Strong geometric forms create visual anchors

**Body Font Stack**

| Variable | Font Stack | Source | Usage |
|----------|-----------|--------|-------|
| `--font-body` | `"Helvetica Neue", Helvetica, Arial, sans-serif` | System | Body text, paragraphs, taglines, links, most UI elements |

**Details:**
- **Helvetica Neue** available on macOS and iOS by default
- Falls back to classic Helvetica on older systems
- Arial ensures universal coverage across all platforms
- Optimized for reading comfort at small sizes (13px base)
- High x-height improves legibility at body text sizes

**System Font Stack**

| Variable | Font Stack | Source | Usage |
|----------|-----------|--------|-------|
| `--font-system` | `-apple-system, system-ui, "Segoe UI", Roboto, sans-serif` | System | Form inputs, email input fields, system UI elements |

**Details:**
- Uses the native OS font for form inputs
- **-apple-system** on macOS/iOS (San Francisco)
- **system-ui** as the cross-platform standard
- **Segoe UI** on Windows
- **Roboto** on Android
- Provides familiar, platform-native appearance for form controls
- Improves perceived performance (no font loading)

**Font Loading Strategy:**

Only Oswald is loaded from Google Fonts using the following optimized approach:
```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Oswald:wght@400;700&display=swap" rel="stylesheet">
```

- Preconnect hints reduce DNS lookup time
- `display=swap` ensures text remains visible during font load (FOIT prevention)
- Only two weights loaded (400, 700) to minimize payload

---

#### Font Size Scale

A focused set of six font sizes covers all use cases. The scale is intentionally limited to prevent inconsistency and maintain visual harmony.

| Variable | Size | Usage | Responsive Behavior |
|----------|------|-------|---------------------|
| `--text-xs` | 11px | Form inputs, input labels, very small UI text | Static across all breakpoints |
| `--text-sm` | 12px | Navigation links, button text, footer text, small labels | Static across all breakpoints |
| `--text-base` | 13px | Body paragraphs, standard content, default text size | **14px** on mobile (≤480px) |
| `--text-md` | 14px | Larger labels, secondary headings (h3 on mobile), tagline on mobile | Static across all breakpoints |
| `--text-lg` | 16px | Subsection headings (h3), prominent UI elements | Static across all breakpoints |
| `--text-4xl` | 80px | Main heading (h1) only | **32px** on mobile (≤480px)<br>**28px** on small mobile (≤360px) |

**Size Selection Guidelines:**

- **text-xs (11px)**: Reserve for secondary UI elements where space is constrained
- **text-sm (12px)**: Navigation, buttons, and labels that need to be compact but readable
- **text-base (13px)**: Default for all body content - optimized for comfortable reading
- **text-md (14px)**: Slight emphasis within body content or taglines
- **text-lg (16px)**: Subsection headings or prominent interactive elements
- **text-4xl (80px)**: Hero heading only - creates immediate visual impact

**Responsive Scaling:**

The system uses **selective responsive scaling** rather than scaling all sizes:
- **text-4xl** dramatically reduces on mobile (80px → 32px → 28px) to fit small screens
- **text-base** slightly increases on mobile (13px → 14px) to improve readability on small screens
- All other sizes remain static to maintain predictable hierarchy

---

#### Font Weights

Three font weights provide emphasis and hierarchy without overwhelming the design.

| Variable | Value | CSS Name | Usage | Availability |
|----------|-------|----------|-------|--------------|
| `--font-light` | 300 | Light | Taglines (h2.tagline), subtle de-emphasis | Helvetica Neue only |
| `--font-normal` | 400 | Regular | Body text, standard content, default weight | All font families |
| `--font-bold` | 700 | Bold | Headings (h1, h2.section-title, h3), buttons, strong emphasis, labels | Oswald & system fonts |

**Weight Usage Guidelines:**

1. **Light (300)**
   - Only used for h2.tagline
   - Creates subtle, secondary text appearance
   - Do NOT use for body text (reduces readability)
   - Only available reliably in Helvetica Neue

2. **Normal (400)**
   - Default weight for all body text
   - Paragraphs, links, standard UI elements
   - Universally available across all fonts

3. **Bold (700)**
   - All headings use bold weight
   - Buttons and prominent call-to-action elements
   - Labels and emphasized UI text
   - Oswald is designed to be used at bold weight

**Typography Weights in Practice:**

```css
/* Headings - Always bold */
h1, h2.section-title, h3 { font-weight: var(--font-bold); }

/* Body text - Always normal */
body, p, a { font-weight: var(--font-normal); }

/* Tagline - Light for subtle de-emphasis */
h2.tagline { font-weight: var(--font-light); }

/* Buttons and labels - Bold for emphasis */
.btn, label { font-weight: var(--font-bold); }
```

---

#### Typography Pairing & Hierarchy

The system establishes clear hierarchy through intentional font pairing and size relationships.

**Primary Typography Patterns:**

| Element | Font Family | Size | Weight | Transform | Color | Line Height |
|---------|-------------|------|--------|-----------|-------|-------------|
| **h1** | Oswald | 80px (4xl) | Bold (700) | UPPERCASE | Black | 1 |
| **h2.tagline** | Helvetica Neue | 14px (md) | Light (300) | none | Gray-600 | Default |
| **h2.section-title** | Oswald | 14px (md) | Bold (700) | UPPERCASE | Black | 1.2 |
| **h3** | Oswald | 16px (lg) | Bold (700) | UPPERCASE | Black | 1 |
| **Body (p)** | Helvetica Neue | 13px (base) | Normal (400) | none | Gray-700 | 1.75 |
| **Navigation** | Oswald | 12px (sm) | Bold (700) | UPPERCASE | Gray-700 | Default |
| **Buttons** | Oswald | 12px (sm) | Bold (700) | UPPERCASE | Varies | Default |
| **Form Inputs** | System | 11px (xs) | Normal (400) | none | Gray-700 | Default |

**Hierarchy Principles:**

1. **Size Contrast**: h1 (80px) vs body (13px) = 6:1 ratio creates dramatic hierarchy
2. **Weight Contrast**: Bold headings vs normal body creates clear distinction
3. **Case Contrast**: UPPERCASE headings vs sentence case body reinforces hierarchy
4. **Color Contrast**: Black headings vs gray-700 body provides subtle hierarchy
5. **Line Height Contrast**: Tight headings (1.0) vs comfortable body (1.75)

**Pairing Guidelines:**

- ✅ **Do:** Pair Oswald headings with Helvetica Neue body text
- ✅ **Do:** Use UPPERCASE for Oswald headings to maximize impact
- ✅ **Do:** Maintain tight line-height (1.0-1.2) for headings
- ✅ **Do:** Use generous line-height (1.75) for body text
- ❌ **Don't:** Mix Oswald and Helvetica within the same heading level
- ❌ **Don't:** Use Oswald for body text (not designed for reading)
- ❌ **Don't:** Use sentence case for Oswald headings (reduces impact)
- ❌ **Don't:** Use font-light (300) for anything other than taglines

---

#### Line Height & Letter Spacing

Vertical rhythm and spacing are critical for readability.

**Line Height Values:**

| Element | Line Height | Rationale |
|---------|-------------|-----------|
| Headings (h1-h6) | 1.0 | Tight spacing for visual impact and compactness |
| h2.section-title | 1.2 | Slightly more breathing room than h1 |
| Body text | 1.75 | Generous spacing for comfortable reading |
| Mobile body | 1.6 | Slightly tighter on mobile to conserve space |

**Letter Spacing:**

- **Default**: 0 (normal) for all elements
- **h1 on mobile**: -1px to compensate for dramatically reduced size
- **Uppercase text**: Inherits default (0) - Oswald is designed for tight uppercase tracking

**Best Practices:**

- Body text line-height (1.75) is optimized for 13px font size
- Heading line-height (1.0) creates visual density and impact
- Do NOT adjust letter-spacing unless on mobile h1
- Trust the typeface design - Oswald is optimized for uppercase use

---

#### Responsive Typography

Typography adapts thoughtfully across three breakpoints to maintain readability and hierarchy.

**Desktop (Default, >768px):**
- h1: 80px, letter-spacing: 0
- Body: 13px, line-height: 1.75
- All other sizes: Standard scale

**Tablet/Mobile (≤480px):**
```css
:root {
  --text-4xl: 32px;  /* h1 dramatically reduced */
  --text-base: 14px; /* body slightly increased for mobile readability */
}

body {
  line-height: 1.6;  /* slightly tighter to conserve vertical space */
}

h1 {
  letter-spacing: -1px; /* tighten spacing to compensate for size reduction */
}

h2.tagline,
h2.section-title,
h3 {
  /* Sizes adjust using updated CSS variables */
}
```

**Small Mobile (≤360px):**
```css
:root {
  --text-4xl: 28px;  /* h1 further reduced for tiny screens */
}
```

**Responsive Strategy:**

1. **Dramatic h1 reduction** (80px → 32px → 28px) prevents overflow
2. **Body size increase** on mobile (13px → 14px) improves readability on small screens
3. **Line-height reduction** on mobile (1.75 → 1.6) conserves vertical space
4. **Negative letter-spacing** on h1 compensates for size reduction

---

#### Usage Guidelines

**When to use each font family:**

1. **--font-heading (Oswald)**
   - All heading elements (h1, h2.section-title, h3)
   - Navigation links
   - Button text
   - Widget headings
   - Labels that need emphasis
   - ANY element that needs visual weight and hierarchy

2. **--font-body (Helvetica Neue)**
   - All body paragraphs
   - Links within content
   - Taglines (h2.tagline)
   - Secondary descriptive text
   - Footer text
   - Most UI elements

3. **--font-system (System fonts)**
   - Form input fields
   - Email signup inputs
   - Platform-native UI elements
   - Elements that should feel "native" to the OS

**When to use each font size:**

- **text-xs (11px)**: Form labels, input placeholders, very small UI text
- **text-sm (12px)**: Navigation, buttons, footer, compact labels
- **text-base (13px)**: Default for all body content
- **text-md (14px)**: Taglines, secondary headings on mobile
- **text-lg (16px)**: h3 headings, prominent UI elements
- **text-4xl (80px)**: h1 ONLY - never use elsewhere

**When to use each font weight:**

- **font-light (300)**: Taglines only (h2.tagline)
- **font-normal (400)**: All body text, links, paragraphs
- **font-bold (700)**: All headings, buttons, labels, emphasis

---

#### Best Practices

**Typography Do's:**

- ✅ Use Oswald for headings, Helvetica Neue for body text
- ✅ Apply UPPERCASE to all Oswald headings for maximum impact
- ✅ Maintain the size hierarchy: h1 > h3 > h2.section-title
- ✅ Use line-height 1.75 for all body text
- ✅ Use line-height 1.0-1.2 for headings
- ✅ Use --font-system for form inputs to match OS conventions
- ✅ Rely on CSS variables for all font properties
- ✅ Test typography at all three responsive breakpoints

**Typography Don'ts:**

- ❌ Don't use Oswald for body text (not designed for reading)
- ❌ Don't use sentence case for Oswald headings (reduces impact)
- ❌ Don't create new font sizes outside the defined scale
- ❌ Don't use font-light (300) except for h2.tagline
- ❌ Don't adjust letter-spacing except for h1 on mobile
- ❌ Don't use text-4xl for anything other than h1
- ❌ Don't load additional Google Fonts (performance impact)
- ❌ Don't mix font families within the same semantic element

---

#### Accessibility Considerations

**Readability:**

- **Base size (13px)** is above the minimum recommended size (12px)
- **Line height (1.75)** exceeds WCAG recommendation (1.5) for improved readability
- **Font contrast**: All text uses colors with WCAG AA+ contrast ratios
- **Font choice**: Helvetica Neue has high x-height for excellent legibility

**Cognitive Accessibility:**

- **Consistent hierarchy**: Predictable heading structure aids comprehension
- **Generous line-height**: Reduces cognitive load for dyslexic users
- **UPPERCASE headings**: Creates clear visual scanning landmarks

**Responsive Accessibility:**

- **Mobile text increase** (13px → 14px): Prevents text from being too small on mobile
- **Dramatic h1 reduction**: Prevents horizontal scrolling on small screens
- **Line-height adjustment**: Maintains readability while conserving space

**Best Practices:**

- Always use semantic HTML (h1, h2, h3) rather than styled divs
- Never rely solely on font size/weight to convey meaning
- Ensure sufficient color contrast (already handled by color system)
- Maintain hierarchy even when styles fail to load (semantic HTML)

---

#### Typography Quick Reference

```
FONT FAMILIES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Heading:  Oswald, Helvetica, Arial, sans-serif
Body:     Helvetica Neue, Helvetica, Arial, sans-serif
System:   -apple-system, system-ui, Segoe UI, Roboto, sans-serif

FONT SIZES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
--text-xs    11px   Form inputs, tiny labels
--text-sm    12px   Navigation, buttons, footer
--text-base  13px   Body text (14px on mobile)
--text-md    14px   Taglines, larger labels
--text-lg    16px   h3 headings
--text-4xl   80px   h1 only (32px mobile, 28px small mobile)

FONT WEIGHTS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
--font-light   300   Taglines only
--font-normal  400   Body text (default)
--font-bold    700   Headings, buttons, labels

HIERARCHY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
h1               Oswald 80px Bold UPPERCASE Black
h2.tagline       Helvetica 14px Light Gray-600
h2.section-title Oswald 14px Bold UPPERCASE Black
h3               Oswald 16px Bold UPPERCASE Black
body             Helvetica 13px Normal Gray-700 (lh: 1.75)
```

---

### Spacing & Layout

The spacing and layout system establishes consistent rhythm and structure throughout the design. Built on a **4px base unit**, the system ensures mathematical harmony and visual alignment across all components.

#### Design Rationale

The spacing system is designed around these core principles:

1. **4px Base Unit** - All spacing is divisible by 4, creating a mathematical foundation for visual consistency
2. **Predictable Scale** - Incremental steps (4px, 8px, 12px, 16px...) make spacing decisions intuitive
3. **Limited Choices** - A focused set of spacing values prevents inconsistency and decision fatigue
4. **Layout Flexibility** - Separate layout dimensions (content width, sidebar width) enable complex layouts
5. **Subtle Borders** - Minimal border radii (2-3px) maintain clean, crisp edges
6. **Smooth Transitions** - Two timing values cover all interaction needs

**Philosophy:**

The 4px grid system creates an invisible framework that aligns elements harmoniously. Rather than arbitrary pixel values, every spacing decision follows the scale. This mathematical consistency creates visual rhythm even when users aren't consciously aware of it.

The layout dimensions (content-width, sidebar-width, gap) are derived from optimal reading line length (~580px content) and classic sidebar proportions. The system prioritizes readability over maximizing screen real estate.

---

#### Spacing Scale

A 4px-based spacing scale provides 9 distinct spacing values for vertical rhythm, horizontal gaps, padding, and margins.

| Variable | Value | Multiplier | Usage | Common Use Cases |
|----------|-------|------------|-------|------------------|
| `--space-1` | 4px | 1× | Micro spacing, tight gaps | Tag padding, small UI element gaps, subtle separation |
| `--space-2` | 8px | 2× | Extra small spacing | Button padding (vertical), list item gaps, tight content spacing |
| `--space-3` | 12px | 3× | Small spacing | Button padding (horizontal), paragraph margins, section spacing |
| `--space-4` | 16px | 4× | Base spacing unit | Standard gaps, padding between related elements, card spacing |
| `--space-5` | 20px | 5× | Medium spacing | Section margins, widget spacing, comfortable padding |
| `--space-6` | 24px | 6× | Large spacing | Major section separation, content block margins, generous padding |
| `--space-8` | 32px | 8× | Extra large spacing | Major layout gaps, significant visual breaks, footer padding |
| `--space-10` | 40px | 10× | 2xl spacing | Major section dividers, primary content area spacing, large gaps |
| `--space-header` | 70px | Special | Header top spacing only | Dedicated spacing for site header from top edge |

**Responsive Behavior:**

The `--space-header` value adapts to conserve vertical space on smaller screens:

| Breakpoint | --space-header | Notes |
|------------|----------------|-------|
| Desktop (>768px) | **70px** | Default - generous top spacing |
| Tablet (≤768px) | **50px** | Reduced to conserve space |
| Mobile (≤480px) | **32px** | Minimal spacing for small screens |

All other spacing values remain static across breakpoints to maintain consistent rhythm.

**Scale Rationale:**

- **space-1 through space-6**: Linear progression (4px increments) for intuitive selection
- **space-8**: Jump to 32px provides a significant visual break
- **space-10**: 40px for major layout divisions
- **No space-7 or space-9**: Intentional gaps in the scale prevent over-specification
- **space-header**: Special-purpose value for header positioning

**Spacing Selection Guidelines:**

- **space-1 (4px)**: Elements that are tightly related (tag groups, inline lists)
- **space-2 (8px)**: Compact components (button padding, tight sections)
- **space-3 (12px)**: Related content (paragraph margins, list spacing)
- **space-4 (16px)**: Default gap - use when unsure
- **space-5 (20px)**: Standard section margins (widget spacing, content blocks)
- **space-6 (24px)**: Major content separation (between components)
- **space-8 (32px)**: Significant visual breaks (footer padding, major sections)
- **space-10 (40px)**: Primary layout gaps (sidebar gap, major dividers)
- **space-header (70px)**: Header positioning only

---

#### Layout Dimensions

Four layout dimensions define the structural foundation of the site's two-column layout (content + sidebar).

| Variable | Value | Usage | Rationale |
|----------|-------|-------|-----------|
| `--content-width` | 580px | Main content area width | Optimal line length for readability (50-75 characters per line at 13px) |
| `--sidebar-width` | 240px | Sidebar width | Comfortable width for widgets without overwhelming the layout |
| `--container-max` | 860px | Maximum container width | Total width: content (580px) + gap (40px) + sidebar (240px) = 860px |
| `--gap` | 40px | Space between content and sidebar | Comfortable visual separation without excessive whitespace |

**Layout Math:**

The layout dimensions work together to create a harmonious two-column structure:

```
┌─────────────────────────────────────────────────┐
│                 container-max                    │
│                    (860px)                       │
│  ┌──────────────────┐  ┌────────────────────┐  │
│  │  content-width   │  │   sidebar-width    │  │
│  │     (580px)      │  │      (240px)       │  │
│  │                  │  │                    │  │
│  │  Main content    │  │   Sidebar widgets  │  │
│  │                  │  │                    │  │
│  └──────────────────┘  └────────────────────┘  │
│         ↑─────gap (40px)─────↑                  │
└─────────────────────────────────────────────────┘

580px + 40px + 240px = 860px ✓
```

**Responsive Behavior:**

Layout dimensions remain static, but the layout shifts from two-column to single-column:

| Breakpoint | Layout Strategy |
|------------|-----------------|
| Desktop (>768px) | Two-column: content + sidebar side-by-side |
| Tablet/Mobile (≤768px) | Single-column: sidebar stacks below content |

At ≤768px, the sidebar moves below the main content, creating a vertical flow. Both content and sidebar become full-width (with appropriate horizontal padding).

**Content Width Rationale:**

580px provides optimal readability:
- At 13px font size (body text), this creates approximately **60-75 characters per line**
- Falls within the ideal range of 50-75 characters for comfortable reading
- Prevents overly long lines that reduce readability
- Leaves room for sidebar without cramping the layout

**Sidebar Width Rationale:**

240px provides comfortable widget space:
- Wide enough for profile images, flight stats, and form inputs
- Narrow enough to maintain content area as the primary focus
- Creates a 70/30 visual weight (content dominates, sidebar supports)

**Gap Rationale:**

40px (--space-10 equivalent) provides clear separation:
- Large enough to visually separate content from sidebar
- Small enough to feel like a unified layout (not disconnected)
- Aligns with the 4px spacing grid (40 = 10 × 4px)

---

#### Border Radii

Two minimal border radius values provide subtle softness without compromising the clean, modern aesthetic.

| Variable | Value | Usage | Common Use Cases |
|----------|-------|-------|------------------|
| `--radius-sm` | 2px | Small corners, subtle rounding | Buttons, tags, small interactive elements, input fields |
| `--radius-md` | 3px | Medium corners | Widgets, cards, larger containers (currently unused) |

**Design Philosophy:**

Border radii are intentionally minimal (2-3px) to maintain a **clean, crisp aesthetic**:
- Not completely square (0px = harsh, geometric)
- Not noticeably rounded (4px+ = softer, friendlier)
- Just enough to soften edges without drawing attention

**Radius Selection Guidelines:**

- **radius-sm (2px)**: Default choice for most interactive elements
  - Buttons (`.btn`, `.btn-primary`)
  - Tags (`.like-btn`, `.share-btn`)
  - Form inputs (email input field)
  - Small UI components

- **radius-md (3px)**: Reserved for larger containers
  - Widgets (`.widget`)
  - Cards or panels (if added in the future)
  - Larger content blocks

**Current Usage:**

Currently, only `--radius-sm` (2px) is actively used:
- Buttons: `.btn`, `.btn-primary`
- Tags: `.like-btn`, `.share-btn`
- Form inputs: email signup field

The `--radius-md` (3px) is reserved for future expansion but maintains the minimal aesthetic.

**Accessibility Note:**

Minimal border radii (2-3px) provide:
- Subtle visual affordance (softness = clickable)
- Sufficient corner softness for focus outlines to display properly
- No impact on contrast or readability

**Best Practices:**

- ✅ Use radius-sm (2px) for most interactive elements
- ✅ Keep border radii minimal to maintain modern aesthetic
- ✅ Apply consistently across similar component types
- ❌ Don't use border-radius values outside the defined scale
- ❌ Don't create heavily rounded elements (>5px) - breaks design consistency
- ❌ Don't use border-radius: 50% for circular elements (use explicit dimensions instead)

---

#### Transition Values

Two transition timing values provide smooth, responsive interactions without feeling sluggish.

| Variable | Value | Easing | Usage | Common Use Cases |
|----------|-------|--------|-------|------------------|
| `--transition-fast` | 0.15s ease | Ease | Quick interactions, immediate feedback | Hover states, small element changes, subtle feedback |
| `--transition-normal` | 0.2s ease | Ease | Standard interactions | Link color changes, button hover, color transitions |

**Timing Philosophy:**

Transitions should feel **immediate but smooth**:
- Fast enough that users don't wait
- Slow enough to appear smooth (not jarring)
- Consistent across similar interactions

**Easing Choice:**

Both transitions use **`ease`** timing function:
- Starts slow, accelerates, then decelerates
- Feels natural and organic
- More pleasant than `linear` (mechanical feeling)
- Less aggressive than `ease-in-out` (too dramatic for subtle transitions)

**Transition Selection Guidelines:**

**transition-fast (0.15s)**
- **Use for:** Micro-interactions requiring immediate feedback
  - Tag hover effects (`.like-btn`, `.share-btn`)
  - Small UI element state changes
  - Immediate visual confirmation
- **Properties:** Background color, border color, opacity, transform (small changes)
- **Goal:** User perceives instant response

**transition-normal (0.2s)**
- **Use for:** Standard interactive elements
  - Link color changes (all `<a>` elements)
  - Button hover states (`.btn`, `.btn-primary`)
  - Color transitions
  - Medium-sized element changes
- **Properties:** Color, background-color, border, opacity
- **Goal:** Smooth, polished interaction

**Current Usage:**

```css
/* Fast transitions - immediate feedback */
.like-btn, .share-btn {
  transition: all var(--transition-fast); /* 0.15s */
}

/* Normal transitions - standard interactions */
a {
  transition: color var(--transition-normal); /* 0.2s */
}

.btn, .btn-primary {
  transition: background-color var(--transition-normal); /* 0.2s */
}
```

**Transition Properties:**

**When to transition specific properties:**

- **color**: Links, text hover states → Use `--transition-normal`
- **background-color**: Buttons, tags → Use `--transition-normal` (large areas), `--transition-fast` (small tags)
- **opacity**: Fade effects → Use `--transition-normal`
- **transform**: Small movements → Use `--transition-fast`
- **all**: Multiple properties changing → Use `--transition-fast` (small elements only)

**Best Practices:**

- ✅ **Do:** Transition specific properties (color, background-color) rather than `all` when possible
- ✅ **Do:** Use transition-fast for small elements requiring immediate feedback
- ✅ **Do:** Use transition-normal for standard hover/focus states
- ✅ **Do:** Apply consistent timing to similar interactions
- ❌ **Don't:** Create transitions longer than 0.3s (feels sluggish)
- ❌ **Don't:** Transition `all` on large elements (performance impact)
- ❌ **Don't:** Use transitions on layout properties (width, height, padding) - causes reflow
- ❌ **Don't:** Mix timing functions (ease, ease-in, linear) - creates inconsistent feel

**Accessibility Considerations:**

Users with vestibular disorders may prefer reduced motion:

```css
@media (prefers-reduced-motion: reduce) {
  * {
    transition-duration: 0.01ms !important;
  }
}
```

**Note:** The current implementation does not include `prefers-reduced-motion` support. Consider adding this for improved accessibility.

---

#### Spacing & Layout Best Practices

**Spacing Do's:**

- ✅ Always use spacing variables (`--space-*`) rather than hardcoded pixel values
- ✅ Follow the 4px grid - all custom spacing should be divisible by 4
- ✅ Use space-4 (16px) as the default when unsure
- ✅ Use larger spacing (space-8, space-10) to create visual hierarchy
- ✅ Maintain consistent spacing between similar components
- ✅ Use space-header only for header positioning

**Spacing Don'ts:**

- ❌ Don't create arbitrary spacing values outside the scale
- ❌ Don't use spacing values that aren't divisible by 4
- ❌ Don't mix spacing inconsistently within the same component
- ❌ Don't use space-header for general-purpose spacing
- ❌ Don't forget that space-7 and space-9 don't exist

**Layout Do's:**

- ✅ Use layout dimensions for structural sizing (content-width, sidebar-width)
- ✅ Respect the two-column layout math (580px + 40px + 240px = 860px)
- ✅ Use container-max for outer container constraints
- ✅ Use gap for content/sidebar separation
- ✅ Test layout at all breakpoints (especially ≤768px stack behavior)

**Layout Don'ts:**

- ❌ Don't hardcode layout widths - use CSS variables
- ❌ Don't exceed container-max width
- ❌ Don't change content-width without considering readability (50-75 chars per line)
- ❌ Don't make sidebar wider than content area (maintains hierarchy)

**Border Radius Do's:**

- ✅ Use radius-sm (2px) for most interactive elements
- ✅ Apply border-radius consistently across button types
- ✅ Use radius-md (3px) only for larger containers
- ✅ Maintain minimal radii to preserve modern aesthetic

**Border Radius Don'ts:**

- ❌ Don't create custom radius values outside the scale
- ❌ Don't use large border radii (>5px) - breaks design consistency
- ❌ Don't mix radius values inconsistently within the same component type

**Transition Do's:**

- ✅ Use transition-fast (0.15s) for small, immediate interactions
- ✅ Use transition-normal (0.2s) for standard hover/focus states
- ✅ Transition specific properties (color, background-color) when possible
- ✅ Apply consistent timing to similar interaction patterns

**Transition Don'ts:**

- ❌ Don't create transitions longer than 0.3s
- ❌ Don't transition layout properties (width, height, padding) - causes reflow
- ❌ Don't use `transition: all` on large elements (performance)
- ❌ Don't mix timing functions - maintain consistent easing

---

#### Spacing & Layout Quick Reference

```
SPACING SCALE (4px base)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
--space-1         4px    Micro spacing
--space-2         8px    Extra small
--space-3        12px    Small
--space-4        16px    Base unit (default)
--space-5        20px    Medium
--space-6        24px    Large
--space-8        32px    Extra large
--space-10       40px    2xl
--space-header   70px    Header only (50px tablet, 32px mobile)

LAYOUT DIMENSIONS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
--content-width   580px   Main content area
--sidebar-width   240px   Sidebar width
--container-max   860px   Maximum container (580+40+240)
--gap             40px    Content/sidebar separation

LAYOUT MATH
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
580px (content) + 40px (gap) + 240px (sidebar) = 860px (container-max)

BORDER RADII
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
--radius-sm       2px    Buttons, tags, inputs (default)
--radius-md       3px    Widgets, large containers

TRANSITIONS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
--transition-fast    0.15s ease   Immediate feedback, small elements
--transition-normal  0.2s ease    Standard interactions, links, buttons

RESPONSIVE BREAKPOINTS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Desktop  (>768px)   Two-column layout, --space-header: 70px
Tablet   (≤768px)   Single-column stack, --space-header: 50px
Mobile   (≤480px)   Single-column stack, --space-header: 32px
```

---

## Components

Components are reusable UI patterns built using the design tokens. Each component has a specific purpose and usage pattern.

### Layout Components

Layout components form the structural foundation of the site. These components establish the page architecture, content flow, and responsive behavior. Built using modern flexbox patterns, they provide a clean two-column layout on desktop that gracefully adapts to single-column on mobile.

#### Design Rationale

The layout system is designed around these principles:

1. **Content-First Architecture** - The layout prioritizes readable content width (580px) over maximizing screen usage
2. **Flexible Two-Column Pattern** - Desktop layout supports content + sidebar; mobile stacks vertically
3. **Semantic HTML Structure** - Uses proper semantic elements (header, nav, main, article, footer)
4. **Flexbox-Based** - Modern flexbox provides reliable, predictable layout behavior
5. **Responsive by Default** - Layout adapts naturally at defined breakpoints without complex overrides

**Philosophy:**

The layout system uses a **container-constrained, content-focused** approach rather than full-width edge-to-edge design. This creates comfortable reading experiences and prevents content from becoming overwhelming on large screens. The two-column pattern (content + sidebar) follows classic blog/portfolio layouts where the primary content dominates (580px) and the sidebar provides supplementary information (240px).

---

#### Component Overview

| Component | Purpose | Layout Method | Responsive Behavior |
|-----------|---------|---------------|---------------------|
| `.site-container` | Outer page container | Block with max-width centering | Max-width adapts, padding reduces on mobile |
| `.site-header` | Page header with branding and navigation | Block with vertical padding | Padding reduces on smaller screens |
| `.site-nav` | Navigation menu | Flexbox horizontal list | Wraps on mobile, gaps adjust |
| `.site-main` | Main content wrapper | Flexbox two-column | Becomes single-column on tablet (≤768px) |
| `.content` | Primary content area | Flex item with fixed width | Becomes full-width on tablet (≤768px) |
| `.sidebar` | Secondary content area (widgets) | Flex item with fixed width | Stacks below content on tablet (≤768px) |
| `.site-footer` | Page footer | Block with border separator | Padding adjusts on mobile |

---

#### `.site-container`

**Purpose:** The outer container that wraps all page content, centers it horizontally, and provides consistent horizontal padding.

**CSS Implementation:**

```css
.site-container {
  max-width: var(--content-width);     /* 580px */
  margin: 0 auto;                       /* Centers horizontally */
  padding: 0 var(--space-5);           /* 20px left/right */
}
```

**HTML Structure:**

```html
<div class="site-container">
  <!-- All page content goes here -->
  <header class="site-header">...</header>
  <main class="site-main">...</main>
  <footer class="contact-section">...</footer>
</div>
```

**Layout Behavior:**

- **Max-width**: Constrains content to `580px` (optimal reading width)
- **Centering**: `margin: 0 auto` centers the container horizontally
- **Horizontal Padding**: `20px` prevents content from touching viewport edges on small screens
- **Responsive**: Padding reduces to `16px` on mobile (≤480px) and `12px` on small phones (≤360px)

**Responsive Overrides:**

```css
/* Mobile (≤480px) */
.site-container {
  padding: 0 var(--space-4);  /* 16px */
}

/* Small phones (≤360px) */
.site-container {
  padding: 0 var(--space-3);  /* 12px */
}
```

**Usage Guidelines:**

- ✅ Use as the outermost wrapper for all page content
- ✅ Only one `.site-container` per page
- ✅ Place all major page sections inside the container
- ❌ Don't nest multiple `.site-container` elements
- ❌ Don't apply additional max-width constraints inside
- ❌ Don't override the horizontal centering behavior

---

#### `.site-header`

**Purpose:** Contains the site branding (h1), tagline (h2.tagline), and primary navigation. Provides generous top spacing to create breathing room at the top of the page.

**CSS Implementation:**

```css
.site-header {
  padding-top: var(--space-header);    /* 70px desktop, 50px tablet, 32px mobile */
  padding-bottom: var(--space-6);      /* 24px */
}
```

**HTML Structure:**

```html
<header class="site-header">
  <h1><a href="/">ABE DIAZ</a></h1>
  <h2 class="tagline">Seattle/Tech/Evangelist</h2>

  <nav class="site-nav">
    <ul>
      <li><a href="/">HOME</a></li>
    </ul>
  </nav>
</header>
```

**Layout Behavior:**

- **Top Padding**: Uses `--space-header` variable (responsive: 70px → 50px → 32px)
- **Bottom Padding**: Fixed 24px creates space before main content
- **No Horizontal Padding**: Inherits from `.site-container`
- **Block Layout**: Default block flow for vertical stacking

**Responsive Behavior:**

| Breakpoint | `padding-top` | Rationale |
|------------|---------------|-----------|
| Desktop (>768px) | **70px** | Generous top spacing creates elegant entrance |
| Tablet (≤768px) | **50px** | Reduced to conserve vertical space |
| Mobile (≤480px) | **32px** | Minimal spacing for small screens |

**Content Guidelines:**

- Should contain: Site branding (h1), optional tagline (h2.tagline), navigation (.site-nav)
- May contain: Additional header widgets or meta information
- Should NOT contain: Main content, sidebar content, or footer content

**Usage Guidelines:**

- ✅ Use once per page as the primary header
- ✅ Keep content focused on branding and navigation
- ✅ Maintain the h1 → h2.tagline → nav hierarchy
- ❌ Don't add horizontal padding (inherited from container)
- ❌ Don't place main content inside the header
- ❌ Don't override --space-header without updating responsive values

---

#### `.site-nav`

**Purpose:** Primary navigation menu using flexbox for horizontal layout with even spacing between links.

**CSS Implementation:**

```css
.site-nav {
  margin-top: var(--space-5);  /* 20px */
}

.site-nav ul {
  list-style: none;
  display: flex;
  gap: var(--space-5);         /* 20px between items */
}

.site-nav a {
  font-size: var(--text-sm);         /* 12px */
  text-transform: uppercase;
  color: var(--color-gray-700);
}

.site-nav a:hover {
  color: var(--color-teal-500);
}
```

**HTML Structure:**

```html
<nav class="site-nav">
  <ul>
    <li><a href="/">HOME</a></li>
    <li><a href="/about">ABOUT</a></li>
    <li><a href="/contact">CONTACT</a></li>
  </ul>
</nav>
```

**Layout Behavior:**

- **Top Margin**: 20px separates navigation from tagline
- **Flexbox List**: `display: flex` creates horizontal layout
- **Gap**: 20px spacing between navigation items
- **No List Styles**: `list-style: none` removes bullets
- **Uppercase Links**: All navigation text is uppercase

**Responsive Behavior:**

```css
/* Mobile (≤480px) */
.site-nav {
  margin-top: var(--space-4);  /* Reduced to 16px */
}

.site-nav ul {
  flex-wrap: wrap;             /* Allows wrapping on narrow screens */
  gap: var(--space-4);         /* Reduced to 16px */
}
```

On mobile:
- Navigation items can wrap to multiple lines
- Gaps reduced to conserve space (20px → 16px)
- Top margin reduced (20px → 16px)

**Typography:**

- **Font**: Inherits `--font-heading` (Oswald)
- **Size**: 12px (--text-sm)
- **Weight**: Bold (700) via font-heading
- **Transform**: UPPERCASE
- **Color**: Gray-700 default, Teal-500 on hover

**Usage Guidelines:**

- ✅ Use within `.site-header` for primary navigation
- ✅ Use semantic `<nav>` element
- ✅ Use unordered list (`<ul>`) for navigation items
- ✅ Keep link text uppercase to match design
- ❌ Don't add padding to individual list items (use gap)
- ❌ Don't override list-style or display properties
- ❌ Don't nest navigation elements

**Accessibility Notes:**

- Uses semantic `<nav>` element for screen readers
- Maintains sufficient link spacing (20px) for touch targets
- Links have clear hover states with color change
- Uppercase text may be harder to read - use sparingly

---

#### `.site-main`

**Purpose:** Main content wrapper that establishes the two-column flexbox layout (content + sidebar) on desktop and single-column on mobile.

**CSS Implementation:**

```css
.site-main {
  display: flex;
  gap: var(--gap);                /* 40px */
  padding-bottom: var(--space-10); /* 40px */
}
```

**HTML Structure:**

```html
<main class="site-main">
  <!-- Primary content area -->
  <article class="content">
    <!-- Main content here -->
  </article>

  <!-- Optional sidebar (if present) -->
  <aside class="sidebar">
    <!-- Sidebar widgets here -->
  </aside>
</main>
```

**Layout Behavior:**

- **Display**: Flexbox enables side-by-side columns
- **Gap**: 40px space between content and sidebar
- **Direction**: Row (horizontal) by default
- **Bottom Padding**: 40px creates space before footer

**Responsive Behavior:**

The layout automatically stacks on tablet/mobile due to flex children becoming full-width:

```css
/* Tablet (≤768px) */
.content {
  max-width: 100%;  /* Content becomes full-width */
}
/* Sidebar naturally stacks below content */
```

| Breakpoint | Layout | Behavior |
|------------|--------|----------|
| Desktop (>768px) | Two-column | Content and sidebar side-by-side with 40px gap |
| Tablet/Mobile (≤768px) | Single-column | Sidebar stacks below content, both full-width |

**Layout Math:**

On desktop, the two columns plus gap should equal the container:
```
580px (content) + 40px (gap) + 240px (sidebar) = 860px total
```

**Note:** Current implementation uses `max-width: var(--content-width)` (580px) on `.site-container`, so the sidebar is not visible on the current site. The CSS is structured to support a two-column layout but HTML only includes `.content`.

**Usage Guidelines:**

- ✅ Use semantic `<main>` element for primary content wrapper
- ✅ Include `.content` for primary content column
- ✅ Optionally include `.sidebar` for secondary content
- ✅ Maintain the content + sidebar order (content first in DOM)
- ❌ Don't add more than two direct children (content + sidebar)
- ❌ Don't override the flex display without understanding layout impact
- ❌ Don't change the gap without considering responsive behavior

**Accessibility Notes:**

- Uses semantic `<main>` landmark for screen readers
- Content appears first in DOM order (important for screen reader flow)
- Single-column mobile layout maintains natural reading order

---

#### `.content`

**Purpose:** Primary content area that contains the main article content, images, and text. Forms the left column in desktop two-column layout.

**CSS Implementation:**

```css
.content {
  flex: 0 0 var(--content-width);  /* Don't grow, don't shrink, 580px basis */
  max-width: var(--content-width);  /* 580px */
}
```

**HTML Structure:**

```html
<article class="content">
  <h2 class="section-title">ABOUT ME</h2>
  <p>Article content...</p>
  <img src="./images/profile.jpg" alt="Profile" class="profile-image">
  <p>More content...</p>
</article>
```

**Layout Behavior:**

- **Flex Basis**: 580px fixed width on desktop
- **Flex Grow**: 0 (won't expand beyond 580px)
- **Flex Shrink**: 0 (won't compress below 580px)
- **Max-Width**: 580px ensures content never exceeds optimal reading width

**Responsive Behavior:**

```css
/* Tablet (≤768px) */
.content {
  max-width: 100%;  /* Becomes full-width */
}
```

On tablet and mobile:
- Becomes full container width (minus padding)
- Flex basis still 580px but max-width allows flexibility
- Content flows naturally in single-column layout

**Content Width Rationale:**

580px is chosen for optimal readability:
- At 13px body font size: ~60-75 characters per line
- Falls within ideal range for comfortable reading
- Prevents overly long lines that reduce comprehension
- Matches classic blog/article layouts

**Typical Content:**

- Section headings (h2.section-title, h3)
- Paragraphs and body text
- Images (profile-image, flight-stats)
- Links and inline content
- Share sections, contact sections

**Usage Guidelines:**

- ✅ Use semantic `<article>` element when content is self-contained
- ✅ Use `<div class="content">` for non-article content
- ✅ Keep content focused on primary information
- ✅ Maintain optimal line length (don't override width)
- ❌ Don't nest multiple `.content` elements
- ❌ Don't override flex properties without understanding layout
- ❌ Don't exceed 580px width (reduces readability)

---

#### `.sidebar`

**Purpose:** Secondary content area for supplementary widgets, forms, and related information. Forms the right column in desktop two-column layout.

**CSS Implementation:**

```css
.sidebar {
  flex: 0 0 var(--sidebar-width);  /* Don't grow, don't shrink, 240px basis */
  max-width: var(--sidebar-width);  /* 240px */
}
```

**HTML Structure:**

```html
<aside class="sidebar">
  <div class="widget">
    <h3 class="widget-title">SUBSCRIBE</h3>
    <p>Get updates...</p>
    <form class="email-form">
      <!-- Form content -->
    </form>
  </div>

  <div class="widget">
    <h3 class="widget-title">CONNECT</h3>
    <!-- Social links -->
  </div>
</aside>
```

**Layout Behavior:**

- **Flex Basis**: 240px fixed width on desktop
- **Flex Grow**: 0 (won't expand beyond 240px)
- **Flex Shrink**: 0 (won't compress below 240px)
- **Max-Width**: 240px ensures consistent sidebar width

**Responsive Behavior:**

On tablet (≤768px), sidebar automatically stacks below content:
- Becomes full container width
- Appears after content in natural DOM order
- Maintains all widget spacing and styling

**Sidebar Width Rationale:**

240px provides comfortable widget space:
- Wide enough for profile images, forms, stats
- Narrow enough to keep content as primary focus
- Creates 70/30 visual weight (content dominates)
- Matches classic blog sidebar proportions

**Typical Content:**

- Widgets (.widget)
- Email signup forms (.email-form)
- Social links (.social-links)
- Profile images
- Related content or meta information

**Current Implementation Note:**

The current HTML does not include a `.sidebar` element. The CSS is structured to support it, but the site currently uses a single-column content-only layout. To add a sidebar:

1. Update `.site-container` max-width from 580px to 860px
2. Add `<aside class="sidebar">` inside `.site-main`
3. Add widgets and content to the sidebar

**Usage Guidelines:**

- ✅ Use semantic `<aside>` element for sidebar
- ✅ Place after `.content` in DOM order
- ✅ Use `.widget` components for sidebar content
- ✅ Keep sidebar content supplementary (not essential)
- ❌ Don't use sidebar for critical content (mobile users see it last)
- ❌ Don't override flex properties without understanding layout
- ❌ Don't make sidebar wider than content area

---

#### `.site-footer`

**Purpose:** Page footer section with border separator. Used for contact links, copyright, and supplementary information.

**CSS Implementation:**

```css
.site-footer {
  font-size: var(--text-sm);            /* 12px */
  color: var(--color-gray-600);         /* Secondary text color */
  padding: var(--space-5) 0;            /* 20px top/bottom */
  border-top: 1px solid var(--color-gray-200);  /* Subtle divider */
}

.site-footer a {
  color: var(--color-gray-600);         /* Match footer text */
}
```

**HTML Structure:**

```html
<footer class="site-footer">
  <p>&copy; 2026 Abe Diaz. All rights reserved.</p>
  <p>
    <a href="/privacy">Privacy Policy</a> ·
    <a href="/terms">Terms of Service</a>
  </p>
</footer>
```

**Note:** The current implementation uses `.contact-section` for the footer rather than `.site-footer`. The `.contact-section` is styled separately but serves a similar purpose.

**Layout Behavior:**

- **Font Size**: 12px (smaller, de-emphasized text)
- **Text Color**: Gray-600 (secondary color, less prominent)
- **Top Border**: 1px gray-200 border creates visual separation
- **Vertical Padding**: 20px top and bottom
- **No Horizontal Padding**: Inherits from `.site-container`

**Typography:**

- Links inherit gray-600 color (not black)
- Links still change to teal on hover (default link behavior)
- Smaller font size reduces visual weight

**Usage Guidelines:**

- ✅ Use semantic `<footer>` element
- ✅ Place at the end of `.site-container`
- ✅ Keep content minimal and supplementary
- ✅ Use for copyright, legal links, site meta information
- ❌ Don't place critical navigation in footer
- ❌ Don't override the border-top separator
- ❌ Don't use for primary content

**Accessibility Notes:**

- Uses semantic `<footer>` landmark element
- Maintains sufficient color contrast (gray-600 on white = 5.7:1)
- Links have clear hover states

---

#### Layout Patterns & Best Practices

**Common Layout Patterns:**

**1. Single-Column Content (Current Implementation)**
```html
<div class="site-container">
  <header class="site-header">
    <h1>Site Title</h1>
    <nav class="site-nav">...</nav>
  </header>

  <main class="site-main">
    <article class="content">
      <!-- Main content -->
    </article>
  </main>

  <footer class="site-footer">
    <!-- Footer content -->
  </footer>
</div>
```

**2. Two-Column Content + Sidebar**
```html
<div class="site-container">
  <header class="site-header">...</header>

  <main class="site-main">
    <article class="content">
      <!-- Primary content -->
    </article>

    <aside class="sidebar">
      <div class="widget">...</div>
      <div class="widget">...</div>
    </aside>
  </main>

  <footer class="site-footer">...</footer>
</div>
```

---

#### Layout Best Practices

**Do's:**

- ✅ Use semantic HTML5 elements (header, nav, main, article, aside, footer)
- ✅ Maintain the established layout hierarchy
- ✅ Let flexbox handle responsive stacking (don't force with media queries)
- ✅ Use the gap property for spacing between flex children
- ✅ Keep content width at 580px for optimal readability
- ✅ Place content before sidebar in DOM order (accessibility)
- ✅ Test layout at all breakpoints (especially 768px stack point)

**Don'ts:**

- ❌ Don't override max-width on `.site-container` without updating child elements
- ❌ Don't add horizontal padding to nested layout elements (container handles this)
- ❌ Don't use floats or positioning for layout (flexbox is cleaner)
- ❌ Don't create layouts wider than `--container-max` (860px)
- ❌ Don't nest multiple `.site-main` or `.site-container` elements
- ❌ Don't override flex properties without understanding the impact
- ❌ Don't place critical content in sidebar (mobile users see it last)

---

#### Responsive Layout Behavior Summary

| Breakpoint | Container Padding | Header Top | Layout | Notes |
|------------|-------------------|------------|--------|-------|
| **Desktop (>768px)** | 20px | 70px | Two-column (content + sidebar) | Optimal desktop experience |
| **Tablet (≤768px)** | 16px | 50px | Single-column (sidebar below) | Content stacks vertically |
| **Mobile (≤480px)** | 16px | 32px | Single-column | Reduced spacing |
| **Small Mobile (≤360px)** | 12px | 32px | Single-column | Minimal padding |

**Key Responsive Changes:**

1. **Container padding** reduces as screens get smaller (20px → 16px → 12px)
2. **Header top spacing** dramatically reduces (70px → 50px → 32px)
3. **Layout shifts** from two-column to single-column at 768px
4. **Navigation wraps** on mobile with reduced gaps
5. **Content width** becomes 100% on tablet/mobile

---

#### Accessibility Considerations

**Semantic HTML:**
- All layout components use proper semantic elements
- Screen readers can identify landmarks (header, nav, main, footer)
- Logical heading hierarchy maintained

**Reading Order:**
- Content appears before sidebar in DOM (screen readers read content first)
- Navigation accessible via keyboard
- Logical tab order maintained

**Touch Targets:**
- Navigation links have adequate spacing (20px gaps)
- Links and interactive elements meet minimum size requirements

**Responsive Accessibility:**
- Single-column mobile layout maintains natural reading order
- Touch targets don't overlap on small screens
- Content remains readable at all breakpoints

---

#### Layout Components Quick Reference

```
LAYOUT STRUCTURE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
.site-container    Outer wrapper, max-width 580px (or 860px with sidebar)
.site-header       Header with branding/nav, padding-top: 70px → 50px → 32px
.site-nav          Horizontal flexbox navigation, gap: 20px
.site-main         Main content wrapper, flexbox row, gap: 40px
.content           Primary content, flex: 0 0 580px
.sidebar           Secondary content, flex: 0 0 240px
.site-footer       Footer with border-top, padding: 20px 0

LAYOUT MATH (Two-Column)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
580px (content) + 40px (gap) + 240px (sidebar) = 860px (container-max)

RESPONSIVE BREAKPOINTS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
>768px   Two-column layout, container padding: 20px
≤768px   Single-column stack, container padding: 16px
≤480px   Single-column, reduced spacing
≤360px   Minimal padding: 12px

FLEXBOX PATTERNS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
.site-nav ul       display: flex, gap: 20px (horizontal list)
.site-main         display: flex, gap: 40px (two-column)
.content           flex: 0 0 580px (fixed-width column)
.sidebar           flex: 0 0 240px (fixed-width column)
```

---

### Typography Components

Typography components are the semantic HTML elements styled with the design system's typography tokens. These components establish content hierarchy, improve readability, and provide consistent styling for text elements throughout the site.

#### Design Rationale

Typography components serve as the foundation for content structure and hierarchy. The system provides:

1. **Clear Visual Hierarchy** - Multiple heading variants create distinct levels of importance
2. **Semantic HTML** - Uses proper heading elements (h1, h2, h3) for accessibility and SEO
3. **Purposeful Variants** - Different heading styles serve specific use cases (tagline vs section-title)
4. **Consistent Link Behavior** - Two link variants (default and accent) provide flexible interaction patterns
5. **Readability-Focused** - Paragraph styles optimized for comfortable reading

**Philosophy:**

The typography component system balances visual impact with readability. Large, bold headings (h1) create immediate visual anchors, while subtle variants (h2.tagline) provide supporting context without competing for attention. The dual link system allows for both subtle integration (default black links) and high-visibility calls-to-action (accent teal links).

---

#### Component Overview

| Component | Font Family | Size | Weight | Color | Transform | Primary Use Case |
|-----------|-------------|------|--------|-------|-----------|------------------|
| **h1** | Oswald | 80px | Bold | Black | UPPERCASE | Main page title, site branding |
| **h2.tagline** | Helvetica Neue | 14px | Light | Gray-600 | none | Subtitle, de-emphasized secondary text |
| **h2.section-title** | Oswald | 14px | Bold | Black | UPPERCASE | Major section headings |
| **h3** | Oswald | 16px | Bold | Gray-700 | UPPERCASE | Subsection headings, widget titles |
| **p** | Helvetica Neue | 13px | Normal | Gray-700 | none | Body text, paragraphs |
| **a** (default) | Helvetica Neue | inherited | Normal | Black | none | Default inline links |
| **a.accent-link** | Helvetica Neue | inherited | Normal | Teal-500 | none | Emphasized links, CTAs |

---

#### `h1` - Main Heading

**Purpose:** The primary page heading, typically used for site branding or page title. Creates maximum visual impact with large size and bold uppercase styling.

**CSS Implementation:**

```css
h1 {
  font-family: var(--font-heading);     /* Oswald */
  font-size: var(--text-4xl);           /* 80px */
  font-weight: var(--font-bold);        /* 700 */
  line-height: 1;
  color: var(--color-black);
  text-transform: uppercase;
  letter-spacing: 0;
  margin-bottom: 0;
}

h1 a {
  color: inherit;                        /* Inherits black */
  text-decoration: none;
}

h1 a:hover {
  color: var(--color-teal-500);
}
```

**HTML Structure:**

```html
<!-- Site branding (current implementation) -->
<h1><a href="/">ABE DIAZ</a></h1>

<!-- Standalone heading -->
<h1>PAGE TITLE</h1>
```

**Styling Details:**

- **Font**: Oswald at 80px creates dramatic visual impact
- **UPPERCASE**: Maximizes Oswald's geometric strength
- **Black color**: Highest contrast for maximum prominence
- **Line-height 1**: Tight spacing for compact, powerful appearance
- **Zero margin-bottom**: Allows tight pairing with h2.tagline
- **Zero letter-spacing**: Oswald is designed for tight uppercase tracking

**Responsive Behavior:**

| Breakpoint | Font Size | Letter Spacing | Notes |
|------------|-----------|----------------|-------|
| Desktop (>768px) | **80px** | 0 | Full impact size |
| Tablet (≤768px) | **48px** | 0 | Reduced for medium screens |
| Mobile (≤480px) | **32px** | -1px | Dramatically reduced, tighter spacing |
| Small Mobile (≤360px) | **28px** | -1px | Further reduction for tiny screens |

The dramatic size reduction (80px → 32px → 28px) prevents horizontal overflow on mobile devices. The negative letter-spacing (-1px) on mobile compensates for the reduced size, maintaining visual density.

**Usage Guidelines:**

- ✅ Use **once per page** as the primary heading (site branding or page title)
- ✅ Always use UPPERCASE text to match the styling
- ✅ Use semantic h1 element (not styled divs)
- ✅ Keep text short and impactful (2-5 words typically)
- ✅ Links in h1 inherit black color and hover to teal
- ❌ Don't use multiple h1 elements on one page (bad for SEO)
- ❌ Don't use for body content or section headings (use h2.section-title instead)
- ❌ Don't override font-size outside responsive breakpoints
- ❌ Don't add margin-bottom (designed to pair tightly with h2.tagline)

**Accessibility Notes:**

- **Semantic HTML**: h1 element provides proper document structure for screen readers
- **High Contrast**: Black on white (21:1 ratio) exceeds WCAG AAA
- **Large Text**: 80px is highly readable for users with low vision
- **Hover States**: Links have clear color change (black → teal)

---

#### `h2.tagline` - Tagline/Subtitle

**Purpose:** A light, de-emphasized subtitle that appears directly below h1. Used for taglines, subtitles, or secondary descriptive text.

**CSS Implementation:**

```css
h2.tagline {
  font-family: var(--font-body);        /* Helvetica Neue */
  font-size: var(--text-md);            /* 14px */
  font-weight: var(--font-light);       /* 300 */
  color: var(--color-gray-600);         /* #666666 */
  text-transform: none;
  margin-top: var(--space-1);           /* 4px */
}
```

**HTML Structure:**

```html
<h1><a href="/">ABE DIAZ</a></h1>
<h2 class="tagline">Seattle/Tech/Evangelist</h2>
```

**Styling Details:**

- **Font**: Helvetica Neue (body font) creates contrast with Oswald h1
- **Light weight (300)**: Creates subtle, de-emphasized appearance
- **Gray-600 color**: Secondary color reduces visual prominence
- **14px size**: Larger than body text (13px) but much smaller than h1
- **Sentence case**: No text-transform (unlike other headings)
- **4px margin-top**: Tight spacing pairs with h1 (which has margin-bottom: 0)

**Responsive Behavior:**

```css
/* Mobile (≤480px) */
h2.tagline {
  font-size: var(--text-base);  /* 14px → 14px (no change, but var updates) */
}
```

On mobile, the tagline effectively remains 14px but uses the --text-base variable which updates to 14px, keeping it consistent with body text.

**Usage Guidelines:**

- ✅ Use immediately after h1 as a subtitle or tagline
- ✅ Use sentence case or lowercase (not UPPERCASE)
- ✅ Keep text concise (2-7 words typically)
- ✅ Use to add context or personality to h1
- ✅ Only use font-light (300) weight - available in Helvetica Neue
- ❌ Don't use for section headings (use h2.section-title instead)
- ❌ Don't use multiple taglines per page
- ❌ Don't use without a preceding h1
- ❌ Don't use for body content or emphasis

**Best Practices:**

**When to use h2.tagline:**
- Site tagline/motto below site name
- Subtitle describing page purpose
- Descriptive text adding context to h1
- Personal descriptor (e.g., "Seattle/Tech/Evangelist")

**When NOT to use h2.tagline:**
- Section headings (use h2.section-title)
- Body content (use p)
- Navigation or links

**Accessibility Notes:**

- **Color Contrast**: Gray-600 on white (5.7:1) meets WCAG AA for all text sizes
- **Semantic h2**: Properly structured heading hierarchy (h1 → h2)
- **Light Weight**: May be harder to read for some users - use sparingly
- **Supporting Content**: Provides context to h1 without being critical content

---

#### `h2.section-title` - Section Headings

**Purpose:** Major section headings that divide content into distinct areas. Bold, uppercase Oswald headings create clear visual breaks and content organization.

**CSS Implementation:**

```css
h2.section-title {
  font-family: var(--font-heading);     /* Oswald */
  font-size: var(--text-md);            /* 14px */
  font-weight: var(--font-bold);        /* 700 */
  color: var(--color-black);
  text-transform: uppercase;
  margin-bottom: var(--space-5);        /* 20px */
}
```

**HTML Structure:**

```html
<h2 class="section-title">ABOUT ME</h2>
<p>Section content...</p>

<h2 class="section-title">RECENT WORK</h2>
<p>More content...</p>
```

**Styling Details:**

- **Font**: Oswald (heading font) matches h1 for consistency
- **Bold weight (700)**: Strong visual presence
- **Black color**: High emphasis, matches h1
- **14px size**: Smaller than h1 but distinct from body text
- **UPPERCASE**: Consistent with other Oswald headings
- **20px margin-bottom**: Generous spacing separates heading from content
- **Line-height 1**: Tight, compact (inherited from h1-h6 reset)

**Responsive Behavior:**

```css
/* Mobile (≤480px) */
h2.section-title {
  font-size: var(--text-base);          /* 14px → 14px (no effective change) */
  margin-bottom: var(--space-4);        /* 20px → 16px */
}
```

On mobile:
- Font size effectively stays 14px (--text-base updates to 14px on mobile)
- Bottom margin reduces from 20px to 16px to conserve vertical space

**Usage Guidelines:**

- ✅ Use for major section divisions (About, Work, Contact, etc.)
- ✅ Always use UPPERCASE text
- ✅ Use multiple times per page to organize content
- ✅ Maintain heading hierarchy (h1 → h2.section-title → h3)
- ✅ Use semantic h2 element
- ❌ Don't use for the main page title (use h1)
- ❌ Don't use for subtle subtitles (use h2.tagline)
- ❌ Don't use sentence case (breaks design consistency)
- ❌ Don't skip heading levels (h1 → h3 without h2)

**Best Practices:**

**When to use h2.section-title:**
- Major content sections (About, Portfolio, Services, Contact)
- Blog post sections or chapters
- Content category headings
- Primary content divisions

**Common Patterns:**

```html
<!-- Content section pattern -->
<h2 class="section-title">ABOUT ME</h2>
<p>Paragraph content...</p>
<p>More content...</p>

<!-- Multiple sections -->
<h2 class="section-title">EXPERIENCE</h2>
<p>Experience details...</p>

<h2 class="section-title">EDUCATION</h2>
<p>Education details...</p>
```

**Accessibility Notes:**

- **Proper Hierarchy**: h2 follows h1, maintains logical document structure
- **High Contrast**: Black on white (21:1) exceeds WCAG AAA
- **Semantic HTML**: Screen readers identify section structure
- **Adequate Spacing**: 20px margin-bottom creates clear visual separation

---

#### `h3` - Subsection Headings

**Purpose:** Subsection headings within content sections. Smaller than h2.section-title but still visually distinct, used for organizing content within major sections.

**CSS Implementation:**

```css
h3 {
  font-family: var(--font-heading);     /* Oswald */
  font-size: var(--text-lg);            /* 16px */
  font-weight: var(--font-bold);        /* 700 */
  line-height: 1;
  color: var(--color-gray-700);         /* #555555 */
  text-transform: uppercase;
  margin-bottom: var(--space-3);        /* 12px */
}
```

**HTML Structure:**

```html
<h2 class="section-title">SERVICES</h2>

<h3>WEB DEVELOPMENT</h3>
<p>Description of web development services...</p>

<h3>CONSULTING</h3>
<p>Description of consulting services...</p>
```

**Styling Details:**

- **Font**: Oswald (heading font)
- **16px size**: Larger than body (13px) and h2.section-title (14px) for hierarchy
- **Bold weight (700)**: Strong emphasis
- **Gray-700 color**: Slightly less prominent than black headings (creates hierarchy)
- **UPPERCASE**: Consistent with other Oswald headings
- **12px margin-bottom**: Moderate spacing before content
- **Line-height 1**: Tight, compact appearance

**Note on Hierarchy:** Interestingly, h3 (16px) is visually **larger** than h2.section-title (14px). The hierarchy is maintained through color (black vs gray-700) and positioning rather than size alone. This creates visual variety while maintaining clear structure.

**Responsive Behavior:**

```css
/* Mobile (≤480px) */
h3 {
  font-size: var(--text-md);  /* 16px → 14px */
}
```

On mobile:
- Font size reduces from 16px to 14px to conserve space
- This brings h3 to the same size as h2.section-title on mobile
- Hierarchy maintained through color and context

**Usage Guidelines:**

- ✅ Use within sections for subsection headings
- ✅ Use after h2.section-title in heading hierarchy
- ✅ Always use UPPERCASE text
- ✅ Use for widget titles, contact sections, content subdivisions
- ✅ Multiple h3 elements can appear within one h2 section
- ❌ Don't use as the primary page heading (use h1)
- ❌ Don't use for major sections (use h2.section-title)
- ❌ Don't skip heading levels in hierarchy
- ❌ Don't use sentence case

**Common Use Cases:**

- Widget titles (Subscribe, Connect, Recent Posts)
- Contact section headings (Contact Me, Follow Me)
- Content subdivisions within major sections
- FAQ question headings
- Service or product category names

**Best Practices:**

```html
<!-- Within a major section -->
<h2 class="section-title">PORTFOLIO</h2>

<h3>WEB PROJECTS</h3>
<p>Project descriptions...</p>

<h3>MOBILE APPS</h3>
<p>App descriptions...</p>

<!-- Widget titles -->
<aside class="sidebar">
  <div class="widget">
    <h3>SUBSCRIBE</h3>
    <p>Get updates...</p>
  </div>
</aside>
```

**Accessibility Notes:**

- **Proper Hierarchy**: h3 follows h2, maintains document outline
- **Color Contrast**: Gray-700 on white (7.4:1) meets WCAG AAA
- **Semantic Structure**: Screen readers navigate by heading levels
- **Adequate Spacing**: 12px margin-bottom separates heading from content

---

#### `p` - Paragraphs

**Purpose:** Standard body text and paragraph content. Optimized for comfortable reading with appropriate line-height and spacing.

**CSS Implementation:**

```css
body {
  font-family: var(--font-body);        /* Helvetica Neue */
  font-size: var(--text-base);          /* 13px */
  font-weight: var(--font-normal);      /* 400 */
  line-height: 1.75;
  color: var(--color-gray-700);         /* #555555 */
}

p {
  margin-bottom: 13px;
}
```

**HTML Structure:**

```html
<p>This is a standard paragraph with body text. It uses Helvetica Neue at 13px with comfortable line-height of 1.75 for optimal readability.</p>

<p>Paragraphs automatically have 13px margin-bottom for vertical rhythm.</p>
```

**Styling Details:**

- **Font**: Helvetica Neue (body font)
- **13px size**: Optimized for comfortable reading at typical screen distances
- **Normal weight (400)**: Standard reading weight
- **Gray-700 color**: Softer than black, reduces eye strain for body text
- **Line-height 1.75**: Generous spacing for comfortable reading (exceeds WCAG 1.5 recommendation)
- **13px margin-bottom**: Matches font size for consistent vertical rhythm

**Responsive Behavior:**

```css
/* Mobile (≤480px) */
:root {
  --text-base: 14px;  /* Increases from 13px */
}

body {
  line-height: 1.6;   /* Slightly tighter from 1.75 */
}

p {
  margin-bottom: var(--space-4);  /* 16px instead of 13px */
}
```

On mobile:
- Font size increases to 14px for better readability on small screens
- Line-height reduces to 1.6 to conserve vertical space
- Margin-bottom increases to 16px (--space-4) for clearer separation

**Usage Guidelines:**

- ✅ Use for all body text and content paragraphs
- ✅ Rely on inherited body styles (no need to style p directly)
- ✅ Use gray-700 color for standard text (inherited)
- ✅ Maintain 1.75 line-height for readability
- ❌ Don't use paragraphs for headings (use h1, h2, h3)
- ❌ Don't override line-height to less than 1.5 (reduces readability)
- ❌ Don't use black color for body text (too harsh for long reading)

**Line Length & Readability:**

With content-width of 580px and 13px font size:
- Approximately **60-75 characters per line**
- Falls within optimal range (50-75 chars) for comfortable reading
- Prevents overly long lines that reduce comprehension

**Best Practices:**

- Keep paragraphs focused (3-5 sentences typically)
- Use paragraph breaks to create visual rhythm
- Don't override inherited body styles unless necessary
- Maintain consistent spacing between paragraphs

**Accessibility Notes:**

- **Color Contrast**: Gray-700 on white (7.4:1) exceeds WCAG AAA for body text
- **Readable Size**: 13px exceeds minimum recommended (12px)
- **Generous Line-Height**: 1.75 improves readability for dyslexic users
- **Mobile Increase**: Text increases to 14px on mobile prevents squinting

---

#### `a` - Default Links

**Purpose:** Standard inline links within content. Default styling uses black color for subtle integration, with teal hover state for clear interaction feedback.

**CSS Implementation:**

```css
a {
  color: var(--color-black);
  text-decoration: none;
  transition: color var(--transition-normal);  /* 0.2s ease */
}

a:hover {
  color: var(--color-teal-500);
}
```

**HTML Structure:**

```html
<p>I work at <a href="https://amazon.com">Amazon</a> on the Disaster Relief team.</p>

<h1><a href="/">ABE DIAZ</a></h1>
```

**Styling Details:**

- **Default color**: Black (same as headings) for subtle integration
- **No underline**: text-decoration: none (cleaner appearance)
- **Smooth transition**: 0.2s color change on hover
- **Hover color**: Teal-500 provides clear interactive feedback
- **Inherits font**: Uses surrounding text font (Oswald in headings, Helvetica in body)

**Interaction States:**

| State | Color | Underline | Notes |
|-------|-------|-----------|-------|
| Default | Black | None | Subtle integration with text |
| Hover | Teal-500 | None | Clear interactive feedback |
| Focus | Teal-500 | None | Same as hover (browser default focus ring appears) |
| Visited | Black | None | No visited state styling |

**Usage Guidelines:**

- ✅ Use for inline links within paragraphs
- ✅ Use for navigation links
- ✅ Use for heading links (h1, h3, etc.)
- ✅ Rely on hover state to indicate interactivity
- ✅ Use when links should integrate subtly with content
- ❌ Don't add underlines (already styled without)
- ❌ Don't override transition timing (maintains consistency)
- ❌ Don't use for high-emphasis CTAs (use .accent-link instead)

**When to Use Default Links:**

- Navigation menu items
- Inline references within paragraphs
- Footer links
- Site branding (h1 link)
- Secondary links that shouldn't draw primary attention

**Accessibility Considerations:**

**Potential Issue:** Links without underlines can be hard to distinguish from surrounding text, especially for users with color blindness.

**Mitigations in this system:**
- **Hover state**: Clear color change to teal provides feedback
- **Context**: Links typically appear in contexts where they're expected (navigation, known clickable areas)
- **Color change**: Black → teal on hover is noticeable
- **Consider**: Adding underlines for better accessibility, or use .accent-link for critical links

**Best Practice:** For critical links or calls-to-action within body text, use `.accent-link` instead, which provides better visual distinction.

**Accessibility Notes:**

- **Color Contrast**: Black on white (21:1) exceeds WCAG AAA
- **Hover Feedback**: Teal color change provides clear interaction cue
- **Keyboard Accessible**: Focus states work (browser default focus ring)
- **Limitation**: Lack of underline may reduce discoverability - consider context

---

#### `.accent-link` - Emphasized Links

**Purpose:** High-visibility links that stand out from surrounding content. Used for calls-to-action, external links, and emphasized references that should draw attention.

**CSS Implementation:**

```css
.accent-link {
  color: var(--color-teal-500);
}

.accent-link:hover {
  text-decoration: underline;
}
```

**HTML Structure:**

```html
<p>Check out my LinkedIn page at <a href="http://linkedin.com/in/abediaz" class="accent-link">http://linkedin.com/in/abediaz</a>.</p>

<p>I graduated from <a href="http://uprm.edu/" class="accent-link">UPR-Mayaguez</a> with a degree in Computer Engineering.</p>
```

**Styling Details:**

- **Teal color**: Highly visible, indicates interactivity
- **No underline by default**: Clean appearance
- **Underline on hover**: Adds additional interaction feedback
- **Inherits transition**: Uses 0.2s transition from base `a` styles
- **Stacks with `a`**: Extends default link behavior

**Interaction States:**

| State | Color | Underline | Notes |
|-------|-------|-----------|-------|
| Default | Teal-500 | None | High visibility |
| Hover | Teal-500 | Underline | Additional emphasis on hover |
| Focus | Teal-500 | Underline (on hover) | Follows hover behavior |
| Visited | Teal-500 | None | No visited state distinction |

**Usage Guidelines:**

- ✅ Use for calls-to-action within body text
- ✅ Use for external links that should stand out
- ✅ Use for emphasized references or important links
- ✅ Use when you want links to be immediately visible
- ✅ Use for URLs displayed as text (e.g., http://linkedin.com/in/abediaz)
- ❌ Don't overuse - reduces effectiveness if everything is accented
- ❌ Don't use for navigation (too prominent)
- ❌ Don't use in headings (already have hover states)

**When to Use .accent-link:**

1. **External references** - Links to other websites, institutions, products
2. **Calls-to-action** - "Check out my work", "Follow me on Twitter"
3. **Emphasized links** - Links that are important to the narrative
4. **Displayed URLs** - When showing the actual URL as link text
5. **Social media links** - Links to LinkedIn, Twitter, Instagram

**When NOT to Use .accent-link:**

1. Navigation menu items (use default styling)
2. Footer links (usually de-emphasized)
3. H1 branding links (use default)
4. Every link in a paragraph (dilutes emphasis)

**Comparison: Default vs Accent Links:**

```html
<!-- Default link - subtle integration -->
<p>I work at <a href="https://amazon.com">Amazon</a>.</p>
<!-- Link is black, blends with text, teal on hover -->

<!-- Accent link - high visibility -->
<p>Connect with me on <a href="http://linkedin.com/in/abediaz" class="accent-link">LinkedIn</a>.</p>
<!-- Link is teal, stands out, underlines on hover -->
```

**Best Practices:**

- Use accent links sparingly (2-5 per page maximum)
- Reserve for truly important or actionable links
- Balance with default links to create hierarchy
- Use for social media and portfolio links
- Consider user intent - what do you want users to click?

**Accessibility Notes:**

- **High Visibility**: Teal color (3.3:1 contrast) is noticeable but below WCAG AA for small text
- **Size Matters**: Teal meets WCAG AA for large text (18px+) only
- **Underline on Hover**: Provides additional non-color cue
- **Better for Color Blindness**: Stands out more than default black links
- **Recommendation**: Accent links are more accessible than default links due to color distinction

**Accessibility Contrast:**

- Teal-500 on white: **3.3:1** (WCAG AA for large text only)
- Use accent links for larger text (14px+) or ensure underline for smaller sizes
- The underline on hover helps users with color vision deficiencies

---

#### Typography Components Best Practices

**Heading Hierarchy:**

- ✅ Always use h1 once per page as the primary heading
- ✅ Follow logical hierarchy: h1 → h2 → h3 (don't skip levels)
- ✅ Use h2.tagline for subtitles, h2.section-title for sections
- ✅ Use h3 for subsections within h2.section-title areas
- ✅ Use semantic HTML for accessibility and SEO
- ❌ Don't use multiple h1 elements
- ❌ Don't skip heading levels (e.g., h1 → h3 without h2)
- ❌ Don't use headings for styling (use CSS classes on p or div)

**Typography Pairing:**

```html
<!-- Correct heading hierarchy -->
<h1><a href="/">ABE DIAZ</a></h1>
<h2 class="tagline">Seattle/Tech/Evangelist</h2>

<h2 class="section-title">ABOUT ME</h2>
<p>Paragraph content...</p>

<h3>BACKGROUND</h3>
<p>More content...</p>
```

**Link Usage:**

- ✅ Use default links for navigation and subtle inline references
- ✅ Use accent links for CTAs and emphasized references
- ✅ Limit accent links to 2-5 per page
- ✅ Ensure links have clear hover states
- ✅ Use descriptive link text ("read the article" not "click here")
- ❌ Don't make everything an accent link
- ❌ Don't override link transitions
- ❌ Don't use vague link text

**Paragraph Spacing:**

- ✅ Let paragraphs inherit body styles
- ✅ Maintain 13px (or 14px mobile) margin-bottom
- ✅ Keep line-height at 1.75 (1.6 mobile)
- ✅ Use content-width (580px) for optimal line length
- ❌ Don't reduce line-height below 1.5
- ❌ Don't create overly long paragraphs (reduces scannability)

**Responsive Typography:**

- ✅ Test all typography at mobile breakpoints (480px, 360px)
- ✅ Trust the responsive CSS variables (--text-4xl, --text-base)
- ✅ Verify heading hierarchy remains clear on mobile
- ✅ Ensure adequate touch targets for links (minimum 44px)
- ❌ Don't override responsive font sizes without testing
- ❌ Don't create layouts that cause horizontal scrolling

---

#### Typography Accessibility Summary

| Element | Color | Contrast | WCAG Level | Notes |
|---------|-------|----------|------------|-------|
| h1 | Black on white | 21:1 | AAA | All sizes |
| h2.tagline | Gray-600 on white | 5.7:1 | AA | All sizes |
| h2.section-title | Black on white | 21:1 | AAA | All sizes |
| h3 | Gray-700 on white | 7.4:1 | AAA | 14px+ |
| p | Gray-700 on white | 7.4:1 | AAA | 13px+ |
| a (default) | Black on white | 21:1 | AAA | Lacks underline - may reduce discoverability |
| a.accent-link | Teal-500 on white | 3.3:1 | AA (Large) | 18px+ only; underline on hover helps |

**Accessibility Best Practices:**

1. **Use Semantic HTML**: Always use h1, h2, h3, p elements (not styled divs)
2. **Maintain Hierarchy**: Logical heading structure helps screen reader navigation
3. **Sufficient Contrast**: All text meets WCAG AA minimum (most exceed AAA)
4. **Readable Sizes**: All text 13px+ exceeds minimum recommendations
5. **Line-Height**: 1.75 for body text exceeds WCAG 1.5 recommendation
6. **Link Distinction**: Consider adding underlines or using accent links for critical CTAs
7. **Focus States**: Ensure keyboard users can see focus (browser default focus rings present)

---

#### Typography Components Quick Reference

```
HEADINGS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
h1                Oswald 80px Bold UPPERCASE Black
                  (48px tablet, 32px mobile, 28px small mobile)
                  Use: Main page title, site branding (once per page)

h2.tagline        Helvetica 14px Light Gray-600
                  Use: Subtitle below h1, de-emphasized secondary text

h2.section-title  Oswald 14px Bold UPPERCASE Black
                  Use: Major section headings, content divisions

h3                Oswald 16px Bold UPPERCASE Gray-700
                  (14px mobile)
                  Use: Subsections, widget titles, contact headings

BODY TEXT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
p                 Helvetica 13px Normal Gray-700 (lh: 1.75)
                  (14px mobile, lh: 1.6)
                  Margin-bottom: 13px (16px mobile)
                  Use: All body text and paragraphs

LINKS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
a (default)       Color: Black → Teal-500 on hover
                  No underline, 0.2s transition
                  Use: Navigation, inline references, subtle links

a.accent-link     Color: Teal-500, underline on hover
                  Use: CTAs, emphasized links, external references
                  Limit: 2-5 per page

HIERARCHY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
h1 > h2.section-title > h3 > p
     h2.tagline (pairs with h1)

RESPONSIVE CHANGES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Mobile (≤480px):
  h1: 80px → 32px (letter-spacing: -1px)
  h3: 16px → 14px
  p: 13px → 14px, line-height: 1.75 → 1.6
  h2.section-title margin-bottom: 20px → 16px

Small Mobile (≤360px):
  h1: 32px → 28px
```

---

### Interactive Components

*This section will document buttons (btn, btn-primary), form inputs (email-form), and interactive elements (like-btn, share-btn).*

**Coming Soon:** Interactive component documentation with state variations and accessibility notes.

---

### Content Components

*This section will document widget, profile-image, flight-stats, contact-section, social-links, share-section, signature, and subscriber-count components.*

**Coming Soon:** Content component documentation with composition patterns.

---

## Responsive Design

### Breakpoints

*This section will document the three breakpoint system (768px, 480px, 360px) with what changes at each breakpoint.*

**Coming Soon:** Responsive breakpoint documentation and adaptation patterns.

---

### Mobile Adaptations

*This section will explain how components adapt on mobile devices and responsive design patterns.*

**Coming Soon:** Mobile adaptation documentation.

---

## CSS Architecture

### Reset & Base Styles

*This section will document the CSS reset approach, box-sizing methodology, and base body/html styles.*

**Coming Soon:** CSS reset and base styles documentation.

---

### Browser Normalization

*This section will cover font smoothing, browser-specific adjustments, and compatibility notes.*

**Coming Soon:** Browser normalization documentation.

---

## Quick Reference

### CSS Variables

*Quick lookup table of all CSS custom properties.*

**Coming Soon:** Complete CSS variables reference table.

---

### Component Classes

*Alphabetical list of all component class names.*

**Coming Soon:** Component class reference.

---

### Common Patterns

*Cheat sheet of frequently used patterns and combinations.*

**Coming Soon:** Common patterns cheat sheet.

---

## Usage Examples

### Best Practices

*This section will provide practical code examples showing how to combine components and follow design system patterns.*

**Coming Soon:** Usage examples and best practices.

---

### Do's and Don'ts

*This section will provide guidance on correct and incorrect usage of the design system.*

**Coming Soon:** Do's and don'ts guidance.

---

## Contributing

This design system evolves with the site. When extending or modifying:

1. **Use existing tokens first** - Before creating new values, check if existing design tokens can solve your need
2. **Maintain the 4px spacing rhythm** - All spacing should be divisible by 4
3. **Follow naming conventions** - Use BEM-like naming for new components (`.component-name`)
4. **Document as you go** - Update this documentation when adding new patterns
5. **Test responsively** - Verify changes work across all breakpoints

---

## Version History

- **v1.0** (2026-01-01) - Initial documentation structure created
  - Foundation sections outlined
  - Design philosophy established
  - Component categories defined

---

*Last Updated: 2026-01-01*
*Maintained by: Abe Diaz*
