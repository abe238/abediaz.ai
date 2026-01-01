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
- **Systematic Consistency**: A [4px spacing scale](#spacing--layout) and carefully chosen [color palette](#color-palette) ensure visual harmony across the entire site.
- **Performance-Conscious**: CSS-first approach with minimal JavaScript dependency for faster load times and better accessibility.
- **Responsive by Default**: Mobile-first thinking with thoughtful [breakpoints](#breakpoints) that adapt to different screen sizes without compromising the design intent.
- **Accessibility Matters**: [Color contrast ratios](#accessibility-summary), semantic HTML, and keyboard navigation are first-class considerations.

**Design Ethos:**

This is a personal site for a technologist and evangelist. The design reflects the subject's personality: direct, authentic, and human. The [teal accent color](#accent-colors) (#36BCAB) adds a touch of warmth to an otherwise neutral palette, while the [Oswald typeface](#font-families) for headings provides strong visual hierarchy without being overly formal.

The design system embraces constraints as a feature, not a limitation. By providing exactly what's needed—no more, no less—it enables rapid development while maintaining consistency.

### Overview

This documentation covers approximately 520 lines of CSS organized into:

- **43 CSS Custom Properties** ([Design Tokens](#design-tokens))
  - [14 color primitives](#color-palette)
  - [12 typography tokens](#typography) (3 fonts, 6 sizes, 3 weights)
  - [9 spacing values](#spacing--layout) (4px-based scale)
  - [4 layout dimensions](#layout-dimensions)
  - [2 border radii](#border-radii)
  - [2 transition timings](#transition-values)

- **15+ UI Components** ([Components](#components))
  - [Layout structures](#layout-components) (container, header, sidebar, footer)
  - [Typography variants](#typography-components) (headings, links, paragraphs)
  - [Interactive elements](#interactive-components) (buttons, forms)
  - [Content modules](#content-components) (widgets, profile, contact sections)

- **3 Responsive Breakpoints** ([Responsive Design](#responsive-design))
  - [Desktop](#desktop-default-768px) (default)
  - [Tablet](#tablet-768px) (≤768px)
  - [Mobile](#mobile-480px) (≤480px)
  - [Small Mobile](#small-mobile-360px) (≤360px)

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
   - Main page headings ([h1](#h1---main-heading))
   - Section titles ([h2.section-title](#h2section-title---section-headings))
   - Subsection headings ([h3](#h3---subsection-headings))
   - Use when maximum emphasis is needed

2. **White (`--color-white`)**
   - Page background
   - Input field backgrounds ([.email-form](#email-form---email-signup-form))
   - Text on colored button backgrounds ([.btn-primary](#btn-primary---primary-button))
   - Clean slate for content

3. **Gray-700 (`--color-gray-700`)**
   - Default for all body text ([paragraphs](#p---paragraphs))
   - Paragraph content
   - Standard links (before hover - see [links](#a---default-links))
   - Primary reading text

4. **Gray-600 (`--color-gray-600`)**
   - Taglines and subtitles ([h2.tagline](#h2tagline---taglinesubtitle))
   - Footer text ([.site-footer](#site-footer))
   - Less prominent information
   - Meta information ([.subscriber-count](#subscriber-count---subscriber-count))

5. **Gray-500 (`--color-gray-500`)**
   - Input borders (default state - see [.email-form](#email-form---email-signup-form))
   - Form field outlines
   - Interactive element boundaries

6. **Gray-200 (`--color-gray-200`)**
   - Section dividers
   - Widget borders ([.widget](#widget---widget-container))
   - Subtle separators
   - Visual rhythm elements

7. **Teal-500 (`--color-teal-500`)**
   - All link hover states (see [links](#a---default-links))
   - Focus indicators
   - Accent links ([.accent-link](#accent-link---emphasized-links))
   - Interactive element feedback
   - Primary call-to-action affordance

8. **Blue-500 (`--color-blue-500`)**
   - LinkedIn button background ([.btn-primary](#btn-primary---primary-button))
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

Components are reusable UI patterns built using the [design tokens](#design-tokens). Each component has a specific purpose and usage pattern. For quick reference, see the [Component Classes](#component-classes) section.

### Layout Components

Layout components form the structural foundation of the site. These components establish the page architecture, content flow, and responsive behavior. Built using modern flexbox patterns, they provide a clean two-column layout on desktop that gracefully adapts to single-column on mobile.

#### Design Rationale

The layout system is designed around these principles:

1. **Content-First Architecture** - The layout prioritizes readable [content width](#layout-dimensions) (580px) over maximizing screen usage
2. **Flexible Two-Column Pattern** - Desktop layout supports content + sidebar; mobile stacks vertically
3. **Semantic HTML Structure** - Uses proper semantic elements (header, nav, main, article, footer)
4. **Flexbox-Based** - Modern flexbox provides reliable, predictable layout behavior
5. **Responsive by Default** - Layout adapts naturally at defined [breakpoints](#breakpoints) without complex overrides

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

Interactive components are elements designed for user interaction—buttons, form inputs, and action triggers. These components provide clear visual affordance (indicating clickability), smooth state transitions, and accessible keyboard/mouse interactions.

#### Design Rationale

Interactive components serve as the bridge between users and functionality. The system provides:

1. **Clear Affordance** - Visual cues (borders, hover states, cursor) indicate interactivity
2. **Consistent State Transitions** - Smooth color/border changes provide feedback
3. **Accessible Interactions** - Focus states, keyboard navigation, and sufficient contrast
4. **Purposeful Variants** - Different button/link styles serve specific use cases
5. **Minimal Styling** - Clean, unobtrusive design that supports content

**Philosophy:**

Interactive components should feel responsive and immediate without being flashy. Subtle hover states (color shifts, border color changes) provide feedback without distracting from content. The system uses the teal accent color consistently for hover/focus states, creating a predictable interaction pattern throughout the site.

Form inputs are designed to feel native and familiar, using system fonts and minimal styling. Buttons are intentionally compact (small font sizes, tight padding) to avoid overwhelming the layout.

---

#### Component Overview

| Component | Display | Size | Color | Border | Padding | Primary Use Case |
|-----------|---------|------|-------|--------|---------|------------------|
| **btn** | inline-block | 11px | — | none | 8px 12px | Base button class (requires variant) |
| **btn-primary** | — | — | White on Blue-500 | none | — | Primary CTA button (LinkedIn, subscribe) |
| **email-form** | block | 13px | Gray-700 | Gray-500 | Label + Input | Email signup forms |
| **like-btn** | inline-flex | 12px | Gray-600 | none | — | Like/heart action with icon |
| **share-btn** | inline-flex | 11px | Gray-600 | Gray-200 | 4px 8px | Share buttons with icons |

---

#### `.btn` - Base Button

**Purpose:** The foundational button class providing core button styling. Always used in combination with a variant class (e.g., `.btn-primary`).

**CSS Implementation:**

```css
.btn {
  display: inline-block;
  font-family: var(--font-system);           /* System fonts for native feel */
  font-size: var(--text-xs);                 /* 11px */
  font-weight: var(--font-normal);           /* 400 */
  padding: var(--space-2) var(--space-3);    /* 8px 12px */
  border: none;
  border-radius: var(--radius-sm);           /* 2px */
  cursor: pointer;
  transition: background-color var(--transition-normal);  /* 0.2s ease */
}
```

**HTML Structure:**

```html
<!-- Must be combined with a variant class -->
<button class="btn btn-primary">Subscribe</button>
<a href="#" class="btn btn-primary">Connect on LinkedIn</a>
```

**Styling Details:**

- **System Font**: Uses OS native fonts (--font-system) for familiar, native button appearance
- **Compact Size**: 11px font keeps buttons unobtrusive
- **Tight Padding**: 8px vertical, 12px horizontal creates compact but clickable target
- **Minimal Radius**: 2px border-radius softens corners without looking rounded
- **Smooth Transition**: 0.2s background-color change for hover states
- **Inline-Block**: Allows padding and respects text flow

**Button Variants:**

The `.btn` class itself provides no color—it must be combined with a variant:

- **btn-primary**: Blue background for primary actions (currently the only variant)

**Usage Guidelines:**

- ✅ Always combine with a variant class (`.btn-primary`)
- ✅ Use semantic `<button>` for actions, `<a>` for navigation
- ✅ Keep button text short and action-oriented (1-3 words)
- ✅ Use system font for native OS appearance
- ❌ Don't use `.btn` alone (requires a variant for color)
- ❌ Don't override font-family (system fonts are intentional)
- ❌ Don't use for non-interactive elements
- ❌ Don't make buttons too large (compact is intentional)

**Accessibility Notes:**

- **Cursor pointer**: Clearly indicates clickability
- **Inline-block**: Allows sufficient padding for touch targets
- **Keyboard accessible**: Works with native button/link keyboard behavior
- **Transition**: Smooth state changes reduce jarring visual shifts

---

#### `.btn-primary` - Primary Button

**Purpose:** The primary call-to-action button with blue background. Used for important actions like "Subscribe" or "Connect on LinkedIn".

**CSS Implementation:**

```css
.btn-primary {
  background-color: var(--color-blue-500);   /* #0073B1 - LinkedIn blue */
  color: var(--color-white);
}

.btn-primary:hover {
  background-color: #005a8c;                 /* Darker blue */
  color: var(--color-white);
}
```

**HTML Structure:**

```html
<!-- Email subscription button -->
<button type="submit" class="btn btn-primary">Subscribe</button>

<!-- LinkedIn link styled as button -->
<a href="https://linkedin.com/in/username" class="btn btn-primary">
  Connect on LinkedIn
</a>
```

**Styling Details:**

- **Blue Background**: Uses LinkedIn brand color (#0073B1)
- **White Text**: High contrast on blue background
- **Darker Hover**: Hover state (#005a8c) provides clear feedback
- **Smooth Transition**: Inherits 0.2s background-color transition from `.btn`

**Color Contrast:**

- **Default State**: White on Blue-500 (#0073B1) = **4.6:1** (WCAG AA for large text 18px+)
- **Hover State**: White on #005a8c = **6.2:1** (WCAG AA for all text sizes)
- **Note**: At 11px, the button text is small, but buttons are considered UI components (not body text)

**Responsive Behavior:**

Buttons maintain consistent styling across all breakpoints. No responsive adjustments needed due to compact base size.

**Usage Guidelines:**

- ✅ Use for primary calls-to-action (Subscribe, Connect, Sign Up)
- ✅ Limit to 1-2 primary buttons per section (avoid CTA overload)
- ✅ Use for external platform actions (LinkedIn, etc.)
- ✅ Ensure button text is action-oriented ("Subscribe" not "Subscription")
- ❌ Don't use multiple primary buttons in close proximity
- ❌ Don't use for destructive actions (delete, remove)
- ❌ Don't override the blue color (maintains LinkedIn brand consistency)

**When to Use:**

- Email newsletter subscription
- Social media connections (LinkedIn)
- Primary form submissions
- Download/get started actions

**When NOT to Use:**

- Navigation links (use default links or `.accent-link`)
- Secondary actions (consider creating `.btn-secondary` variant)
- Inline text links (use `<a>` with appropriate class)

**Accessibility Notes:**

- **Sufficient Contrast**: Meets WCAG AA for interactive components
- **Clear Hover State**: Color darkens on hover, providing visual feedback
- **Semantic HTML**: Use `<button type="submit">` for forms, `<a href="...">` for links
- **Keyboard Accessible**: Inherits native button/link keyboard behavior (Enter/Space)
- **Focus Outline**: Browser default focus outline visible (not removed with outline:none)

---

#### `.email-form` - Email Signup Form

**Purpose:** A form component for email address collection, typically used in newsletter signups or subscription widgets. Provides labeled input field with focus states.

**CSS Implementation:**

```css
.email-form {
  margin-top: var(--space-3);               /* 12px */
}

.email-form label {
  display: block;
  font-size: var(--text-base);              /* 13px */
  color: var(--color-gray-700);             /* #555555 */
  margin-bottom: var(--space-2);            /* 8px */
}

.email-form input[type="email"] {
  width: 100%;
  padding: var(--space-2) var(--space-3);   /* 8px 12px */
  font-family: var(--font-body);            /* Helvetica Neue */
  font-size: var(--text-base);              /* 13px */
  border: 1px solid var(--color-gray-500);  /* #767676 */
  border-radius: 0;                         /* Sharp corners for inputs */
  background: var(--color-white);
  margin-bottom: var(--space-3);            /* 12px */
}

.email-form input[type="email"]:focus {
  outline: none;
  border-color: var(--color-teal-500);      /* Teal focus state */
}
```

**HTML Structure:**

```html
<form class="email-form" action="/subscribe" method="post">
  <label for="email">Email Address</label>
  <input
    type="email"
    id="email"
    name="email"
    placeholder="your@email.com"
    required
  >
  <button type="submit" class="btn btn-primary">Subscribe</button>
</form>
```

**Styling Details:**

**Form Container:**
- **12px top margin**: Separates form from preceding content
- **Block display**: Stacks label, input, button vertically

**Label:**
- **Block display**: Full-width, forces input to new line
- **13px font**: Matches body text size
- **Gray-700 color**: Standard body text color
- **8px bottom margin**: Tight spacing to input

**Input Field:**
- **100% width**: Full-width within container
- **8px 12px padding**: Comfortable input area matching button padding
- **Body font**: Helvetica Neue for consistent text appearance
- **13px font**: Matches body text for seamless reading
- **Gray-500 border**: Medium gray (#767676) provides clear boundary
- **Zero border-radius**: Sharp corners (intentional design choice)
- **White background**: Clean, standard input appearance
- **12px bottom margin**: Space before submit button

**Focus State:**
- **No outline**: Default browser outline removed (controversial, but common)
- **Teal border**: Border changes to accent color on focus
- **Clear visual feedback**: Border color shift indicates active input

**Input Border Radius Rationale:**

Inputs use `border-radius: 0` (sharp corners) while buttons use `border-radius: 2px`. This is an intentional design choice:
- **Inputs**: Sharp corners feel more "form-like" and traditional
- **Buttons**: Subtle rounding indicates interactivity/clickability
- The contrast helps visually distinguish input fields from buttons

**Responsive Behavior:**

```css
/* Mobile (≤480px) */
.email-form input[type="email"] {
  font-size: var(--text-base);  /* 13px → 14px on mobile */
}
```

On mobile, input text size increases to 14px (via --text-base variable update), preventing iOS zoom on focus.

**Usage Guidelines:**

- ✅ Use semantic `<form>` element with proper action/method
- ✅ Include `<label>` for accessibility (explicit for/id association)
- ✅ Use `type="email"` for mobile keyboard optimization
- ✅ Add `required` attribute for basic validation
- ✅ Pair with `.btn-primary` submit button
- ✅ Use placeholder text for example format ("your@email.com")
- ❌ Don't use without proper label (hidden or visible)
- ❌ Don't remove focus styles without alternative indication
- ❌ Don't make inputs narrower than container (100% width is intentional)
- ❌ Don't use for other input types (text, password) without testing

**Form Composition Pattern:**

Typical email form structure:
1. **Container**: `<form class="email-form">`
2. **Label**: Descriptive text ("Email Address", "Your Email")
3. **Input**: `type="email"` with proper attributes
4. **Submit Button**: `<button class="btn btn-primary">Subscribe</button>`

**Accessibility Notes:**

- **Label Association**: Explicit `for`/`id` pairing ensures screen reader announcement
- **Input Type**: `type="email"` triggers appropriate mobile keyboard (@ key visible)
- **Border Contrast**: Gray-500 (#767676) border = **4.6:1** (sufficient for UI components)
- **Focus Indicator**: Teal border provides clear focus indication
- **Semantic HTML**: Proper `<form>`, `<label>`, `<input>` elements
- **Keyboard Accessible**: Tab navigation works naturally

**Focus State Considerations:**

The form removes the default outline (`outline: none`) and replaces it with a border color change. This approach has trade-offs:

**Pros:**
- ✅ Cleaner visual appearance
- ✅ Teal border aligns with brand colors
- ✅ Still provides clear focus indication

**Cons:**
- ❌ May be less obvious than default outline for some users
- ❌ Requires ensuring border color change is sufficient

**Best Practice Recommendation:** Consider adding both border color change AND a subtle box-shadow for even clearer focus indication:

```css
.email-form input[type="email"]:focus {
  outline: none;
  border-color: var(--color-teal-500);
  box-shadow: 0 0 0 2px rgba(54, 188, 171, 0.2);  /* Optional enhancement */
}
```

---

#### `.like-btn` - Like Button

**Purpose:** An interactive like/heart button that allows users to express appreciation for content. Displays inline with an icon and changes color on hover.

**CSS Implementation:**

```css
.like-btn {
  display: inline-flex;
  align-items: center;
  gap: var(--space-2);                      /* 8px between icon and text */
  font-size: var(--text-sm);                /* 12px */
  color: var(--color-gray-600);             /* #666666 */
  cursor: pointer;
}

.like-btn:hover {
  color: var(--color-teal-500);             /* Teal on hover */
}
```

**HTML Structure:**

```html
<!-- Like button with icon -->
<button class="like-btn">
  <span>❤️</span>
  <span>Like</span>
</button>

<!-- Like button with count -->
<div class="like-section">
  <button class="like-btn">
    <span>❤️</span>
    <span>Like</span>
  </button>
  <span class="like-count">42</span>
</div>
```

**Styling Details:**

- **Inline-Flex**: Horizontal layout with icon + text
- **Center Alignment**: Vertically centers icon with text
- **8px Gap**: Comfortable spacing between icon and label
- **12px Font**: Small, unobtrusive text size
- **Gray-600 Color**: Secondary color (lower emphasis)
- **Pointer Cursor**: Clearly indicates clickability
- **No Border/Background**: Clean, minimal appearance
- **Color-Only Hover**: Simple teal color shift on interaction

**Interactive States:**

| State | Color | Cursor | Notes |
|-------|-------|--------|-------|
| **Default** | Gray-600 (#666666) | pointer | Neutral, low-emphasis |
| **Hover** | Teal-500 (#36BCAB) | pointer | Accent color indicates interactivity |
| **Active/Liked** | — | — | Not defined in CSS (requires JS state management) |

**Transition:**

The `.like-btn` doesn't explicitly define a transition, so color changes are instant. Consider adding:

```css
.like-btn {
  transition: color var(--transition-fast);  /* 0.15s smooth color change */
}
```

**Responsive Behavior:**

Like buttons maintain consistent styling across all breakpoints. The compact 12px size works well on mobile.

**Usage Guidelines:**

- ✅ Use semantic `<button>` element for interactive like action
- ✅ Include visual icon (❤️, 👍, or SVG icon)
- ✅ Include text label ("Like", "Love", "Appreciate")
- ✅ Pair with `.like-count` for displaying like count
- ✅ Use in `.like-section` container with count display
- ❌ Don't use without icon (icon provides visual affordance)
- ❌ Don't use for navigation (use links instead)
- ❌ Don't remove cursor:pointer (critical for affordance)

**Like Section Pattern:**

Typical like section includes button + count:

```html
<div class="like-section">
  <button class="like-btn">
    <span>❤️</span>
    <span>Like</span>
  </button>
  <span class="like-count">42</span>
</div>
```

**Accessibility Notes:**

- **Semantic Button**: Uses `<button>` for proper keyboard interaction
- **Icon + Text**: Redundant cues (visual + textual) improve understanding
- **Cursor Pointer**: Visual affordance for mouse users
- **Color Contrast**: Gray-600 on white = **5.7:1** (WCAG AA for all text)
- **Hover Feedback**: Color change provides clear interaction feedback
- **Keyboard Accessible**: Native button behavior (Space/Enter to activate)

**Implementation Considerations:**

The CSS defines visual styling only. Full like functionality requires JavaScript for:

1. **State Management**: Track liked/unliked state
2. **Visual Indication**: Add `.liked` class or inline style when active
3. **Count Updates**: Increment/decrement like count
4. **Persistence**: Store like state (localStorage, database)
5. **Interaction**: Handle click events and API calls

**Suggested Active State:**

Consider adding a `.liked` state class:

```css
.like-btn.liked {
  color: var(--color-teal-500);
  font-weight: var(--font-bold);
}
```

---

#### `.share-btn` - Share Button

**Purpose:** Small, bordered buttons for sharing content on social platforms. Displays inline with icons and changes border/text color on hover.

**CSS Implementation:**

```css
.share-btn {
  display: inline-flex;
  align-items: center;
  gap: var(--space-2);                      /* 8px between icon and text */
  font-size: var(--text-xs);                /* 11px */
  color: var(--color-gray-600);             /* #666666 */
  padding: var(--space-1) var(--space-2);   /* 4px 8px */
  border: 1px solid var(--color-gray-200);  /* Light gray border */
  border-radius: var(--radius-sm);          /* 2px */
  background: var(--color-white);
  cursor: pointer;
  transition: all var(--transition-fast);   /* 0.15s smooth transition */
}

.share-btn:hover {
  border-color: var(--color-teal-500);      /* Teal border */
  color: var(--color-teal-500);             /* Teal text */
}
```

**HTML Structure:**

```html
<!-- Share buttons in share-section -->
<div class="share-section">
  <h4 class="share-title">Share this post</h4>
  <div class="share-buttons">
    <button class="share-btn">
      <span>🐦</span>
      <span>Twitter</span>
    </button>
    <button class="share-btn">
      <span>📘</span>
      <span>Facebook</span>
    </button>
    <button class="share-btn">
      <span>💼</span>
      <span>LinkedIn</span>
    </button>
  </div>
</div>
```

**Styling Details:**

- **Inline-Flex**: Horizontal layout with icon + platform name
- **Center Alignment**: Vertically centers icon with text
- **8px Gap**: Spacing between icon and text
- **11px Font**: Extra small, compact text
- **Compact Padding**: 4px vertical, 8px horizontal (minimal but clickable)
- **Gray-200 Border**: Subtle light gray outline
- **2px Radius**: Minimal corner rounding
- **White Background**: Clean appearance
- **Fast Transition**: 0.15s smooth hover effect (border + color)

**Interactive States:**

| State | Text Color | Border Color | Background | Transition |
|-------|------------|--------------|------------|------------|
| **Default** | Gray-600 | Gray-200 | White | — |
| **Hover** | Teal-500 | Teal-500 | White | 0.15s ease (all) |

**Transition Behavior:**

Uses `transition: all` with 0.15s duration, affecting:
- `color` (text color)
- `border-color`
- Any other properties that change

**Note:** `transition: all` is convenient but less performant than specifying individual properties. Consider:

```css
.share-btn {
  transition: color var(--transition-fast),
              border-color var(--transition-fast);
}
```

**Share Buttons Container:**

Share buttons are typically grouped in a `.share-buttons` flex container:

```css
.share-buttons {
  display: flex;
  gap: var(--space-4);                      /* 16px between buttons */
  align-items: center;
}
```

**Responsive Behavior:**

Share buttons maintain consistent styling across breakpoints. The compact 11px font and tight padding work well on mobile touch targets.

**Touch Target Consideration:**

At 4px vertical padding, share buttons may be smaller than the recommended 44x44px touch target. Consider increasing padding on mobile:

```css
/* Mobile Enhancement (not currently in CSS) */
@media (max-width: 480px) {
  .share-btn {
    padding: var(--space-2) var(--space-3);  /* 8px 12px - larger touch target */
  }
}
```

**Usage Guidelines:**

- ✅ Use semantic `<button>` for share actions (or `<a>` for direct share links)
- ✅ Include platform icon (emoji or SVG)
- ✅ Include platform name text ("Twitter", "Facebook", "LinkedIn")
- ✅ Group multiple share buttons in `.share-buttons` container
- ✅ Use within `.share-section` for proper spacing/organization
- ✅ Keep button text concise (platform name only)
- ❌ Don't use without icon (icon aids quick recognition)
- ❌ Don't make buttons too large (compact is intentional)
- ❌ Don't use for non-sharing actions

**Share Section Pattern:**

Complete share section structure:

```html
<div class="share-section">
  <h4 class="share-title">Share this post</h4>
  <div class="share-buttons">
    <button class="share-btn" data-platform="twitter">
      <span>🐦</span>
      <span>Twitter</span>
    </button>
    <button class="share-btn" data-platform="facebook">
      <span>📘</span>
      <span>Facebook</span>
    </button>
    <button class="share-btn" data-platform="linkedin">
      <span>💼</span>
      <span>LinkedIn</span>
    </button>
  </div>
</div>
```

**Accessibility Notes:**

- **Semantic Buttons**: Uses `<button>` for proper interaction
- **Icon + Text**: Dual visual cues improve comprehension
- **Border Visual**: Border provides shape definition (not just color)
- **Hover Feedback**: Both border and text color change
- **Cursor Pointer**: Indicates clickability
- **Keyboard Accessible**: Native button keyboard behavior
- **Color Contrast**:
  - Default text (Gray-600 on white): **5.7:1** (WCAG AA)
  - Hover text (Teal-500 on white): **3.3:1** (WCAG AA for large text only)
  - Border provides additional visual boundary

**Touch Target Considerations:**

Current padding creates compact buttons that may not meet the 44x44px minimum touch target recommendation. Options:

1. **Increase padding on mobile** (recommended)
2. **Accept smaller targets** (icons provide some targeting assistance)
3. **Add invisible clickable area** (::before/::after pseudo-element)

**Implementation Considerations:**

Share buttons require JavaScript for functionality:

1. **Share URLs**: Generate platform-specific share URLs
2. **Click Handlers**: Open share dialogs or new windows
3. **Analytics**: Track which platforms users share to
4. **Native Share API**: Consider using `navigator.share()` on supported devices

**Example Share URL Patterns:**

- **Twitter**: `https://twitter.com/intent/tweet?url={url}&text={text}`
- **Facebook**: `https://facebook.com/sharer/sharer.php?u={url}`
- **LinkedIn**: `https://linkedin.com/sharing/share-offsite/?url={url}`

---

#### Interactive Components Best Practices

**Do's:**

- ✅ Use teal accent color for all hover/focus states (consistency)
- ✅ Provide clear cursor feedback (cursor: pointer)
- ✅ Use semantic HTML (`<button>`, `<input>`, `<form>`)
- ✅ Include both visual and text cues (icons + labels)
- ✅ Ensure sufficient color contrast for accessibility
- ✅ Provide smooth transitions for state changes (0.15-0.2s)
- ✅ Use system fonts for form inputs (native feel)
- ✅ Test interactive elements with keyboard navigation
- ✅ Maintain minimum 44x44px touch targets on mobile

**Don'ts:**

- ❌ Don't remove focus indicators without alternatives
- ❌ Don't use color alone to indicate state (use borders, icons too)
- ❌ Don't make buttons/inputs too small (accessibility)
- ❌ Don't use `transition: all` excessively (performance)
- ❌ Don't override system fonts in form inputs
- ❌ Don't create interactive elements that look non-interactive
- ❌ Don't use vague button text ("Click here" vs "Subscribe")
- ❌ Don't place too many primary buttons close together

---

#### Accessibility Summary

| Component | Color Contrast | Keyboard Access | Focus Indicator | Touch Target | Notes |
|-----------|----------------|-----------------|-----------------|--------------|-------|
| **btn-primary** | 4.6:1 (AA large) | ✅ Native | Browser default | 8x12px padding | Consider larger mobile padding |
| **email-form** | 4.6:1 border | ✅ Native | Teal border | Full-width | Border-only focus (no outline) |
| **like-btn** | 5.7:1 (AA all) | ✅ Native | Browser default | No padding | Icon + text provide redundant cues |
| **share-btn** | 5.7:1 (AA all) | ✅ Native | Browser default | 4x8px padding | Small touch target—consider mobile enhancement |

**Key Accessibility Wins:**

1. ✅ All interactive elements use semantic HTML
2. ✅ Color contrast meets or exceeds WCAG AA
3. ✅ Hover states provide clear visual feedback
4. ✅ Cursor changes indicate interactivity
5. ✅ Form labels properly associated with inputs
6. ✅ Icon + text combinations provide redundant information

**Areas for Enhancement:**

1. ⚠️ Share buttons may need larger mobile touch targets
2. ⚠️ Email input removes outline (consider adding box-shadow alternative)
3. ⚠️ Like button needs defined active/liked state
4. ⚠️ Consider explicit focus styles matching teal theme

---

#### Interactive Components Quick Reference

```
BUTTONS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
.btn              Base button class (requires variant)
.btn-primary      Blue button (White on #0073B1)
                  Hover: White on #005a8c

FORMS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
.email-form       Email signup form container
  label           13px Gray-700, 8px margin-bottom
  input[email]    Full-width, 8x12px padding, Gray-500 border
                  Focus: Teal-500 border, no outline

INTERACTIVE ELEMENTS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
.like-btn         Inline-flex, 12px Gray-600, no border
                  Hover: Teal-500 color
.share-btn        Inline-flex, 11px, 4x8px padding
                  Border: Gray-200 (1px)
                  Hover: Teal-500 border + text

HOVER STATE PATTERN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
All interactive elements → Teal-500 accent on hover

TRANSITIONS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Buttons:     0.2s ease (background-color)
Share/Like:  0.15s ease (color, border-color)
```

---

### Content Components

Content components are specialized elements designed to structure and present information on the site. These components include images, widget containers, social link groups, contact sections, and signature elements. Unlike layout components (which define page structure) or interactive components (which handle user actions), content components focus on displaying information in a semantically meaningful and visually consistent way.

#### Design Rationale

Content components provide reusable patterns for common content types:

1. **Semantic Structure** - Each component uses appropriate HTML elements (article, aside, footer) for meaning
2. **Consistent Spacing** - Predictable margins using the 4px spacing scale
3. **Visual Hierarchy** - Section borders, headings, and spacing create clear content boundaries
4. **Responsive Adaptation** - Components adjust spacing/sizing across breakpoints
5. **Composition Patterns** - Components can be combined to create rich content layouts

**Philosophy:**

Content components should feel lightweight and unobtrusive, letting the actual content shine. They provide just enough structure and spacing to organize information without imposing heavy visual styling. Borders are minimal (1px, gray-200), spacing is generous but not excessive, and components work equally well in main content or sidebar contexts.

----

#### Component Overview

| Component | Type | Margin | Border | Primary Use Case |
|-----------|------|--------|--------|------------------|
| **widget** | Container | 24px bottom | none | Sidebar content blocks |
| **profile-image** | Image | — | none | Main content area profile photos |
| **flight-stats** | Image | 20px vertical | none | Infographic/data visualization images |
| **contact-section** | Section | 32px top | 1px top (gray-200) | Footer contact information |
| **social-links** | List | — | none | Vertical social media link lists |
| **share-section** | Section | 24px top | 1px top (gray-200) | Content sharing areas |
| **signature** | Text | 20px top | none | Author signatures/bylines |
| **subscriber-count** | Text | 8px top | none | Newsletter subscriber metrics |

----

#### `.widget` - Widget Container

**Purpose:** A reusable container component for sidebar content blocks like "About", "Subscribe", or "Popular Posts". Provides consistent bottom spacing to separate multiple stacked widgets.

**CSS Implementation:**

```css
.widget {
  margin-bottom: var(--space-6);               /* 24px bottom spacing */
}

.widget-title {
  font-family: var(--font-heading);            /* Oswald */
  font-size: var(--text-lg);                   /* 16px */
  font-weight: var(--font-bold);               /* 700 */
  text-transform: uppercase;
  color: var(--color-black);
  margin-bottom: var(--space-3);               /* 12px */
}

.widget p {
  font-size: var(--text-base);                 /* 13px */
  color: var(--color-gray-700);                /* #555555 */
}
```

**HTML Structure:**

```html
<!-- About Widget -->
<aside class="sidebar">
  <div class="widget">
    <h3 class="widget-title">ABOUT</h3>
    <p>
      A passionate technologist attending conferences,
      traveling, and meeting interesting people worldwide.
    </p>
  </div>

  <!-- Subscribe Widget -->
  <div class="widget">
    <h3 class="widget-title">SUBSCRIBE</h3>
    <p>Get updates delivered to your inbox.</p>
    <form class="email-form">
      <label for="email">Email Address</label>
      <input type="email" id="email" required>
      <button type="submit" class="btn btn-primary">Subscribe</button>
    </form>
  </div>

  <!-- Social Links Widget -->
  <div class="widget">
    <h3 class="widget-title">FOLLOW ME</h3>
    <div class="social-links">
      <a href="https://twitter.com/username">Twitter</a>
      <a href="https://linkedin.com/in/username">LinkedIn</a>
    </div>
  </div>
</aside>
```

**Styling Details:**

**Widget Container:**
- **24px bottom margin**: Separates stacked widgets in sidebar
- **No border/padding**: Clean, minimal container
- **Block display**: Full-width within sidebar

**Widget Title (.widget-title):**
- **Oswald font**: Matches site heading style
- **16px size**: Larger than body text but smaller than main headings
- **Bold weight**: Creates hierarchy within widget
- **UPPERCASE**: Consistent with site heading style
- **12px bottom margin**: Tight spacing to widget content

**Widget Paragraphs:**
- **13px base size**: Matches site body text
- **Gray-700 color**: Standard body text color
- **Default line-height**: 1.75 for readability

**Responsive Behavior:**

Widgets maintain consistent styling across all breakpoints. When sidebar is removed on mobile, widgets can be stacked in the main content area.

**Usage Guidelines:**

- ✅ Use in sidebar areas for grouped content
- ✅ Stack multiple widgets vertically (margin-bottom provides spacing)
- ✅ Include `.widget-title` for each widget (even if visually hidden)
- ✅ Combine with other components (email-form, social-links)
- ❌ Don't nest widgets inside widgets (flat structure only)
- ❌ Don't override the 24px margin-bottom (maintains rhythm)
- ❌ Don't use in main content area (use sections instead)
- ❌ Don't add excessive content (keep widgets concise)

**Composition Patterns:**

Widgets commonly contain:
- **Text only**: Simple about/bio content
- **Form**: Email subscription forms
- **Link lists**: Social links, recent posts
- **Images**: Small profile photos, badges

**Accessibility Notes:**

- **Semantic HTML**: Use `<aside>` for sidebar, `<div class="widget">` for each widget
- **Heading hierarchy**: Widget titles should be `<h3>` (assuming h1 is site title, h2 is section titles)
- **Landmark regions**: Sidebar should be wrapped in `<aside>` landmark
- **Navigation**: If widget contains navigation links, wrap in `<nav>` element

----

#### `.profile-image` - Profile Image

**Purpose:** Full-width image component for profile photos in the main content area. Maintains aspect ratio and responsively scales to fit container width.

**CSS Implementation:**

```css
.profile-image {
  width: 100%;                                 /* Full-width of container */
  max-width: var(--content-width);             /* 580px max */
  height: auto;                                /* Maintain aspect ratio */
  display: block;                              /* Remove inline spacing */
}
```

**HTML Structure:**

```html
<article class="content">
  <h2 class="section-title">ABOUT ME</h2>

  <p>Introduction paragraph...</p>

  <img
    src="./images/profile.jpg"
    alt="Abe Diaz"
    class="profile-image"
    loading="lazy"
  >

  <p>Biography continues after image...</p>
</article>
```

**Styling Details:**

- **100% width**: Fills content area width (typically 580px)
- **580px max-width**: Matches content area width
- **Auto height**: Preserves image aspect ratio (no distortion)
- **Block display**: Eliminates inline image spacing issues
- **No margin**: Uses natural paragraph spacing around it

**Responsive Behavior:**

| Breakpoint | Margin | Behavior |
|------------|--------|----------|
| **Desktop** (>768px) | Default | Full content width (580px) |
| **Tablet** (≤768px) | 16px vertical | Slightly reduced spacing |
| **Mobile** (≤480px) | 16px vertical | Scales to mobile content width |

```css
/* Responsive adjustments */
@media (max-width: 768px) {
  .profile-image,
  .flight-stats {
    margin: var(--space-4) 0;              /* 16px vertical */
  }
}
```

**Usage Guidelines:**

- ✅ Use for main profile/bio photos in content area
- ✅ Include descriptive alt text (person's name, context)
- ✅ Use `loading="lazy"` for performance
- ✅ Place naturally within paragraph flow
- ✅ Optimize images (WebP format, appropriate dimensions)
- ❌ Don't use for small thumbnails (no class needed)
- ❌ Don't use in sidebar (consider smaller fixed width)
- ❌ Don't apply multiple image classes simultaneously
- ❌ Don't skip alt text (critical for accessibility)

**Image Optimization:**

- **Recommended width**: 1160px (2x for retina displays)
- **Format**: WebP with JPEG fallback
- **Compression**: 80-85% quality
- **Aspect ratio**: 3:2 or 4:3 for portraits

**Accessibility Notes:**

- **Alt text required**: Describe who/what is in the photo
- **Block display**: Integrates naturally with screen reader flow
- **Lazy loading**: Improves performance without affecting accessibility
- **Sufficient size**: Full-width images are easier to see for low-vision users

----

#### `.flight-stats` - Flight Stats Image

**Purpose:** Full-width image component for data visualizations, infographics, and statistical graphics. Provides vertical spacing to separate from surrounding content.

**CSS Implementation:**

```css
.flight-stats {
  width: 100%;                                 /* Full-width of container */
  height: auto;                                /* Maintain aspect ratio */
  margin: var(--space-5) 0;                    /* 20px vertical spacing */
}
```

**HTML Structure:**

```html
<article class="content">
  <p>Travel statistics and journey details...</p>

  <img
    src="./images/flight-stats.png"
    alt="Flight Stats Infographic showing 150 flights to 42 countries"
    class="flight-stats"
    loading="lazy"
  >

  <p>Additional travel information...</p>
</article>
```

**Styling Details:**

- **100% width**: Fills content area (no max-width restriction)
- **Auto height**: Preserves infographic aspect ratio
- **20px vertical margin**: Creates breathing room above/below
- **No max-width**: Can exceed content width if needed

**Difference from `.profile-image`:**

| Property | profile-image | flight-stats |
|----------|---------------|--------------|
| **max-width** | 580px | none |
| **margin** | none (uses paragraph flow) | 20px vertical |
| **Use case** | Profile photos | Data visualizations |

**Responsive Behavior:**

| Breakpoint | Margin | Behavior |
|------------|--------|----------|
| **Desktop** (>768px) | 20px vertical | Full content width |
| **Tablet** (≤768px) | 16px vertical | Scaled to fit |
| **Mobile** (≤480px) | 16px vertical | Stacked display |

```css
@media (max-width: 768px) {
  .profile-image,
  .flight-stats {
    margin: var(--space-4) 0;              /* 16px vertical (tighter) */
  }
}
```

**Usage Guidelines:**

- ✅ Use for infographics, charts, and data visualizations
- ✅ Provide detailed alt text describing the data
- ✅ Use high-resolution images (infographics need clarity)
- ✅ Include margin for visual separation
- ✅ Consider text alternative for complex data
- ❌ Don't use for decorative images (use img without class)
- ❌ Don't use for photos (use `.profile-image` instead)
- ❌ Don't include data only as an image (accessibility)
- ❌ Don't use tiny fonts in infographic (hard to read)

**Alt Text Best Practices:**

For data visualizations, alt text should summarize key information:

```html
<!-- ❌ Poor alt text -->
<img src="stats.png" alt="Stats" class="flight-stats">

<!-- ✅ Good alt text -->
<img
  src="flight-stats.png"
  alt="Flight Stats Infographic showing 150 flights across 42 countries over 5 years, with top destinations including Japan (12 trips), UK (8 trips), and Mexico (6 trips)"
  class="flight-stats"
>
```

**Accessibility Notes:**

- **Detailed alt text**: Must describe the data, not just say "infographic"
- **Text alternative**: Consider providing data in text/table format as well
- **High contrast**: Ensure infographic text/colors are readable
- **Sufficient size**: Full-width ensures legibility on all devices

----

#### `.contact-section` - Contact Section

**Purpose:** A footer section component for contact information and social links. Features top border and generous padding to visually separate from main content.

**CSS Implementation:**

```css
.contact-section {
  margin-top: var(--space-8);                  /* 32px top margin */
  padding-top: var(--space-6);                 /* 24px top padding */
  padding-bottom: var(--space-6);              /* 24px bottom padding */
  border-top: 1px solid var(--color-gray-200); /* Top border separator */
}

.contact-section h3 {
  margin-bottom: var(--space-3);               /* 12px below heading */
}
```

**HTML Structure:**

```html
<footer class="contact-section">
  <h3>CONTACT ME:</h3>
  <div class="social-links-inline">
    <a href="https://linkedin.com/in/username" class="accent-link">LinkedIn</a>
    <a href="https://twitter.com/username" class="accent-link">Twitter</a>
    <a href="mailto:email@example.com" class="accent-link">Email</a>
  </div>
</footer>
```

**Styling Details:**

**Section Container:**
- **32px top margin**: Large gap from preceding content
- **24px top/bottom padding**: Generous internal spacing
- **1px top border**: Gray-200 border creates visual separation
- **No max-width**: Spans full container width

**Heading (h3):**
- **12px bottom margin**: Tight spacing to social links
- **Inherits h3 styles**: Oswald, 16px, bold, uppercase

**Responsive Behavior:**

| Breakpoint | Top Margin | Top/Bottom Padding | Changes |
|------------|------------|-------------------|---------|
| **Desktop** (>768px) | 32px | 24px / 24px | Standard spacing |
| **Tablet** (≤768px) | 24px | 20px / 32px | Tighter top, more bottom |
| **Mobile** (≤480px) | 24px | 20px / 32px | Same as tablet |

```css
@media (max-width: 768px) {
  .contact-section {
    margin-top: var(--space-6);                /* 24px (tighter) */
    padding-top: var(--space-5);               /* 20px (tighter) */
    padding-bottom: var(--space-8);            /* 32px (more breathing room) */
  }
}
```

**Usage Guidelines:**

- ✅ Use as page footer for contact information
- ✅ Combine with `.social-links-inline` for horizontal links
- ✅ Use semantic `<footer>` element
- ✅ Keep contact methods limited (3-5 links maximum)
- ❌ Don't use multiple contact-section elements per page
- ❌ Don't remove the top border (provides visual separation)
- ❌ Don't place above main content (footer positioning)
- ❌ Don't include lengthy content (keep concise)

**Composition Patterns:**

The contact section commonly contains:
- **Heading**: "CONTACT ME:", "GET IN TOUCH:", "CONNECT:"
- **Social links inline**: Horizontal list of platform links
- **Optional**: Email address, phone, location
- **Optional**: Newsletter signup (`.email-form`)

**Accessibility Notes:**

- **Semantic footer**: Use `<footer>` element (landmark role)
- **Heading hierarchy**: Ensure h3 follows site heading structure (h1 → h2 → h3)
- **Link text**: Use platform names, not "click here"
- **Sufficient contrast**: Border (gray-200) and link colors meet WCAG standards
- **Touch targets**: Links must be at least 44x44px on mobile

----

#### `.social-links` - Social Links (Vertical)

**Purpose:** A vertical stack of social media links, typically used in sidebar widgets. Creates consistent spacing between links in a column layout.

**CSS Implementation:**

```css
.social-links {
  display: flex;
  flex-direction: column;                      /* Vertical stack */
  gap: var(--space-2);                         /* 8px between links */
}

.social-links a {
  color: var(--color-gray-700);                /* #555555 */
}
```

**HTML Structure:**

```html
<!-- In sidebar widget -->
<div class="widget">
  <h3 class="widget-title">FOLLOW ME</h3>
  <div class="social-links">
    <a href="https://twitter.com/username">Twitter</a>
    <a href="https://linkedin.com/in/username">LinkedIn</a>
    <a href="https://instagram.com/username">Instagram</a>
    <a href="https://github.com/username">GitHub</a>
  </div>
</div>
```

**Styling Details:**

- **Flexbox column**: Stacks links vertically
- **8px gap**: Consistent spacing using modern gap property
- **Gray-700 links**: Matches body text color (#555555)
- **No bullets/list styles**: Clean, minimal appearance

**Link Styling:**

Links inside `.social-links` inherit default link styles:
- **Gray-700 color**: `#555555` (default state)
- **Teal-500 hover**: Accent color on hover (from global `a:hover`)
- **Underline on hover**: Standard link behavior
- **13px font size**: Matches body text (`--text-base`)

**Responsive Behavior:**

No responsive adjustments needed. The vertical stack works well on all screen sizes.

**Usage Guidelines:**

- ✅ Use for vertical sidebar link lists
- ✅ Limit to 4-6 links (avoid overwhelming)
- ✅ Use consistent platform names ("Twitter" not "@username")
- ✅ Order by importance/usage (most used first)
- ❌ Don't use for horizontal layouts (use `.social-links-inline`)
- ❌ Don't add icons without text (text is primary)
- ❌ Don't include too many platforms (focus on active ones)
- ❌ Don't use generic text ("Social Media" vs platform names)

**Comparison: Vertical vs Inline Social Links**

| Property | social-links | social-links-inline |
|----------|--------------|---------------------|
| **Direction** | column (vertical) | row (horizontal) |
| **Gap** | 8px | 20px (desktop), 24px (mobile) |
| **Font size** | 13px (base) | 13px → 14px responsive |
| **Use case** | Sidebar widgets | Footer contact section |

**Accessibility Notes:**

- **Descriptive links**: Platform names are clear and self-describing
- **Sufficient spacing**: 8px gap creates distinct click targets
- **Color contrast**: Gray-700 on white = 5.7:1 (WCAG AA)
- **Hover feedback**: Teal color change indicates interactivity

----

#### `.share-section` - Share Section

**Purpose:** A bordered section for content sharing options (share buttons, social sharing tools). Provides visual separation with top border and spacing.

**CSS Implementation:**

```css
.share-section {
  margin-top: var(--space-6);                  /* 24px top margin */
  padding-top: var(--space-5);                 /* 20px top padding */
  border-top: 1px solid var(--color-gray-200); /* Top border separator */
}
```

**HTML Structure:**

```html
<article class="content">
  <h2 class="section-title">ARTICLE TITLE</h2>
  <p>Article content goes here...</p>

  <!-- Share Section at end of article -->
  <div class="share-section">
    <h3>SHARE THIS:</h3>
    <div>
      <button class="share-btn">
        <svg><!-- Twitter icon --></svg>
        Twitter
      </button>
      <button class="share-btn">
        <svg><!-- Facebook icon --></svg>
        Facebook
      </button>
      <button class="share-btn">
        <svg><!-- LinkedIn icon --></svg>
        LinkedIn
      </button>
    </div>
  </div>
</article>
```

**Styling Details:**

- **24px top margin**: Separates from article content
- **20px top padding**: Creates space inside border
- **1px top border**: Gray-200 border (#EEEEEE) for subtle separation
- **No bottom padding/margin**: Relies on natural content spacing

**Responsive Behavior:**

No responsive adjustments defined. The component maintains consistent spacing across all breakpoints.

**Usage Guidelines:**

- ✅ Use at end of articles/posts for sharing options
- ✅ Combine with `.share-btn` components
- ✅ Include heading ("Share This:", "Share:", "Spread the word:")
- ✅ Limit share platforms (3-5 most relevant)
- ❌ Don't place at top of content (end of article is standard)
- ❌ Don't use without border (visual separation is key)
- ❌ Don't include too many platforms (creates decision fatigue)
- ❌ Don't make sharing the primary CTA (content is primary)

**Composition Patterns:**

Share sections commonly contain:
- **Heading**: Optional h3 or strong text
- **Share buttons**: `.share-btn` elements for each platform
- **Optional**: Share count displays
- **Optional**: Direct social platform embed widgets

**Common Use Cases:**

1. **Blog post sharing**: Twitter, LinkedIn, Facebook
2. **Portfolio sharing**: LinkedIn, Twitter, Email
3. **Video sharing**: YouTube, Twitter, Facebook
4. **Photo sharing**: Instagram, Twitter, Pinterest

**Accessibility Notes:**

- **Semantic grouping**: Wrap in `<div>` or `<aside>` (not structural)
- **Clear heading**: "Share This" clearly indicates purpose
- **Button labels**: Share buttons must include platform names (not icon-only)
- **Border contrast**: Gray-200 border may be subtle (sufficient for visual users)

----

#### `.signature` - Signature

**Purpose:** A text component for author signatures or bylines. Uses normal font style (not italic) with top spacing to separate from preceding content.

**CSS Implementation:**

```css
.signature {
  font-style: normal;                          /* Override italic default */
  margin-top: var(--space-5);                  /* 20px top spacing */
}
```

**HTML Structure:**

```html
<article class="content">
  <p>Article or letter content...</p>

  <p class="signature">
    — Abe Diaz<br>
    Seattle, WA
  </p>
</article>

<!-- Alternative with cite element -->
<blockquote>
  <p>Quote content...</p>
  <cite class="signature">Abe Diaz</cite>
</blockquote>
```

**Styling Details:**

- **Normal font style**: Explicitly sets `font-style: normal` (overrides italic)
- **20px top margin**: Creates separation from article content
- **Inherits body styles**: Uses standard body font, size, color, line-height

**Why `font-style: normal`?**

The `.signature` class is often applied to elements that default to italic:
- `<cite>` elements (default: italic)
- `<em>` or `<i>` elements
- Author attribution blocks

Setting `font-style: normal` ensures signatures appear upright, not italicized.

**Typography:**

- **Font**: Helvetica Neue (body font)
- **Size**: 13px (--text-base)
- **Color**: Gray-700 (#555555)
- **Weight**: Normal (400)
- **Line height**: 1.75

**Responsive Behavior:**

No responsive adjustments needed. The signature maintains consistent styling across all breakpoints.

**Usage Guidelines:**

- ✅ Use for author signatures at end of articles/letters
- ✅ Use for quote attributions with `<cite>` element
- ✅ Include em dash (—) before name for visual style
- ✅ Keep concise (name, location, role)
- ❌ Don't use for headers/titles (wrong semantic meaning)
- ❌ Don't apply to interactive elements (buttons, links)
- ❌ Don't override the 20px margin (maintains rhythm)
- ❌ Don't include lengthy biographical information

**Content Patterns:**

```html
<!-- Simple signature -->
<p class="signature">— Abe Diaz</p>

<!-- With location -->
<p class="signature">
  — Abe Diaz<br>
  Seattle, WA
</p>

<!-- With role/title -->
<p class="signature">
  — Abe Diaz<br>
  Sr. Technical Program Manager, Amazon
</p>

<!-- As cite element -->
<cite class="signature">Abe Diaz, 2026</cite>
```

**Accessibility Notes:**

- **Semantic HTML**: Use `<cite>` for quote attributions, `<p>` for letter signatures
- **Normal font**: Ensures readability (italic can reduce legibility)
- **Sufficient spacing**: 20px margin clearly separates signature from content
- **Standard contrast**: Inherits body text color (5.7:1 ratio)

----

#### `.subscriber-count` - Subscriber Count

**Purpose:** A small, muted text component for displaying newsletter subscriber metrics. Provides context about newsletter popularity/reach.

**CSS Implementation:**

```css
.subscriber-count {
  font-size: var(--text-sm);                   /* 12px */
  color: var(--color-gray-600);                /* #767676 - Lighter gray */
  margin-top: var(--space-2);                  /* 8px top spacing */
}
```

**HTML Structure:**

```html
<!-- In subscription widget -->
<div class="widget">
  <h3 class="widget-title">SUBSCRIBE</h3>
  <p>Get weekly updates delivered to your inbox.</p>

  <form class="email-form">
    <label for="email">Email Address</label>
    <input type="email" id="email" required>
    <button type="submit" class="btn btn-primary">Subscribe</button>
  </form>

  <p class="subscriber-count">Join 2,847 subscribers</p>
</div>
```

**Styling Details:**

- **12px font size**: Smaller than body text (13px), indicating secondary information
- **Gray-600 color**: Lighter gray (#767676) for muted, subtle appearance
- **8px top margin**: Tight spacing from form/preceding content
- **Inherits**: Body font family (Helvetica Neue), normal weight (400)

**Typography:**

- **Font**: Helvetica Neue (body font)
- **Size**: 12px (--text-sm)
- **Color**: Gray-600 (#767676)
- **Weight**: Normal (400)
- **Line height**: Default (1.75)

**Responsive Behavior:**

No responsive adjustments needed. The subtle metric display works well at all screen sizes.

**Usage Guidelines:**

- ✅ Use for newsletter subscriber counts
- ✅ Use for social follower counts
- ✅ Keep text concise ("Join 2,847 subscribers")
- ✅ Place below subscription form or social links
- ✅ Update count periodically (avoid stale numbers)
- ❌ Don't make subscriber count prominent (it's supplementary)
- ❌ Don't use for primary metrics (use larger text)
- ❌ Don't show low counts if discouraging (wait until impressive)
- ❌ Don't use deceptive numbers (be honest about subscribers)

**Content Patterns:**

```html
<!-- Subscriber count -->
<p class="subscriber-count">Join 2,847 subscribers</p>

<!-- Follower count -->
<p class="subscriber-count">5,234 followers</p>

<!-- Download count -->
<p class="subscriber-count">Downloaded 1,203 times</p>

<!-- View count -->
<p class="subscriber-count">Viewed 12,456 times</p>
```

**Social Proof Psychology:**

Subscriber counts serve as social proof, indicating:
- **Popularity**: High numbers suggest valuable content
- **Community**: Others are interested, creating FOMO (fear of missing out)
- **Credibility**: Established audience implies trustworthiness
- **Momentum**: Growing numbers indicate active, current content

**Best Practices:**

1. **Show when impressive**: Don't display until count is meaningful (>500)
2. **Round numbers**: "Join 2,800+ subscribers" vs "Join 2,847 subscribers"
3. **Keep updated**: Stale numbers look abandoned
4. **Be honest**: Fake numbers damage credibility
5. **Make it timely**: "Join 100+ subscribers this week" adds urgency

**Accessibility Notes:**

- **Sufficient contrast**: Gray-600 on white = 4.6:1 (WCAG AA)
- **Not critical information**: Supplementary content, not required to understand CTA
- **Screen reader friendly**: Plain text, no special formatting needed
- **Small size acceptable**: Not primary content, so 12px is appropriate

----

#### Content Components Best Practices

**Do's:**

- ✅ Use semantic HTML elements (aside, article, footer, cite)
- ✅ Maintain consistent spacing using design tokens
- ✅ Provide descriptive alt text for all images
- ✅ Combine components for rich layouts (widget + social-links)
- ✅ Keep content concise within components
- ✅ Use top borders for visual section separation
- ✅ Optimize images for performance (WebP, lazy loading)
- ✅ Follow heading hierarchy (h1 → h2 → h3)

**Don'ts:**

- ❌ Don't nest content components excessively (flat structure preferred)
- ❌ Don't skip alt text on images (accessibility requirement)
- ❌ Don't override component spacing without reason (breaks rhythm)
- ❌ Don't use decorative borders/styling (minimal design philosophy)
- ❌ Don't include outdated information (subscriber counts, stats)
- ❌ Don't use generic link text ("click here", "learn more")
- ❌ Don't create overly complex widget layouts
- ❌ Don't place contact sections above main content

----

#### Composition Examples

**Sidebar with Multiple Widgets:**

```html
<aside class="sidebar">
  <!-- About Widget -->
  <div class="widget">
    <h3 class="widget-title">ABOUT</h3>
    <img src="./images/avatar.jpg" alt="Abe Diaz" style="width: 100%; border-radius: 50%;">
    <p>Passionate technologist and traveler.</p>
  </div>

  <!-- Subscribe Widget -->
  <div class="widget">
    <h3 class="widget-title">SUBSCRIBE</h3>
    <p>Get updates via email.</p>
    <form class="email-form">
      <label for="email">Email Address</label>
      <input type="email" id="email" required>
      <button type="submit" class="btn btn-primary">Subscribe</button>
    </form>
    <p class="subscriber-count">Join 2,800+ subscribers</p>
  </div>

  <!-- Social Links Widget -->
  <div class="widget">
    <h3 class="widget-title">FOLLOW ME</h3>
    <div class="social-links">
      <a href="https://twitter.com/username">Twitter</a>
      <a href="https://linkedin.com/in/username">LinkedIn</a>
      <a href="https://instagram.com/username">Instagram</a>
    </div>
  </div>
</aside>
```

**Article with Images and Share Section:**

```html
<article class="content">
  <h2 class="section-title">MY TRAVEL STORY</h2>

  <p>Introduction paragraph about traveling...</p>

  <img
    src="./images/profile.jpg"
    alt="Abe Diaz at Mount Fuji, Japan"
    class="profile-image"
    loading="lazy"
  >

  <p>More content about the journey...</p>

  <img
    src="./images/flight-stats.png"
    alt="Flight statistics: 150 flights to 42 countries"
    class="flight-stats"
    loading="lazy"
  >

  <p>Final thoughts...</p>

  <p class="signature">
    — Abe Diaz<br>
    Seattle, WA
  </p>

  <!-- Share Section -->
  <div class="share-section">
    <h3>SHARE THIS STORY:</h3>
    <button class="share-btn">Twitter</button>
    <button class="share-btn">LinkedIn</button>
    <button class="share-btn">Facebook</button>
  </div>
</article>
```

**Footer Contact Section:**

```html
<footer class="contact-section">
  <h3>CONTACT ME:</h3>
  <div class="social-links-inline">
    <a href="https://linkedin.com/in/abediaz" class="accent-link">LinkedIn</a>
    <a href="https://twitter.com/abe238" class="accent-link">Twitter</a>
    <a href="mailto:abe@example.com" class="accent-link">Email</a>
  </div>
</footer>
```

----

#### Accessibility Summary

| Component | Semantic HTML | Alt Text | Color Contrast | Spacing | Notes |
|-----------|---------------|----------|----------------|---------|-------|
| **widget** | `<aside>`, `<div>` | N/A | Heading: 21:1, Body: 5.7:1 | 24px bottom | Use h3 for widget-title |
| **profile-image** | `<img>` | ✅ Required | N/A | Natural flow | Descriptive alt text critical |
| **flight-stats** | `<img>` | ✅ Required | N/A | 20px vertical | Describe data in alt text |
| **contact-section** | `<footer>` | N/A | Border: 21:1 | 32px top, 24px padding | Footer landmark role |
| **social-links** | `<div>`, `<nav>` | N/A | Links: 5.7:1 | 8px gap | Platform names required |
| **share-section** | `<div>` | N/A | Border: 21:1 | 24px top, 20px padding | Use with share buttons |
| **signature** | `<p>`, `<cite>` | N/A | 5.7:1 | 20px top | Semantic cite element |
| **subscriber-count** | `<p>` | N/A | 4.6:1 (AA) | 8px top | Supplementary info |

**Key Accessibility Wins:**

1. ✅ All components use appropriate semantic HTML
2. ✅ Image components require alt text (enforced by HTML spec)
3. ✅ Color contrast meets or exceeds WCAG AA (4.5:1 minimum)
4. ✅ Consistent spacing using 4px-based scale
5. ✅ Clear heading hierarchy (h1 → h2 → h3)
6. ✅ Landmark regions (footer, aside) for screen reader navigation

**Areas for Enhancement:**

1. ⚠️ Consider adding aria-label to widget sections
2. ⚠️ Ensure share buttons have proper aria-labels
3. ⚠️ Consider adding live region for subscriber count updates
4. ⚠️ Test keyboard navigation through social links

----

#### Content Components Quick Reference

```
CONTAINERS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
.widget           Sidebar content block
                  Margin-bottom: 24px
                  .widget-title → Oswald 16px UPPERCASE
                  .widget p → 13px Gray-700

IMAGES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
.profile-image    Full-width profile photo
                  Max-width: 580px, height: auto
.flight-stats     Full-width infographic/data viz
                  Margin: 20px vertical, height: auto

SECTIONS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
.contact-section  Footer contact area
                  Border-top: 1px Gray-200
                  Margin-top: 32px, Padding: 24px vertical
.share-section    Content sharing area
                  Border-top: 1px Gray-200
                  Margin-top: 24px, Padding-top: 20px

LINK GROUPS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
.social-links     Vertical social link stack
                  Flex-direction: column, Gap: 8px
                  Links: Gray-700 → Teal-500 hover
.social-links-inline  Horizontal social link row
                  Gap: 20px (desktop), 24px (mobile)
                  Font-size: 13px → 14px responsive

TEXT ELEMENTS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
.signature        Author signature/byline
                  Font-style: normal, Margin-top: 20px
.subscriber-count Newsletter metrics
                  Font-size: 12px, Color: Gray-600
                  Margin-top: 8px

RESPONSIVE CHANGES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
@768px:
  profile-image, flight-stats → 16px vertical margin
  contact-section → margin-top 24px, padding 20px/32px
  social-links-inline → gap 24px, font-size 14px
```

---

## Responsive Design

### Breakpoints

The design system uses a **desktop-first responsive strategy** with three strategic breakpoints that adapt the design for progressively smaller screens. Each breakpoint introduces specific overrides to maintain readability, usability, and visual hierarchy. See also [Layout Components](#layout-components) and [Typography](#typography) for component-specific responsive behavior.

#### Design Rationale

The breakpoint system is designed around **real-world device categories** rather than arbitrary pixel values:

1. **768px (Tablet)** - iPads and tablet devices in portrait mode
2. **480px (Mobile)** - Standard smartphones in portrait orientation
3. **360px (Small Phones)** - Compact Android devices and older iPhones

This **desktop-first approach** (`max-width` media queries) means:
- Base styles are optimized for desktop/larger screens
- Each breakpoint progressively simplifies and condenses the layout
- Override only what's necessary—most styles cascade from desktop defaults

#### Breakpoint Overview

| Breakpoint | Media Query | Target Devices | Strategy | Changes |
|------------|-------------|----------------|----------|---------|
| **Desktop** | Default (>768px) | Laptops, desktops, large tablets | Base styles | All default design tokens |
| **Tablet** | `@media (max-width: 768px)` | iPads, medium tablets | Moderate scaling | Reduced h1 size, header padding, full-width content |
| **Mobile** | `@media (max-width: 480px)` | Smartphones | Aggressive adaptation | Smaller typography, flexible navigation, compact spacing |
| **Small Mobile** | `@media (max-width: 360px)` | Compact phones | Minimal refinement | Further h1 reduction, tighter padding |

---

#### Desktop (Default, >768px)

The desktop layout represents the **canonical design** with full spacing, large typography, and two-column layout.

**No media queries required** - these are the default CSS variable values:

```css
:root {
  --text-4xl: 80px;
  --text-base: 13px;
  --space-header: 70px;
}

body {
  line-height: 1.75;
}

.site-container {
  max-width: var(--container-max); /* 860px */
  padding: 0 var(--space-6); /* 24px */
}

.content {
  max-width: var(--content-width); /* 580px */
}
```

**Characteristics:**
- Two-column layout (content + sidebar)
- Large h1 (80px) with dramatic visual impact
- Generous spacing throughout (24px container padding, 70px header padding)
- Optimal line-height (1.75) for comfortable reading

---

#### Tablet (≤768px)

The first breakpoint begins adapting the design for **medium-sized screens** like iPads and tablets.

```css
@media (max-width: 768px) {
  :root {
    --text-4xl: 48px;       /* h1 reduced from 80px → 48px */
    --space-header: 50px;   /* header padding reduced from 70px → 50px */
  }

  .site-container {
    padding: 0 var(--space-4); /* 16px horizontal padding */
  }

  .content {
    max-width: 100%;        /* content area takes full width */
  }
}
```

**Key Changes:**

| Element | Desktop Value | Tablet Value | Change | Rationale |
|---------|---------------|--------------|--------|-----------|
| h1 size (`--text-4xl`) | 80px | 48px | -40% | Prevents overflow, maintains hierarchy |
| Header padding (`--space-header`) | 70px | 50px | -29% | Conserves vertical space |
| Container padding | 24px | 16px | -33% | More content width on narrower screens |
| Content max-width | 580px | 100% | Full width | Eliminates sidebar, uses all available space |

**Visual Impact:**
- h1 is still large (48px) but won't overwhelm tablet screens
- Content area expands to full width (sidebar may collapse or stack below)
- Slightly tighter padding creates more breathing room for content
- Header reduces vertical space consumption

---

#### Mobile (≤480px)

The mobile breakpoint introduces **significant adaptations** for smartphone screens, prioritizing readability and touch-friendly interactions.

```css
@media (max-width: 480px) {
  /* CSS Variable Overrides */
  :root {
    --text-4xl: 32px;       /* h1 dramatically reduced: 48px → 32px */
    --text-base: 14px;      /* body text increased: 13px → 14px */
    --space-header: 32px;   /* header padding further reduced: 50px → 32px */
  }

  /* Base Element Adjustments */
  body {
    line-height: 1.6;       /* tighter line-height: 1.75 → 1.6 */
  }

  .site-container {
    padding: 0 var(--space-4); /* maintains 16px padding */
  }

  /* Typography Refinements */
  h1 {
    letter-spacing: -1px;   /* tighten spacing to compensate for size reduction */
  }

  h2.tagline {
    font-size: var(--text-base); /* 14px (uses updated --text-base) */
  }

  h2.section-title {
    font-size: var(--text-base);      /* 14px */
    margin-bottom: var(--space-4);    /* 16px */
  }

  h3 {
    font-size: var(--text-md); /* 14px */
  }

  /* Navigation Adaptations */
  .site-nav {
    margin-top: var(--space-4); /* 16px */
  }

  .site-nav ul {
    flex-wrap: wrap;            /* navigation items wrap on small screens */
    gap: var(--space-4);        /* 16px gap between nav items */
  }

  /* Content Components */
  .profile-image,
  .flight-stats {
    margin: var(--space-4) 0;   /* 16px vertical margin (reduced from 20px) */
  }

  p {
    margin-bottom: var(--space-4); /* 16px paragraph spacing */
  }

  /* Footer Section */
  .contact-section {
    margin-top: var(--space-6);     /* 24px */
    padding-top: var(--space-5);    /* 20px */
    padding-bottom: var(--space-8); /* 32px */
  }

  /* Social Links */
  .social-links-inline {
    gap: var(--space-6); /* 24px gap between social links */
  }

  .social-links-inline a {
    font-size: var(--text-md);      /* 14px */
    padding: var(--space-2) 0;      /* 8px vertical padding */
  }
}
```

**Key Changes:**

| Element/Property | Desktop | Mobile | Change | Rationale |
|------------------|---------|--------|--------|-----------|
| h1 size | 80px | 32px | -60% | Prevents overflow on small screens |
| Body text size | 13px | 14px | +8% | Improves readability on mobile |
| Body line-height | 1.75 | 1.6 | -9% | Conserves vertical space |
| Header padding | 70px | 32px | -54% | Significant space savings |
| h1 letter-spacing | 0 | -1px | Tighter | Compensates for dramatic size reduction |
| Navigation layout | Single row | Wrapping | Flexible | Touch-friendly, prevents overflow |
| Image margins | 20px | 16px | -20% | Tighter spacing for mobile |
| Heading sizes | Various | Smaller | Unified | All headings use base or md sizes |

**Mobile Strategy:**

1. **Typography Scaling**: Dramatic h1 reduction (80px → 32px) with compensatory letter-spacing
2. **Body Text Enhancement**: Increase base font size (13px → 14px) for better mobile readability
3. **Spacing Reduction**: Tighter vertical rhythms conserve screen real estate
4. **Navigation Flexibility**: Wrapping navigation ensures touch targets remain accessible
5. **Line-Height Optimization**: Slightly tighter (1.6) balances readability with space efficiency

---

#### Small Mobile (≤360px)

The final breakpoint provides **minimal refinements** for compact Android phones and older iPhones with very small screens.

```css
@media (max-width: 360px) {
  :root {
    --text-4xl: 28px;       /* h1 further reduced: 32px → 28px */
  }

  .site-container {
    padding: 0 var(--space-3); /* 12px horizontal padding (reduced from 16px) */
  }
}
```

**Key Changes:**

| Element | Mobile (480px) | Small Mobile (360px) | Change | Rationale |
|---------|----------------|----------------------|--------|-----------|
| h1 size | 32px | 28px | -12.5% | Final reduction for tiny screens |
| Container padding | 16px | 12px | -25% | Maximize content width on narrowest devices |

**Small Mobile Philosophy:**
- **Minimal intervention**: Only adjust what's absolutely necessary
- **h1 refinement**: Ensures header fits comfortably on 320-360px screens
- **Padding reduction**: Every pixel counts—reduce horizontal padding to maximize content area
- **Everything else cascades**: All mobile (480px) styles still apply

---

#### Desktop-First vs Mobile-First

This design system uses a **desktop-first approach** with `max-width` media queries.

**Why Desktop-First?**

✅ **Pros:**
- Base styles represent the "ideal" design without constraints
- Simpler mental model: start complex, progressively simplify
- Easier to remove/condense than to add complexity
- Matches the design process: design for desktop, then adapt for mobile

❌ **Cons:**
- Not the modern "mobile-first" best practice for progressive enhancement
- Larger CSS file size for mobile users (though negligible for this small system)

**Mobile-First Alternative:**

A mobile-first approach would use `min-width` queries and start with mobile as the base:

```css
/* Base styles = Mobile (not used in this system) */
:root { --text-4xl: 28px; }

/* Progressively enhance for larger screens */
@media (min-width: 361px) { :root { --text-4xl: 32px; } }
@media (min-width: 481px) { :root { --text-4xl: 48px; } }
@media (min-width: 769px) { :root { --text-4xl: 80px; } }
```

**Current System Trade-offs:**
- Desktop-first aligns with this site's **desktop-centric audience** (technologist portfolio)
- Simplifies development: easier to override than build up
- Still fully responsive and mobile-friendly—just different implementation strategy

---

#### Responsive Design Patterns

**Common Adaptation Patterns:**

1. **Typography Scaling**
   - Reduce large typography dramatically (h1: 80px → 48px → 32px → 28px)
   - Increase small typography slightly (body: 13px → 14px on mobile)
   - Adjust line-height to balance readability with space constraints

2. **Spacing Condensation**
   - Header padding: 70px → 50px → 32px
   - Container padding: 24px → 16px → 12px
   - Component margins: 20px → 16px on mobile

3. **Layout Simplification**
   - Two-column → Single column (content max-width: 580px → 100%)
   - Fixed widths → Fluid/responsive widths
   - Flexbox wrapping for navigation and inline elements

4. **Touch Target Optimization**
   - Navigation gap increases on mobile (20px → 16px, allows wrapping)
   - Social link padding increases (8px vertical padding on mobile)
   - Buttons maintain minimum 44x44px touch target size

---

#### Best Practices

**✅ Do:**

- ✅ Test on real devices at each breakpoint (especially 360px for budget Android phones)
- ✅ Use CSS variables for values that change across breakpoints (`--text-4xl`, `--space-header`)
- ✅ Override only what's necessary—let desktop styles cascade when possible
- ✅ Consider touch targets on mobile (minimum 44x44px recommended)
- ✅ Test navigation wrapping at 480px with varying content lengths
- ✅ Verify h1 doesn't overflow at each breakpoint, especially with longer names
- ✅ Use browser DevTools responsive mode to test all three breakpoints

**❌ Don't:**

- ❌ Don't add breakpoints for specific devices (iPad Pro, iPhone X, etc.)—the three breakpoints cover all cases
- ❌ Don't override CSS variables unnecessarily—only change what needs to change
- ❌ Don't create new spacing values in media queries—use existing CSS variables
- ❌ Don't forget to test wrapping behavior for navigation and social links
- ❌ Don't reduce font sizes below 14px on mobile (accessibility concern)
- ❌ Don't create device-specific hacks—stick to the three established breakpoints

---

#### Accessibility Considerations

**Responsive Accessibility:**

1. **Font Size Minimums**
   - Mobile body text increases to 14px (from 13px) for better readability
   - Never goes below 11px (form inputs) on any device
   - Respects user font size preferences (uses px but scalable with browser zoom)

2. **Touch Targets**
   - Navigation links have adequate spacing (16px gap on mobile, allows wrapping)
   - Social links include 8px vertical padding on mobile
   - Buttons maintain minimum touch target size across breakpoints

3. **Spacing & Breathing Room**
   - Line-height reduces minimally (1.75 → 1.6) to preserve readability
   - Container padding ensures content never touches screen edges (12px minimum)
   - Header padding (32px minimum on mobile) prevents cramped appearance

4. **Reading Order & Flow**
   - Single-column layout on mobile maintains logical reading order
   - Navigation wraps naturally without disrupting tab order
   - Content-first approach ensures primary content is accessible

---

#### Breakpoint Quick Reference

**Responsive CSS Variables:**

| Variable | Desktop (>768px) | Tablet (≤768px) | Mobile (≤480px) | Small Mobile (≤360px) |
|----------|------------------|-----------------|-----------------|------------------------|
| `--text-4xl` | 80px | 48px | 32px | 28px |
| `--text-base` | 13px | 13px | 14px | 14px |
| `--space-header` | 70px | 50px | 32px | 32px |

**Responsive Layout Changes:**

| Element | Desktop | Tablet | Mobile | Small Mobile |
|---------|---------|--------|--------|--------------|
| `.site-container` padding | 24px | 16px | 16px | 12px |
| `.content` max-width | 580px | 100% | 100% | 100% |
| `body` line-height | 1.75 | 1.75 | 1.6 | 1.6 |
| `h1` letter-spacing | 0 | 0 | -1px | -1px |
| `.site-nav ul` | No wrap | No wrap | Wraps | Wraps |

**Component-Specific Adaptations (Mobile only, ≤480px):**

- `h2.tagline`, `h2.section-title`, `h3` → All use `--text-base` or `--text-md`
- `.site-nav` → `margin-top: 16px`, `gap: 16px`, `flex-wrap: wrap`
- `.profile-image`, `.flight-stats` → `margin: 16px 0`
- `p` → `margin-bottom: 16px`
- `.contact-section` → Adjusted padding (24px / 20px / 32px)
- `.social-links-inline` → `gap: 24px`, `font-size: 14px`, `padding: 8px 0`

---

#### Testing Checklist

Before deploying responsive changes, verify:

- [ ] **768px**: h1 (48px) fits comfortably, content expands to full width
- [ ] **480px**: Navigation wraps gracefully, h1 (32px) doesn't overflow, body text is readable at 14px
- [ ] **360px**: h1 (28px) fits within narrow width, 12px container padding provides adequate margins
- [ ] All breakpoints: Touch targets are at least 44x44px, text contrast meets WCAG AA standards
- [ ] Test on actual devices: iPad (768px), iPhone (480px), budget Android phone (360px)
- [ ] Verify content never touches screen edges at any breakpoint
- [ ] Ensure navigation remains usable when items wrap
- [ ] Check that images scale proportionally and don't overflow

---

### Mobile Adaptations

Mobile adaptations are documented throughout this design system. For comprehensive mobile behavior, refer to:

- **[Breakpoints](#breakpoints)** - Complete breakpoint system with device targets (768px, 480px, 360px)
- **[Responsive Typography](#responsive-typography)** - Font size adaptations across breakpoints
- **[Responsive Layout Behavior](#responsive-layout-behavior-summary)** - How layout components adapt on mobile
- **[Interactive Components](#interactive-components)** - Touch-friendly button and form sizing
- **[Usage Examples](#usage-examples)** - Mobile-first code examples and best practices

**Key Mobile Adaptations:**

1. **Typography Scaling** - h1 reduces from 80px → 32px on mobile for better fit
2. **Spacing Condensation** - Header padding reduces from 70px → 32px on mobile
3. **Layout Simplification** - Two-column desktop layout becomes single-column on tablet (≤768px)
4. **Touch Optimization** - Buttons and links maintain minimum 44px touch targets
5. **Navigation Wrapping** - Horizontal navigation wraps to multiple rows on mobile with flexible gaps

---

## CSS Architecture

### Reset & Base Styles

The design system uses a minimal, modern CSS reset approach that establishes a clean foundation for all components. Rather than a heavy-handed reset that removes all browser defaults, this approach targets specific pain points for predictable, consistent styling across browsers.

#### Design Rationale

Modern CSS resets have evolved from the aggressive "burn it all down" approach (like CSS Reset by Eric Meyer) to more thoughtful, surgical normalization. This design system follows the **modern box-model reset** philosophy:

1. **Universal Box-Sizing** - Apply `border-box` to all elements for intuitive sizing
2. **Zero Margins & Padding** - Remove browser defaults to prevent layout surprises
3. **Preserve Semantic Defaults** - Let browsers handle accessibility features (focus outlines, form controls)

This approach provides:
- ✅ **Predictability** - Elements behave consistently across browsers
- ✅ **Control** - Explicit spacing decisions, no hidden browser defaults
- ✅ **Simplicity** - Minimal reset code, easier to understand and maintain
- ✅ **Accessibility** - Preserves important browser features like focus indicators

---

#### Universal Reset

All elements, including pseudo-elements (`::before`, `::after`), receive the same baseline reset:

```css
*, *::before, *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}
```

**Property Breakdown:**

| Property | Value | Rationale | Impact |
|----------|-------|-----------|--------|
| `box-sizing` | `border-box` | Width/height includes padding and borders (not just content) | Makes sizing calculations intuitive and predictable |
| `margin` | `0` | Removes all browser default margins | Prevents unexpected spacing between elements |
| `padding` | `0` | Removes all browser default padding | Ensures consistent internal spacing |

**Why Border-Box?**

The default CSS box model (`content-box`) is counterintuitive:
```
/* content-box (browser default) */
width: 300px + padding: 20px + border: 1px = 342px actual width

/* border-box (our approach) */
width: 300px (includes padding and border) = 300px actual width
```

With `border-box`, when you set `width: 300px`, the element is **exactly 300px wide** regardless of padding or borders. This makes responsive layouts and component sizing dramatically easier.

**Pseudo-Elements Included:**

Including `::before` and `::after` in the reset is crucial because:
- These elements can add unexpected layout changes if they inherit different box models
- Ensures decorative elements (icons, dividers) behave predictably
- Prevents edge cases where pseudo-elements break layouts

---

#### HTML Root Element

The `<html>` element establishes the foundational typography and rendering settings for the entire document:

```css
html {
  font-size: 16px;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
```

**Property Breakdown:**

| Property | Value | Purpose | Notes |
|----------|-------|---------|-------|
| `font-size` | `16px` | Sets the root font size for rem calculations | Browser default is 16px, we make it explicit |
| `-webkit-font-smoothing` | `antialiased` | Improves font rendering on WebKit browsers (Chrome, Safari, Edge) | Makes fonts appear lighter and smoother |
| `-moz-osx-font-smoothing` | `grayscale` | Improves font rendering on Firefox/macOS | Prevents subpixel rendering artifacts |

**Root Font Size Strategy:**

While the design system uses `px` units for most typography (see [Typography System](#typography-system)), the `<html>` font-size is set to `16px` to:
- Maintain browser default for accessibility (users can still zoom)
- Provide a stable base for any future `rem`-based spacing
- Ensure consistent baseline across browsers

**Design Note:** The design system currently uses `px` units throughout (e.g., `var(--text-base): 13px`) rather than `rem` units. This is a deliberate choice for pixel-perfect control in a single-page design. If the site expands to multiple pages or requires more flexible scaling, consider migrating to `rem`-based typography.

---

#### Body Element

The `<body>` element establishes the default typography and color scheme for all content:

```css
body {
  font-family: var(--font-body);      /* Helvetica Neue */
  font-size: var(--text-base);        /* 13px */
  font-weight: var(--font-normal);    /* 400 */
  line-height: 1.75;                  /* 22.75px for 13px text */
  color: var(--color-gray-700);       /* #555555 */
  background-color: var(--color-white); /* #FFFFFF */
}
```

**Property Breakdown:**

| Property | Value | Token | Computed | Purpose |
|----------|-------|-------|----------|---------|
| `font-family` | `var(--font-body)` | Helvetica Neue, Helvetica, Arial, sans-serif | - | Clean, readable body text |
| `font-size` | `var(--text-base)` | `13px` | 13px | Compact but readable base size |
| `font-weight` | `var(--font-normal)` | `400` | 400 | Standard weight for body text |
| `line-height` | `1.75` | - | 22.75px | Comfortable reading rhythm (1.5-1.8 is optimal) |
| `color` | `var(--color-gray-700)` | `#555555` | Dark gray | Softer than pure black, easier on eyes |
| `background-color` | `var(--color-white)` | `#FFFFFF` | Pure white | Clean, modern backdrop |

**Typography Rationale:**

- **13px base size:** Slightly smaller than the standard 16px, optimized for information density while maintaining readability. Matches Twitter's compact aesthetic.
- **1.75 line-height:** Provides generous vertical rhythm. For 13px text, this creates ~22.75px line height (10px of breathing room between lines).
- **Gray-700 color (#555555):** Softer than pure black (#000000), reducing eye strain during extended reading. Black is reserved for high-emphasis headings.

**Accessibility:**

- **Color contrast:** Gray-700 on white = **7.4:1** (WCAG AAA for normal text)
- **Font size:** 13px is readable but approaches the minimum for comfortable reading. All interactive elements use larger sizes (14px+).
- **Line height:** 1.75 exceeds WCAG recommendation of 1.5 for improved readability.

**Inheritance:**

All properties set on `<body>` cascade to child elements unless explicitly overridden. This means:
- All text inherits Helvetica Neue unless a component specifies a different font
- All paragraphs inherit 13px/1.75 unless explicitly styled (e.g., headings use Oswald)
- All content inherits gray-700 unless overridden (e.g., headings use black)

---

#### Best Practices

**Do's:**

- ✅ **Do** rely on the universal reset for consistent spacing—all margins/padding are intentional
- ✅ **Do** use design tokens (`var(--color-gray-700)`) instead of hardcoded values
- ✅ **Do** override body defaults for specific components (headings, widgets, forms)
- ✅ **Do** maintain the 1.75 line-height for body text to ensure readability
- ✅ **Do** preserve the border-box model—never override it with content-box

**Don'ts:**

- ❌ **Don't** set margins on elements expecting browser defaults (e.g., `<p>` has no margin—add it explicitly)
- ❌ **Don't** use `content-box` for individual components—keep border-box consistent
- ❌ **Don't** override font-smoothing properties—they're optimized for cross-browser rendering
- ❌ **Don't** reduce line-height below 1.5 for body text—impairs readability
- ❌ **Don't** use pure black (#000000) for body text—reserve it for headings

---

### Browser Normalization

Modern browsers have converged on many rendering behaviors, but subtle differences remain in font rendering, form controls, and default styles. This section documents the browser-specific adjustments applied to ensure consistent visual presentation.

#### Font Smoothing

Font smoothing (also called anti-aliasing) affects how browsers render text, especially on non-retina displays. Different browsers use different default rendering methods, which can make the same font look dramatically different.

**WebKit Browsers (Chrome, Safari, Edge)**

```css
-webkit-font-smoothing: antialiased;
```

| Value | Effect | Notes |
|-------|--------|-------|
| `antialiased` | Uses grayscale anti-aliasing instead of subpixel rendering | Makes fonts appear lighter and smoother |
| `subpixel-antialiased` (default) | Uses RGB subpixel rendering | Can cause color fringing on non-retina displays |
| `none` | No anti-aliasing | Produces jagged edges, not recommended |

**Why `antialiased`?**

- Creates consistent font weights across retina and non-retina displays
- Prevents color fringing artifacts on LCD screens
- Matches the design aesthetic (clean, modern, minimal)
- **Trade-off:** Text appears slightly thinner than browser default

**Firefox on macOS**

```css
-moz-osx-font-smoothing: grayscale;
```

| Value | Effect | Notes |
|-------|--------|-------|
| `grayscale` | Uses grayscale anti-aliasing | Matches WebKit's `antialiased` behavior |
| `auto` (default) | Browser decides based on font size and display | Can cause inconsistency |

**Why `grayscale`?**

- Ensures Firefox/macOS matches WebKit rendering
- Prevents thicker/bolder text appearance in Firefox
- Creates visual consistency across browsers on macOS

**Windows & Linux:**

Font smoothing properties are ignored on Windows and most Linux distributions because:
- Windows uses ClearType (subpixel rendering) by default
- Linux font rendering varies by distribution and configuration
- These platforms handle font smoothing at the OS level

**Visual Comparison:**

```
Default (subpixel):        Antialiased (grayscale):
- Thicker strokes          - Thinner strokes
- Color fringing on edges  - Clean gray edges
- Varies by display type   - Consistent across displays
- Higher contrast          - Softer appearance
```

---

#### Cross-Browser Considerations

**No Additional Normalization Required**

Unlike older CSS resets (Normalize.css, Reset CSS), this design system does **not** include:
- ❌ Form element normalization (inputs, buttons, textareas)
- ❌ HTML5 element display fixes (`<article>`, `<section>`, etc.)
- ❌ List style resets (`<ul>`, `<ol>`)
- ❌ Table border/spacing normalization

**Why not?**

Modern browsers (Chrome 90+, Firefox 88+, Safari 14+, Edge 90+) have largely standardized:
- HTML5 semantic elements are universally supported
- Form controls have consistent baseline behavior
- Default styles are minimal and predictable

**Targeted overrides are applied per-component instead:**
- Buttons get custom styles via `.btn` and `.btn-primary` classes
- Forms get custom styles via `.email-form` input styling
- Lists are unstyled by default (the universal reset removes margins/padding)

---

#### Browser Support

**Primary Target:** Modern evergreen browsers with automatic updates.

| Browser | Minimum Version | Notes |
|---------|-----------------|-------|
| Chrome | 90+ | Full support, font smoothing applied |
| Firefox | 88+ | Full support, grayscale smoothing on macOS |
| Safari | 14+ | Full support, native antialiasing |
| Edge | 90+ (Chromium) | Full support, identical to Chrome |

**Degradation Strategy:**

- Older browsers ignore font-smoothing properties (graceful degradation)
- Box-sizing: border-box is supported in IE9+ (not a concern for modern sites)
- No polyfills or vendor-prefix fallbacks are included (assumes modern browser baseline)

**Testing Recommendations:**

- ✅ Test on macOS Chrome/Firefox/Safari to verify font smoothing consistency
- ✅ Test on Windows Chrome/Edge to verify no rendering issues
- ✅ Test responsive breakpoints (768px, 480px, 360px) across browsers
- ✅ Verify form inputs/buttons render consistently

---

#### Accessibility Notes

**Font Smoothing & Accessibility:**

The `antialiased` font smoothing makes text appear **lighter/thinner**, which can reduce readability for users with:
- Low vision
- Older displays (non-retina)
- Bright ambient lighting

**Mitigation strategies in this design:**
- ✅ Strong color contrast (gray-700 on white = 7.4:1, exceeds WCAG AAA)
- ✅ Generous line-height (1.75 for body text)
- ✅ Readable font sizes (13px minimum, 14px+ for interactive elements)
- ✅ Bold font-weight (700) for headings to maintain readability despite antialiasing

**User Preferences:**

The design does not currently respect user font smoothing preferences. Consider adding:

```css
@media (prefers-reduced-transparency: reduce) {
  html {
    -webkit-font-smoothing: subpixel-antialiased;
    -moz-osx-font-smoothing: auto;
  }
}
```

This would restore browser default font rendering for users who prefer high contrast/reduced visual effects.

**Browser Zoom:**

Because the root `font-size` is set to `16px` (browser default), users can still zoom using browser controls (Cmd/Ctrl +/-). The design respects user zoom preferences.

---

#### Quick Reference

**Reset Code:**

```css
/* Universal Reset */
*, *::before, *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

/* Root Element */
html {
  font-size: 16px;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

/* Body Defaults */
body {
  font-family: var(--font-body);        /* Helvetica Neue */
  font-size: var(--text-base);          /* 13px */
  font-weight: var(--font-normal);      /* 400 */
  line-height: 1.75;                    /* Comfortable reading */
  color: var(--color-gray-700);         /* #555555 */
  background-color: var(--color-white); /* #FFFFFF */
}
```

**Key Takeaways:**

| Concept | Value | Impact |
|---------|-------|--------|
| Box Model | `border-box` everywhere | Width/height includes padding + border |
| Margins/Padding | `0` on all elements | No browser defaults, all spacing is explicit |
| Root Font Size | `16px` | Standard baseline, supports user zoom |
| Font Smoothing | `antialiased` / `grayscale` | Consistent rendering across browsers |
| Body Font | Helvetica Neue, 13px, gray-700 | Clean, readable default |
| Line Height | `1.75` | Generous vertical rhythm for readability |

---

## Quick Reference

*Fast lookup tables for rapid development. All design tokens and component classes at a glance.*

---

### CSS Variables

Complete reference of all 43 CSS custom properties organized by category.

#### Colors (14 tokens)

| Variable | Value | Usage |
|----------|-------|-------|
| `--color-black` | `#000000` | Headings (h1, h2.section-title, h3) |
| `--color-white` | `#FFFFFF` | Page background, input fields, button text |
| `--color-gray-50` | `#F3F3F3` | Reserved (lightest gray) |
| `--color-gray-100` | `#F1F1F1` | Reserved (very light gray) |
| `--color-gray-200` | `#DDDDDD` | Borders, dividers, widget outlines |
| `--color-gray-300` | `#AAAAAA` | Reserved (mid-light gray) |
| `--color-gray-500` | `#767676` | Input borders, form outlines |
| `--color-gray-600` | `#666666` | Secondary text (taglines, footer) |
| `--color-gray-700` | `#555555` | Body text, standard content |
| `--color-gray-800` | `#32373C` | Reserved (dark gray) |
| `--color-gray-900` | `#222222` | Reserved (near-black) |
| `--color-teal-500` | `#36BCAB` | Links, hover states, focus indicators |
| `--color-blue-500` | `#0073B1` | LinkedIn button background |
| `--color-blue-700` | `#2E4453` | Reserved (platform integration) |

#### Typography (12 tokens)

**Font Families (3)**
| Variable | Value | Usage |
|----------|-------|-------|
| `--font-heading` | `"Oswald", Helvetica, Arial, sans-serif` | Headings, navigation, buttons |
| `--font-body` | `"Helvetica Neue", Helvetica, Arial, sans-serif` | Body text, paragraphs, links |
| `--font-system` | `-apple-system, system-ui, "Segoe UI", Roboto, sans-serif` | Form inputs, system UI |

**Font Sizes (6)**
| Variable | Value | Usage |
|----------|-------|-------|
| `--text-xs` | `11px` | Form inputs, tiny labels |
| `--text-sm` | `12px` | Navigation, buttons, footer |
| `--text-base` | `13px` | Body text (14px on mobile ≤480px) |
| `--text-md` | `14px` | Taglines, larger labels |
| `--text-lg` | `16px` | h3 headings |
| `--text-4xl` | `80px` | h1 only (48px tablet, 32px mobile, 28px small) |

**Font Weights (3)**
| Variable | Value | Usage |
|----------|-------|-------|
| `--font-light` | `300` | Taglines only (h2.tagline) |
| `--font-normal` | `400` | Body text (default weight) |
| `--font-bold` | `700` | Headings, buttons, labels |

#### Spacing (9 tokens)

| Variable | Value | Usage |
|----------|-------|-------|
| `--space-1` | `4px` | Micro spacing, minimal gaps |
| `--space-2` | `8px` | Extra small spacing, icon gaps |
| `--space-3` | `12px` | Small spacing, tight margins |
| `--space-4` | `16px` | Base unit, standard padding |
| `--space-5` | `20px` | Medium spacing, section gaps |
| `--space-6` | `24px` | Large spacing, major sections |
| `--space-8` | `32px` | Extra large spacing, prominent separation |
| `--space-10` | `40px` | 2xl spacing, maximum separation |
| `--space-header` | `70px` | Header only (50px tablet, 32px mobile) |

#### Layout (4 tokens)

| Variable | Value | Usage |
|----------|-------|-------|
| `--content-width` | `580px` | Main content area width |
| `--sidebar-width` | `240px` | Sidebar width |
| `--container-max` | `860px` | Maximum container (580+40+240) |
| `--gap` | `40px` | Content/sidebar separation |

#### Borders (2 tokens)

| Variable | Value | Usage |
|----------|-------|-------|
| `--radius-sm` | `2px` | Buttons, inputs, tags (default) |
| `--radius-md` | `3px` | Widgets, large containers |

#### Transitions (2 tokens)

| Variable | Value | Usage |
|----------|-------|-------|
| `--transition-fast` | `0.15s ease` | Immediate feedback, small elements |
| `--transition-normal` | `0.2s ease` | Standard interactions, links, buttons |

---

### Component Classes

Alphabetical reference of all component class names with their primary purpose.

#### Layout Components

| Class | Purpose | Type |
|-------|---------|------|
| `.content` | Primary content area (580px wide, full-width on tablet) | Structural |
| `.sidebar` | Secondary sidebar area (240px wide, stacks on tablet) | Structural |
| `.site-container` | Outer page wrapper with centered max-width | Structural |
| `.site-footer` | Footer area with top border separator | Structural |
| `.site-header` | Header area with responsive top padding | Structural |
| `.site-main` | Main content wrapper (flexbox two-column) | Structural |
| `.site-nav` | Navigation container with horizontal flexbox | Structural |

#### Typography Components

| Class | Purpose | Type |
|-------|---------|------|
| `.accent-link` | Teal-colored link with underline on hover | Typography |
| `h1` | Main page heading (80px → 32px mobile, uppercase, black) | Typography |
| `h2.section-title` | Section heading (14px, uppercase, bold, black) | Typography |
| `h2.tagline` | Subtitle/tagline (14px, light weight, gray-600) | Typography |
| `h3` | Subsection heading (16px, uppercase, gray-700) | Typography |

#### Interactive Components

| Class | Purpose | Type |
|-------|---------|------|
| `.btn` | Base button class (11px, system font, 2px radius) | Interactive |
| `.btn-primary` | Primary CTA button (LinkedIn blue background) | Interactive |
| `.email-form` | Email signup form wrapper | Interactive |
| `.like-btn` | Like/heart button with icon support | Interactive |
| `.like-section` | Container for like button and count | Interactive |
| `.share-btn` | Individual share button (bordered, teal on hover) | Interactive |
| `.share-buttons` | Container for share button group | Interactive |

#### Content Components

| Class | Purpose | Type |
|-------|---------|------|
| `.contact-section` | Footer contact area with top border/padding | Content |
| `.flight-stats` | Full-width infographic image (responsive margins) | Content |
| `.like-count` | Like count display text | Content |
| `.profile-image` | Full-width profile photo (max 580px) | Content |
| `.share-section` | Bordered sharing area with top margin | Content |
| `.share-title` | Share section heading (12px, bold) | Content |
| `.signature` | Author byline text (normal font-style) | Content |
| `.social-links` | Vertical flexbox link stack (8px gap) | Content |
| `.social-links-inline` | Horizontal inline link group (20px gap, footer) | Content |
| `.subscriber-count` | Newsletter subscriber count display | Content |
| `.widget` | Sidebar widget container (24px bottom margin) | Content |
| `.widget-title` | Widget heading (16px, uppercase, bold) | Content |

---

### Common Patterns

Frequently used combinations and patterns for rapid implementation.

#### Two-Column Layout Pattern

```html
<div class="site-container">
  <main class="site-main">
    <div class="content">
      <!-- Main content goes here -->
    </div>
    <aside class="sidebar">
      <!-- Widgets go here -->
    </aside>
  </main>
</div>
```

**Key Points:**
- `.site-main` uses flexbox with 40px gap
- Content is 580px, sidebar is 240px
- Stacks vertically on tablet (≤768px)

#### Sidebar Widget Pattern

```html
<div class="widget">
  <h4 class="widget-title">Widget Title</h4>
  <p>Widget content goes here...</p>
</div>
```

**Key Points:**
- 24px bottom margin between widgets
- Widget title is 16px, uppercase, bold
- Widget content inherits base text styles

#### Email Signup Form Pattern

```html
<form class="email-form">
  <label for="email">Your email:</label>
  <input type="email" id="email" placeholder="you@example.com">
  <button type="submit" class="btn btn-primary">Subscribe</button>
</form>
```

**Key Points:**
- Input border changes to teal on focus
- Button uses LinkedIn blue (#0073B1)
- Full-width input with 100% width

#### Share Button Group Pattern

```html
<div class="share-section">
  <div class="share-title">Share this:</div>
  <div class="share-buttons">
    <button class="share-btn">Share on X</button>
    <button class="share-btn">Share on LinkedIn</button>
  </div>
</div>
```

**Key Points:**
- Share section has top border and padding
- Buttons have gray border, teal on hover
- Uses 0.15s transition for fast feedback

#### Section Heading Pattern

```html
<h2 class="section-title">Section Title</h2>
<p>Section content starts here...</p>
```

**Key Points:**
- Always uppercase, 14px, bold, black
- 20px bottom margin
- Use for major content sections

#### Navigation Pattern

```html
<nav class="site-nav">
  <ul>
    <li><a href="#about">About</a></li>
    <li><a href="#work">Work</a></li>
    <li><a href="#contact">Contact</a></li>
  </ul>
</nav>
```

**Key Points:**
- Horizontal flexbox with 20px gap
- 12px uppercase text
- Gray-700 default, teal on hover

#### Profile Image Pattern

```html
<img src="profile.jpg" alt="Profile photo" class="profile-image">
```

**Key Points:**
- Full-width, max 580px
- 20px vertical margin (16px on mobile)
- Auto height preserves aspect ratio

#### Contact Section Pattern

```html
<section class="contact-section">
  <h3>Get in touch</h3>
  <div class="social-links-inline">
    <a href="#">Email</a>
    <a href="#">LinkedIn</a>
    <a href="#">X (Twitter)</a>
  </div>
</section>
```

**Key Points:**
- 32px top margin, 24px top/bottom padding
- Gray-200 top border separator
- Inline links with 20px gap (24px on mobile)

#### Accent Link Pattern

```html
<p>Check out my <a href="#work" class="accent-link">latest work</a>.</p>
```

**Key Points:**
- Teal color by default
- Underline appears on hover
- Use for emphasized links within content

#### Responsive Typography Pattern

```css
/* Automatically responsive via CSS variables */
font-size: var(--text-4xl);  /* 80px → 48px → 32px → 28px */
font-size: var(--text-base);  /* 13px → 14px on mobile */
```

**Key Points:**
- Use CSS variables for automatic responsiveness
- `--text-4xl` dramatically scales down on mobile
- `--text-base` slightly increases for mobile readability

#### Spacing Stack Pattern

```html
<!-- Stack elements with consistent spacing -->
<section>
  <h2 class="section-title">Title</h2>      <!-- 20px bottom -->
  <p style="margin-bottom: var(--space-5)">First paragraph</p>    <!-- 20px -->
  <p style="margin-bottom: var(--space-5)">Second paragraph</p>   <!-- 20px -->
  <div class="widget">Widget content</div>   <!-- 24px bottom -->
</section>
```

**Key Points:**
- Use `--space-5` (20px) for paragraph gaps
- Use `--space-6` (24px) for component gaps
- Maintain 4px-based rhythm throughout

#### Button State Pattern

```html
<button class="btn btn-primary">Primary Action</button>
<a href="#" class="btn">Secondary Action</a>
```

**Key Points:**
- `.btn` provides base styles (padding, radius, font)
- `.btn-primary` adds LinkedIn blue background
- Use `<a class="btn">` for link-styled buttons
- 0.2s transition on background color

---

### Quick Reference Cheat Sheet

**Most Common Values:**
```
Colors:
  Primary Text:      var(--color-gray-700)    #555555
  Headings:          var(--color-black)       #000000
  Secondary Text:    var(--color-gray-600)    #666666
  Accent/Links:      var(--color-teal-500)    #36BCAB
  Borders:           var(--color-gray-200)    #DDDDDD

Typography:
  Body Font:         var(--font-body)         Helvetica Neue
  Heading Font:      var(--font-heading)      Oswald
  Body Size:         var(--text-base)         13px
  Button Size:       var(--text-sm)           12px

Spacing:
  Tight:             var(--space-2)           8px
  Standard:          var(--space-4)           16px
  Relaxed:           var(--space-5)           20px
  Section:           var(--space-6)           24px

Layout:
  Content Width:     var(--content-width)     580px
  Content/Sidebar:   var(--gap)               40px
  Max Container:     var(--container-max)     860px
```

**Breakpoints:**
```
Desktop:       default (no media query)
Tablet:        @media (max-width: 768px)
Mobile:        @media (max-width: 480px)
Small Mobile:  @media (max-width: 360px)
```

**Common Transitions:**
```
Fast feedback:     var(--transition-fast)    0.15s ease
Standard:          var(--transition-normal)  0.2s ease
```

---

## Usage Examples

This section demonstrates real-world patterns for combining components and following design system principles. These examples show how individual design tokens and components work together to create cohesive, accessible interfaces.

---

### Complete Page Layouts

#### Example 1: Basic Article Page

This example shows the complete structure for a simple article page with header, content, and footer.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Article Title | Abe Diaz</title>
</head>
<body>
  <div class="site-container">
    <!-- Header with navigation -->
    <header class="site-header">
      <h1><a href="/">ABE DIAZ</a></h1>
      <h2 class="tagline">Seattle/Tech/Evangelist</h2>

      <nav class="site-nav">
        <ul>
          <li><a href="/">HOME</a></li>
          <li><a href="/about">ABOUT</a></li>
          <li><a href="/contact">CONTACT</a></li>
        </ul>
      </nav>
    </header>

    <!-- Main content area -->
    <main class="site-main">
      <article class="content">
        <h2 class="section-title">ARTICLE TITLE</h2>

        <p>Opening paragraph with <a href="#" class="accent-link">accent links</a>
        for external references.</p>

        <img
          src="/images/article-image.jpg"
          alt="Descriptive alt text"
          class="profile-image"
          loading="lazy"
        >

        <p>Additional content paragraphs flow naturally with proper spacing
        from the design system tokens.</p>
      </article>
    </main>

    <!-- Footer contact section -->
    <footer class="contact-section">
      <h3>CONTACT ME:</h3>
      <div class="social-links-inline">
        <a href="https://linkedin.com/in/username" class="accent-link">LinkedIn</a>
        <a href="https://twitter.com/username" class="accent-link">Twitter</a>
      </div>
    </footer>
  </div>
</body>
</html>
```

**Key Design Decisions:**

- **Semantic HTML**: Uses proper semantic tags (`<header>`, `<main>`, `<article>`, `<footer>`)
- **Single Container**: `.site-container` provides max-width and centering
- **Vertical Rhythm**: Components naturally stack with consistent spacing
- **Responsive**: Layout adapts automatically at defined breakpoints
- **Accessibility**: Proper heading hierarchy (h1 → h2 → h3) and alt text on images

---

#### Example 2: Two-Column Layout with Sidebar

This example demonstrates a content-sidebar layout pattern for richer pages.

```html
<div class="site-container">
  <header class="site-header">
    <h1><a href="/">ABE DIAZ</a></h1>
    <h2 class="tagline">Seattle/Tech/Evangelist</h2>

    <nav class="site-nav">
      <ul>
        <li><a href="/">HOME</a></li>
        <li><a href="/blog">BLOG</a></li>
      </ul>
    </nav>
  </header>

  <main class="site-main">
    <!-- Primary content: 580px width -->
    <article class="content">
      <h2 class="section-title">BLOG POST TITLE</h2>

      <p>Main article content goes here with proper paragraph spacing.</p>

      <h3>Section Heading</h3>
      <p>Subsection content maintains proper hierarchy.</p>

      <!-- Share section for engagement -->
      <div class="share-section">
        <p><strong>Share this post:</strong></p>
        <button class="share-btn">Twitter</button>
        <button class="share-btn">LinkedIn</button>
        <button class="share-btn">Facebook</button>
      </div>
    </article>

    <!-- Sidebar: 240px width with 40px gap -->
    <aside class="sidebar">
      <!-- About widget -->
      <div class="widget">
        <h4 class="widget-title">ABOUT</h4>
        <p>Brief bio or description of the site author.</p>
      </div>

      <!-- Newsletter signup widget -->
      <div class="widget">
        <h4 class="widget-title">NEWSLETTER</h4>
        <form class="email-form">
          <label for="email">Subscribe for updates:</label>
          <input
            type="email"
            id="email"
            placeholder="your@email.com"
            required
          >
          <button type="submit" class="btn btn-primary">Subscribe</button>
        </form>
        <p class="subscriber-count">Join 1,234 subscribers</p>
      </div>

      <!-- Social links widget -->
      <div class="widget">
        <h4 class="widget-title">CONNECT</h4>
        <div class="social-links">
          <a href="#">LinkedIn</a>
          <a href="#">Twitter</a>
          <a href="#">GitHub</a>
          <a href="#">Instagram</a>
        </div>
      </div>
    </aside>
  </main>

  <footer class="contact-section">
    <h3>GET IN TOUCH</h3>
    <div class="social-links-inline">
      <a href="#" class="accent-link">Email</a>
      <a href="#" class="accent-link">LinkedIn</a>
    </div>
  </footer>
</div>
```

**Key Design Decisions:**

- **Flexbox Layout**: `.site-main` uses flexbox to create the two-column layout
- **Fixed Widths**: Content (580px) + Gap (40px) + Sidebar (240px) = Container (860px)
- **Widget Pattern**: Reusable `.widget` containers with consistent spacing
- **Form Integration**: `.email-form` follows design system patterns
- **Responsive Collapse**: At 768px breakpoint, layout stacks to single column

---

### Component Combinations

#### Pattern 1: Interactive Article Engagement

Combine share buttons with like functionality for reader engagement.

```html
<article class="content">
  <h2 class="section-title">ENGAGING ARTICLE</h2>

  <p>Your article content with meaningful information.</p>

  <!-- Engagement section -->
  <div class="share-section">
    <!-- Like button with icon support -->
    <button class="like-btn" aria-label="Like this article">
      <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
        <path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/>
      </svg>
      Like
    </button>

    <!-- Share buttons -->
    <p><strong>Share this:</strong></p>
    <button class="share-btn">Twitter</button>
    <button class="share-btn">LinkedIn</button>
    <button class="share-btn">Copy Link</button>
  </div>

  <!-- Author signature -->
  <p class="signature">— Abe Diaz</p>
</article>
```

**Why This Works:**

- `.share-section` provides visual separation with top border
- `.like-btn` uses inline-flex for icon + text alignment
- `.share-btn` maintains consistent styling with hover states
- `.signature` adds personal touch at article end
- All spacing follows the 4px rhythm (20px, 24px values)

---

#### Pattern 2: Sidebar Widget Stack

Create a cohesive sidebar experience with multiple widget types.

```html
<aside class="sidebar">
  <!-- Profile widget -->
  <div class="widget">
    <img
      src="/images/avatar.jpg"
      alt="Profile photo"
      class="profile-image"
    >
    <h4 class="widget-title">ABE DIAZ</h4>
    <p>Technical Program Manager passionate about technology,
    disaster relief, and connecting people.</p>
  </div>

  <!-- Newsletter widget -->
  <div class="widget">
    <h4 class="widget-title">NEWSLETTER</h4>
    <form class="email-form">
      <label for="newsletter-email">Get weekly updates:</label>
      <input
        type="email"
        id="newsletter-email"
        placeholder="your@email.com"
        required
      >
      <button type="submit" class="btn btn-primary">Subscribe</button>
    </form>
    <p class="subscriber-count">Join 2,500+ readers</p>
  </div>

  <!-- Recent posts widget -->
  <div class="widget">
    <h4 class="widget-title">RECENT POSTS</h4>
    <p><a href="/post-1">Understanding Design Systems</a></p>
    <p><a href="/post-2">CSS Architecture Best Practices</a></p>
    <p><a href="/post-3">Building Accessible Interfaces</a></p>
  </div>

  <!-- Social widget -->
  <div class="widget">
    <h4 class="widget-title">FOLLOW</h4>
    <div class="social-links">
      <a href="https://linkedin.com/in/username">LinkedIn</a>
      <a href="https://twitter.com/username">Twitter</a>
      <a href="https://github.com/username">GitHub</a>
    </div>
  </div>
</aside>
```

**Why This Works:**

- Each `.widget` has consistent 24px bottom margin (auto-applied)
- `.widget-title` uses uppercase Oswald for visual hierarchy
- `.widget p` uses smaller 12px font for compact sidebar content
- `.social-links` provides vertical stack with 8px gaps
- `.subscriber-count` adds social proof with subtle styling
- All widgets follow the same structural pattern for consistency

---

#### Pattern 3: Typography Hierarchy

Demonstrate proper heading hierarchy and link usage.

```html
<article class="content">
  <!-- Page title -->
  <h2 class="section-title">DESIGN SYSTEM GUIDE</h2>

  <!-- Introduction paragraph -->
  <p>This guide explains how to use the design system effectively.
  Learn more about <a href="#tokens" class="accent-link">design tokens</a>
  and <a href="#components" class="accent-link">components</a>.</p>

  <!-- Section with subsection -->
  <h3>Getting Started</h3>
  <p>Begin by understanding the core principles. Regular links like
  <a href="#intro">this one</a> use default black styling, while external
  references like the <a href="https://example.com" class="accent-link">official docs</a>
  use accent styling.</p>

  <h3>Design Tokens</h3>
  <p>Design tokens provide the foundation for consistent styling across
  the entire system.</p>

  <!-- Nested content -->
  <h3>Components</h3>
  <p>Components combine tokens to create reusable interface patterns.</p>
</article>
```

**Why This Works:**

- **h2.section-title**: Used once per page as primary heading (28px, uppercase)
- **h3**: Used for content sections (16px, uppercase, maintains hierarchy)
- **Default links**: Black with teal hover for internal navigation
- **.accent-link**: Teal color for external links and primary CTAs
- **Paragraph spacing**: Automatic 20px margin-bottom maintains rhythm
- **Heading spacing**: h3 has 24px top, 16px bottom for clear sections

---

#### Pattern 4: Form with Primary CTA

Create effective forms using design system components.

```html
<div class="widget">
  <h4 class="widget-title">GET STARTED</h4>

  <form class="email-form">
    <!-- Form label -->
    <label for="signup-email">
      Enter your email to receive updates:
    </label>

    <!-- Email input with proper attributes -->
    <input
      type="email"
      id="signup-email"
      name="email"
      placeholder="your@email.com"
      aria-describedby="email-help"
      required
    >

    <!-- Helper text -->
    <p id="email-help" class="subscriber-count" style="margin-top: var(--space-2);">
      We respect your privacy. Unsubscribe anytime.
    </p>

    <!-- Primary CTA button -->
    <button type="submit" class="btn btn-primary">
      Subscribe Now
    </button>

    <!-- Alternative secondary action -->
    <a href="/privacy" class="btn" style="margin-top: var(--space-2);">
      View Privacy Policy
    </a>
  </form>

  <!-- Social proof -->
  <p class="subscriber-count">
    Trusted by 5,000+ subscribers
  </p>
</div>
```

**Why This Works:**

- `.email-form` provides consistent form styling (24px bottom margin)
- `label` uses 12px font-size, gray-700 color for readability
- `input` has teal focus state (4.6:1 contrast ratio) for accessibility
- `.btn-primary` uses LinkedIn blue (#0073B1) for strong visual hierarchy
- `.btn` (secondary) maintains subtle styling for less important actions
- `.subscriber-count` adds social proof without overwhelming
- Helper text uses proper `aria-describedby` for screen readers
- Spacing uses design tokens (--space-2 for tight elements)

---

#### Pattern 5: Content with Inline Images

Integrate images within article content properly.

```html
<article class="content">
  <h2 class="section-title">TRAVEL ADVENTURES</h2>

  <p>I'm passionate about traveling and experiencing different cultures
  around the world.</p>

  <!-- Profile/content image -->
  <img
    src="/images/travel-photo.jpg"
    alt="Abe Diaz at the Eiffel Tower in Paris"
    class="profile-image"
    loading="lazy"
    width="580"
    height="387"
  >

  <p>Each journey teaches me something new about people, technology,
  and the world we share.</p>

  <!-- Data visualization / infographic -->
  <img
    src="/images/flight-stats.png"
    alt="Flight statistics showing 50 countries visited and 200,000+ miles flown"
    class="flight-stats"
    loading="lazy"
    width="580"
    height="400"
  >

  <p>These numbers represent more than just miles—they represent
  connections, experiences, and memories.</p>
</article>
```

**Why This Works:**

- `.profile-image`: Full-width photos (max-width: 580px) with 20px vertical margin
- `.flight-stats`: Infographics with 20px margin, no max-width constraint
- Both classes use `loading="lazy"` for performance
- Width/height attributes prevent layout shift during load
- Alt text provides meaningful descriptions for accessibility
- Images are contextually placed within content flow
- Responsive: Both change to 16px margin at 768px breakpoint

---

### Best Practices

#### Design Token Usage

**DO:**
✓ Always use CSS variables for styling
```css
.custom-component {
  color: var(--color-gray-700);
  font-size: var(--text-base);
  margin-bottom: var(--space-5);
}
```

✓ Maintain the 4px spacing rhythm
```css
.custom-spacing {
  /* Good: Divisible by 4 */
  padding: var(--space-4) var(--space-6); /* 16px 24px */
  margin-top: var(--space-8); /* 32px */
}
```

✓ Use semantic color choices
```css
.article-text {
  color: var(--color-gray-700); /* Body text */
}

.article-heading {
  color: var(--color-black); /* Headings */
}

.external-link {
  color: var(--color-teal-500); /* Accent/CTAs */
}
```

**DON'T:**
✗ Avoid hardcoded values
```css
/* Bad: Hardcoded instead of using tokens */
.bad-component {
  color: #555555; /* Use var(--color-gray-700) */
  font-size: 13px; /* Use var(--text-base) */
  margin: 15px; /* Not on 4px rhythm */
}
```

✗ Don't break the spacing rhythm
```css
/* Bad: Random spacing values */
.bad-spacing {
  margin: 7px; /* Not divisible by 4 */
  padding: 15px 22px; /* Random values */
}
```

✗ Don't create arbitrary colors
```css
/* Bad: New colors not in the palette */
.bad-color {
  color: #FF5733; /* Not in design system */
  background: linear-gradient(...); /* Adds unnecessary complexity */
}
```

---

#### Component Composition

**DO:**
✓ Combine components semantically
```html
<!-- Good: Semantic structure with proper nesting -->
<article class="content">
  <h2 class="section-title">ARTICLE TITLE</h2>
  <p>Content paragraph with <a href="#" class="accent-link">proper links</a>.</p>

  <div class="share-section">
    <button class="share-btn">Share</button>
  </div>
</article>
```

✓ Use proper heading hierarchy
```html
<!-- Good: Logical h1 → h2 → h3 progression -->
<h1>ABE DIAZ</h1>
<h2 class="tagline">Seattle/Tech/Evangelist</h2>

<h2 class="section-title">MAIN SECTION</h2>
<h3>Subsection Title</h3>
```

✓ Apply classes to appropriate elements
```html
<!-- Good: Classes match element semantics -->
<nav class="site-nav">
  <ul>
    <li><a href="/">HOME</a></li>
  </ul>
</nav>

<form class="email-form">
  <label for="email">Email:</label>
  <input type="email" id="email">
</form>
```

**DON'T:**
✗ Don't nest components incorrectly
```html
<!-- Bad: Improper nesting -->
<div class="widget">
  <div class="content"> <!-- Don't nest .content inside .widget -->
    <h2 class="section-title">TITLE</h2>
  </div>
</div>
```

✗ Don't skip heading levels
```html
<!-- Bad: Jumping from h1 to h3 -->
<h1>ABE DIAZ</h1>
<h3>Section</h3> <!-- Should be h2 -->
```

✗ Don't misuse component classes
```html
<!-- Bad: Using layout classes on wrong elements -->
<button class="site-container">Click me</button> <!-- Wrong element -->
<div class="btn">Not a button</div> <!-- Should use <button> -->
```

---

#### Responsive Design

**DO:**
✓ Design mobile-first mentally, even with desktop-first CSS
```css
/* Good: Base styles work on all sizes */
.component {
  padding: var(--space-4);
  font-size: var(--text-base);
}

/* Adjustments for smaller screens */
@media (max-width: 768px) {
  .component {
    padding: var(--space-3);
  }
}
```

✓ Test at all breakpoints (768px, 480px, 360px)
```css
/* Good: Thoughtful responsive adjustments */
.site-header {
  padding-top: var(--space-header); /* 70px */
}

@media (max-width: 768px) {
  .site-header {
    padding-top: 50px;
  }
}

@media (max-width: 480px) {
  .site-header {
    padding-top: 32px;
  }
}
```

✓ Ensure touch targets are at least 44×44px on mobile
```css
/* Good: Adequate touch targets */
.share-btn,
.like-btn {
  padding: var(--space-2) var(--space-4); /* 8px 16px */
  min-height: 44px; /* Ensures mobile usability */
}
```

**DON'T:**
✗ Don't forget to test on actual devices
```css
/* Bad: Assuming desktop behavior */
.component {
  cursor: pointer; /* Mobile has no cursor */
  hover: /* effect */; /* Mobile has no hover */
}
```

✗ Don't create too many breakpoints
```css
/* Bad: Over-engineering breakpoints */
@media (max-width: 1200px) { /* Not in system */ }
@media (max-width: 992px) { /* Not in system */ }
@media (max-width: 768px) { /* OK */ }
@media (max-width: 640px) { /* Not in system */ }
@media (max-width: 480px) { /* OK */ }
```

✗ Don't make text too small on mobile
```css
/* Bad: Unreadable mobile text */
@media (max-width: 480px) {
  body {
    font-size: 10px; /* Too small! Minimum is 12px */
  }
}
```

---

#### Accessibility

**DO:**
✓ Use semantic HTML elements
```html
<!-- Good: Semantic structure -->
<header class="site-header">...</header>
<nav class="site-nav">...</nav>
<main class="site-main">...</main>
<article class="content">...</article>
<aside class="sidebar">...</aside>
<footer class="contact-section">...</footer>
```

✓ Provide meaningful alt text
```html
<!-- Good: Descriptive alt text -->
<img
  src="/profile.jpg"
  alt="Abe Diaz presenting at a technology conference in Seattle"
  class="profile-image"
>

<img
  src="/stats.png"
  alt="Flight statistics: 50 countries visited, 200,000 miles flown"
  class="flight-stats"
>
```

✓ Ensure sufficient color contrast
```css
/* Good: All combinations meet WCAG AA (4.5:1 minimum) */
.text {
  color: var(--color-gray-700); /* 7.4:1 on white */
}

.btn-primary {
  background: var(--color-blue-500); /* 4.6:1 with white text */
  color: var(--color-white);
}
```

✓ Support keyboard navigation
```css
/* Good: Clear focus states */
a:focus,
button:focus,
input:focus {
  outline: 2px solid var(--color-teal-500);
  outline-offset: 2px;
}
```

**DON'T:**
✗ Don't use divs for everything
```html
<!-- Bad: Non-semantic markup -->
<div class="header">
  <div class="navigation">
    <div class="nav-item">Home</div>
  </div>
</div>
```

✗ Don't omit alt text or use generic descriptions
```html
<!-- Bad: Missing or poor alt text -->
<img src="/photo.jpg" alt=""> <!-- Missing -->
<img src="/photo.jpg" alt="image"> <!-- Generic -->
<img src="/photo.jpg" alt="photo123.jpg"> <!-- Filename -->
```

✗ Don't rely only on color to convey meaning
```html
<!-- Bad: Color-only indication -->
<p style="color: red;">Error</p> <!-- Needs icon or text -->

<!-- Good: Multiple indicators -->
<p style="color: var(--color-red-500);">
  <strong>Error:</strong> Please check your input
</p>
```

✗ Don't remove focus outlines without replacement
```css
/* Bad: Removes keyboard navigation visibility */
*:focus {
  outline: none; /* Never do this! */
}

/* Good: Custom focus styling */
*:focus {
  outline: 2px solid var(--color-teal-500);
  outline-offset: 2px;
}
```

---

### Extending the Design System

When adding new components or patterns to the design system, follow these guidelines to maintain consistency and quality.

#### Before Adding New Tokens

**Ask yourself:**

1. **Can existing tokens solve this need?**
   - Review the [Quick Reference](#quick-reference) to see if a token already exists
   - Consider if a slight adjustment to usage could work with existing values

2. **Does this token fit the system's philosophy?**
   - Minimalism: Is this token truly necessary?
   - Consistency: Does it align with the 4px rhythm (spacing) or existing scales (typography)?
   - Accessibility: Does it meet WCAG standards?

3. **Will this token be reused?**
   - One-off values should be inline styles or component-specific
   - Only promote to token status if used 3+ times

**Adding a new color:**

```css
/* ❌ DON'T: Add arbitrary colors */
:root {
  --color-random-pink: #FF69B4; /* Breaks palette cohesion */
}

/* ✅ DO: Extend existing color families */
:root {
  --color-gray-400: #888888; /* Fills gap in gray scale */
}

/* Document in this guide with:
   - Hex value
   - Use case
   - Contrast ratios
   - When to use vs. existing colors
*/
```

**Adding new spacing:**

```css
/* ❌ DON'T: Break the 4px rhythm */
:root {
  --space-7: 26px; /* Not divisible by 4 */
}

/* ✅ DO: Maintain 4px multiples */
:root {
  --space-7: 28px; /* 4px × 7 */
}

/* Ensure it fits logically:
   --space-6: 24px;
   --space-7: 28px;  ← New value
   --space-8: 32px;
*/
```

**Adding new typography:**

```css
/* ❌ DON'T: Create random sizes */
:root {
  --text-random: 15px; /* Doesn't fit scale */
}

/* ✅ DO: Extend the typographic scale logically */
:root {
  --text-xl: 18px; /* Fits between --text-lg (16px) and --text-4xl (80px) */
}

/* Consider:
   - When will this be used? (e.g., pull quotes, callouts)
   - Does it create clear hierarchy?
   - Does it adapt responsively?
*/
```

---

#### Creating New Components

**1. Start with Semantic HTML**

```html
<!-- ❌ BAD: Div soup -->
<div class="new-component">
  <div class="new-component-title">Title</div>
  <div class="new-component-content">
    <div class="new-component-text">Text</div>
  </div>
</div>

<!-- ✅ GOOD: Semantic structure -->
<aside class="callout">
  <h4 class="callout-title">Important Note</h4>
  <p>This is a callout box for highlighting important information.</p>
</aside>
```

**2. Use Existing Design Tokens**

```css
/* ❌ BAD: Hardcoded values */
.callout {
  background: #F5F5F5;
  border-left: 4px solid #36BCAB;
  padding: 12px 16px;
  margin-bottom: 20px;
}

/* ✅ GOOD: Design system tokens */
.callout {
  background-color: var(--color-gray-50);
  border-left: var(--space-1) solid var(--color-teal-500);
  padding: var(--space-3) var(--space-4);
  margin-bottom: var(--space-5);
  border-radius: var(--radius-sm);
}

.callout-title {
  font-family: var(--font-heading);
  font-size: var(--text-md);
  font-weight: var(--font-bold);
  color: var(--color-black);
  margin-bottom: var(--space-2);
  text-transform: uppercase;
}

.callout p {
  font-size: var(--text-sm);
  color: var(--color-gray-700);
  margin-bottom: 0; /* Last child */
}
```

**3. Consider Responsive Behavior**

```css
/* Add responsive adaptations where needed */
@media (max-width: 768px) {
  .callout {
    padding: var(--space-2) var(--space-3);
    margin-bottom: var(--space-4);
  }
}
```

**4. Test for Accessibility**

```html
<!-- Ensure proper ARIA attributes if needed -->
<aside class="callout" role="complementary" aria-label="Important note">
  <h4 class="callout-title">Security Notice</h4>
  <p>Always use HTTPS for sensitive data.</p>
</aside>
```

**5. Document the Component**

Add to the [Component Documentation](#components) section with:
- **Purpose**: What problem does this solve?
- **CSS Implementation**: Full CSS code
- **HTML Structure**: Example markup
- **Usage Guidelines**: When to use, when not to use
- **Accessibility Notes**: ARIA requirements, contrast ratios
- **Responsive Behavior**: How it adapts at breakpoints

---

#### Contributing Checklist

Before submitting a new component or token to the design system:

- [ ] **Necessity Check**: Can existing patterns solve this need?
- [ ] **Naming**: Follows BEM-like conventions (`.component-name`, `.component-name__element`)
- [ ] **Tokens**: Uses CSS variables exclusively (no hardcoded values)
- [ ] **Spacing**: Maintains 4px rhythm for all spacing values
- [ ] **Typography**: Uses system fonts and type scale
- [ ] **Colors**: Uses palette colors or extends existing families logically
- [ ] **Accessibility**: Meets WCAG 2.1 AA standards (contrast, semantics, keyboard)
- [ ] **Responsive**: Tested at all three breakpoints (768px, 480px, 360px)
- [ ] **Browser Support**: Works in Chrome, Firefox, Safari, Edge (current versions)
- [ ] **Documentation**: Added to design-system.md with full details
- [ ] **Examples**: Provided usage examples in documentation
- [ ] **Consistency**: Follows existing patterns for similar components

---

### Do's and Don'ts

#### Color Usage

**DO:**
✓ Use `--color-gray-700` (#555555) for body text
✓ Use `--color-black` (#000000) for headings
✓ Use `--color-teal-500` (#36BCAB) for accent elements and CTAs
✓ Use `--color-gray-200` (#DDDDDD) for borders and dividers
✓ Ensure all text has 4.5:1 contrast ratio minimum (WCAG AA)

**DON'T:**
✗ Don't use light grays (50, 100) for text
✗ Don't create new accent colors outside the palette
✗ Don't use teal for large text blocks (reserve for accents)
✗ Don't use insufficient contrast combinations

---

#### Typography

**DO:**
✓ Use Oswald for all headings (h1-h6, `.section-title`, `.widget-title`)
✓ Use Helvetica Neue for body text, paragraphs, and UI elements
✓ Use system fonts for form inputs to match OS conventions
✓ Maintain proper heading hierarchy (h1 → h2 → h3, never skip)
✓ Use `--text-base` (13px) for standard body text

**DON'T:**
✗ Don't mix font families arbitrarily
✗ Don't use Oswald for body text (too bold/condensed)
✗ Don't create text smaller than 12px (minimum for accessibility)
✗ Don't use ALL CAPS for long paragraphs (uppercase is for headings/labels)
✗ Don't skip heading levels (e.g., h1 to h3)

---

#### Spacing

**DO:**
✓ Always use spacing tokens (`--space-1` through `--space-10`)
✓ Maintain 4px base unit (all spacing divisible by 4)
✓ Use `--space-5` (20px) for paragraph bottom margins
✓ Use `--space-6` (24px) for section spacing
✓ Use `--space-4` (16px) for general component padding

**DON'T:**
✗ Don't use arbitrary spacing values (e.g., 15px, 22px, 37px)
✗ Don't create spacing that breaks the 4px rhythm
✗ Don't over-space elements (maintain visual proximity for related items)
✗ Don't under-space touch targets on mobile (minimum 44×44px)

---

#### Layout

**DO:**
✓ Use `.site-container` as the outermost wrapper (max-width: 860px)
✓ Use `.content` (580px) and `.sidebar` (240px) for two-column layouts
✓ Let `.site-main` handle flexbox layout automatically
✓ Use semantic HTML5 elements (`<header>`, `<main>`, `<article>`, `<aside>`, `<footer>`)
✓ Design for single-column mobile collapse at 768px

**DON'T:**
✗ Don't create wider containers than `--container-max` (860px)
✗ Don't use fixed heights (allow content to flow naturally)
✗ Don't nest `.site-container` inside itself
✗ Don't use three-column layouts (system supports one or two columns)
✗ Don't fight the flexbox layout with custom widths

---

#### Components

**DO:**
✓ Use `.btn` for base button styles, add `.btn-primary` for CTAs
✓ Use `.accent-link` for external links and important internal links
✓ Use `.widget` for sidebar content modules
✓ Use `.section-title` for h2 section headings
✓ Use `.tagline` for h2 subheadings under h1

**DON'T:**
✗ Don't apply `.btn` to non-interactive elements
✗ Don't use `.accent-link` on every link (reserve for emphasis)
✗ Don't nest structural components incorrectly (e.g., `.content` inside `.widget`)
✗ Don't create custom button styles—extend `.btn` instead
✗ Don't mix component classes inappropriately

---

#### Forms

**DO:**
✓ Use `.email-form` for newsletter signup forms
✓ Always include proper `<label>` elements with `for` attributes
✓ Use `required` attribute for mandatory fields
✓ Provide visual focus states (teal border on input focus)
✓ Include helper text for complex inputs

**DON'T:**
✗ Don't use placeholder text as labels
✗ Don't omit `<label>` elements
✗ Don't create multi-column form layouts on mobile
✗ Don't remove focus states
✗ Don't use red for errors without accompanying text

---

#### Responsive Design

**DO:**
✓ Test at all three breakpoints: 768px (tablet), 480px (mobile), 360px (small mobile)
✓ Reduce header spacing on mobile (70px → 50px → 32px)
✓ Stack two-column layouts to single column at 768px
✓ Increase base font size to 14px at 480px for readability
✓ Ensure touch targets are at least 44×44px on mobile

**DON'T:**
✗ Don't create breakpoints outside the system (768px, 480px, 360px only)
✗ Don't make mobile font sizes smaller than desktop
✗ Don't hide important content on mobile
✗ Don't create horizontal scrolling on mobile
✗ Don't assume mouse interaction (use touch-friendly patterns)

---

#### Accessibility

**DO:**
✓ Use semantic HTML elements for their intended purpose
✓ Provide meaningful alt text for all images
✓ Ensure 4.5:1 contrast ratio for normal text, 3:1 for large text
✓ Support keyboard navigation with visible focus states
✓ Use ARIA attributes when semantic HTML isn't sufficient

**DON'T:**
✗ Don't rely only on color to convey meaning
✗ Don't remove focus outlines without providing alternatives
✗ Don't use automatic carousels or auto-playing media
✗ Don't create keyboard traps
✗ Don't use generic link text like "click here" or "read more"

---

#### Performance

**DO:**
✓ Use `loading="lazy"` for images below the fold
✓ Specify `width` and `height` attributes on images
✓ Use CSS transitions for subtle animations (0.15s or 0.2s)
✓ Minimize use of JavaScript for styling (CSS-first approach)
✓ Load web fonts with `display=swap` for faster text rendering

**DON'T:**
✗ Don't use heavy JavaScript frameworks for simple interactions
✗ Don't create complex CSS animations that impact performance
✗ Don't load unnecessary web font weights/styles
✗ Don't use large unoptimized images
✗ Don't create deep nesting in CSS selectors (impacts performance)

---

#### Maintenance

**DO:**
✓ Document new components in design-system.md
✓ Use CSS variables for all new values
✓ Follow existing naming conventions
✓ Test changes across all breakpoints
✓ Update documentation when patterns change

**DON'T:**
✗ Don't add inline styles (use classes and design tokens)
✗ Don't create one-off components without documentation
✗ Don't modify existing tokens without updating documentation
✗ Don't break existing component patterns
✗ Don't leave TODO comments in production code

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

- **v1.0** (2026-01-01) - Complete design system documentation
  - Documented all 43 CSS custom properties (14 colors, 12 typography, 9 spacing, 4 layout, 2 borders, 2 transitions)
  - Documented all 31 component classes (7 layout, 5 typography, 7 interactive, 12 content)
  - Documented 3 responsive breakpoints with complete adaptation patterns
  - Created comprehensive usage examples and best practices
  - Added cross-references between related sections
  - Included accessibility guidelines with WCAG contrast ratios
  - Provided quick reference section for rapid lookup

---

*Last Updated: 2026-01-01*
*Maintained by: Abe Diaz*
