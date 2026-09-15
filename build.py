#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
from gen import page_shell, write, icon, T, SITE_NAME
from content import (
    PROFILE, READOUT, STRIP_EN, STRIP_FR, RESEARCH_INTERESTS_EN, RESEARCH_INTERESTS_FR,
    QUICK_FACTS_EN, QUICK_FACTS_FR, ABOUT_EN, ABOUT_FR, AT_A_GLANCE, RESEARCH, PROJECTS, CV,
)

L = {"en": {}, "fr": {}}
L["en"].update({
    "home_highlights": "Featured research", "view": "View \u2192", "latest_projects": "Latest projects",
    "research_interests": "Research interests", "view_cv": "Open CV", "quick_facts": "Quick facts",
    "about_eyebrow": "About", "about_title": "A research-first AI profile",
    "about_desc": "M.Sc. graduate in Intelligent Computer Systems, whose thesis focused on detecting steganography hidden inside diffusion-generated images.",
    "glance": "At a glance", "research_eyebrow": "Research", "research_title": "Research",
    "research_desc": "The thesis write-up below is kept close to publication form, so it can grow into one over time.",
    "read_more": "Read more \u2192", "back_research": "\u2190 Research", "with": "With",
    "projects_eyebrow": "Projects", "projects_title": "Selected projects",
    "projects_desc": "Each project page covers the goal, the build, and the outcome.",
    "view_project": "View project \u2192", "back_projects": "\u2190 Projects",
    "cv_eyebrow": "CV", "cv_title": "Curriculum Vitae",
    "cv_desc": "M.Sc. graduate in Intelligent Computer Systems \u2014 machine learning, computer vision and steganalysis of generative AI.",
    "download": "Download PDF", "core_skills": "Core skills", "tools": "Libraries & tools", "math": "Mathematics",
    "languages": "Languages", "education": "Education", "research_h": "Research", "tech_exp": "Technical experience",
    "publications": "Publications", "contact_eyebrow": "Contact", "contact_title": "Get in touch",
    "contact_desc": "Reach out directly, or find code, notebooks and public work through the profiles below.",
    "email_label": "Email", "email_title": "Direct contact", "email_body": "For research discussions, internships, thesis-related questions, or collaboration.",
    "profiles": "Profiles", "form_title": "Send a message", "form_desc": "This opens your email client with the message pre-filled \u2014 nothing is stored on this site.",
    "f_name": "Name", "f_email": "Your email", "f_message": "Message", "f_send": "Send message",
    "f_note": "Opening your email client\u2026",
    "cv_placeholder": "Final CV (PDF) \u2014 to be added.",
})
L["fr"].update({
    "home_highlights": "Recherche à la une", "view": "Voir \u2192", "latest_projects": "Derniers projets",
    "research_interests": "Domaines de recherche", "view_cv": "Voir le CV", "quick_facts": "En bref",
    "about_eyebrow": "À propos", "about_title": "Un profil IA tourné vers la recherche",
    "about_desc": "Diplômée d'un Master en Systèmes Informatiques Intelligents, avec un mémoire consacré à la détection de stéganographie dissimulée dans des images générées par diffusion.",
    "glance": "En bref", "research_eyebrow": "Recherche", "research_title": "Recherche",
    "research_desc": "Le mémoire ci-dessous est présenté sous une forme proche d'une publication, afin de pouvoir évoluer vers celle-ci.",
    "read_more": "Lire la suite \u2192", "back_research": "\u2190 Recherche", "with": "Avec",
    "projects_eyebrow": "Projets", "projects_title": "Projets sélectionnés",
    "projects_desc": "Chaque fiche projet détaille l'objectif, la réalisation et le résultat.",
    "view_project": "Voir le projet \u2192", "back_projects": "\u2190 Projets",
    "cv_eyebrow": "CV", "cv_title": "Curriculum Vitae",
    "cv_desc": "Diplômée d'un Master en Systèmes Informatiques Intelligents \u2014 machine learning, vision par ordinateur et stéganalyse de l'IA générative.",
    "download": "Télécharger le PDF", "core_skills": "Compétences clés", "tools": "Bibliothèques & outils", "math": "Mathématiques",
    "languages": "Langues", "education": "Formation", "research_h": "Recherche", "tech_exp": "Expérience technique",
    "publications": "Publications", "contact_eyebrow": "Contact", "contact_title": "Me contacter",
    "contact_desc": "Écrivez-moi directement, ou retrouvez code, notebooks et travaux publics via les profils ci-dessous.",
    "email_label": "E-mail", "email_title": "Contact direct", "email_body": "Pour un échange de recherche, un stage, une question liée au mémoire, ou une collaboration.",
    "profiles": "Profils", "form_title": "Envoyer un message", "form_desc": "Ceci ouvre votre client mail avec le message pré-rempli \u2014 rien n'est stocké sur ce site.",
    "f_name": "Nom", "f_email": "Votre e-mail", "f_message": "Message", "f_send": "Envoyer le message",
    "f_note": "Ouverture de votre client mail\u2026",
    "cv_placeholder": "CV définitif (PDF) \u2014 à venir.",
})

