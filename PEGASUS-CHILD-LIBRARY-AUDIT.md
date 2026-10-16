# pegasus-child library audit (JS/CSS)

Audited 2026-10-15 from a fresh clone of `Visionquest-Development/pegasus-child`: all 33 remote branches except master. Latest versions were checked against the npm registry, and CDN URLs were confirmed to return 200.

Policy: update within the same major version only. Major upgrades, licence changes and customised files are listed as needs review. Only `chore/update-libraries-<site>` branches were pushed; site branches were not touched (they auto-deploy). Nothing was merged.

## Summary matrix

| Branch | Same-major updates | Majors / needs review | PR | Status |
|---|---|---|---|---|
| 34oak_theme | 2 | 0 | https://github.com/Visionquest-Development/pegasus-child/pull/8 | PR open |
| 34oak_theme_backend | 2 | 0 | https://github.com/Visionquest-Development/pegasus-child/pull/9 | PR open |
| cadence_group_theme | 2 | 4 | https://github.com/Visionquest-Development/pegasus-child/pull/17 | PR open |
| elliotint_theme | 0 | 0 | — | nothing to update |
| gentwo_theme | 0 | 0 | — | nothing to update |
| hfhsga_theme | 0 | 0 | — | nothing to update |
| iconic-entertainment-group | 0 | 0 | — | nothing to update |
| mabellas_theme | 0 | 1 | — | skipped: only update is lightbox over a custom CSS |
| mixmarket_theme | 0 | 1 | — | skipped: only update is lightbox over a custom CSS |
| opp_new_site | 2 | 3 | https://github.com/Visionquest-Development/pegasus-child/pull/18 | PR open |
| organizepluscleaning | 0 | 0 | — | nothing to update |
| osps26_theme | 0 | 0 | — | nothing to update |
| outlaw_coffee_theme | 0 | 0 | — | nothing to update |
| pegasustheme_child | 3 | 0 | https://github.com/Visionquest-Development/pegasus-child/pull/13 | PR open |
| qbiqcamp_theme | 3 | 4 | https://github.com/Visionquest-Development/pegasus-child/pull/16 | PR open |
| qbiqsystem_theme | 1 | 0 | https://github.com/Visionquest-Development/pegasus-child/pull/15 | PR open |
| renecdesign_theme | 2 | 1 | https://github.com/Visionquest-Development/pegasus-child/pull/10 | PR open |
| ricecapital_theme | 0 | 0 | — | nothing to update |
| righthandrenovations | 0 | 0 | — | nothing to update |
| russell_theme | 3 | 0 | https://github.com/Visionquest-Development/pegasus-child/pull/11 | PR open |
| sage_theme | 7 | 4 | https://github.com/Visionquest-Development/pegasus-child/pull/19 | PR open |
| saltcellar_theme | 0 | 1 | — | skipped: only update is lightbox over a custom CSS |
| shorinjionline | 0 | 0 | — | nothing to update |
| stoutbros_theme | 0 | 0 | — | nothing to update |
| sugarpeddler_theme | 0 | 0 | — | nothing to update |
| theloft2025_theme | 1 | 2 | https://github.com/Visionquest-Development/pegasus-child/pull/12 | PR open |
| tommygs_theme | 0 | 1 | — | skipped: only update is lightbox over a custom CSS |
| ulg_events_theme | 0 | 1 | — | push blocked (secret scanning) |
| ulg_theme | 0 | 1 | — | push blocked (secret scanning) |
| uptownlifegroup | 0 | 1 | — | push blocked (secret scanning) |
| valorcare_theme | 0 | 0 | — | nothing to update |
| vineandvision_theme | 1 | 0 | https://github.com/Visionquest-Development/pegasus-child/pull/14 | PR open |
| vqdev_theme | 6 | 9 | https://github.com/Visionquest-Development/pegasus-child/pull/20 | PR open |

## Per-branch detail

### 34oak_theme

PR: https://github.com/Visionquest-Development/pegasus-child/pull/8

| Library | Current | Latest | Type | File | Risk | Status |
|---|---|---|---|---|---|---|
| Lightbox2 JS | 2.11.4 | 2.12.0 | local | `js/lightbox.min.js` | low (same major) | updated in PR |
| Lightbox2 CSS | 2.11.4 | 2.12.0 | local | `css/lightbox.min.css` | low (same major) | updated in PR |

