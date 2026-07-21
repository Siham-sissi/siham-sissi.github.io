# Portfolio — Siham Larbi

Static site (plain HTML/CSS/JS, no build step, no npm dependency) generated from
`gen.py` + `content.py` + `build.py`. Bilingual (EN at the root, FR under `/fr/`),
with a dark mode toggle, mobile navigation, scroll animations, and a contact form.

## Before you publish — please update

A few placeholders need your real information; search for them or check here:

| What | Where | Current placeholder |
|---|---|---|
| Email | `content.py` → `EMAIL` (top of `build.py` too) | `siham.larbi@example.com` |
| GitHub profile | `build.py` (`https://github.com/siham-larbi`) | placeholder |
| Kaggle profile | `build.py` (`https://www.kaggle.com/sihamlarbi`) | placeholder |
| LinkedIn | `content.py` | already set to `linkedin.com/in/siham-larbi` — confirm it's correct |
| High-school name (CV → Education) | `build.py` → `build_cv()` | `[nom de l'établissement]` / `[high school name]` |
| Final CV PDF | `documents/cv-siham-larbi.pdf` | not included — see `documents/README.md` |

After editing, rebuild with:

```bash
python3 build.py
```

This regenerates every `.html` file from the templates — never hand-edit the
generated `.html` files directly, edit `content.py` / `build.py` / `gen.py` instead.

## Structure

```
index.html, about.html, research.html, projects.html, cv.html, contact.html
research/generative-steganography.html
projects/<slug>.html            (8 project pages)
fr/…                            (French mirror of every page above)
assets/style.css, assets/script.js
images/, documents/
```

## Publishing to GitHub Pages

See the deployment instructions provided alongside this project. In short: push this
folder to a repository named `<your-github-username>.github.io`, then in the repo's
**Settings → Pages**, set the source to **GitHub Actions** (the workflow in
`.github/workflows/deploy.yml` is already included and will deploy on every push
to `main`).
