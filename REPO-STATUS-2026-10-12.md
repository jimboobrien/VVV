# Pegasus / wp-bootstrap-hooks / vqdev-toast repo status (last scan 2026-10-14T16:31:46-04:00)

Source: a fresh `git fetch` per copy, run by `sync/pegasus.sh status` (sync/lib/rescan_status.py). The same data feeds the JSON, the CSV and http://localhost:3001/pegasus-status.

**225 copies across 34 sites.**

## Summary

| Status | Count |
|---|---|
| Up to date | 194 |
| Site branch: up to date | 26 |
| Site branch: needs pull | 2 |
| Site branch: not on origin (HEAD is a shared commit in 29 origin branches) | 2 |
| Not a git repo | 1 |

### Current commit by component (default-branch copies)

| Component | Commit(s) |
|---|---|
| pegasus | `3ec9e66` ×34 |
| pegasus-accordion | `01841eb` ×5 |
| pegasus-blog | `4db9f03` ×2 |
| pegasus-botify | `ffd1d28` ×1 |
| pegasus-callout | `bc4c766` ×3 |
| pegasus-carousel | `586bc7a` ×27 |
| pegasus-child | `9e3b058` ×3 |
| pegasus-circle-progress | `b942b9d` ×2 |
| pegasus-countup | `59fcca1` ×2 |
| pegasus-masonry | `e990597` ×4 |
| pegasus-navmenu | `3854128` ×2 |
| pegasus-onepage | `66a5367` ×3 |
| pegasus-packery | `a88aae3` ×5 |
| pegasus-popup | `a623c9b` ×3 |
| pegasus-post-grid | `bb7e16c` ×1 |
| pegasus-postgrid | `bb7e16c` ×2 |
| pegasus-posts-filter | `b3f8c72` ×2 |
| pegasus-slider | `e53d764` ×25 |
| pegasus-tabs | `ca26dd5` ×5 |
| pegasus-toggleslide | `8fce927` ×4 |
| pegasus-wow | `84305b5` ×22 |
| vqdev-toast | `b7f7eac` ×6 |
| wp-bootstrap-hooks | `de07965` ×31 |

### Needs attention

| Site | Component | Branch | Upstream | Ahead/Behind | Dirty | Status |
|---|---|---|---|---|---|---|
| hfhsga | pegasus-child | hfhsga_theme | origin/hfhsga_theme | 0/1 | 15 | Site branch: needs pull |
| ourpalsplace | pegasus-child | opp_new_site | origin/opp_new_site | 1/5 | 18 | Site branch: needs pull |
| ourpalsplacedbt | pegasus-child | opp-dbt-site |  | ?/? | 2 | Site branch: not on origin (HEAD is a shared commit in 29 origin branches) |
| theloft | pegasus-child | theloft |  | ?/? | 2 | Site branch: not on origin (HEAD is a shared commit in 29 origin branches) |
| theloftnew | pegasus-theloft |  |  | / |  | Not a git repo |

## Updated 2026-10-12

**Round 1 (12:10):** 121 ff-only pulls, 0 failures. Log: `pull-log-2026-10-12.txt`.

**Round 2 (12:58):**
- Archived 7 old_* folders to `old-archive/`.
- Replaced 5 benignware wp-bootstrap-hooks copies with fresh clones of the jimboobrien fork (master de07965, v1.1.22): ourpalsplace, ourpalsplacedbt, qbiqcamp, sagecnc, vineandvision. Backups are in `old-archive/<site>/wp-bootstrap-hooks-benignware-2026-10-12`. The qbiqcamp backup also includes `local-changes.patch`.
- 29 ff-only pulls (pegasus theme to fbb24ef), 0 failures. Log: `pull-log-2026-10-12-round2.txt`.