### 34oak_theme_backend

PR: https://github.com/Visionquest-Development/pegasus-child/pull/9

| Library | Current | Latest | Type | File | Risk | Status |
|---|---|---|---|---|---|---|
| Lightbox2 JS | 2.11.4 | 2.12.0 | local | `js/lightbox.min.js` | low (same major) | updated in PR |
| Lightbox2 CSS | 2.11.4 | 2.12.0 | local | `css/lightbox.min.css` | low (same major) | updated in PR |

### cadence_group_theme

PR: https://github.com/Visionquest-Development/pegasus-child/pull/17

| Library | Current | Latest | Type | File | Risk | Status |
|---|---|---|---|---|---|---|
| Flickity (pkgd) | 2.2.1 | 2.3.0 | local | `js/flickety.js` | low (same major) | updated in PR |
| Font Awesome (CDN) | 4.2.0 | 4.7.0 | CDN | `functions.php` | low (same major) | updated in PR |
| Flickity | 2.3.0 | 3.0.0 | local | `js/flickety.js` | major: needs review | flagged |
| imagesLoaded | 4.1.4 | 5.0.0 | local | `js/imagesloaded.js` | major: needs review | flagged |
| Isotope | 3.0.6 | 3.0.6 (latest) | local | `js/isotope.js` | none (current) | flagged |
| Modernizr | 2.8.3 | 3.13.1 | local | `js/modernizer.js` | major: custom build needed | flagged |
| Font Awesome | 4.7.0 | 6.x/7.x | CDN | `functions.php` | major: icon class names change (fa → fa-solid etc.) | flagged |

### elliotint_theme

PR: —

No vendored or CDN third-party JS/CSS found; only the theme's own `style.css` and custom JS.

### gentwo_theme

PR: —

No vendored or CDN third-party JS/CSS found; only the theme's own `style.css` and custom JS.

### hfhsga_theme

PR: —

No vendored or CDN third-party JS/CSS found; only the theme's own `style.css` and custom JS.

### iconic-entertainment-group

PR: —

No vendored or CDN third-party JS/CSS found; only the theme's own `style.css` and custom JS.

### mabellas_theme

PR: —

| Library | Current | Latest | Type | File | Risk | Status |
|---|---|---|---|---|---|---|
| Lightbox2 | 2.11.4 (custom inline-SVG CSS) | 2.12.0 | local | `js/lightbox.min.js, css/lightbox.min.css` | needs review: 2.12 rewrites the markup/CSS | flagged |

### mixmarket_theme

PR: —

| Library | Current | Latest | Type | File | Risk | Status |
|---|---|---|---|---|---|---|
| Lightbox2 | 2.11.4 (custom inline-SVG CSS) | 2.12.0 | local | `js/lightbox.min.js, css/lightbox.min.css` | needs review: 2.12 rewrites the markup/CSS | flagged |

### opp_new_site

PR: https://github.com/Visionquest-Development/pegasus-child/pull/18

| Library | Current | Latest | Type | File | Risk | Status |
|---|---|---|---|---|---|---|
| Magnific Popup JS | 1.0.1 | 1.2.0 | local | `js/jquery.magnific-popup.min.js` | low (same major) | updated in PR |
| jquery.matchHeight | 0.7.0 | 0.7.2 | local | `js/jquery.matchHeight-min.js` | low (same major) | updated in PR |
| Slick | 1.5.0 | 1.8.1 (same major) / 2.0.0 | local | `js/slick.js, css/slick*.css` | needs review: 1.8 wraps slides in extra row divs | flagged |
| Magnific Popup CSS | unknown (custom) | 1.2.0 | local | `css/magnific.css` | left as is: may be customised | flagged |
| FitVids | unknown | 1.2.0 | local | `js/fitvids.js` | unversioned: needs review | flagged |

### organizepluscleaning

PR: —

No vendored or CDN third-party JS/CSS found; only the theme's own `style.css` and custom JS.

### osps26_theme

PR: —

| Library | Current | Latest | Type | File | Risk | Status |
|---|---|---|---|---|---|---|
| (custom only) | — | — | local | `css/osps26-design.css, js/osps26-design.js` | no third-party libs | flagged |

### outlaw_coffee_theme

PR: —

