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

*This section will document all 14 color tokens with hex values, usage guidelines, accessibility notes, and visual representations.*

**Coming Soon:** Complete color palette documentation with swatches and contrast ratios.

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