from content import PROFILE as _P
EMAIL = "siham.larbi@example.com"

def tags_html(items):
    return '<div class="tags">' + "".join('<span class="tag">%s</span>' % t for t in items) + "</div>"

def collab_html(names, label):
    if not names:
        return ""
    out = '<div class="collab"><span class="collab-label">%s</span>' % label
    for n in names:
        out += '<span class="name">%s</span>' % n
    out += "</div>"
    return out

def readout_html(lang):
    cells = ""
    for r in READOUT:
        lbl = r["lbl_en"] if lang == "en" else r["lbl_fr"]
        cells += '<div><div class="val">%s</div><div class="lbl">%s</div></div>' % (r["val"], lbl)
    return '<div class="readout reveal">%s</div>' % cells

def strip_html(lang):
    items = STRIP_EN if lang == "en" else STRIP_FR
    track = "".join("<span>%s</span>" % s for s in items)
    return '<div class="strip"><div class="strip-track">%s%s</div></div>' % (track, track)

# ---------------------------------------------------------------------------
# HOME
# ---------------------------------------------------------------------------
def build_home(lang, depth):
    t = L[lang]
    p = PROFILE[lang]
    quick = QUICK_FACTS_EN if lang == "en" else QUICK_FACTS_FR
    interests = RESEARCH_INTERESTS_EN if lang == "en" else RESEARCH_INTERESTS_FR
    featured_research = [RESEARCH]
    featured_projects = [pr for pr in PROJECTS if pr["featured"]]

    research_cards = "".join(research_card(r, lang, depth, i) for i, r in enumerate(featured_research))
    project_cards = "".join(project_card(pr, lang, depth, i) for i, pr in enumerate(featured_projects))

    body = """
<section class="hero">
  <div class="reveal">
    <p class="eyebrow">{role}</p>
    <h1>{name}</h1>
    <p class="lede">{lede}</p>
    <div class="actions">
      <a class="btn primary" href="{cv_href}">{view_cv} {arrow}</a>
      <a class="btn" href="{gh}" target="_blank" rel="noopener noreferrer">{github_icon} GitHub</a>
      <a class="btn" href="{kg}" target="_blank" rel="noopener noreferrer">{kaggle_icon} Kaggle</a>
      <a class="btn" href="{li}" target="_blank" rel="noopener noreferrer">{linkedin_icon} LinkedIn</a>
    </div>
  </div>
  <div class="noise-panel reveal">
    <canvas id="noise-canvas" aria-hidden="true"></canvas>
    <div class="noise-caption"><span>latent noise field</span><span>steganalysis · live</span></div>
  </div>
</section>

{strip}

{readout}

<section class="section">
  <div class="section-head reveal">
    <p class="eyebrow">{research_eyebrow}</p>
    <h2>{home_highlights}</h2>
  </div>
  <div class="grid cols-2">{research_cards}</div>
</section>

<section class="section">
  <div class="section-head reveal">
    <p class="eyebrow">Engineering</p>
    <h2>{latest_projects}</h2>
  </div>
  <div class="grid cols-3">{project_cards}</div>
</section>
""".format(
        role=p["title"], name=SITE_NAME, lede=p["lede"],
        cv_href="cv.html",
        view_cv=t["view_cv"], arrow=icon("arrow"),
        gh="https://github.com/siham-larbi", kg="https://www.kaggle.com/sihamlarbi", li="https://linkedin.com/in/siham-larbi",
        github_icon=icon("github"), kaggle_icon=icon("kaggle"), linkedin_icon=icon("linkedin"),
        strip=strip_html(lang), readout=readout_html(lang),
        research_eyebrow=t["research_eyebrow"], home_highlights=t["home_highlights"], research_cards=research_cards,
        latest_projects=t["latest_projects"], project_cards=project_cards,
    )
    title = "%s \u2014 %s" % (SITE_NAME, p["title"])
    page = page_shell(lang, depth, "home", "", title, p["lede"], body)
    write(("fr/index.html" if lang == "fr" else "index.html"), page)