No vendored or CDN third-party JS/CSS found; only the theme's own `style.css` and custom JS.

### pegasustheme_child

PR: https://github.com/Visionquest-Development/pegasus-child/pull/13

| Library | Current | Latest | Type | File | Risk | Status |
|---|---|---|---|---|---|---|
| Lightbox2 JS | 2.11.4 | 2.12.0 | local | `js/lightbox.min.js` | low (same major) | updated in PR |
| Lightbox2 CSS | 2.11.4 | 2.12.0 | local | `css/lightbox.min.css` | low (same major) | updated in PR |
| Prism (CDN) | 1.29.0 | 1.30.0 | CDN | `functions.php` | low (same major) | updated in PR |

### qbiqcamp_theme

PR: https://github.com/Visionquest-Development/pegasus-child/pull/16

| Library | Current | Latest | Type | File | Risk | Status |
|---|---|---|---|---|---|---|
| Lightbox2 JS | 2.11.4 | 2.12.0 | local | `js/lightbox.min.js` | low (same major) | updated in PR |
| Lightbox2 CSS | 2.11.4 | 2.12.0 | local | `css/lightbox.min.css` | low (same major) | updated in PR |
| FitVids (CDN) | 1.1.0 | 1.2.0 | CDN | `functions.php` | low (same major) | updated in PR |
| WOW.js | 1.0.3 | 1.3.0 (GitHub; GPL/commercial licence since 1.1.3) | local | `js/wow.js` | licence change: needs review | flagged |
| Animate.css | 3.x (2015) | 4.1.1 | local | `css/animate.min.css` | major: class names gain an animate__ prefix | flagged |
| Magnific Popup | empty file (0 bytes) | 1.2.0 | local | `js/magnific-popup.min.js` | file is empty: fix or remove | flagged |
| FitVids (local copy) | unknown | 1.2.0 | local | `js/fitvids.js` | unversioned: needs review | flagged |

### qbiqsystem_theme

PR: https://github.com/Visionquest-Development/pegasus-child/pull/15

| Library | Current | Latest | Type | File | Risk | Status |
|---|---|---|---|---|---|---|
| Bootstrap Icons (CDN) | 1.11.3 | 1.13.2 | CDN | `functions.php` | low (same major) | updated in PR |

### renecdesign_theme

PR: https://github.com/Visionquest-Development/pegasus-child/pull/10

| Library | Current | Latest | Type | File | Risk | Status |
|---|---|---|---|---|---|---|
| Lightbox2 JS | 2.11.4 | 2.12.0 | local | `js/lightbox.min.js` | low (same major) | updated in PR |
| Lightbox2 CSS | 2.11.4 | 2.12.0 | local | `css/lightbox.min.css` | low (same major) | updated in PR |
| Isotope | 3.0.6 | 3.0.6 (latest) | local | `js/isotope.js` | none (current) | flagged |
| imagesLoaded | 4.1.4 | 5.0.0 | local | `js/imagesloaded.js` | major: needs review | flagged |

### ricecapital_theme

PR: —

No vendored or CDN third-party JS/CSS found; only the theme's own `style.css` and custom JS.

### righthandrenovations

PR: —

No vendored or CDN third-party JS/CSS found; only the theme's own `style.css` and custom JS.

### russell_theme

PR: https://github.com/Visionquest-Development/pegasus-child/pull/11

| Library | Current | Latest | Type | File | Risk | Status |
|---|---|---|---|---|---|---|
| Lightbox2 JS | 2.11.4 | 2.12.0 | local | `js/lightbox.min.js` | low (same major) | updated in PR |
| Lightbox2 CSS | 2.11.4 | 2.12.0 | local | `css/lightbox.min.css` | low (same major) | updated in PR |
| Bootstrap Icons (CDN) | 1.11.3 | 1.13.2 | CDN | `functions.php` | low (same major) | updated in PR |

### sage_theme

PR: https://github.com/Visionquest-Development/pegasus-child/pull/19

