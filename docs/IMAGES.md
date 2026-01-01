# Image Optimization Guidelines

> Comprehensive guide for image requirements, optimization, and best practices for abediaz.ai

---

## Table of Contents

- [Quick Reference](#quick-reference)
- [File Format Guidelines](#file-format-guidelines)
- [Size Limits by Image Type](#size-limits-by-image-type)
- [Recommended Dimensions](#recommended-dimensions)
- [Optimization Workflow](#optimization-workflow)
- [Responsive Images](#responsive-images)
- [Lazy Loading](#lazy-loading)
- [Tools & Resources](#tools--resources)

---

## Quick Reference

| Image Type | Max File Size | Recommended Format | Typical Dimensions |
|------------|---------------|-------------------|-------------------|
| **Profile Images** | 200 KB | WebP + JPEG fallback | 580px - 1200px width |
| **Open Graph (Social)** | 300 KB | JPEG or WebP | 1200x630px |
| **Content Images** | 500 KB | WebP + JPEG fallback | Variable (max 2000px width) |
| **Icons & Logos** | 50 KB | SVG (preferred) or PNG | Variable |
| **Screenshots** | 500 KB | PNG or WebP | Max 2000px width |

---

## File Format Guidelines

### When to Use Each Format

#### **WebP** (Recommended for most cases)
- **Use for:** Profile images, content photos, screenshots
- **Pros:** Superior compression, 25-35% smaller than JPEG with same quality
- **Cons:** Requires JPEG fallback for older browsers
- **Browser Support:** 95%+ (all modern browsers)
- **Quality setting:** 80-85 for photos, 90-95 for UI screenshots

#### **JPEG**
- **Use for:** Fallback for WebP, photos with complex gradients
- **Pros:** Universal browser support, good for photos
- **Cons:** Larger file sizes than WebP
- **Quality setting:** 80-85 (sweet spot for file size vs. quality)
- **Progressive:** Always use progressive JPEGs for better perceived performance

#### **PNG**
- **Use for:** Screenshots with text, images requiring transparency
- **Pros:** Lossless compression, supports transparency
- **Cons:** Much larger file sizes than WebP/JPEG
- **Optimization:** Always run through PNG compression (pngcrush, optipng)
- **When to avoid:** Photos without transparency need

#### **SVG**
- **Use for:** Logos, icons, simple graphics
- **Pros:** Scalable, tiny file sizes, crisp at any resolution
- **Cons:** Not suitable for photos or complex images
- **Optimization:** Minify with SVGO, remove unnecessary metadata

### Format Decision Tree

```
Is it a logo or icon?
├─ Yes → Use SVG
└─ No → Does it need transparency?
    ├─ Yes → Use PNG (optimize aggressively)
    └─ No → Is it a photo?
        ├─ Yes → Use WebP with JPEG fallback
        └─ No → Use WebP for modern browsers, PNG fallback
```

---

## Size Limits by Image Type

### Profile Images
**Maximum file size:** 200 KB per file

Profile images are critical for first impressions and appear above the fold. They must load quickly on mobile connections.

- **Primary display (WebP):** < 150 KB at 1200px width
- **Fallback (JPEG):** < 200 KB at 1200px width
- **Thumbnail versions:** < 50 KB at 400px width

**Example:**
```
profile-1200.webp  → 145 KB (primary)
profile-1200.jpg   → 195 KB (fallback)
profile-580.webp   → 60 KB (content width)
profile-580.jpg    → 85 KB (fallback)
```

### Open Graph (Social Sharing) Images
**Maximum file size:** 300 KB

Open Graph images appear when sharing links on social media (LinkedIn, Twitter, Facebook). These must be optimized to avoid slow link previews.

- **Dimensions:** 1200x630px (Facebook/LinkedIn standard)
- **Format:** JPEG or WebP
- **Target size:** 250-300 KB maximum
- **Aspect ratio:** 1.91:1 (important for proper display)

### Content Images
**Maximum file size:** 500 KB per image

Content images include screenshots, diagrams, infographics, and other visual content within pages.

- **Photos/Screenshots:** < 400 KB at 2000px max width
- **Diagrams/Charts:** < 300 KB (use PNG or WebP)
- **Complex infographics:** < 500 KB (consider breaking into multiple images)

### Icons & UI Elements
**Maximum file size:** 50 KB

Small UI elements should be extremely lightweight.

- **SVG icons:** < 10 KB (minified)
- **PNG icons:** < 30 KB (use CSS sprites when possible)
- **Favicon set:** < 50 KB total

---

## Recommended Dimensions

### Profile Images

The site uses a CSS variable `--content-width` set to 580px for main content display.

| Use Case | Width | Height | Notes |
|----------|-------|--------|-------|
| **Content display** | 580px | Auto | Matches --content-width CSS variable |
| **High-res display** | 1200px | Auto | For retina/high-DPI screens |
| **Thumbnail** | 400px | Auto | For smaller contexts |
| **Original backup** | Keep original | Keep original | Store separately, not in public images/ |

**Aspect ratio:** Maintain original aspect ratio (don't force square crops unless design requires it)

### Open Graph Images

| Platform | Recommended Size | Minimum Size | Aspect Ratio |
|----------|-----------------|--------------|--------------|
| **Facebook** | 1200x630px | 600x315px | 1.91:1 |
| **LinkedIn** | 1200x627px | 1200x627px | 1.91:1 |
| **Twitter** | 1200x675px | 600x335px | 16:9 or 1.91:1 |
| **Universal** | 1200x630px | 1200x630px | 1.91:1 |

**Recommendation:** Use 1200x630px for all platforms (works everywhere)

### Content Images

| Type | Max Width | Max Height | Notes |
|------|-----------|------------|-------|
| **Full-width photos** | 2000px | 1500px | Responsive, served at smaller sizes on mobile |
| **Inline screenshots** | 1600px | 1200px | Typical desktop screenshot |
| **Charts/Diagrams** | 1200px | 800px | Easier to view and smaller file size |
| **Mobile screenshots** | 750px | 1334px | Actual device dimensions acceptable |

**Important:** Always provide `width` and `height` attributes in HTML to prevent [Cumulative Layout Shift (CLS)](https://web.dev/cls/)

---

## Optimization Workflow

### Step-by-Step Process

#### 1. **Prepare the Image**
- [ ] Crop to desired composition
- [ ] Resize to maximum needed dimensions (see [Recommended Dimensions](#recommended-dimensions))
- [ ] Check image orientation (EXIF data)

#### 2. **Choose Optimization Tool**

**For quick/single images:**
- [Squoosh.app](https://squoosh.app) - Browser-based, visual comparison
- [ImageOptim](https://imageoptim.com/) - Mac app, drag-and-drop (free)

**For batch optimization:**
- [ImageOptim CLI](https://imageoptim.com/api) - Command-line for scripts
- [sharp](https://sharp.pixelplumbing.com/) - Node.js library
- [Pillow](https://pillow.readthedocs.io/) - Python library

#### 3. **Optimize for WebP**
Using Squoosh.app:
1. Upload image to [squoosh.app](https://squoosh.app)
2. Select **WebP** format in right panel
3. Adjust quality slider to **80-85** for photos
4. Compare original vs. optimized (use slider)
5. Ensure file size meets target (see [Size Limits](#size-limits-by-image-type))
6. Download optimized image

#### 4. **Create JPEG Fallback**
Using Squoosh.app:
1. Keep same image loaded
2. Change format to **MozJPEG**
3. Set quality to **80-85**
4. Enable **Progressive** option
5. Download optimized JPEG

#### 5. **Verify Results**
- [ ] Check file sizes meet limits
- [ ] Visually compare quality (zoom to 100%)
- [ ] Test on actual device/browser
- [ ] Verify dimensions are correct

#### 6. **Backup Original**
- [ ] Store original high-resolution image in a separate location (not in `images/` folder)
- [ ] Consider cloud storage (Google Drive, Dropbox) for originals
- [ ] Name originals clearly: `profile-original-6510x4286.jpg`

### Example: Optimizing profile.jpg

**Current state:** 13.9 MB at 6510x4286px (Canon EOS R export)

**Target outputs:**
```bash
# Content display (580px width)
profile-580.webp   → Target: <60 KB
profile-580.jpg    → Target: <85 KB

# High-res display (1200px width)
profile-1200.webp  → Target: <150 KB
profile-1200.jpg   → Target: <200 KB
```

**Process:**
1. **Resize in Squoosh:**
   - Upload profile.jpg to squoosh.app
   - Click "Resize" in right panel
   - Set width to 1200px (height will auto-adjust)
   - Select WebP format, quality 82
   - Download as `profile-1200.webp`

2. **Create JPEG fallback:**
   - Without reloading, change format to MozJPEG
   - Set quality to 82, enable Progressive
   - Download as `profile-1200.jpg`

3. **Repeat for 580px version:**
   - Reload original or re-upload
   - Resize to 580px width
   - WebP quality 80 → `profile-580.webp`
   - JPEG quality 80, Progressive → `profile-580.jpg`

4. **Backup original:**
   - Move `profile.jpg` to backup location
   - Rename to `profile-original-6510x4286.jpg`

---

## Responsive Images

### Using srcset for Resolution Switching

Serve different image sizes based on viewport width and device pixel density.

**Example: Profile image with responsive sizes**
```html
<picture>
  <source
    type="image/webp"
    srcset="images/profile-580.webp 580w,
            images/profile-1200.webp 1200w"
    sizes="(max-width: 600px) 100vw, 580px"
  />
  <source
    type="image/jpeg"
    srcset="images/profile-580.jpg 580w,
            images/profile-1200.jpg 1200w"
    sizes="(max-width: 600px) 100vw, 580px"
  />
  <img
    src="images/profile-1200.jpg"
    alt="Abe Diaz profile photo"
    width="1200"
    height="789"
    loading="lazy"
  />
</picture>
```

### Key Attributes

| Attribute | Purpose | Required? |
|-----------|---------|-----------|
| `srcset` | List of image sources with widths | Recommended |
| `sizes` | How wide the image will display at different viewports | Recommended |
| `width` | Intrinsic width (prevents CLS) | **Yes** |
| `height` | Intrinsic height (prevents CLS) | **Yes** |
| `loading` | Lazy loading behavior | Recommended |
| `alt` | Accessibility description | **Yes** |

---

## Lazy Loading

### Implementation

Use the native `loading="lazy"` attribute for images below the fold:

```html
<img
  src="images/content-image.jpg"
  alt="Descriptive alt text"
  width="1200"
  height="800"
  loading="lazy"
/>
```

### When to Use Lazy Loading

| Scenario | Use loading="lazy"? | Reason |
|----------|-------------------|--------|
| **Hero images** | ❌ No | Above the fold, needed immediately |
| **Profile images (above fold)** | ⚠️ Maybe | If below fold on mobile, yes |
| **Content images** | ✅ Yes | Saves bandwidth, improves initial load |
| **Footer images** | ✅ Yes | Far below fold, low priority |
| **Open Graph images** | ❌ No | Meta tags, not rendered in page |

### Browser Support

- **Supported:** Chrome 77+, Edge 79+, Firefox 75+, Safari 15.4+
- **Coverage:** ~95% of users
- **Fallback:** Browsers without support load images immediately (safe progressive enhancement)

---

## Tools & Resources

### Optimization Tools

| Tool | Platform | Best For | Price |
|------|----------|----------|-------|
| [Squoosh.app](https://squoosh.app) | Web | Quick visual optimization | Free |
| [ImageOptim](https://imageoptim.com/) | Mac | Batch processing, drag-and-drop | Free |
| [TinyPNG](https://tinypng.com/) | Web | PNG compression | Free (limited) |
| [SVGOMG](https://jakearchibald.github.io/svgomg/) | Web | SVG optimization | Free |
| [sharp](https://sharp.pixelplumbing.com/) | Node.js | Automated builds, scripting | Free (OSS) |

### Testing & Validation

- [Google PageSpeed Insights](https://pagespeed.web.dev/) - Overall page performance
- [WebPageTest](https://www.webpagetest.org/) - Detailed waterfall analysis
- [Chrome DevTools](https://developer.chrome.com/docs/devtools/) - Network panel, coverage
- [Lighthouse](https://developer.chrome.com/docs/lighthouse/) - Web vitals audit

### Learning Resources

- [web.dev: Image Optimization](https://web.dev/fast/#optimize-your-images)
- [MDN: Responsive Images](https://developer.mozilla.org/en-US/docs/Learn/HTML/Multimedia_and_embedding/Responsive_images)
- [Essential Image Optimization](https://images.guide/) - Free ebook by Addy Osmani
- [WebP Documentation](https://developers.google.com/speed/webp)

---

## Checklist for New Images

Before adding any image to the site:

- [ ] Image is cropped and composed properly
- [ ] Resized to maximum needed dimensions (see [Recommended Dimensions](#recommended-dimensions))
- [ ] Optimized using Squoosh or ImageOptim
- [ ] File size is under limit for image type (see [Size Limits](#size-limits-by-image-type))
- [ ] WebP version created (for photos)
- [ ] JPEG/PNG fallback created
- [ ] Original high-res backed up (not in `images/` folder)
- [ ] HTML includes `width` and `height` attributes
- [ ] `alt` text is descriptive and meaningful
- [ ] `loading="lazy"` added if below the fold
- [ ] Tested on actual device (mobile + desktop)
- [ ] Verified no layout shift (CLS) when image loads

---

## Common Pitfalls

### ❌ Don't:
- Upload camera-raw or export images directly to `images/` without optimization
- Use PNG for photos (unless transparency is required)
- Forget `width`/`height` attributes (causes layout shift)
- Serve massive images and rely on CSS to resize (wastes bandwidth)
- Use `loading="lazy"` on above-the-fold hero images
- Skip creating WebP versions for modern browsers

### ✅ Do:
- Always optimize before committing images
- Use WebP with JPEG/PNG fallback
- Include intrinsic dimensions in HTML
- Create multiple sizes for responsive delivery
- Test on slow 3G to verify performance
- Keep original high-res versions as backups (outside repo)

---

## Git & Version Control

### .gitattributes Configuration

Ensure binary files are handled correctly:

```gitattributes
# Images
*.jpg binary
*.jpeg binary
*.png binary
*.gif binary
*.webp binary
*.svg text
```

### Large File Strategy

For images over 5 MB (before optimization):

1. **Never commit** large unoptimized images
2. Store originals in cloud storage (Google Drive, Dropbox)
3. Only commit optimized versions to repository
4. Consider Git LFS for assets if project scales

---

*Last updated: January 2026*
*For questions or suggestions, contact the site maintainer.*