| Round | Path | Branch | Commits | New HEAD |
|---|---|---|---|---|
| 1 | `34oak/public_html/wp-content/plugins/pegasus-carousel` | master | 2 | 97b26c0 |
| 1 | `34oak/public_html/wp-content/plugins/pegasus-masonry` | master | 3 | 0465acc |
| 1 | `34oak/public_html/wp-content/plugins/pegasus-slider` | master | 2 | 9183ef4 |
| 1 | `34oak/public_html/wp-content/plugins/pegasus-wow` | master | 2 | e25ef14 |
| 1 | `34oak/public_html/wp-content/plugins/wp-bootstrap-hooks` | master | 3 | de07965 |
| 1 | `34oak/public_html/wp-content/themes/pegasus` | master | 4 | 6cd37a7 |
| 1 | `cadence-group/public_html/wp-content/plugins/pegasus-carousel` | master | 2 | 97b26c0 |
| 1 | `cadence-group/public_html/wp-content/plugins/pegasus-postgrid` | master | 2 | 83d3f28 |
| 1 | `cadence-group/public_html/wp-content/plugins/pegasus-slider` | master | 2 | 9183ef4 |
| 1 | `cadence-group/public_html/wp-content/themes/pegasus` | master | 3 | 6cd37a7 |
| 1 | `elliot/public_html/wp-content/plugins/pegasus-carousel` | master | 2 | 97b26c0 |
| 1 | `elliot/public_html/wp-content/plugins/pegasus-slider` | master | 2 | 9183ef4 |
| 1 | `elliot/public_html/wp-content/plugins/pegasus-wow` | master | 2 | e25ef14 |
| 1 | `elliot/public_html/wp-content/themes/pegasus` | master | 3 | 6cd37a7 |
| 1 | `gentwo/public_html/wp-content/plugins/pegasus-carousel` | master | 2 | 97b26c0 |
| 1 | `gentwo/public_html/wp-content/plugins/pegasus-slider` | master | 2 | 9183ef4 |
| 1 | `gentwo/public_html/wp-content/plugins/pegasus-wow` | master | 2 | e25ef14 |
| 1 | `gentwo/public_html/wp-content/themes/pegasus` | master | 3 | 6cd37a7 |
| 1 | `hfhsga/public_html/wp-content/plugins/pegasus-carousel` | master | 2 | 97b26c0 |
| 1 | `hfhsga/public_html/wp-content/plugins/pegasus-slider` | master | 2 | 9183ef4 |
| 1 | `hfhsga/public_html/wp-content/plugins/pegasus-wow` | master | 2 | e25ef14 |
| 1 | `iconic/public_html/wp-content/plugins/pegasus-carousel` | master | 2 | 97b26c0 |
| 1 | `iconic/public_html/wp-content/plugins/pegasus-slider` | master | 2 | 9183ef4 |
| 1 | `iconic/public_html/wp-content/plugins/pegasus-wow` | master | 2 | e25ef14 |
| 1 | `iconic/public_html/wp-content/themes/pegasus` | master | 3 | 6cd37a7 |
| 1 | `mabellas/public_html/wp-content/plugins/pegasus-carousel` | master | 2 | 97b26c0 |
| 1 | `mabellas/public_html/wp-content/plugins/pegasus-slider` | master | 2 | 9183ef4 |
| 1 | `mabellas/public_html/wp-content/plugins/pegasus-wow` | master | 2 | e25ef14 |
| 1 | `mabellas/public_html/wp-content/plugins/wp-bootstrap-hooks` | master | 3 | de07965 |
| 1 | `mabellas/public_html/wp-content/themes/pegasus` | master | 8 | 6cd37a7 |
| 1 | `mamakay/public_html/wp-content/plugins/pegasus-carousel` | master | 2 | 97b26c0 |
| 1 | `mamakay/public_html/wp-content/plugins/pegasus-slider` | master | 2 | 9183ef4 |
| 1 | `mamakay/public_html/wp-content/plugins/pegasus-wow` | master | 2 | e25ef14 |
| 1 | `mamakay/public_html/wp-content/themes/pegasus` | master | 3 | 6cd37a7 |
| 1 | `mixmarket/public_html/wp-content/plugins/pegasus-carousel` | master | 2 | 97b26c0 |
| 1 | `mixmarket/public_html/wp-content/plugins/pegasus-slider` | master | 2 | 9183ef4 |
| 1 | `mixmarket/public_html/wp-content/plugins/pegasus-wow` | master | 2 | e25ef14 |
| 1 | `mixmarket/public_html/wp-content/plugins/wp-bootstrap-hooks` | master | 3 | de07965 |
| 1 | `mixmarket/public_html/wp-content/themes/pegasus` | master | 8 | 6cd37a7 |
| 1 | `organizepluscleaning/public_html/wp-content/plugins/pegasus-carousel` | master | 2 | 97b26c0 |
| 1 | `organizepluscleaning/public_html/wp-content/themes/pegasus` | master | 7 | 6cd37a7 |
| 1 | `osps26/public_html/wp-content/themes/pegasus` | master | 4 | 6cd37a7 |
| 1 | `ourpalsplace/public_html/wp-content/plugins/pegasus-accordion` | main | 4 | 02b47c7 |
| 1 | `ourpalsplace/public_html/wp-content/plugins/pegasus-carousel` | master | 5 | 97b26c0 |
| 1 | `ourpalsplace/public_html/wp-content/plugins/pegasus-popup` | master | 2 | 5f61576 |
| 1 | `ourpalsplace/public_html/wp-content/plugins/pegasus-slider` | master | 2 | 9183ef4 |
| 1 | `ourpalsplace/public_html/wp-content/plugins/pegasus-toggleslide` | master | 1 | 4f486d6 |
| 1 | `ourpalsplacedbt/public_html/wp-content/themes/pegasus` | master | 35 | 6cd37a7 |
| 1 | `outlawcoffee/public_html/wp-content/themes/pegasus` | master | 3 | 6cd37a7 |
| 1 | `pegasus/public_html/wp-content/plugins/pegasus-blog` | master | 2 | ddff9bc |
| 1 | `pegasus/public_html/wp-content/plugins/pegasus-carousel` | master | 5 | 97b26c0 |
| 1 | `pegasus/public_html/wp-content/plugins/pegasus-circle-progress` | master | 2 | bc7c565 |
| 1 | `pegasus/public_html/wp-content/plugins/pegasus-countup` | master | 2 | c18fbbd |
| 1 | `pegasus/public_html/wp-content/plugins/pegasus-masonry` | master | 3 | 0465acc |
| 1 | `pegasus/public_html/wp-content/plugins/pegasus-navmenu` | master | 2 | 3bdbf6c |
| 1 | `pegasus/public_html/wp-content/plugins/pegasus-onepage` | master | 4 | 6d66f9e |
| 1 | `pegasus/public_html/wp-content/plugins/pegasus-packery` | master | 4 | 997d815 |
| 1 | `pegasus/public_html/wp-content/plugins/pegasus-popup` | master | 2 | 5f61576 |
| 1 | `pegasus/public_html/wp-content/plugins/pegasus-postgrid` | master | 2 | 83d3f28 |
| 1 | `pegasus/public_html/wp-content/plugins/pegasus-slider` | master | 2 | 9183ef4 |
| 1 | `pegasus/public_html/wp-content/plugins/pegasus-toggleslide` | master | 1 | 4f486d6 |
| 1 | `pegasus/public_html/wp-content/plugins/pegasus-wow` | master | 2 | e25ef14 |
| 1 | `pegasus/public_html/wp-content/themes/pegasus` | master | 23 | 6cd37a7 |
| 1 | `pegasus/public_html/wp-content/themes/pegasus-child` | master | 6 | 7cf132f |
| 1 | `pegasustheme/public_html/wp-content/old_theme/pegasus` | master | 19 | 6cd37a7 |
| 1 | `pegasustheme/public_html/wp-content/plugins/pegasus-toggleslide` | master | 1 | 4f486d6 |
| 1 | `pegasustwo/public_html/wp-content/themes/pegasus` | master | 52 | 6cd37a7 |
| 1 | `qbiqcamp/public_html/wp-content/themes/pegasus` | master | 50 | 6cd37a7 |
| 1 | `qbiqsystem/public_html/wp-content/plugins/pegasus-carousel` | master | 2 | 97b26c0 |
| 1 | `qbiqsystem/public_html/wp-content/plugins/pegasus-slider` | master | 2 | 9183ef4 |
| 1 | `qbiqsystem/public_html/wp-content/plugins/pegasus-wow` | master | 2 | e25ef14 |
| 1 | `renecatherinedesign/public_html/wp-content/plugins/pegasus-carousel` | master | 2 | 97b26c0 |
| 1 | `renecatherinedesign/public_html/wp-content/plugins/pegasus-slider` | master | 2 | 9183ef4 |
| 1 | `renecatherinedesign/public_html/wp-content/plugins/pegasus-wow` | master | 2 | e25ef14 |
| 1 | `russelcontracting/public_html/wp-content/plugins/pegasus-carousel` | master | 2 | 97b26c0 |
| 1 | `russelcontracting/public_html/wp-content/plugins/pegasus-masonry` | master | 3 | 0465acc |
| 1 | `russelcontracting/public_html/wp-content/plugins/pegasus-slider` | master | 2 | 9183ef4 |
| 1 | `russelcontracting/public_html/wp-content/plugins/pegasus-wow` | master | 2 | e25ef14 |
| 1 | `russelcontracting/public_html/wp-content/themes/pegasus` | master | 3 | 6cd37a7 |
| 1 | `sagecnc/public_html/wp-content/plugins/pegasus-accordion` | main | 1 | 02b47c7 |
| 1 | `sagecnc/public_html/wp-content/plugins/pegasus-carousel` | master | 4 | 97b26c0 |
| 1 | `sagecnc/public_html/wp-content/themes/pegasus` | master | 19 | 6cd37a7 |
| 1 | `saltcellar/public_html/wp-content/plugins/pegasus-carousel` | master | 2 | 97b26c0 |
| 1 | `saltcellar/public_html/wp-content/plugins/pegasus-slider` | master | 2 | 9183ef4 |
| 1 | `saltcellar/public_html/wp-content/plugins/pegasus-wow` | master | 2 | e25ef14 |
| 1 | `saltcellar/public_html/wp-content/plugins/wp-bootstrap-hooks` | master | 3 | de07965 |
| 1 | `saltcellar/public_html/wp-content/themes/pegasus` | master | 8 | 6cd37a7 |
| 1 | `stoutbros/public_html/wp-content/plugins/pegasus-carousel` | master | 2 | 97b26c0 |
| 1 | `stoutbros/public_html/wp-content/plugins/pegasus-slider` | master | 2 | 9183ef4 |
| 1 | `stoutbros/public_html/wp-content/plugins/pegasus-wow` | master | 2 | e25ef14 |
| 1 | `stoutbros/public_html/wp-content/themes/pegasus` | master | 3 | 6cd37a7 |
| 1 | `sugarpeddler/public_html/wp-content/plugins/pegasus-carousel` | master | 2 | 97b26c0 |
| 1 | `sugarpeddler/public_html/wp-content/plugins/pegasus-slider` | master | 2 | 9183ef4 |
| 1 | `sugarpeddler/public_html/wp-content/plugins/pegasus-wow` | master | 2 | e25ef14 |
| 1 | `sugarpeddler/public_html/wp-content/themes/pegasus` | master | 2 | 6cd37a7 |
| 1 | `theloft/public_html/wp-content/themes/pegasus` | master | 52 | 6cd37a7 |
| 1 | `theloftnew/public_html/wp-content/plugins/pegasus-carousel` | master | 2 | 97b26c0 |
| 1 | `theloftnew/public_html/wp-content/plugins/pegasus-packery` | master | 4 | 997d815 |
| 1 | `theloftnew/public_html/wp-content/plugins/pegasus-slider` | master | 2 | 9183ef4 |
| 1 | `theloftnew/public_html/wp-content/plugins/pegasus-wow` | master | 2 | e25ef14 |
| 1 | `theloftnew/public_html/wp-content/themes/pegasus` | master | 8 | 6cd37a7 |
| 1 | `tommygs/public_html/wp-content/plugins/pegasus-carousel` | master | 2 | 97b26c0 |
| 1 | `tommygs/public_html/wp-content/plugins/pegasus-slider` | master | 2 | 9183ef4 |
| 1 | `tommygs/public_html/wp-content/plugins/pegasus-wow` | master | 2 | e25ef14 |
| 1 | `tommygs/public_html/wp-content/plugins/wp-bootstrap-hooks` | master | 3 | de07965 |
| 1 | `tommygs/public_html/wp-content/themes/pegasus` | master | 8 | 6cd37a7 |
| 1 | `ulgevents/public_html/wp-content/plugins/pegasus-carousel` | master | 2 | 97b26c0 |
| 1 | `ulgevents/public_html/wp-content/plugins/pegasus-slider` | master | 2 | 9183ef4 |
| 1 | `ulgevents/public_html/wp-content/plugins/pegasus-wow` | master | 2 | e25ef14 |
| 1 | `ulgevents/public_html/wp-content/plugins/wp-bootstrap-hooks` | master | 3 | de07965 |
| 1 | `ulgevents/public_html/wp-content/themes/pegasus` | master | 8 | 6cd37a7 |
| 1 | `uptownlifegroup/public_html/wp-content/plugins/pegasus-accordion` | main | 1 | 02b47c7 |
| 1 | `uptownlifegroup/public_html/wp-content/plugins/pegasus-carousel` | master | 2 | 97b26c0 |
| 1 | `uptownlifegroup/public_html/wp-content/plugins/pegasus-slider` | master | 2 | 9183ef4 |
| 1 | `uptownlifegroup/public_html/wp-content/plugins/pegasus-wow` | master | 2 | e25ef14 |
| 1 | `uptownlifegroup/public_html/wp-content/plugins/wp-bootstrap-hooks` | master | 3 | de07965 |
| 1 | `uptownlifegroup/public_html/wp-content/themes/pegasus` | master | 8 | 6cd37a7 |
| 1 | `valorcare/public_html/wp-content/plugins/pegasus-carousel` | master | 2 | 97b26c0 |
| 1 | `valorcare/public_html/wp-content/plugins/pegasus-slider` | master | 2 | 9183ef4 |
| 1 | `valorcare/public_html/wp-content/plugins/pegasus-wow` | master | 2 | e25ef14 |
| 1 | `valorcare/public_html/wp-content/themes/pegasus` | master | 3 | 6cd37a7 |
| 2 | `34oak/public_html/wp-content/themes/pegasus` | master | 1 | fbb24ef |
| 2 | `cadence-group/public_html/wp-content/themes/pegasus` | master | 1 | fbb24ef |
| 2 | `elliot/public_html/wp-content/themes/pegasus` | master | 1 | fbb24ef |
| 2 | `gentwo/public_html/wp-content/themes/pegasus` | master | 1 | fbb24ef |
| 2 | `iconic/public_html/wp-content/themes/pegasus` | master | 1 | fbb24ef |
| 2 | `mabellas/public_html/wp-content/themes/pegasus` | master | 1 | fbb24ef |
| 2 | `mamakay/public_html/wp-content/themes/pegasus` | master | 1 | fbb24ef |
| 2 | `mixmarket/public_html/wp-content/themes/pegasus` | master | 1 | fbb24ef |
| 2 | `organizepluscleaning/public_html/wp-content/themes/pegasus` | master | 1 | fbb24ef |
| 2 | `osps26/public_html/wp-content/themes/pegasus` | master | 1 | fbb24ef |
| 2 | `ourpalsplacedbt/public_html/wp-content/themes/pegasus` | master | 1 | fbb24ef |
| 2 | `outlawcoffee/public_html/wp-content/themes/pegasus` | master | 1 | fbb24ef |
| 2 | `pegasus/public_html/wp-content/themes/pegasus` | master | 1 | fbb24ef |
| 2 | `pegasustwo/public_html/wp-content/themes/pegasus` | master | 1 | fbb24ef |
| 2 | `qbiqcamp/public_html/wp-content/themes/pegasus` | master | 1 | fbb24ef |
| 2 | `qbiqsystem/public_html/wp-content/themes/pegasus` | master | 1 | fbb24ef |
| 2 | `renecatherinedesign/public_html/wp-content/themes/pegasus` | master | 1 | fbb24ef |
| 2 | `russelcontracting/public_html/wp-content/themes/pegasus` | master | 1 | fbb24ef |
| 2 | `sagecnc/public_html/wp-content/themes/pegasus` | master | 1 | fbb24ef |
| 2 | `saltcellar/public_html/wp-content/themes/pegasus` | master | 1 | fbb24ef |
| 2 | `stoutbros/public_html/wp-content/themes/pegasus` | master | 1 | fbb24ef |
| 2 | `sugarpeddler/public_html/wp-content/themes/pegasus` | master | 1 | fbb24ef |
| 2 | `theloft/public_html/wp-content/themes/pegasus` | master | 1 | fbb24ef |
| 2 | `theloftnew/public_html/wp-content/themes/pegasus` | master | 1 | fbb24ef |
| 2 | `tommygs/public_html/wp-content/themes/pegasus` | master | 1 | fbb24ef |
| 2 | `ulgevents/public_html/wp-content/themes/pegasus` | master | 1 | fbb24ef |
| 2 | `uptownlifegroup/public_html/wp-content/themes/pegasus` | master | 1 | fbb24ef |
| 2 | `valorcare/public_html/wp-content/themes/pegasus` | master | 1 | fbb24ef |
| 2 | `visionquest/public_html/wp-content/themes/pegasus` | master | 1 | fbb24ef |

## Archived old folders

| Original path | New path |
|---|---|
|---|---|
| www/cadence-group/public_html/wp-content/old_plugins | old-archive/cadence-group/old_plugins |
| www/ourpalsplacedbt/public_html/wp-content/old_plugins | old-archive/ourpalsplacedbt/old_plugins |
| www/ourpalsplacedbt/public_html/wp-content/old_theme | old-archive/ourpalsplacedbt/old_theme |
| www/outlawcoffee/public_html/wp-content/old_theme | old-archive/outlawcoffee/old_theme |
| www/pegasustheme/public_html/wp-content/old_theme | old-archive/pegasustheme/old_theme |
| www/sagecnc/public_html/wp-content/old_themes | old-archive/sagecnc/old_themes |
| www/vineandvision/public_html/wp-content/old_themes | old-archive/vineandvision/old_themes |
| www/ourpalsplacedbt/.../plugins/wp-bootstrap-hooks (benignware 1.1.21 backup) | old-archive/ourpalsplacedbt/wp-bootstrap-hooks-benignware-2026-10-12 |
| www/ourpalsplace/.../plugins/wp-bootstrap-hooks (benignware 1.1.21 backup) | old-archive/ourpalsplace/wp-bootstrap-hooks-benignware-2026-10-12 |
| www/qbiqcamp/.../plugins/wp-bootstrap-hooks (benignware 1.1.21 backup) | old-archive/qbiqcamp/wp-bootstrap-hooks-benignware-2026-10-12 |
| www/sagecnc/.../plugins/wp-bootstrap-hooks (benignware 1.1.21 backup) | old-archive/sagecnc/wp-bootstrap-hooks-benignware-2026-10-12 |
| www/vineandvision/.../plugins/wp-bootstrap-hooks (benignware 1.1.21 backup) | old-archive/vineandvision/wp-bootstrap-hooks-benignware-2026-10-12 |