| Library | Current | Latest | Type | File | Risk | Status |
|---|---|---|---|---|---|---|
| Lightbox2 JS | 2.11.4 | 2.12.0 | local | `js/lightbox.min.js` | low (same major) | updated in PR |
| Lightbox2 CSS | 2.11.4 | 2.12.0 | local | `css/lightbox.min.css` | low (same major) | updated in PR |
| jquery.matchHeight | 0.7.0 | 0.7.2 | local | `js/matchHeight.js` | low (same major) | updated in PR |
| imagesLoaded (pkgd) | 4.1.2 | 4.1.4 | local | `js/imagesLoaded.js` | low (same major) | updated in PR |
| Magnific Popup JS | 1.1.0 | 1.2.0 | local | `js/magnific-popup.min.js` | low (same major) | updated in PR |
| Swiper JS | 8.3.2 | 8.4.7 | local | `js/swiper-bundle.min.js` | low (same major) | updated in PR |
| Swiper CSS | 8.3.2 | 8.4.7 | local | `css/swiper-bundle.min.css` | low (same major) | updated in PR |
| Swiper | 8.4.7 | 14.x | local | `js/swiper-bundle.min.js` | major: API changes, needs review | flagged |
| imagesLoaded | 4.1.4 | 5.0.0 | local | `js/imagesLoaded.js` | major: needs review | flagged |
| Masonry | 3.3.2 | 4.2.2 | local | `js/masonry.js` | major: needs review | flagged |
| Packery | 1.4.3 | 3.0.0 | local | `js/packery.min.js` | major: needs review | flagged |
| WOW.js | 1.3.0 | 1.3.0 | local | `js/wow.min.js` | current | flagged |
| Waypoints / CounterUp / Pace / nice-select | 4.0.1 / 1.0 / 1.2.4 / 1.x | current | local | `js/` | no update needed | flagged |

### saltcellar_theme

PR: —

| Library | Current | Latest | Type | File | Risk | Status |
|---|---|---|---|---|---|---|
| Lightbox2 | 2.11.4 (custom inline-SVG CSS) | 2.12.0 | local | `js/lightbox.min.js, css/lightbox.min.css` | needs review: 2.12 rewrites the markup/CSS | flagged |

### shorinjionline

PR: —

| Library | Current | Latest | Type | File | Risk | Status |
|---|---|---|---|---|---|---|
| (custom only) | — | — | local | `script.js` | no third-party libs | flagged |

### stoutbros_theme

PR: —

No vendored or CDN third-party JS/CSS found; only the theme's own `style.css` and custom JS.

### sugarpeddler_theme

PR: —

No vendored or CDN third-party JS/CSS found; only the theme's own `style.css` and custom JS.

### theloft2025_theme

PR: https://github.com/Visionquest-Development/pegasus-child/pull/12

| Library | Current | Latest | Type | File | Risk | Status |
|---|---|---|---|---|---|---|
| jquery.matchHeight | 0.7.0 | 0.7.2 | local | `js/matchHeight.js` | low (same major) | updated in PR |
| Lightbox2 | 2.11.4 (custom inline-SVG CSS) | 2.12.0 | local | `js/lightbox.min.js, css/lightbox.min.css` | needs review: 2.12 rewrites the markup/CSS; this branch has a custom self-contained CSS | flagged |
| Packery | 1.4.3 | 3.0.0 | local | `js/packery.js` | major: needs review | flagged |

### tommygs_theme

PR: —

| Library | Current | Latest | Type | File | Risk | Status |
|---|---|---|---|---|---|---|
| Lightbox2 | 2.11.4 (custom inline-SVG CSS) | 2.12.0 | local | `js/lightbox.min.js, css/lightbox.min.css` | needs review: 2.12 rewrites the markup/CSS | flagged |

### ulg_events_theme

PR: —

| Library | Current | Latest | Type | File | Risk | Status |
|---|---|---|---|---|---|---|
| Mapbox GL JS (CDN) | 3.0.1 | 3.33.0 | CDN | `uptown-restaurant-map.php` | low (same major) | blocked: push protection |

### ulg_theme

PR: —

| Library | Current | Latest | Type | File | Risk | Status |
|---|---|---|---|---|---|---|
| Mapbox GL JS (CDN) | 3.0.1 | 3.33.0 | CDN | `uptown-restaurant-map.php` | low (same major) | blocked: push protection |

### uptownlifegroup

PR: —

| Library | Current | Latest | Type | File | Risk | Status |
|---|---|---|---|---|---|---|
| Mapbox GL JS (CDN) | 3.0.1 | 3.33.0 | CDN | `uptown-restaurant-map.php` | low (same major) | blocked: push protection |

