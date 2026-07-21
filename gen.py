#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generates the full static site for Siham Larbi's portfolio."""
import os

ROOT = os.path.dirname(os.path.abspath(__file__))

SITE_NAME = "Siham Larbi"
EMAIL = "siham.larbi@example.com"  # PLACEHOLDER - to be replaced by Siham
GITHUB = "https://github.com/siham-larbi"  # PLACEHOLDER - to be replaced
KAGGLE = "https://www.kaggle.com/sihamlarbi"  # PLACEHOLDER - to be replaced
LINKEDIN = "https://linkedin.com/in/siham-larbi"

# ---------------------------------------------------------------------------
# Icons (custom line-icon set, distinct from the original site's icon style)
# ---------------------------------------------------------------------------
ICONS = {
    "home": '<path d="M3 10.5 12 3l9 7.5" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/><path d="M5.5 9.5V20a1 1 0 0 0 1 1H9a1 1 0 0 0 1-1v-4.5a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1V20a1 1 0 0 0 1 1h2.5a1 1 0 0 0 1-1V9.5" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/>',
    "about": '<circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="m15 9-2 5-5 2 2-5Z" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linejoin="round"/>',
    "research": '<path d="M9 2.5h6M10 2.5v5.2L5.6 15a2 2 0 0 0 1.7 3h9.4a2 2 0 0 0 1.7-3L14 7.7V2.5" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/><path d="M8 14h8" stroke="currentColor" stroke-width="1.4" stroke-linecap="round"/>',
    "projects": '<path d="m12 3 8.5 4.5L12 12 3.5 7.5Z" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/><path d="m3.5 12 8.5 4.5L20.5 12M3.5 16.3 12 20.8l8.5-4.5" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/>',
    "cv": '<path d="M7 2.5h7l4 4V21a1 1 0 0 1-1 1H7a1 1 0 0 1-1-1V3.5a1 1 0 0 1 1-1Z" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/><path d="M14 2.5V7h4M9 12h6M9 15.3h6M9 18.6h4" stroke="currentColor" stroke-width="1.4" stroke-linecap="round"/>',
    "contact": '<rect x="2.5" y="5" width="19" height="14" rx="1.6" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="m3.5 6.5 8.5 6.5 8.5-6.5" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/>',
    "mail": '<rect x="2.5" y="5" width="19" height="14" rx="1.6" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="m3.5 6.5 8.5 6.5 8.5-6.5" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/>',
    "download": '<path d="M12 3.5v11m0 0 3.6-3.6M12 14.5 8.4 10.9M5 17.5v2a1.6 1.6 0 0 0 1.6 1.6h10.8A1.6 1.6 0 0 0 19 19.5v-2" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/>',
    "external": '<path d="M14 4.5h5.5V10M19.2 4.8l-9 9M9 5.5H6.2A1.7 1.7 0 0 0 4.5 7.2v10.6a1.7 1.7 0 0 0 1.7 1.7h10.6a1.7 1.7 0 0 0 1.7-1.7V15" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/>',
    "arrow": '<path d="M4 12h15.5M13 5.5 19.5 12 13 18.5" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/>',
    "menu": '<path d="M4 6.5h16M4 12h16M4 17.5h16" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/>',
    "github": '<path fill="currentColor" d="M12 .5C5.73.5.5 5.73.5 12c0 5.09 3.29 9.4 7.86 10.93.58.1.79-.25.79-.56 0-.28-.01-1.02-.02-2-3.2.7-3.88-1.54-3.88-1.54-.52-1.33-1.28-1.69-1.28-1.69-1.04-.72.08-.7.08-.7 1.15.08 1.76 1.19 1.76 1.19 1.03 1.76 2.7 1.25 3.36.96.1-.75.4-1.25.73-1.54-2.56-.29-5.25-1.28-5.25-5.71 0-1.26.45-2.29 1.19-3.09-.12-.29-.52-1.47.11-3.06 0 0 .97-.31 3.18 1.18a11.1 11.1 0 0 1 5.8 0c2.2-1.49 3.17-1.18 3.17-1.18.63 1.59.23 2.77.12 3.06.74.8 1.18 1.83 1.18 3.09 0 4.44-2.7 5.42-5.27 5.7.42.36.79 1.08.79 2.17 0 1.57-.01 2.83-.01 3.22 0 .31.21.67.8.56A10.52 10.52 0 0 0 23.5 12C23.5 5.73 18.27.5 12 .5Z"/>',
    "linkedin": '<path fill="currentColor" d="M20.45 20.45h-3.55v-5.57c0-1.33-.02-3.03-1.85-3.03-1.85 0-2.14 1.45-2.14 2.94v5.66H9.36V9h3.41v1.56h.05c.47-.9 1.63-1.85 3.36-1.85 3.6 0 4.27 2.37 4.27 5.45v6.29ZM5.34 7.43a2.06 2.06 0 1 1 0-4.12 2.06 2.06 0 0 1 0 4.12ZM7.12 20.45H3.56V9h3.56v11.45ZM22.22 0H1.77C.79 0 0 .77 0 1.73v20.54C0 23.23.79 24 1.77 24h20.45c.98 0 1.78-.77 1.78-1.73V1.73C24 .77 23.2 0 22.22 0Z"/>',
    "kaggle": '<path fill="currentColor" d="M18.83 21.53h-3.4l-6.14-7.94-1.83 1.75v6.19H4.72V2.47h2.74v10.42l7.44-7.9h3.31l-6.87 7.25 7.49 9.29Z"/>',
}