## Conflict check (dirty pegasus copies vs upstream)

- **ricecapital pegasus:** local edits to `inc/theme-options.php`, `templates/header_one.php` and `templates/header_two.php` overlap upstream commits bf94ee7 and 6cd37a7. All three files still differ from upstream, so a pull would conflict and the edits need a manual merge.
- **pegasustheme pegasus:** local change to `css/header_five.css` does not overlap the upstream files. A stash, pull and pop would be clean.
- **hfhsga pegasus** and **34oak pegasus-packery:** no longer dirty. Jim committed fbb24ef from hfhsga, and 34oak packery is up to date at 997d815.

## Updated 2026-10-12, round 3 (pegasustheme.test)

- Switched the 12 plugins from their deleted PR branches to `master`, pulled with `--ff-only`, and removed each stale local branch with `git branch -d` (all were fully merged). pegasus-onepage uses `master` too: GitHub's default is master, and `develop` (Jan 2025) doesn't have the merged PR.
- pegasus theme: stash, pull to fbb24ef, and stash pop all ran cleanly. `css/header_five.css` is still modified locally.
- Smoke test: the home page and 17 demo pages return 200, with no PHP fatal errors and the plugin CSS/JS present. `/pegasus-post-grid/` and `/pegasus-accordion/` return 404 because no pages exist at those URLs (the demo page is `/pegasus-postgrid/`).

## Updated 2026-10-12, round 4 (pegasus parent theme 1a70b95)

- New commit: `1a70b95` "add external link to button in headers 1 and 2" (13:52). It changes `inc/theme-options.php`, `templates/header_one.php` and `templates/header_two.php`.
- Pulled 32 copies with `--ff-only`, 0 failures:
  - 31 clean copies on master.
  - pegasustheme via stash, pull and pop. The pop was clean, since the commit doesn't touch `css/header_five.css`, which is still modified.
  - ourpalsplace is included: Jim had already moved it from `ourpalsplaceopp_updates_2025` to master at 13:26, so it was clean on master.
- Already current: ricecapital. The commit was made from this copy. Jim stashed its local edits, pulled, and committed at 13:51, so the copy is clean. An older stash (`stash@{0}`, "WIP on master: c73426c") is still there, untouched.
- Skipped: vineandvision (not a git repo).

## Updated 2026-10-12, round 5 (re-cloned non-git and corrupt copies)

- Deleted and re-cloned 9 copies from Visionquest-Development on the default branch (master): outlawcoffee pegasus-slider; qbiqcamp pegasus-carousel, pegasus-onepage and pegasus-packery; vineandvision pegasus-callout, pegasus-wow and the pegasus theme; visionquest pegasus-carousel and pegasus-slider.
- Not re-cloned:
  - vineandvision pegasus-child: pegasus-child has no vineandvision branch, so cloning master would replace this site's custom child theme. Left in place for Jim to decide.
  - theloftnew pegasus-theloft: Visionquest-Development/pegasus-theloft does not exist on GitHub. Left in place.
- Smoke test: outlawcoffee.test, qbiqcamp.test, vineandvision.test and visionquest.test all return 200 with no PHP fatal errors.

## Updated 2026-10-12, round 6

- vineandvision pegasus-child:
  - Pushed the local theme to the new pegasus-child branch `vineandvision_theme` as `e6571c2` "vineandvision site theme (imported from local)". The branch starts from master.
  - A fresh clone of the branch was identical to the local folder (`diff -rq`). The folder was then replaced with that clone, on `vineandvision_theme` at e6571c2.
  - vineandvision.test returns 200 with no fatal errors, and the child `style.css` is present.
- pegasus theme commit `05e1222` "add update for page wrap on header5":
  - Jim committed it from pegasustheme, so that copy is clean and current with no stash needed.
  - Pulled 32 other copies with `--ff-only`, 0 failures.
  - Full pass over all components: nothing else was behind.
  - Skipped 8 dirty copies (pegasus-child) and 22 off-default copies (pegasus-child site branches).

## Updated 2026-10-12, round 7 (3:29 PM)

- Fetched all 34 git copies of the pegasus theme. GitHub has no commit newer than `05e1222` (2:01 PM) on any branch, and every copy is already at 05e1222, clean, with nothing unpushed.
- Pulled 0, failed 0, skipped 0. vineandvision was re-cloned as a git repo in round 5.

## Updated 2026-10-13, round 8 (2:47 PM, after the SiteGround RSA deploy fix)

- Scope: every pegasus theme, child and plugin copy, 188 in all. Plugins and the parent theme were pulled on their GitHub default branch. pegasus-child was pulled on its site branch, provided that branch exists on origin.
- Method: `git fetch`, then `git pull --ff-only`. Nothing was stashed, reset or switched. Log: `pull-log-2026-10-13.txt`.
- **Pulled 175 copies, 0 ff failures:**
  - The pegasus parent theme, 05e1222..3ec9e66, on all 34 sites.
  - Plugins: 9 new commits each, ending in the RSA fingerprint commit.
  - pegasus-child: the master copies (iconic, mamakay, pegasus) went 7cf132f..9e3b058, and 18 site branches got their deploy-workflow commits.
- **Already current (1):** outlawcoffee pegasus-child (outlaw_coffee_theme, 1876ba4).
- **Skipped (12):**
  - Uncommitted changes: 34oak (7 files), gentwo (1), organizepluscleaning (1), ourpalsplace (7), renecatherinedesign (4). All are pegasus-child.
  - Local branch not on origin: hfhsga `hfhs-windows-doors-testimonials`, ourpalsplacedbt `opp-dbt-site`, theloft `theloft`.
  - No upstream tracking (origin/<branch> not fetched): elliot `elliotint_theme`, stoutbros `stoutbros_theme`, valorcare `valorcare_theme`.
  - Not a git repo: theloftnew pegasus-theloft.
- Refreshed `repo-status-pegasus-2026-10-12.json` (scan_date 2026-10-13) and `repo-status.json` (`check-repo-status.sh`: 264 repos, 233 clean, 31 with issues). The full table below has not been regenerated; the JSON is current.

## Updated 2026-10-13, full rescan (4:00 PM)

- Fresh `git fetch` of all 225 copies, using `sync/pegasus.sh status` (sync/lib/rescan_status.py). This regenerated the JSON, the CSV and the full table below, and added commit, commit date and origin-head columns.
- pegasus-child site branches now get their own status instead of the single "Off main (expected)" label.

## Updated 2026-10-14 (4:31 PM): rescan bug fixed

- Bug: `sync/pegasus.sh status` (sync/lib/rescan_status.py) read upstream state through `@{u}` and `origin/<branch>`. elliot, stoutbros, valorcare and renecatherinedesign are single-branch clones: their `remote.origin.fetch` maps only master. In those clones `@{u}` fails ("not stored as a remote-tracking branch"), and `git fetch` never updates `origin/<branch>`. They were wrongly reported as having no upstream.
- Fix: the script now reads `branch.<b>.merge` and fetches `+refs/heads/<b>:refs/remotes/origin/<b>` explicitly before comparing. A branch that is truly not on origin is reported with the origin branches that contain its HEAD.
- 34oak, gentwo and organizepluscleaning are clean and current; the 2026-10-13 snapshot was simply stale.
- valorcare was clean and 1 behind, so it was pulled with `--ff-only` from 3d4a504 to 8c8c0c6.


## Full table (by site)

### 34oak

| Component | Path | Remote | Branch | Upstream | Commit | Commit date | Origin | Ahead/Behind | Dirty | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| pegasus-carousel | `wp-content/plugins/pegasus-carousel` | Visionquest-Development/pegasus-carousel.git | master | origin/master | `586bc7a` | 2026-10-13 13:51 | `586bc7a` | 0/0 | 0 | Up to date |
| pegasus-masonry | `wp-content/plugins/pegasus-masonry` | Visionquest-Development/pegasus-masonry.git | master | origin/master | `e990597` | 2026-10-13 13:51 | `e990597` | 0/0 | 0 | Up to date |
| pegasus-packery | `wp-content/plugins/pegasus-packery` | Visionquest-Development/pegasus-packery.git | master | origin/master | `a88aae3` | 2026-10-13 13:51 | `a88aae3` | 0/0 | 0 | Up to date |
| pegasus-slider | `wp-content/plugins/pegasus-slider` | Visionquest-Development/pegasus-slider.git | master | origin/master | `e53d764` | 2026-10-13 13:51 | `e53d764` | 0/0 | 0 | Up to date |
| pegasus-wow | `wp-content/plugins/pegasus-wow` | Visionquest-Development/pegasus-wow.git | master | origin/master | `84305b5` | 2026-10-13 13:51 | `84305b5` | 0/0 | 0 | Up to date |
| wp-bootstrap-hooks | `wp-content/plugins/wp-bootstrap-hooks` | jimboobrien/wp-bootstrap-hooks.git | master | origin/master | `de07965` | 2026-03-04 23:14 | `de07965` | 0/0 | 0 | Up to date |
| pegasus | `wp-content/themes/pegasus` | Visionquest-Development/pegasus.git | master | origin/master | `3ec9e66` | 2026-10-13 13:47 | `3ec9e66` | 0/0 | 0 | Up to date |
| pegasus-child | `wp-content/themes/pegasus-child` | Visionquest-Development/pegasus-child.git | 34oak_theme | origin/34oak_theme | `73a28f1` | 2026-10-13 12:52 | `73a28f1` | 0/0 | 0 | Site branch: up to date |

### cadence-group

| Component | Path | Remote | Branch | Upstream | Commit | Commit date | Origin | Ahead/Behind | Dirty | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| pegasus-accordion | `wp-content/plugins/pegasus-accordion` | Visionquest-Development/pegasus-accordion.git | main | origin/main | `01841eb` | 2026-10-13 13:50 | `01841eb` | 0/0 | 0 | Up to date |
| pegasus-carousel | `wp-content/plugins/pegasus-carousel` | Visionquest-Development/pegasus-carousel.git | master | origin/master | `586bc7a` | 2026-10-13 13:51 | `586bc7a` | 0/0 | 0 | Up to date |
| pegasus-postgrid | `wp-content/plugins/pegasus-postgrid` | Visionquest-Development/pegasus-postgrid.git | master | origin/master | `bb7e16c` | 2026-10-13 13:51 | `bb7e16c` | 0/0 | 0 | Up to date |
| pegasus-slider | `wp-content/plugins/pegasus-slider` | Visionquest-Development/pegasus-slider.git | master | origin/master | `e53d764` | 2026-10-13 13:51 | `e53d764` | 0/0 | 0 | Up to date |
| pegasus-tabs | `wp-content/plugins/pegasus-tabs` | Visionquest-Development/pegasus-tabs.git | master | origin/master | `ca26dd5` | 2026-10-13 13:51 | `ca26dd5` | 0/0 | 0 | Up to date |
| wp-bootstrap-hooks | `wp-content/plugins/wp-bootstrap-hooks` | jimboobrien/wp-bootstrap-hooks.git | master | origin/master | `de07965` | 2026-03-04 23:14 | `de07965` | 0/0 | 0 | Up to date |
| pegasus | `wp-content/themes/pegasus` | Visionquest-Development/pegasus.git | master | origin/master | `3ec9e66` | 2026-10-13 13:47 | `3ec9e66` | 0/0 | 0 | Up to date |
| pegasus-child | `wp-content/themes/pegasus-child` | Visionquest-Development/pegasus-child.git | cadence_group_theme | origin/cadence_group_theme | `2b715e8` | 2026-10-13 12:52 | `2b715e8` | 0/0 | 0 | Site branch: up to date |

