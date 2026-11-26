# Changelog

## 1.1.0 (2026-11-25)
- **Guided report page.** The skill now presents its result as a self-contained HTML page (`assets/report-template.html`) that walks through the analysis one idea per screen, with a "Show all" switch for a single printable page. The skill fills in only the page's JSON data block, following `assets/report-schema.md`. When it can't create files, it falls back to markdown as before.
- Added the Linewright example page and `tools/build_report.py`.
- The analysis itself (gates, content and wording rules) is unchanged from 1.0.0, which is the evaluated version.

## 1.0.0 (2026-11-25)
- First public release: the final version from the [evaluation](https://github.com/KShervington/good-to-great-eval).
