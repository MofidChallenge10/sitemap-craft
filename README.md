<div align="center">

<img src="assets/hero.svg" alt="Sitemap Craft animated illustration" width="100%"/>

# Sitemap Craft

**A small static-site sitemap generator with stable URLs and last-modified dates.**

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/) [![License: MIT](https://img.shields.io/badge/License-MIT-2F855A.svg)](LICENSE)

</div>

## Why it exists

Create a sitemap.xml from a static site's published HTML files. Indexes HTML files under a local directory, skips hidden paths and uses file modification times for lastmod. It does not crawl remote pages, infer canonical URLs or validate robots.txt.

## Features

- Recursive HTML discovery
- Hidden-file and hidden-directory exclusion
- XML-escaped absolute URLs
- UTC lastmod dates from file metadata

## Quick start

Python 3.10+; no third-party packages.

```bash
git clone https://github.com/MofidChallenge10/sitemap-craft.git
cd sitemap-craft
python tool.py --help
```

### Example

```bash
python tool.py ./public https://example.com --output public/sitemap.xml
```

## Self-test

```bash
python tool.py --self-test
```

The self-test uses the standard-library `unittest` module. Network-based tools do not contact external services during self-test.

## Scope and safety

Indexes HTML files under a local directory, skips hidden paths and uses file modification times for lastmod. It does not crawl remote pages, infer canonical URLs or validate robots.txt. Review output before using it in production workflows.

## Design notes

The illustration is an original lightweight SVG. Motion is decorative and stops when `prefers-reduced-motion` is enabled; CLI output remains plain and pipe-friendly.

## Contributing

Issues and pull requests are welcome. Keep dependencies minimal, add focused tests for behavior changes, and update examples when options change.

## License

MIT — see [LICENSE](LICENSE).