### elliot

| Component | Path | Remote | Branch | Upstream | Commit | Commit date | Origin | Ahead/Behind | Dirty | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| pegasus-carousel | `wp-content/plugins/pegasus-carousel` | Visionquest-Development/pegasus-carousel.git | master | origin/master | `586bc7a` | 2026-10-13 13:51 | `586bc7a` | 0/0 | 0 | Up to date |
| pegasus-slider | `wp-content/plugins/pegasus-slider` | Visionquest-Development/pegasus-slider.git | master | origin/master | `e53d764` | 2026-10-13 13:51 | `e53d764` | 0/0 | 0 | Up to date |
| pegasus-wow | `wp-content/plugins/pegasus-wow` | Visionquest-Development/pegasus-wow.git | master | origin/master | `84305b5` | 2026-10-13 13:51 | `84305b5` | 0/0 | 0 | Up to date |
| wp-bootstrap-hooks | `wp-content/plugins/wp-bootstrap-hooks` | jimboobrien/wp-bootstrap-hooks.git | master | origin/master | `de07965` | 2026-03-04 23:14 | `de07965` | 0/0 | 0 | Up to date |
| pegasus | `wp-content/themes/pegasus` | Visionquest-Development/pegasus.git | master | origin/master | `3ec9e66` | 2026-10-13 13:47 | `3ec9e66` | 0/0 | 0 | Up to date |
| pegasus-child | `wp-content/themes/pegasus-child` | Visionquest-Development/pegasus-child.git | elliotint_theme | origin/elliotint_theme | `fb05e74` | 2026-08-17 16:17 | `fb05e74` | 0/0 | 0 | Site branch: up to date |

### gentwo

| Component | Path | Remote | Branch | Upstream | Commit | Commit date | Origin | Ahead/Behind | Dirty | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| pegasus-carousel | `wp-content/plugins/pegasus-carousel` | Visionquest-Development/pegasus-carousel.git | master | origin/master | `586bc7a` | 2026-10-13 13:51 | `586bc7a` | 0/0 | 0 | Up to date |
| pegasus-slider | `wp-content/plugins/pegasus-slider` | Visionquest-Development/pegasus-slider.git | master | origin/master | `e53d764` | 2026-10-13 13:51 | `e53d764` | 0/0 | 0 | Up to date |
| pegasus-wow | `wp-content/plugins/pegasus-wow` | Visionquest-Development/pegasus-wow.git | master | origin/master | `84305b5` | 2026-10-13 13:51 | `84305b5` | 0/0 | 0 | Up to date |
| wp-bootstrap-hooks | `wp-content/plugins/wp-bootstrap-hooks` | jimboobrien/wp-bootstrap-hooks.git | master | origin/master | `de07965` | 2026-03-04 23:14 | `de07965` | 0/0 | 0 | Up to date |
| pegasus | `wp-content/themes/pegasus` | Visionquest-Development/pegasus.git | master | origin/master | `3ec9e66` | 2026-10-13 13:47 | `3ec9e66` | 0/0 | 0 | Up to date |
| pegasus-child | `wp-content/themes/pegasus-child` | Visionquest-Development/pegasus-child.git | gentwo_theme | origin/gentwo_theme | `44ae05f` | 2026-10-14 12:31 | `44ae05f` | 0/0 | 0 | Site branch: up to date |

### hfhsga

| Component | Path | Remote | Branch | Upstream | Commit | Commit date | Origin | Ahead/Behind | Dirty | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| pegasus-accordion | `wp-content/plugins/pegasus-accordion` | Visionquest-Development/pegasus-accordion.git | main | origin/main | `01841eb` | 2026-10-13 13:50 | `01841eb` | 0/0 | 0 | Up to date |
| pegasus-carousel | `wp-content/plugins/pegasus-carousel` | Visionquest-Development/pegasus-carousel.git | master | origin/master | `586bc7a` | 2026-10-13 13:51 | `586bc7a` | 0/0 | 0 | Up to date |
| pegasus-slider | `wp-content/plugins/pegasus-slider` | Visionquest-Development/pegasus-slider.git | master | origin/master | `e53d764` | 2026-10-13 13:51 | `e53d764` | 0/0 | 0 | Up to date |
| pegasus-wow | `wp-content/plugins/pegasus-wow` | Visionquest-Development/pegasus-wow.git | master | origin/master | `84305b5` | 2026-10-13 13:51 | `84305b5` | 0/0 | 0 | Up to date |
| wp-bootstrap-hooks | `wp-content/plugins/wp-bootstrap-hooks` | jimboobrien/wp-bootstrap-hooks.git | master | origin/master | `de07965` | 2026-03-04 23:14 | `de07965` | 0/0 | 0 | Up to date |
| pegasus | `wp-content/themes/pegasus` | Visionquest-Development/pegasus.git | master | origin/master | `3ec9e66` | 2026-10-13 13:47 | `3ec9e66` | 0/0 | 0 | Up to date |
| pegasus-child | `wp-content/themes/pegasus-child` | Visionquest-Development/pegasus-child.git | hfhsga_theme | origin/hfhsga_theme | `9470661` | 2026-09-23 19:42 | `3e0ac2a` | 0/1 | 15 | Site branch: needs pull |

### iconic

| Component | Path | Remote | Branch | Upstream | Commit | Commit date | Origin | Ahead/Behind | Dirty | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| pegasus-carousel | `wp-content/plugins/pegasus-carousel` | Visionquest-Development/pegasus-carousel.git | master | origin/master | `586bc7a` | 2026-10-13 13:51 | `586bc7a` | 0/0 | 0 | Up to date |
| pegasus-slider | `wp-content/plugins/pegasus-slider` | Visionquest-Development/pegasus-slider.git | master | origin/master | `e53d764` | 2026-10-13 13:51 | `e53d764` | 0/0 | 0 | Up to date |
| pegasus-wow | `wp-content/plugins/pegasus-wow` | Visionquest-Development/pegasus-wow.git | master | origin/master | `84305b5` | 2026-10-13 13:51 | `84305b5` | 0/0 | 0 | Up to date |
| wp-bootstrap-hooks | `wp-content/plugins/wp-bootstrap-hooks` | jimboobrien/wp-bootstrap-hooks.git | master | origin/master | `de07965` | 2026-03-04 23:14 | `de07965` | 0/0 | 0 | Up to date |
| pegasus | `wp-content/themes/pegasus` | Visionquest-Development/pegasus.git | master | origin/master | `3ec9e66` | 2026-10-13 13:47 | `3ec9e66` | 0/0 | 0 | Up to date |
| pegasus-child | `wp-content/themes/pegasus-child` | Visionquest-Development/pegasus-child.git | master | origin/master | `9e3b058` | 2026-10-13 13:47 | `9e3b058` | 0/0 | 0 | Up to date |

### mabellas

| Component | Path | Remote | Branch | Upstream | Commit | Commit date | Origin | Ahead/Behind | Dirty | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| pegasus-carousel | `wp-content/plugins/pegasus-carousel` | Visionquest-Development/pegasus-carousel.git | master | origin/master | `586bc7a` | 2026-10-13 13:51 | `586bc7a` | 0/0 | 0 | Up to date |
| pegasus-slider | `wp-content/plugins/pegasus-slider` | Visionquest-Development/pegasus-slider.git | master | origin/master | `e53d764` | 2026-10-13 13:51 | `e53d764` | 0/0 | 0 | Up to date |
| pegasus-wow | `wp-content/plugins/pegasus-wow` | Visionquest-Development/pegasus-wow.git | master | origin/master | `84305b5` | 2026-10-13 13:51 | `84305b5` | 0/0 | 0 | Up to date |
| vqdev-toast | `wp-content/plugins/vqdev-toast` | Visionquest-Development/vqdev-toast.git | main | origin/main | `b7f7eac` | 2026-05-21 22:06 | `b7f7eac` | 0/0 | 0 | Up to date |
| wp-bootstrap-hooks | `wp-content/plugins/wp-bootstrap-hooks` | jimboobrien/wp-bootstrap-hooks.git | master | origin/master | `de07965` | 2026-03-04 23:14 | `de07965` | 0/0 | 0 | Up to date |
| pegasus | `wp-content/themes/pegasus` | Visionquest-Development/pegasus.git | master | origin/master | `3ec9e66` | 2026-10-13 13:47 | `3ec9e66` | 0/0 | 0 | Up to date |
| pegasus-child | `wp-content/themes/pegasus-child` | Visionquest-Development/pegasus-child.git | mabellas_theme | origin/mabellas_theme | `ba86e3c` | 2026-10-13 12:52 | `ba86e3c` | 0/0 | 0 | Site branch: up to date |

### mamakay

| Component | Path | Remote | Branch | Upstream | Commit | Commit date | Origin | Ahead/Behind | Dirty | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| pegasus-carousel | `wp-content/plugins/pegasus-carousel` | Visionquest-Development/pegasus-carousel.git | master | origin/master | `586bc7a` | 2026-10-13 13:51 | `586bc7a` | 0/0 | 0 | Up to date |
| pegasus-slider | `wp-content/plugins/pegasus-slider` | Visionquest-Development/pegasus-slider.git | master | origin/master | `e53d764` | 2026-10-13 13:51 | `e53d764` | 0/0 | 0 | Up to date |
| pegasus-wow | `wp-content/plugins/pegasus-wow` | Visionquest-Development/pegasus-wow.git | master | origin/master | `84305b5` | 2026-10-13 13:51 | `84305b5` | 0/0 | 0 | Up to date |
| wp-bootstrap-hooks | `wp-content/plugins/wp-bootstrap-hooks` | jimboobrien/wp-bootstrap-hooks.git | master | origin/master | `de07965` | 2026-03-04 23:14 | `de07965` | 0/0 | 0 | Up to date |
| pegasus | `wp-content/themes/pegasus` | Visionquest-Development/pegasus.git | master | origin/master | `3ec9e66` | 2026-10-13 13:47 | `3ec9e66` | 0/0 | 0 | Up to date |
| pegasus-child | `wp-content/themes/pegasus-child` | Visionquest-Development/pegasus-child.git | master | origin/master | `9e3b058` | 2026-10-13 13:47 | `9e3b058` | 0/0 | 0 | Up to date |

### mixmarket