### valorcare_theme

PR: —

No vendored or CDN third-party JS/CSS found; only the theme's own `style.css` and custom JS.

### vineandvision_theme

PR: https://github.com/Visionquest-Development/pegasus-child/pull/14

| Library | Current | Latest | Type | File | Risk | Status |
|---|---|---|---|---|---|---|
| jquery.matchHeight | 0.7.0 | 0.7.2 | local | `js/matchHeight.js` | low (same major) | updated in PR |

### vqdev_theme

PR: https://github.com/Visionquest-Development/pegasus-child/pull/20

| Library | Current | Latest | Type | File | Risk | Status |
|---|---|---|---|---|---|---|
| Lightbox2 JS | 2.11.4 | 2.12.0 | local | `js/lightbox.min.js` | low (same major) | updated in PR |
| Lightbox2 CSS | 2.11.4 | 2.12.0 | local | `css/lightbox.min.css` | low (same major) | updated in PR |
| jquery.matchHeight | 0.7.0 | 0.7.2 | local | `js/jquery.matchHeight-min.js` | low (same major) | updated in PR |
| GSAP + ScrollTrigger (CDN) | 3.11.2 | 3.15.0 | CDN | `functions.php` | low (same major) | updated in PR |
| Foundation JS (CDN) | 5.5.0 | 5.5.3 | CDN | `functions.php` | low (same major) | updated in PR |
| Hammer.js (CDN) | 2.0.6 | 2.0.8 | CDN | `functions.php` | low (same major) | updated in PR |
| Slick | 1.5.0 | 1.8.1 / 2.0.0 | local | `js/slick.js, css/slick*.css` | needs review: 1.8 wraps slides in extra row divs | flagged |
| Masonry | 3.3.2 | 4.2.2 | local | `js/masonry.js` | major: needs review | flagged |
| Packery | 1.4.3 | 3.0.0 | local | `js/packery.pkgd.js` | major: needs review | flagged |
| MixItUp | 2.1.10 | 3.3.2 | local | `js/mixitup.js` | major: API rewrite | flagged |
| Modernizr | 2.8.3 | 3.13.1 | local | `js/modernizr.custom.js` | major: custom build | flagged |
| Foundation JS | 5.5.3 | 6.9.0 | CDN | `functions.php` | major: needs review | flagged |
| Animate.css | 3.x | 4.1.1 | local | `css/animate*.css` | major: class prefix | flagged |
| jQuery Parallax (Ian Lunn) | 1.1.3 | unmaintained | local | `js/parallax.js` | consider replacing | flagged |
| Stellar.js | 0.6.2 | 0.6.2 (unmaintained) | CDN | `functions.php` | consider replacing | flagged |

## Notes

- **Lightbox2 2.12.0** rewrites the markup and CSS (fixed overlay, CSS variables), so the JS and CSS are updated together. mabellas, mixmarket, saltcellar, tommygs and theloft2025 ship a custom self-contained `lightbox.min.css` with inline SVG icons, so their lightbox was not updated; they need review.
- **Slick 1.5 → 1.8.1** (opp_new_site, vqdev) is the same major, but 1.8 wraps slides in extra row `<div>`s, which can break theme CSS. It is flagged rather than applied.
- **vqdev `js/parallax.js`** is Ian Lunn's jQuery Parallax 1.1.3, not pixelcog's parallax.js, so it was not swapped. That library and Stellar.js are unmaintained.
- **qbiqcamp `js/magnific-popup.min.js`** is an empty file (0 bytes).
- **WOW.js** is GPL/commercial since 1.1.3. qbiqcamp (1.0.3) was left as is.
- **ulg_events_theme, ulg_theme and uptownlifegroup:** the Mapbox GL 3.0.1 → 3.33.0 commit is ready locally, but GitHub push protection rejected it. `uptown-restaurant-map.php` already contains a Mapbox access token, and secret scanning flags any commit touching that file. Options: move the token to wp-config/an option and rotate it, or approve the bypass in GitHub (Jim's call).
- SRI: no `integrity` attributes in any branch. Enqueue versions are empty, false or `filemtime`, so no version-string edits were needed.
- Every branch must be smoke-tested before merge; merging into a site branch triggers the SiteGround deploy.