def icon(name, cls="icon"):
    return '<svg class="%s" viewBox="0 0 24 24" aria-hidden="true">%s</svg>' % (cls, ICONS[name])

# ---------------------------------------------------------------------------
# i18n strings
# ---------------------------------------------------------------------------
NAV = [
    ("home", "index.html", "home"),
    ("about", "about.html", "about"),
    ("research", "research.html", "research"),
    ("projects", "projects.html", "projects"),
    ("cv", "cv.html", "cv"),
    ("contact", "contact.html", "contact"),
]

T = {
    "en": {
        "nav": {"home": "Home", "about": "About", "research": "Research", "projects": "Projects", "cv": "CV", "contact": "Contact"},
        "role": "AI Research Portfolio",
        "lang_other": "FR",
        "footer_tag": "Portfolio built to be read, not just browsed.",
        "toggle_theme": "Toggle dark mode",
        "toggle_nav": "Toggle navigation",
    },
    "fr": {
        "nav": {"home": "Accueil", "about": "À propos", "research": "Recherche", "projects": "Projets", "cv": "CV", "contact": "Contact"},
        "role": "Portfolio de recherche IA",
        "lang_other": "EN",
        "footer_tag": "Un portfolio pensé pour être lu, pas seulement parcouru.",
        "toggle_theme": "Basculer le mode sombre",
        "toggle_nav": "Afficher la navigation",
    },
}

# ---------------------------------------------------------------------------
# Layout helpers
# ---------------------------------------------------------------------------

def asset_path(depth, p):
    return ("../" * depth) + p

def nav_html(lang, depth, current):
    t = T[lang]
    prefix = "fr/" if lang == "fr" else ""
    items = []
    for key, href, iconname in NAV:
        active = " active" if key == current else ""
        target = asset_path(depth, prefix + href)
        items.append(
            '<a href="%s" class="side-nav-link%s">%s<span>%s</span></a>'
            % (target, active, icon(iconname, "icon"), t["nav"][key])
        )
    return "\n".join(items)

def lang_switch_html(lang, depth, page):
    """page: root-relative EN path like 'about.html', 'projects/slug.html', or '' for home."""
    file = page if page else "index.html"
    en_href = asset_path(depth, file)
    fr_href = asset_path(depth, "fr/" + file)
    en_active = "active" if lang == "en" else ""
    fr_active = "active" if lang == "fr" else ""
    return (
        '<div class="lang-switch">'
        '<a href="%s" class="%s">EN</a>'
        '<a href="%s" class="%s">FR</a>'
        "</div>" % (en_href, en_active, fr_href, fr_active)
    )

def page_shell(lang, depth, current_nav, page_key, title, description, body_html, extra_head=""):
    t = T[lang]
    root_rel = asset_path(depth, "")
    css = asset_path(depth, "assets/style.css")
    js = asset_path(depth, "assets/script.js")
    nav = nav_html(lang, depth, current_nav)
    langswitch = lang_switch_html(lang, depth, page_key)

    social = ""
    for name, url in (("github", GITHUB), ("linkedin", LINKEDIN), ("kaggle", KAGGLE)):
        social += '<a href="%s" target="_blank" rel="noopener noreferrer" aria-label="%s">%s</a>' % (url, name, icon(name, "icon"))

    home_href = asset_path(depth, "fr/index.html") if lang == "fr" else asset_path(depth, "index.html")

    return """<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="{description}">
<link rel="icon" href="{favicon}">
<link rel="stylesheet" href="{css}">
<title>{title}</title>
{extra_head}
</head>
<body>
<button class="nav-toggle" id="nav-toggle" aria-label="{toggle_nav}" aria-expanded="false">{menu_icon}</button>
<div class="scrim" id="scrim"></div>
<div class="app-shell">
  <aside class="sidebar" id="sidebar">
    <a href="{home_href}" class="brand" aria-label="{site_name}">
      <span class="brand-mark">SL</span>
      <span class="brand-text">
        <span class="brand-name">{site_name}</span>
        <span class="brand-role">{role}</span>
      </span>
    </a>
    <nav class="side-nav" aria-label="Main">
      {nav}
    </nav>
    <div class="sidebar-foot">
      {langswitch}
      <div class="theme-row">
        <span>{toggle_theme}</span>
        <button class="theme-switch" id="theme-switch" aria-label="{toggle_theme}"><span class="knob"></span></button>
      </div>
      <div class="social-row">{social}</div>
    </div>
  </aside>
  <main class="content">
    {body}
    <footer class="site-footer">
      <p>&copy; <span id="year">2026</span> {site_name}. {footer_tag}</p>
    </footer>
  </main>
</div>
<script src="{js}"></script>
</body>
</html>
""".format(
        lang=lang,
        description=description,
        favicon=asset_path(depth, "images/favicon.svg"),
        css=css,
        title=title,
        extra_head=extra_head,
        toggle_nav=t["toggle_nav"],
        menu_icon=icon("menu", "icon"),
        home_href=home_href,
        site_name=SITE_NAME,
        role=t["role"],
        nav=nav,
        langswitch=langswitch,
        toggle_theme=t["toggle_theme"],
        social=social,
        body=body_html,
        footer_tag=t["footer_tag"],
        js=js,
    )


def write(path, content):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)

print("template module loaded")