| Component | Path | Remote | Branch | Upstream | Commit | Commit date | Origin | Ahead/Behind | Dirty | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| pegasus-carousel | `wp-content/plugins/pegasus-carousel` | Visionquest-Development/pegasus-carousel.git | master | origin/master | `586bc7a` | 2026-10-13 13:51 | `586bc7a` | 0/0 | 0 | Up to date |
| pegasus-slider | `wp-content/plugins/pegasus-slider` | Visionquest-Development/pegasus-slider.git | master | origin/master | `e53d764` | 2026-10-13 13:51 | `e53d764` | 0/0 | 0 | Up to date |
| pegasus-wow | `wp-content/plugins/pegasus-wow` | Visionquest-Development/pegasus-wow.git | master | origin/master | `84305b5` | 2026-10-13 13:51 | `84305b5` | 0/0 | 0 | Up to date |
| vqdev-toast | `wp-content/plugins/vqdev-toast` | Visionquest-Development/vqdev-toast.git | main | origin/main | `b7f7eac` | 2026-05-21 22:06 | `b7f7eac` | 0/0 | 0 | Up to date |
| wp-bootstrap-hooks | `wp-content/plugins/wp-bootstrap-hooks` | jimboobrien/wp-bootstrap-hooks.git | master | origin/master | `de07965` | 2026-03-04 23:14 | `de07965` | 0/0 | 0 | Up to date |
| pegasus | `wp-content/themes/pegasus` | Visionquest-Development/pegasus.git | master | origin/master | `3ec9e66` | 2026-10-13 13:47 | `3ec9e66` | 0/0 | 0 | Up to date |
| pegasus-child | `wp-content/themes/pegasus-child` | Visionquest-Development/pegasus-child.git | mixmarket_theme | origin/mixmarket_theme | `b974e3b` | 2026-10-13 12:52 | `b974e3b` | 0/0 | 0 | Site branch: up to date |

### organizepluscleaning

| Component | Path | Remote | Branch | Upstream | Commit | Commit date | Origin | Ahead/Behind | Dirty | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| pegasus-carousel | `wp-content/plugins/pegasus-carousel` | Visionquest-Development/pegasus-carousel.git | master | origin/master | `586bc7a` | 2026-10-13 13:51 | `586bc7a` | 0/0 | 0 | Up to date |
| wp-bootstrap-hooks | `wp-content/plugins/wp-bootstrap-hooks` | jimboobrien/wp-bootstrap-hooks.git | master | origin/master | `de07965` | 2026-03-04 23:14 | `de07965` | 0/0 | 0 | Up to date |
| pegasus | `wp-content/themes/pegasus` | Visionquest-Development/pegasus.git | master | origin/master | `3ec9e66` | 2026-10-13 13:47 | `3ec9e66` | 0/0 | 0 | Up to date |
| pegasus-child | `wp-content/themes/pegasus-child` | Visionquest-Development/pegasus-child.git | organizepluscleaning | origin/organizepluscleaning | `0921db5` | 2026-10-14 12:34 | `0921db5` | 0/0 | 0 | Site branch: up to date |

### osps26

| Component | Path | Remote | Branch | Upstream | Commit | Commit date | Origin | Ahead/Behind | Dirty | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| wp-bootstrap-hooks | `wp-content/plugins/wp-bootstrap-hooks` | jimboobrien/wp-bootstrap-hooks.git | master | origin/master | `de07965` | 2026-03-04 23:14 | `de07965` | 0/0 | 0 | Up to date |
| pegasus | `wp-content/themes/pegasus` | Visionquest-Development/pegasus.git | master | origin/master | `3ec9e66` | 2026-10-13 13:47 | `3ec9e66` | 0/0 | 0 | Up to date |
| pegasus-child | `wp-content/themes/pegasus-child` | Visionquest-Development/pegasus-child.git | osps26_theme | origin/osps26_theme | `49d519a` | 2026-10-13 12:52 | `49d519a` | 0/0 | 0 | Site branch: up to date |

### ourpalsplace

| Component | Path | Remote | Branch | Upstream | Commit | Commit date | Origin | Ahead/Behind | Dirty | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| pegasus-accordion | `wp-content/plugins/pegasus-accordion` | Visionquest-Development/pegasus-accordion.git | main | origin/main | `01841eb` | 2026-10-13 13:50 | `01841eb` | 0/0 | 0 | Up to date |
| pegasus-carousel | `wp-content/plugins/pegasus-carousel` | Visionquest-Development/pegasus-carousel.git | master | origin/master | `586bc7a` | 2026-10-13 13:51 | `586bc7a` | 0/0 | 0 | Up to date |
| pegasus-popup | `wp-content/plugins/pegasus-popup` | Visionquest-Development/pegasus-popup.git | master | origin/master | `a623c9b` | 2026-10-13 13:51 | `a623c9b` | 0/0 | 0 | Up to date |
| pegasus-slider | `wp-content/plugins/pegasus-slider` | Visionquest-Development/pegasus-slider.git | master | origin/master | `e53d764` | 2026-10-13 13:51 | `e53d764` | 0/0 | 0 | Up to date |
| pegasus-toggleslide | `wp-content/plugins/pegasus-toggleslide` | Visionquest-Development/pegasus-toggleslide.git | master | origin/master | `8fce927` | 2026-10-13 13:51 | `8fce927` | 0/0 | 0 | Up to date |
| wp-bootstrap-hooks | `wp-content/plugins/wp-bootstrap-hooks` | jimboobrien/wp-bootstrap-hooks.git | master | origin/master | `de07965` | 2026-03-04 23:14 | `de07965` | 0/0 | 0 | Up to date |
| pegasus | `wp-content/themes/pegasus` | Visionquest-Development/pegasus.git | master | origin/master | `3ec9e66` | 2026-10-13 13:47 | `3ec9e66` | 0/0 | 0 | Up to date |
| pegasus-child | `wp-content/themes/pegasus-child` | Visionquest-Development/pegasus-child.git | opp_new_site | origin/opp_new_site | `79a76a6` | 2026-10-14 14:33 | `0c09924` | 1/5 | 18 | Site branch: needs pull |

### ourpalsplacedbt

| Component | Path | Remote | Branch | Upstream | Commit | Commit date | Origin | Ahead/Behind | Dirty | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| wp-bootstrap-hooks | `wp-content/plugins/wp-bootstrap-hooks` | jimboobrien/wp-bootstrap-hooks.git | master | origin/master | `de07965` | 2026-03-04 23:14 | `de07965` | 0/0 | 0 | Up to date |
| pegasus | `wp-content/themes/pegasus` | Visionquest-Development/pegasus.git | master | origin/master | `3ec9e66` | 2026-10-13 13:47 | `3ec9e66` | 0/0 | 0 | Up to date |
| pegasus-child | `wp-content/themes/pegasus-child` | Visionquest-Development/pegasus-child.git | opp-dbt-site |  | `825fab6` | 2024-12-17 00:10 | `` | ?/? | 2 | Site branch: not on origin (HEAD is a shared commit in 29 origin branches) |

### outlawcoffee

| Component | Path | Remote | Branch | Upstream | Commit | Commit date | Origin | Ahead/Behind | Dirty | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| pegasus-slider | `wp-content/plugins/pegasus-slider` | Visionquest-Development/pegasus-slider.git | master | origin/master | `e53d764` | 2026-10-13 13:51 | `e53d764` | 0/0 | 0 | Up to date |
| wp-bootstrap-hooks | `wp-content/plugins/wp-bootstrap-hooks` | jimboobrien/wp-bootstrap-hooks.git | master | origin/master | `de07965` | 2026-03-04 23:14 | `de07965` | 0/0 | 0 | Up to date |
| pegasus | `wp-content/themes/pegasus` | Visionquest-Development/pegasus.git | master | origin/master | `3ec9e66` | 2026-10-13 13:47 | `3ec9e66` | 0/0 | 0 | Up to date |
| pegasus-child | `wp-content/themes/pegasus-child` | Visionquest-Development/pegasus-child.git | outlaw_coffee_theme | origin/outlaw_coffee_theme | `1876ba4` | 2026-08-03 23:29 | `1876ba4` | 0/0 | 0 | Site branch: up to date |

### pegasus

| Component | Path | Remote | Branch | Upstream | Commit | Commit date | Origin | Ahead/Behind | Dirty | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| pegasus-blog | `wp-content/plugins/pegasus-blog` | https://github.com/Visionquest-Development/pegasus-blog | master | origin/master | `4db9f03` | 2026-10-13 13:50 | `4db9f03` | 0/0 | 0 | Up to date |
| pegasus-callout | `wp-content/plugins/pegasus-callout` | https://github.com/Visionquest-Development/pegasus-callout | master | origin/master | `bc4c766` | 2026-10-13 13:51 | `bc4c766` | 0/0 | 0 | Up to date |
| pegasus-carousel | `wp-content/plugins/pegasus-carousel` | https://github.com/Visionquest-Development/pegasus-carousel | master | origin/master | `586bc7a` | 2026-10-13 13:51 | `586bc7a` | 0/0 | 0 | Up to date |
| pegasus-circle-progress | `wp-content/plugins/pegasus-circle-progress` | https://github.com/Visionquest-Development/pegasus-circle-progress | master | origin/master | `b942b9d` | 2026-10-13 13:51 | `b942b9d` | 0/0 | 0 | Up to date |
| pegasus-countup | `wp-content/plugins/pegasus-countup` | https://github.com/Visionquest-Development/pegasus-countup | master | origin/master | `59fcca1` | 2026-10-13 13:51 | `59fcca1` | 0/0 | 0 | Up to date |
| pegasus-masonry | `wp-content/plugins/pegasus-masonry` | https://github.com/Visionquest-Development/pegasus-masonry | master | origin/master | `e990597` | 2026-10-13 13:51 | `e990597` | 0/0 | 0 | Up to date |
| pegasus-navmenu | `wp-content/plugins/pegasus-navmenu` | https://github.com/Visionquest-Development/pegasus-navmenu | master | origin/master | `3854128` | 2026-10-13 13:51 | `3854128` | 0/0 | 0 | Up to date |
| pegasus-onepage | `wp-content/plugins/pegasus-onepage` | https://github.com/Visionquest-Development/pegasus-onepage | master | origin/master | `66a5367` | 2026-10-13 13:51 | `66a5367` | 0/0 | 0 | Up to date |
| pegasus-packery | `wp-content/plugins/pegasus-packery` | https://github.com/Visionquest-Development/pegasus-packery | master | origin/master | `a88aae3` | 2026-10-13 13:51 | `a88aae3` | 0/0 | 0 | Up to date |
| pegasus-popup | `wp-content/plugins/pegasus-popup` | https://github.com/Visionquest-Development/pegasus-popup | master | origin/master | `a623c9b` | 2026-10-13 13:51 | `a623c9b` | 0/0 | 0 | Up to date |
| pegasus-postgrid | `wp-content/plugins/pegasus-postgrid` | https://github.com/Visionquest-Development/pegasus-postgrid | master | origin/master | `bb7e16c` | 2026-10-13 13:51 | `bb7e16c` | 0/0 | 0 | Up to date |
| pegasus-posts-filter | `wp-content/plugins/pegasus-posts-filter` | https://github.com/Visionquest-Development/pegasus-posts-filter | master | origin/master | `b3f8c72` | 2026-10-13 13:51 | `b3f8c72` | 0/0 | 0 | Up to date |
| pegasus-slider | `wp-content/plugins/pegasus-slider` | https://github.com/Visionquest-Development/pegasus-slider | master | origin/master | `e53d764` | 2026-10-13 13:51 | `e53d764` | 0/0 | 0 | Up to date |
| pegasus-tabs | `wp-content/plugins/pegasus-tabs` | https://github.com/Visionquest-Development/pegasus-tabs | master | origin/master | `ca26dd5` | 2026-10-13 13:51 | `ca26dd5` | 0/0 | 0 | Up to date |
| pegasus-toggleslide | `wp-content/plugins/pegasus-toggleslide` | https://github.com/Visionquest-Development/pegasus-toggleslide | master | origin/master | `8fce927` | 2026-10-13 13:51 | `8fce927` | 0/0 | 0 | Up to date |
| pegasus-wow | `wp-content/plugins/pegasus-wow` | https://github.com/Visionquest-Development/pegasus-wow | master | origin/master | `84305b5` | 2026-10-13 13:51 | `84305b5` | 0/0 | 0 | Up to date |
| pegasus | `wp-content/themes/pegasus` | Visionquest-Development/pegasus.git | master | origin/master | `3ec9e66` | 2026-10-13 13:47 | `3ec9e66` | 0/0 | 0 | Up to date |
| pegasus-child | `wp-content/themes/pegasus-child` | Visionquest-Development/pegasus-child.git | master | origin/master | `9e3b058` | 2026-10-13 13:47 | `9e3b058` | 0/0 | 0 | Up to date |