def research_card(r, lang, depth, idx):
    title = r["title_en"] if lang == "en" else r["title_fr"]
    summary = r["summary_en"] if lang == "en" else r["summary_fr"]
    status = r["status_en"] if lang == "en" else r["status_fr"]
    href = "research/%s.html" % r["slug"]
    return """<article class="card reveal">
  <p class="date">{status} / {date}</p>
  <h3><a href="{href}">{title}</a></h3>
  <p>{summary}</p>
  <div class="foot">
    {tags}
    {collab}
    <a class="view" href="{href}">{read_more}</a>
  </div>
</article>""".format(status=status, date=r["date"], href=href, title=title, summary=summary,
                       tags=tags_html(r["tags"]), collab=collab_html(r["collaborators"], L[lang]["with"]),
                       read_more=L[lang]["read_more"])

def project_card(pr, lang, depth, idx):
    title = pr["title_en"] if lang == "en" else pr["title_fr"]
    summary = pr["summary_en"] if lang == "en" else pr["summary_fr"]
    href = "projects/%s.html" % pr["slug"]
    return """<article class="card reveal">
  <p class="date">{date}</p>
  <h3><a href="{href}">{title}</a></h3>
  <p>{summary}</p>
  <div class="foot">
    {tags}
    {collab}
    <a class="view" href="{href}">{view_project}</a>
  </div>
</article>""".format(date=pr["date"], href=href, title=title, summary=summary,
                      tags=tags_html(pr["tech"]), collab=collab_html(pr["collaborators"], L[lang]["with"]),
                      view_project=L[lang]["view_project"])

# ---------------------------------------------------------------------------
# ABOUT
# ---------------------------------------------------------------------------
def build_about(lang, depth):
    t = L[lang]
    paras = ABOUT_EN if lang == "en" else ABOUT_FR
    glance = AT_A_GLANCE[lang]
    interests = RESEARCH_INTERESTS_EN if lang == "en" else RESEARCH_INTERESTS_FR
    prose = "".join("<p>%s</p>" % pp for pp in paras)
    body = """
<div class="section-head reveal">
  <p class="eyebrow">{eyebrow}</p>
  <h2>{title}</h2>
  <p>{desc}</p>
</div>
<div class="grid cols-2" style="grid-template-columns: .8fr 1.2fr; align-items: start; gap: 2.2rem;">
  <aside class="panel reveal">
    <p class="panel-title">{glance}</p>
    <dl class="definition-list">
      <dt>{name_lbl}</dt><dd>{name}</dd>
      <dt>{loc_lbl}</dt><dd>{loc}</dd>
      <dt>{focus_lbl}</dt><dd>{focus}</dd>
      <dt>{lang_lbl}</dt><dd>{lang_val}</dd>
    </dl>
  </aside>
  <div class="prose reveal">
    {prose}
    <h2>{interests_h}</h2>
    {tags}
  </div>
</div>
""".format(eyebrow=t["about_eyebrow"], title=t["about_title"], desc=t["about_desc"], glance=t["glance"],
           name_lbl=glance["title"], name=SITE_NAME, loc_lbl=glance["location"], loc=PROFILE[lang]["location"],
           focus_lbl=glance["focus"], focus=glance["focus_val"], lang_lbl=glance["languages"], lang_val=glance["languages_val"],
           prose=prose, interests_h=t["research_interests"], tags=tags_html(interests))
    title = "%s \u2014 %s" % (t["about_title"], SITE_NAME)
    page = page_shell(lang, depth, "about", "about.html", title, t["about_desc"], body)
    write(("fr/about.html" if lang == "fr" else "about.html"), page)

# ---------------------------------------------------------------------------
# RESEARCH (list + detail)
# ---------------------------------------------------------------------------
def build_research_list(lang, depth):
    t = L[lang]
    cards = research_card(RESEARCH, lang, depth, 0)
    body = """
<div class="section-head reveal">
  <p class="eyebrow">{eyebrow}</p>
  <h2>{title}</h2>
  <p>{desc}</p>
</div>
<div class="grid cols-2">{cards}</div>
""".format(eyebrow=t["research_eyebrow"], title=t["research_title"], desc=t["research_desc"], cards=cards)
    title = "%s \u2014 %s" % (t["research_title"], SITE_NAME)
    page = page_shell(lang, depth, "research", "research.html", title, t["research_desc"], body)
    write(("fr/research.html" if lang == "fr" else "research.html"), page)

def build_research_detail(lang, depth):
    t = L[lang]
    r = RESEARCH
    title =
