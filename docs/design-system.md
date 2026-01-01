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

*This section will document the 4px-based spacing scale, layout dimensions, border radii, and transition values.*

**Coming Soon:** Complete spacing and layout token documentation.

---

## Components

Components are reusable UI patterns built using the design tokens. Each component has a specific purpose and usage pattern.

### Layout Components

*This section will document structural components: site-container, site-header, site-nav, site-main, content, sidebar, site-footer.*

**Coming Soon:** Layout component documentation with HTML structure examples.

---

### Typography Components

*This section will document heading variants (h1, h2.tagline, h2.section-title, h3), paragraph styles, and link styles.*

**Coming Soon:** Typography component documentation with usage examples.

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
