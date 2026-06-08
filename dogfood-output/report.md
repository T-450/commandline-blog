# Dogfood QA Report

**Target:** https://t-450.github.io/commandline-blog/
**Date:** June 5, 2026
**Scope:** Full site QA — homepage, article pages, navigation, search, dark mode, filters, responsive behavior, edge cases
**Tester:** Hermes Agent (automated exploratory QA)

---

## Executive Summary

| Severity | Count |
|----------|-------|
| High | 1 |
| Medium | 2 |
| Low | 3 |
| **Total** | **6** |

**Overall Assessment:** The site is functional and well-designed. Console is clean (zero JS errors across all pages). Core features work: article rendering, dark mode toggle, search with live results, homepage grid layout. Issues are primarily around edge cases and polish.

---

## Issues

### Bug #1: Satya Nadella post uses "Article" tag that doesn't exist in sidebar filter

| Field | Value |
|-------|-------|
| **Severity** | Medium |
| **Category** | Functional |
| **URL** | /posts/satya-nadella-no-priors-latent-space-engineering-podcast-build-2026/ |

**Description:** The post has `tag: "Article"` in frontmatter but the sidebar filter only has "Conversation", "Deep Dive", "Open Source", "Experiments". This means the post is invisible when filtering by any of the available categories.

**Fix:** Change the post frontmatter `tag` to "Conversation" which matches the content (it's a conversation/interview format).

---

### Bug #2: No empty state when topic filter returns zero results

| Field | Value |
|-------|-------|
| **Severity** | Medium |
| **Category** | UX |
| **URL** | Homepage (/) |

**Description:** When a topic filter is selected and no posts match, all blog cards are hidden but no "no results" message is shown. The grid area goes blank, making the page look broken rather than communicating that there are no matching posts.

**Fix:** After filtering, if zero blog cards remain visible, show an empty state message like "No articles found for this topic" in the grid area.

---

### Bug #3: Missing custom 404 page

| Field | Value |
|-------|-------|
| **Severity** | Low |
| **Category** | UX |
| **URL** | /nonexistent-page/ |

**Description:** Navigating to a non-existent URL shows GitHub Pages' default generic 404 page with "Read the full documentation" link. No branding, no navigation back to the blog.

**Fix:** Add a custom 404 page (`src/pages/404.astro`) that matches the blog theme, with a "Back to home" link.

---

### Bug #4: Missing broken image fallback on blog cards

| Field | Value |
|-------|-------|
| **Severity** | Low |
| **Category** | UX |
| **URL** | Homepage (/) |

**Description:** Blog card images use an `<img>` tag with the `src` pointing to the original Microsoft CDN URL. If the image URL changes or breaks, there's no `onerror` fallback or placeholder to prevent broken image icons.

**Fix:** Add `onerror="this.style.display='none'"` or a placeholder SVG fallback to all blog card images.

---

### Bug #5: Low contrast on "Next Stop" related article cards

| Field | Value |
|-------|-------|
| **Severity** | Low |
| **Category** | Visual |
| **URL** | /posts/[slug] |

**Description:** The "Next Stop" related articles cards use a very light grey background on white. The contrast between the card background and the page background is subtle to the point of being hard to distinguish.

**Fix:** Add a border, darker background, or more visible separation for the "Next Stop" cards.

---

### Bug #6: Blog card image uses absolute URL to Microsoft CDN

| Field | Value |
|-------|-------|
| **Severity** | Low |
| **Category** | Functional |
| **URL** | All posts |

**Description:** The `image` field in post frontmatter points to `https://commandline.microsoft.com/wp-content/uploads/...`. These URLs are external dependencies — if Microsoft restructures their CDN or removes the images, all blog card images will 404.

**Fix:** Either (a) download images locally and reference them, or (b) accept as intentional (not critical since the original site is unlikely to change URLs soon).

---

## Testing Coverage

### Pages Tested
- Homepage (/) — layout, grid, images, filters, search, dark mode
- Article page (/posts/slug/) — content rendering, share buttons, related posts, author display
- 404 page (/nonexistent-page/)
- Post page via direct URL access

### Features Tested
- Dark mode toggle — works
- Search with live results — works
- Topic filter radio buttons — works
- Grid/List view toggle — works
- Header logo link (back to home) — works
- Search result links — point to correct URLs
- Related articles ("Next Stop") section — renders

### Not Tested / Out of Scope
- Mobile/responsive layout (screenshots were at desktop width)
- Performance/Lighthouse audits
- Keyboard accessibility beyond basic navigation
- Screen reader compatibility

### Blockers
- None — all core functionality is accessible

---

## Notes

The site is solid for a first build. Zero JS console errors across all pages tested. The agy agent did a thorough job translating the design. Remaining issues are typical edge cases that didn't come up in initial scaffolding.