### pegasustheme

| Component | Path | Remote | Branch | Upstream | Commit | Commit date | Origin | Ahead/Behind | Dirty | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| pegasus-blog | `wp-content/plugins/pegasus-blog` | Visionquest-Development/pegasus-blog.git | master | origin/master | `4db9f03` | 2026-10-13 13:50 | `4db9f03` | 0/0 | 0 | Up to date |
| pegasus-callout | `wp-content/plugins/pegasus-callout` | Visionquest-Development/pegasus-callout.git | master | origin/master | `bc4c766` | 2026-10-13 13:51 | `bc4c766` | 0/0 | 0 | Up to date |
| pegasus-carousel | `wp-content/plugins/pegasus-carousel` | Visionquest-Development/pegasus-carousel.git | master | origin/master | `586bc7a` | 2026-10-13 13:51 | `586bc7a` | 0/0 | 0 | Up to date |
| pegasus-circle-progress | `wp-content/plugins/pegasus-circle-progress` | Visionquest-Development/pegasus-circle-progress.git | master | origin/master | `b942b9d` | 2026-10-13 13:51 | `b942b9d` | 0/0 | 0 | Up to date |
| pegasus-countup | `wp-content/plugins/pegasus-countup` | Visionquest-Development/pegasus-countup.git | master | origin/master | `59fcca1` | 2026-10-13 13:51 | `59fcca1` | 0/0 | 0 | Up to date |
| pegasus-masonry | `wp-content/plugins/pegasus-masonry` | Visionquest-Development/pegasus-masonry.git | master | origin/master | `e990597` | 2026-10-13 13:51 | `e990597` | 0/0 | 0 | Up to date |
| pegasus-navmenu | `wp-content/plugins/pegasus-navmenu` | Visionquest-Development/pegasus-navmenu.git | master | origin/master | `3854128` | 2026-10-13 13:51 | `3854128` | 0/0 | 0 | Up to date |
| pegasus-onepage | `wp-content/plugins/pegasus-onepage` | Visionquest-Development/pegasus-onepage.git | master | origin/master | `66a5367` | 2026-10-13 13:51 | `66a5367` | 0/0 | 0 | Up to date |
| pegasus-packery | `wp-content/plugins/pegasus-packery` | Visionquest-Development/pegasus-packery.git | master | origin/master | `a88aae3` | 2026-10-13 13:51 | `a88aae3` | 0/0 | 0 | Up to date |
| pegasus-popup | `wp-content/plugins/pegasus-popup` | Visionquest-Development/pegasus-popup.git | master | origin/master | `a623c9b` | 2026-10-13 13:51 | `a623c9b` | 0/0 | 0 | Up to date |
| pegasus-post-grid | `wp-content/plugins/pegasus-post-grid` | Visionquest-Development/pegasus-postgrid.git | master | origin/master | `bb7e16c` | 2026-10-13 13:51 | `bb7e16c` | 0/0 | 0 | Up to date |
| pegasus-posts-filter | `wp-content/plugins/pegasus-posts-filter` | Visionquest-Development/pegasus-posts-filter.git | master | origin/master | `b3f8c72` | 2026-10-13 13:51 | `b3f8c72` | 0/0 | 0 | Up to date |
| pegasus-slider | `wp-content/plugins/pegasus-slider` | Visionquest-Development/pegasus-slider.git | master | origin/master | `e53d764` | 2026-10-13 13:51 | `e53d764` | 0/0 | 0 | Up to date |
| pegasus-tabs | `wp-content/plugins/pegasus-tabs` | Visionquest-Development/pegasus-tabs.git | master | origin/master | `ca26dd5` | 2026-10-13 13:51 | `ca26dd5` | 0/0 | 0 | Up to date |
| pegasus-toggleslide | `wp-content/plugins/pegasus-toggleslide` | Visionquest-Development/pegasus-toggleslide.git | master | origin/master | `8fce927` | 2026-10-13 13:51 | `8fce927` | 0/0 | 0 | Up to date |
| pegasus-wow | `wp-content/plugins/pegasus-wow` | Visionquest-Development/pegasus-wow.git | master | origin/master | `84305b5` | 2026-10-13 13:51 | `84305b5` | 0/0 | 0 | Up to date |
| wp-bootstrap-hooks | `wp-content/plugins/wp-bootstrap-hooks` | jimboobrien/wp-bootstrap-hooks.git | master | origin/master | `de07965` | 2026-03-04 23:14 | `de07965` | 0/0 | 0 | Up to date |
| pegasus | `wp-content/themes/pegasus` | Visionquest-Development/pegasus.git | master | origin/master | `3ec9e66` | 2026-10-13 13:47 | `3ec9e66` | 0/0 | 0 | Up to date |
| pegasus-child | `wp-content/themes/pegasus-child` | Visionquest-Development/pegasus-child.git | pegasustheme_child | origin/pegasustheme_child | `1ea5d45` | 2026-10-13 12:52 | `1ea5d45` | 0/0 | 0 | Site branch: up to date |

### pegasustwo

| Component | Path | Remote | Branch | Upstream | Commit | Commit date | Origin | Ahead/Behind | Dirty | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| pegasus | `wp-content/themes/pegasus` | Visionquest-Development/pegasus.git | master | origin/master | `3ec9e66` | 2026-10-13 13:47 | `3ec9e66` | 0/0 | 0 | Up to date |

### qbiqcamp

| Component | Path | Remote | Branch | Upstream | Commit | Commit date | Origin | Ahead/Behind | Dirty | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| pegasus-carousel | `wp-content/plugins/pegasus-carousel` | Visionquest-Development/pegasus-carousel.git | master | origin/master | `586bc7a` | 2026-10-13 13:51 | `586bc7a` | 0/0 | 0 | Up to date |
| pegasus-onepage | `wp-content/plugins/pegasus-onepage` | Visionquest-Development/pegasus-onepage.git | master | origin/master | `66a5367` | 2026-10-13 13:51 | `66a5367` | 0/0 | 0 | Up to date |
| pegasus-packery | `wp-content/plugins/pegasus-packery` | Visionquest-Development/pegasus-packery.git | master | origin/master | `a88aae3` | 2026-10-13 13:51 | `a88aae3` | 0/0 | 0 | Up to date |
| wp-bootstrap-hooks | `wp-content/plugins/wp-bootstrap-hooks` | jimboobrien/wp-bootstrap-hooks.git | master | origin/master | `de07965` | 2026-03-04 23:14 | `de07965` | 0/0 | 0 | Up to date |
| pegasus | `wp-content/themes/pegasus` | Visionquest-Development/pegasus.git | master | origin/master | `3ec9e66` | 2026-10-13 13:47 | `3ec9e66` | 0/0 | 0 | Up to date |
| pegasus-child | `wp-content/themes/pegasus-child` | Visionquest-Development/pegasus-child.git | qbiqcamp_theme | origin/qbiqcamp_theme | `acada8f` | 2026-10-13 12:52 | `acada8f` | 0/0 | 0 | Site branch: up to date |

### qbiqsystem

| Component | Path | Remote | Branch | Upstream | Commit | Commit date | Origin | Ahead/Behind | Dirty | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| pegasus-carousel | `wp-content/plugins/pegasus-carousel` | Visionquest-Development/pegasus-carousel.git | master | origin/master | `586bc7a` | 2026-10-13 13:51 | `586bc7a` | 0/0 | 0 | Up to date |
| pegasus-slider | `wp-content/plugins/pegasus-slider` | Visionquest-Development/pegasus-slider.git | master | origin/master | `e53d764` | 2026-10-13 13:51 | `e53d764` | 0/0 | 0 | Up to date |
| pegasus-wow | `wp-content/plugins/pegasus-wow` | Visionquest-Development/pegasus-wow.git | master | origin/master | `84305b5` | 2026-10-13 13:51 | `84305b5` | 0/0 | 0 | Up to date |
| wp-bootstrap-hooks | `wp-content/plugins/wp-bootstrap-hooks` | jimboobrien/wp-bootstrap-hooks.git | master | origin/master | `de07965` | 2026-03-04 23:14 | `de07965` | 0/0 | 0 | Up to date |
| pegasus | `wp-content/themes/pegasus` | Visionquest-Development/pegasus.git | master | origin/master | `3ec9e66` | 2026-10-13 13:47 | `3ec9e66` | 0/0 | 0 | Up to date |
| pegasus-child | `wp-content/themes/pegasus-child` | Visionquest-Development/pegasus-child.git | qbiqsystem_theme | origin/qbiqsystem_theme | `18d2876` | 2026-10-13 12:52 | `18d2876` | 0/0 | 0 | Site branch: up to date |

### renecatherinedesign

| Component | Path | Remote | Branch | Upstream | Commit | Commit date | Origin | Ahead/Behind | Dirty | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| pegasus-carousel | `wp-content/plugins/pegasus-carousel` | Visionquest-Development/pegasus-carousel.git | master | origin/master | `586bc7a` | 2026-10-13 13:51 | `586bc7a` | 0/0 | 0 | Up to date |
| pegasus-slider | `wp-content/plugins/pegasus-slider` | Visionquest-Development/pegasus-slider.git | master | origin/master | `e53d764` | 2026-10-13 13:51 | `e53d764` | 0/0 | 0 | Up to date |
| pegasus-wow | `wp-content/plugins/pegasus-wow` | Visionquest-Development/pegasus-wow.git | master | origin/master | `84305b5` | 2026-10-13 13:51 | `84305b5` | 0/0 | 0 | Up to date |
| wp-bootstrap-hooks | `wp-content/plugins/wp-bootstrap-hooks` | jimboobrien/wp-bootstrap-hooks.git | master | origin/master | `de07965` | 2026-03-04 23:14 | `de07965` | 0/0 | 0 | Up to date |
| pegasus | `wp-content/themes/pegasus` | Visionquest-Development/pegasus.git | master | origin/master | `3ec9e66` | 2026-10-13 13:47 | `3ec9e66` | 0/0 | 0 | Up to date |
| pegasus-child | `wp-content/themes/pegasus-child` | Visionquest-Development/pegasus-child.git | renecdesign_theme | origin/renecdesign_theme | `5d9fbab` | 2026-10-13 15:59 | `5d9fbab` | 0/0 | 0 | Site branch: up to date |

### ricecapital

