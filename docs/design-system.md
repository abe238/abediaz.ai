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

*This section will document the font families (Oswald, Helvetica Neue, System), font sizes, weights, and their intended usage.*

**Coming Soon:** Typography system documentation including font stacks and pairing guidelines.

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