| Component | Path | Remote | Branch | Upstream | Commit | Commit date | Origin | Ahead/Behind | Dirty | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| wp-bootstrap-hooks | `wp-content/plugins/wp-bootstrap-hooks` | jimboobrien/wp-bootstrap-hooks.git | master | origin/master | `de07965` | 2026-03-04 23:14 | `de07965` | 0/0 | 0 | Up to date |
| pegasus | `wp-content/themes/pegasus` | Visionquest-Development/pegasus.git | master | origin/master | `3ec9e66` | 2026-10-13 13:47 | `3ec9e66` | 0/0 | 0 | Up to date |
| pegasus-child | `wp-content/themes/pegasus-child` | Visionquest-Development/pegasus-child.git | ricecapital_theme | origin/ricecapital_theme | `317efbc` | 2026-10-13 12:52 | `317efbc` | 0/0 | 0 | Site branch: up to date |

### russelcontracting

| Component | Path | Remote | Branch | Upstream | Commit | Commit date | Origin | Ahead/Behind | Dirty | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| pegasus-carousel | `wp-content/plugins/pegasus-carousel` | Visionquest-Development/pegasus-carousel.git | master | origin/master | `586bc7a` | 2026-10-13 13:51 | `586bc7a` | 0/0 | 0 | Up to date |
| pegasus-masonry | `wp-content/plugins/pegasus-masonry` | Visionquest-Development/pegasus-masonry.git | master | origin/master | `e990597` | 2026-10-13 13:51 | `e990597` | 0/0 | 0 | Up to date |
| pegasus-slider | `wp-content/plugins/pegasus-slider` | Visionquest-Development/pegasus-slider.git | master | origin/master | `e53d764` | 2026-10-13 13:51 | `e53d764` | 0/0 | 0 | Up to date |
| pegasus-wow | `wp-content/plugins/pegasus-wow` | Visionquest-Development/pegasus-wow.git | master | origin/master | `84305b5` | 2026-10-13 13:51 | `84305b5` | 0/0 | 0 | Up to date |
| wp-bootstrap-hooks | `wp-content/plugins/wp-bootstrap-hooks` | jimboobrien/wp-bootstrap-hooks.git | master | origin/master | `de07965` | 2026-03-04 23:14 | `de07965` | 0/0 | 0 | Up to date |
| pegasus | `wp-content/themes/pegasus` | Visionquest-Development/pegasus.git | master | origin/master | `3ec9e66` | 2026-10-13 13:47 | `3ec9e66` | 0/0 | 0 | Up to date |
| pegasus-child | `wp-content/themes/pegasus-child` | Visionquest-Development/pegasus-child.git | russell_theme | origin/russell_theme | `e7b7b0e` | 2026-10-13 12:52 | `e7b7b0e` | 0/0 | 0 | Site branch: up to date |

### sagecnc

| Component | Path | Remote | Branch | Upstream | Commit | Commit date | Origin | Ahead/Behind | Dirty | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| pegasus-accordion | `wp-content/plugins/pegasus-accordion` | Visionquest-Development/pegasus-accordion.git | main | origin/main | `01841eb` | 2026-10-13 13:50 | `01841eb` | 0/0 | 0 | Up to date |
| pegasus-carousel | `wp-content/plugins/pegasus-carousel` | Visionquest-Development/pegasus-carousel.git | master | origin/master | `586bc7a` | 2026-10-13 13:51 | `586bc7a` | 0/0 | 0 | Up to date |
| pegasus-tabs | `wp-content/plugins/pegasus-tabs` | Visionquest-Development/pegasus-tabs.git | master | origin/master | `ca26dd5` | 2026-10-13 13:51 | `ca26dd5` | 0/0 | 0 | Up to date |
| wp-bootstrap-hooks | `wp-content/plugins/wp-bootstrap-hooks` | jimboobrien/wp-bootstrap-hooks.git | master | origin/master | `de07965` | 2026-03-04 23:14 | `de07965` | 0/0 | 0 | Up to date |
| pegasus | `wp-content/themes/pegasus` | Visionquest-Development/pegasus.git | master | origin/master | `3ec9e66` | 2026-10-13 13:47 | `3ec9e66` | 0/0 | 0 | Up to date |
| pegasus-child | `wp-content/themes/pegasus-child` | Visionquest-Development/pegasus-child.git | sage_theme | origin/sage_theme | `de78fc9` | 2026-10-13 12:52 | `de78fc9` | 0/0 | 0 | Site branch: up to date |

### saltcellar

| Component | Path | Remote | Branch | Upstream | Commit | Commit date | Origin | Ahead/Behind | Dirty | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| pegasus-carousel | `wp-content/plugins/pegasus-carousel` | Visionquest-Development/pegasus-carousel.git | master | origin/master | `586bc7a` | 2026-10-13 13:51 | `586bc7a` | 0/0 | 0 | Up to date |
| pegasus-slider | `wp-content/plugins/pegasus-slider` | Visionquest-Development/pegasus-slider.git | master | origin/master | `e53d764` | 2026-10-13 13:51 | `e53d764` | 0/0 | 0 | Up to date |
| pegasus-tabs | `wp-content/plugins/pegasus-tabs` | Visionquest-Development/pegasus-tabs.git | master | origin/master | `ca26dd5` | 2026-10-13 13:51 | `ca26dd5` | 0/0 | 0 | Up to date |
| pegasus-wow | `wp-content/plugins/pegasus-wow` | Visionquest-Development/pegasus-wow.git | master | origin/master | `84305b5` | 2026-10-13 13:51 | `84305b5` | 0/0 | 0 | Up to date |
| vqdev-toast | `wp-content/plugins/vqdev-toast` | Visionquest-Development/vqdev-toast.git | main | origin/main | `b7f7eac` | 2026-05-21 22:06 | `b7f7eac` | 0/0 | 0 | Up to date |
| wp-bootstrap-hooks | `wp-content/plugins/wp-bootstrap-hooks` | jimboobrien/wp-bootstrap-hooks.git | master | origin/master | `de07965` | 2026-03-04 23:14 | `de07965` | 0/0 | 0 | Up to date |
| pegasus | `wp-content/themes/pegasus` | Visionquest-Development/pegasus.git | master | origin/master | `3ec9e66` | 2026-10-13 13:47 | `3ec9e66` | 0/0 | 0 | Up to date |
| pegasus-child | `wp-content/themes/pegasus-child` | Visionquest-Development/pegasus-child.git | saltcellar_theme | origin/saltcellar_theme | `5dab356` | 2026-10-13 12:52 | `5dab356` | 0/0 | 0 | Site branch: up to date |

### stoutbros

| Component | Path | Remote | Branch | Upstream | Commit | Commit date | Origin | Ahead/Behind | Dirty | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| pegasus-carousel | `wp-content/plugins/pegasus-carousel` | Visionquest-Development/pegasus-carousel.git | master | origin/master | `586bc7a` | 2026-10-13 13:51 | `586bc7a` | 0/0 | 0 | Up to date |
| pegasus-slider | `wp-content/plugins/pegasus-slider` | Visionquest-Development/pegasus-slider.git | master | origin/master | `e53d764` | 2026-10-13 13:51 | `e53d764` | 0/0 | 0 | Up to date |
| pegasus-wow | `wp-content/plugins/pegasus-wow` | Visionquest-Development/pegasus-wow.git | master | origin/master | `84305b5` | 2026-10-13 13:51 | `84305b5` | 0/0 | 0 | Up to date |
| wp-bootstrap-hooks | `wp-content/plugins/wp-bootstrap-hooks` | jimboobrien/wp-bootstrap-hooks.git | master | origin/master | `de07965` | 2026-03-04 23:14 | `de07965` | 0/0 | 0 | Up to date |
| pegasus | `wp-content/themes/pegasus` | Visionquest-Development/pegasus.git | master | origin/master | `3ec9e66` | 2026-10-13 13:47 | `3ec9e66` | 0/0 | 0 | Up to date |
| pegasus-child | `wp-content/themes/pegasus-child` | Visionquest-Development/pegasus-child.git | stoutbros_theme | origin/stoutbros_theme | `d751acd` | 2026-08-20 17:48 | `d751acd` | 0/0 | 0 | Site branch: up to date |

### sugarpeddler

| Component | Path | Remote | Branch | Upstream | Commit | Commit date | Origin | Ahead/Behind | Dirty | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| pegasus-carousel | `wp-content/plugins/pegasus-carousel` | Visionquest-Development/pegasus-carousel.git | master | origin/master | `586bc7a` | 2026-10-13 13:51 | `586bc7a` | 0/0 | 0 | Up to date |
| pegasus-slider | `wp-content/plugins/pegasus-slider` | Visionquest-Development/pegasus-slider.git | master | origin/master | `e53d764` | 2026-10-13 13:51 | `e53d764` | 0/0 | 0 | Up to date |
| pegasus-wow | `wp-content/plugins/pegasus-wow` | Visionquest-Development/pegasus-wow.git | master | origin/master | `84305b5` | 2026-10-13 13:51 | `84305b5` | 0/0 | 0 | Up to date |
| vqdev-toast | `wp-content/plugins/vqdev-toast` | Visionquest-Development/vqdev-toast.git | main | origin/main | `b7f7eac` | 2026-05-21 22:06 | `b7f7eac` | 0/0 | 0 | Up to date |
| wp-bootstrap-hooks | `wp-content/plugins/wp-bootstrap-hooks` | jimboobrien/wp-bootstrap-hooks.git | master | origin/master | `de07965` | 2026-03-04 23:14 | `de07965` | 0/0 | 0 | Up to date |
| pegasus | `wp-content/themes/pegasus` | Visionquest-Development/pegasus.git | master | origin/master | `3ec9e66` | 2026-10-13 13:47 | `3ec9e66` | 0/0 | 0 | Up to date |
| pegasus-child | `wp-content/themes/pegasus-child` | Visionquest-Development/pegasus-child.git | sugarpeddler_theme | origin/sugarpeddler_theme | `d929b66` | 2026-10-13 12:52 | `d929b66` | 0/0 | 0 | Site branch: up to date |

### theloft

| Component | Path | Remote | Branch | Upstream | Commit | Commit date | Origin | Ahead/Behind | Dirty | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| pegasus | `wp-content/themes/pegasus` | Visionquest-Development/pegasus.git | master | origin/master | `3ec9e66` | 2026-10-13 13:47 | `3ec9e66` | 0/0 | 0 | Up to date |
| pegasus-child | `wp-content/themes/pegasus-child` | Visionquest-Development/pegasus-child.git | theloft |  | `825fab6` | 2024-12-17 00:10 | `` | ?/? | 2 | Site branch: not on origin (HEAD is a shared commit in 29 origin branches) |

### theloftnew

| Component | Path | Remote | Branch | Upstream | Commit | Commit date | Origin | Ahead/Behind | Dirty | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| pegasus-carousel | `wp-content/plugins/pegasus-carousel` | Visionquest-Development/pegasus-carousel.git | master | origin/master | `586bc7a` | 2026-10-13 13:51 | `586bc7a` | 0/0 | 0 | Up to date |
| pegasus-packery | `wp-content/plugins/pegasus-packery` | Visionquest-Development/pegasus-packery.git | master | origin/master | `a88aae3` | 2026-10-13 13:51 | `a88aae3` | 0/0 | 0 | Up to date |
| pegasus-slider | `wp-content/plugins/pegasus-slider` | Visionquest-Development/pegasus-slider.git | master | origin/master | `e53d764` | 2026-10-13 13:51 | `e53d764` | 0/0 | 0 | Up to date |
| pegasus-wow | `wp-content/plugins/pegasus-wow` | Visionquest-Development/pegasus-wow.git | master | origin/master | `84305b5` | 2026-10-13 13:51 | `84305b5` | 0/0 | 0 | Up to date |
| vqdev-toast | `wp-content/plugins/vqdev-toast` | Visionquest-Development/vqdev-toast.git | main | origin/main | `b7f7eac` | 2026-05-21 22:06 | `b7f7eac` | 0/0 | 0 | Up to date |
| wp-bootstrap-hooks | `wp-content/plugins/wp-bootstrap-hooks` | jimboobrien/wp-bootstrap-hooks.git | master | origin/master | `de07965` | 2026-03-04 23:14 | `de07965` | 0/0 | 0 | Up to date |
| pegasus | `wp-content/themes/pegasus` | Visionquest-Development/pegasus.git | master | origin/master | `3ec9e66` | 2026-10-13 13:47 | `3ec9e66` | 0/0 | 0 | Up to date |
| pegasus-child | `wp-content/themes/pegasus-child` | Visionquest-Development/pegasus-child.git | theloft2025_theme | origin/theloft2025_theme | `4051078` | 2026-10-13 12:52 | `4051078` | 0/0 | 0 | Site branch: up to date |
| pegasus-theloft | `wp-content/themes/pegasus-theloft` |  |  |  | `` |  | `` | / |  | Not a git repo |

### tommygs

| Component | Path | Remote | Branch | Upstream | Commit | Commit date | Origin | Ahead/Behind | Dirty | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| pegasus-carousel | `wp-content/plugins/pegasus-carousel` | Visionquest-Development/pegasus-carousel.git | master | origin/master | `586bc7a` | 2026-10-13 13:51 | `586bc7a` | 0/0 | 0 | Up to date |
| pegasus-slider | `wp-content/plugins/pegasus-slider` | Visionquest-Development/pegasus-slider.git | master | origin/master | `e53d764` | 2026-10-13 13:51 | `e53d764` | 0/0 | 0 | Up to date |
| pegasus-wow | `wp-content/plugins/pegasus-wow` | Visionquest-Development/pegasus-wow.git | master | origin/master | `84305b5` | 2026-10-13 13:51 | `84305b5` | 0/0 | 0 | Up to date |
| vqdev-toast | `wp-content/plugins/vqdev-toast` | Visionquest-Development/vqdev-toast.git | main | origin/main | `b7f7eac` | 2026-05-21 22:06 | `b7f7eac` | 0/0 | 0 | Up to date |
| wp-bootstrap-hooks | `wp-content/plugins/wp-bootstrap-hooks` | jimboobrien/wp-bootstrap-hooks.git | master | origin/master | `de07965` | 2026-03-04 23:14 | `de07965` | 0/0 | 0 | Up to date |
| pegasus | `wp-content/themes/pegasus` | Visionquest-Development/pegasus.git | master | origin/master | `3ec9e66` | 2026-10-13 13:47 | `3ec9e66` | 0/0 | 0 | Up to date |
| pegasus-child | `wp-content/themes/pegasus-child` | Visionquest-Development/pegasus-child.git | tommygs_theme | origin/tommygs_theme | `684bbe8` | 2026-10-13 12:52 | `684bbe8` | 0/0 | 0 | Site branch: up to date |

### ulgevents

| Component | Path | Remote | Branch | Upstream | Commit | Commit date | Origin | Ahead/Behind | Dirty | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| pegasus-carousel | `wp-content/plugins/pegasus-carousel` | Visionquest-Development/pegasus-carousel.git | master | origin/master | `586bc7a` | 2026-10-13 13:51 | `586bc7a` | 0/0 | 0 | Up to date |
| pegasus-slider | `wp-content/plugins/pegasus-slider` | Visionquest-Development/pegasus-slider.git | master | origin/master | `e53d764` | 2026-10-13 13:51 | `e53d764` | 0/0 | 0 | Up to date |
| pegasus-wow | `wp-content/plugins/pegasus-wow` | Visionquest-Development/pegasus-wow.git | master | origin/master | `84305b5` | 2026-10-13 13:51 | `84305b5` | 0/0 | 0 | Up to date |
| wp-bootstrap-hooks | `wp-content/plugins/wp-bootstrap-hooks` | jimboobrien/wp-bootstrap-hooks.git | master | origin/master | `de07965` | 2026-03-04 23:14 | `de07965` | 0/0 | 0 | Up to date |
| pegasus | `wp-content/themes/pegasus` | Visionquest-Development/pegasus.git | master | origin/master | `3ec9e66` | 2026-10-13 13:47 | `3ec9e66` | 0/0 | 0 | Up to date |
| pegasus-child | `wp-content/themes/pegasus-child` | Visionquest-Development/pegasus-child.git | ulg_events_theme | origin/ulg_events_theme | `c06b498` | 2026-10-13 12:53 | `c06b498` | 0/0 | 0 | Site branch: up to date |

### uptownlifegroup

| Component | Path | Remote | Branch | Upstream | Commit | Commit date | Origin | Ahead/Behind | Dirty | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| pegasus-accordion | `wp-content/plugins/pegasus-accordion` | Visionquest-Development/pegasus-accordion.git | main | origin/main | `01841eb` | 2026-10-13 13:50 | `01841eb` | 0/0 | 0 | Up to date |
| pegasus-carousel | `wp-content/plugins/pegasus-carousel` | Visionquest-Development/pegasus-carousel.git | master | origin/master | `586bc7a` | 2026-10-13 13:51 | `586bc7a` | 0/0 | 0 | Up to date |
| pegasus-slider | `wp-content/plugins/pegasus-slider` | Visionquest-Development/pegasus-slider.git | master | origin/master | `e53d764` | 2026-10-13 13:51 | `e53d764` | 0/0 | 0 | Up to date |
| pegasus-toggleslide | `wp-content/plugins/pegasus-toggleslide` | Visionquest-Development/pegasus-toggleslide.git | master | origin/master | `8fce927` | 2026-10-13 13:51 | `8fce927` | 0/0 | 0 | Up to date |
| pegasus-wow | `wp-content/plugins/pegasus-wow` | Visionquest-Development/pegasus-wow.git | master | origin/master | `84305b5` | 2026-10-13 13:51 | `84305b5` | 0/0 | 0 | Up to date |
| wp-bootstrap-hooks | `wp-content/plugins/wp-bootstrap-hooks` | jimboobrien/wp-bootstrap-hooks.git | master | origin/master | `de07965` | 2026-03-04 23:14 | `de07965` | 0/0 | 0 | Up to date |
| pegasus | `wp-content/themes/pegasus` | Visionquest-Development/pegasus.git | master | origin/master | `3ec9e66` | 2026-10-13 13:47 | `3ec9e66` | 0/0 | 0 | Up to date |
| pegasus-child | `wp-content/themes/pegasus-child` | Visionquest-Development/pegasus-child.git | ulg_theme | origin/ulg_theme | `2f012dc` | 2026-10-13 12:53 | `2f012dc` | 0/0 | 0 | Site branch: up to date |

### valorcare

| Component | Path | Remote | Branch | Upstream | Commit | Commit date | Origin | Ahead/Behind | Dirty | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| pegasus-carousel | `wp-content/plugins/pegasus-carousel` | Visionquest-Development/pegasus-carousel.git | master | origin/master | `586bc7a` | 2026-10-13 13:51 | `586bc7a` | 0/0 | 0 | Up to date |
| pegasus-slider | `wp-content/plugins/pegasus-slider` | Visionquest-Development/pegasus-slider.git | master | origin/master | `e53d764` | 2026-10-13 13:51 | `e53d764` | 0/0 | 0 | Up to date |
| pegasus-wow | `wp-content/plugins/pegasus-wow` | Visionquest-Development/pegasus-wow.git | master | origin/master | `84305b5` | 2026-10-13 13:51 | `84305b5` | 0/0 | 0 | Up to date |
| wp-bootstrap-hooks | `wp-content/plugins/wp-bootstrap-hooks` | jimboobrien/wp-bootstrap-hooks.git | master | origin/master | `de07965` | 2026-03-04 23:14 | `de07965` | 0/0 | 0 | Up to date |
| pegasus | `wp-content/themes/pegasus` | Visionquest-Development/pegasus.git | master | origin/master | `3ec9e66` | 2026-10-13 13:47 | `3ec9e66` | 0/0 | 0 | Up to date |
| pegasus-child | `wp-content/themes/pegasus-child` | Visionquest-Development/pegasus-child.git | valorcare_theme | origin/valorcare_theme | `8c8c0c6` | 2026-10-13 12:53 | `8c8c0c6` | 0/0 | 0 | Site branch: up to date |

### vineandvision

| Component | Path | Remote | Branch | Upstream | Commit | Commit date | Origin | Ahead/Behind | Dirty | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| pegasus-callout | `wp-content/plugins/pegasus-callout` | Visionquest-Development/pegasus-callout.git | master | origin/master | `bc4c766` | 2026-10-13 13:51 | `bc4c766` | 0/0 | 0 | Up to date |
| pegasus-wow | `wp-content/plugins/pegasus-wow` | Visionquest-Development/pegasus-wow.git | master | origin/master | `84305b5` | 2026-10-13 13:51 | `84305b5` | 0/0 | 0 | Up to date |
| wp-bootstrap-hooks | `wp-content/plugins/wp-bootstrap-hooks` | jimboobrien/wp-bootstrap-hooks.git | master | origin/master | `de07965` | 2026-03-04 23:14 | `de07965` | 0/0 | 0 | Up to date |
| pegasus | `wp-content/themes/pegasus` | Visionquest-Development/pegasus.git | master | origin/master | `3ec9e66` | 2026-10-13 13:47 | `3ec9e66` | 0/0 | 0 | Up to date |
| pegasus-child | `wp-content/themes/pegasus-child` | Visionquest-Development/pegasus-child.git | vineandvision_theme | origin/vineandvision_theme | `e949fe3` | 2026-10-13 12:53 | `e949fe3` | 0/0 | 0 | Site branch: up to date |

### visionquest

| Component | Path | Remote | Branch | Upstream | Commit | Commit date | Origin | Ahead/Behind | Dirty | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| pegasus-botify | `wp-content/plugins/pegasus-botify` | Visionquest-Development/pegasus-botify.git | main | origin/main | `ffd1d28` | 2026-10-13 13:50 | `ffd1d28` | 0/0 | 0 | Up to date |
| pegasus-carousel | `wp-content/plugins/pegasus-carousel` | Visionquest-Development/pegasus-carousel.git | master | origin/master | `586bc7a` | 2026-10-13 13:51 | `586bc7a` | 0/0 | 0 | Up to date |
| pegasus-slider | `wp-content/plugins/pegasus-slider` | Visionquest-Development/pegasus-slider.git | master | origin/master | `e53d764` | 2026-10-13 13:51 | `e53d764` | 0/0 | 0 | Up to date |
| wp-bootstrap-hooks | `wp-content/plugins/wp-bootstrap-hooks` | jimboobrien/wp-bootstrap-hooks.git | master | origin/master | `de07965` | 2026-03-04 23:14 | `de07965` | 0/0 | 0 | Up to date |
| pegasus | `wp-content/themes/pegasus` | Visionquest-Development/pegasus.git | master | origin/master | `3ec9e66` | 2026-10-13 13:47 | `3ec9e66` | 0/0 | 0 | Up to date |
| pegasus-child | `wp-content/themes/pegasus-child` | Visionquest-Development/pegasus-child.git | vqdev_theme | origin/vqdev_theme | `8dcde68` | 2026-10-13 12:53 | `8dcde68` | 0/0 | 0 | Site branch: up to date |
