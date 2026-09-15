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
    title = r["title_en"] if lang == "en" else r["title_fr"]
    summary = r["summary_en"] if lang == "en" else r["summary_fr"]
    status = r["status_en"] if lang == "en" else r["status_fr"]
    body_content = r["body_en"] if lang == "en" else r["body_fr"]
    links_html = ""
    for i, l in enumerate(r["links"]):
        variant = "primary" if i == 0 else ""
        label = l["label_en"] if lang == "en" else l["label_fr"]
        links_html += '<a class="btn %s" href="%s" target="_blank" rel="noopener noreferrer">%s %s</a>' % (variant, l["url"], label, icon("external"))

    body = """
<a class="back-link" href="{back}">{back_label}</a>
<div style="margin-top:1.6rem;">
  <p class="eyebrow">{status} / {date}</p>
  <h1 style="font-size: clamp(1.9rem, 3.6vw, 2.6rem); line-height:1.12;">{title}</h1>
  <p class="lede" style="margin-top:.9rem; max-width: 62ch;">{summary}</p>
  {tags}
  {collab}
</div>
<img src="{image}" alt="" style="margin-top:2rem; border:1px solid var(--line); border-radius:4px; background:var(--bg-panel);" loading="lazy">
<div class="actions" style="margin-top:1.6rem;">{links}</div>
<div class="prose" style="margin-top:2.2rem;">{content}</div>
""".format(back="../research.html", back_label=t["back_research"], status=status, date=r["date"], title=title,
           summary=summary, tags=tags_html(r["tags"]), collab=collab_html(r["collaborators"], t["with"]),
           image=r["image"], links=links_html, content=body_content)
    full_title = "%s \u2014 %s" % (title, SITE_NAME)
    page = page_shell(lang, depth, "research", "research/%s.html" % r["slug"], full_title, summary, body)
    write(("fr/research/%s.html" % r["slug"]) if lang == "fr" else ("research/%s.html" % r["slug"]), page)

# ---------------------------------------------------------------------------
# PROJECTS (list + detail)
# ---------------------------------------------------------------------------
def build_projects_list(lang, depth):
    t = L[lang]
    cards = "".join(project_card(pr, lang, depth, i) for i, pr in enumerate(PROJECTS))
    body = """
<div class="section-head reveal">
  <p class="eyebrow">{eyebrow}</p>
  <h2>{title}</h2>
  <p>{desc}</p>
</div>
<div class="grid cols-3">{cards}</div>
""".format(eyebrow=t["projects_eyebrow"], title=t["projects_title"], desc=t["projects_desc"], cards=cards)
    title = "%s \u2014 %s" % (t["projects_title"], SITE_NAME)
    page = page_shell(lang, depth, "projects", "projects.html", title, t["projects_desc"], body)
    write(("fr/projects.html" if lang == "fr" else "projects.html"), page)

def build_project_detail(pr, lang, depth):
    t = L[lang]
    title = pr["title_en"] if lang == "en" else pr["title_fr"]
    summary = pr["summary_en"] if lang == "en" else pr["summary_fr"]
    body_content = pr["body_en"] if lang == "en" else pr["body_fr"]
    links_html = ""
    for i, l in enumerate(pr["links"]):
        variant = "primary" if i == 0 else ""
        label = l["label_en"] if lang == "en" else l["label_fr"]
        links_html += '<a class="btn %s" href="%s" target="_blank" rel="noopener noreferrer">%s %s</a>' % (variant, l["url"], label, icon("external"))

    body = """
<a class="back-link" href="../projects.html">{back_label}</a>
<div style="margin-top:1.6rem;">
  <p class="eyebrow">{date}</p>
  <h1 style="font-size: clamp(1.9rem, 3.6vw, 2.6rem); line-height:1.12;">{title}</h1>
  <p class="lede" style="margin-top:.9rem; max-width: 62ch;">{summary}</p>
  {tags}
  {collab}
</div>
<div class="actions" style="margin-top:1.6rem;">{links}</div>
<div class="prose" style="margin-top:2.2rem;">{content}</div>
""".format(back_label=t["back_projects"], date=pr["date"], title=title, summary=summary,
           tags=tags_html(pr["tech"]), collab=collab_html(pr["collaborators"], t["with"]),
           links=links_html, content=body_content)
    full_title = "%s \u2014 %s" % (title, SITE_NAME)
    page = page_shell(lang, depth, "projects", "projects/%s.html" % pr["slug"], full_title, summary, body)
    write(("fr/projects/%s.html" % pr["slug"]) if lang == "fr" else ("projects/%s.html" % pr["slug"]), page)

# ---------------------------------------------------------------------------
# CV
# ---------------------------------------------------------------------------
def build_cv(lang, depth):
    t = L[lang]
    cv_pdf_href = "/documents/cv-siham-larbi.pdf"
    langs_html = "".join("<li>%s</li>" % (li["en"] if lang == "en" else li["fr"]) for li in CV["languages"])

    if lang == "en":
        edu = """
<p><strong>Master's Degree, Intelligent Computer Systems</strong> \u2014 Mouloud Mammeri University of Tizi-Ouzou (2024\u20132026)</p>
<p><strong>Bachelor's Degree in Computer Science</strong> \u2014 Mouloud Mammeri University of Tizi-Ouzou (2022\u20132024)</p>
<p><strong>First Year, Mathematics and Computer Science</strong> \u2014 Mouloud Mammeri University of Tizi-Ouzou (2021\u20132022)</p>
<p><strong>Scientific Baccalaureate</strong>, Honours \u2014 [high school name] (2021)</p>
"""
        research_p = """
<p><strong>Graduate research (2026):</strong> "Detecting Steganography from Generative Models: Distinguishing Steganographic Images from Synthetic Images." Carried out with Idir Rebhi, supervised by M. Samy Sadi and Mlle Hedir Tassadit, Universit\u00e9 Mouloud Mammeri de Tizi-Ouzou.</p>
<ul>
<li>Diffusion-model-based approach</li>
<li>Built and organized a dedicated dataset</li>
<li>Designed an inversion pipeline on Stable Diffusion</li>
<li>Reproduced a state-of-the-art detection method (NS-DSer)</li>
<li>Developed a deep-learning detection approach</li>
<li>Trained and evaluated classifiers (CNN, SVM, Random Forest, FLD, etc.)</li>
<li>Ran the performance evaluation and experimental analysis</li>
</ul>
<p>Full write-up on the <a href="research/generative-steganography.html">Research</a> page.</p>
"""
        tech_p = """
<p><strong>Computer Science Internship, District Commercial Naftal, Tizi-Ouzou (2024)</strong> \u2014 analysis of the company's information system, evaluation of business processes, study of enterprise information management, technical internship report.</p>
<p><strong>Bachelor's final project (2024)</strong> \u2014 Oil Mill Management Application (Python/PyQt5, Qt Designer, MySQL), with Idir Rebhi: UML modeling and a written dissertation.</p>
<p>Selected graduate and personal projects \u2014 see the <a href="projects.html">Projects</a> page for details, collaborators and links.</p>
"""
        pub_p = "<p>No publications yet. This section will be updated if the thesis leads to a conference or journal submission.</p>"
    else:
        edu = """
<p><strong>Master, Syst\u00e8mes Informatiques Intelligents</strong> \u2014 Universit\u00e9 Mouloud Mammeri de Tizi-Ouzou (2024\u20132026)</p>
<p><strong>Licence en Informatique</strong> \u2014 Universit\u00e9 Mouloud Mammeri de Tizi-Ouzou (2022\u20132024)</p>
<p><strong>1\u00e8re ann\u00e9e Math\u00e9matiques et Informatique</strong> \u2014 Universit\u00e9 Mouloud Mammeri de Tizi-Ouzou (2021\u20132022)</p>
<p><strong>Baccalaur\u00e9at scientifique</strong>, mention \u2014 [nom de l'\u00e9tablissement] (2021)</p>
"""
        research_p = """
<p><strong>Travail de recherche du master (2026) :</strong> « D\u00e9tection de st\u00e9ganographie issue de mod\u00e8les g\u00e9n\u00e9ratifs : distinction entre images st\u00e9ganographi\u00e9es et images synth\u00e9tiques ». R\u00e9alis\u00e9 avec Idir Rebhi, sous la direction de M. Samy Sadi et Mlle Hedir Tassadit, Universit\u00e9 Mouloud Mammeri de Tizi-Ouzou.</p>
<ul>
<li>Approche fond\u00e9e sur les mod\u00e8les de diffusion</li>
<li>Constitution et organisation d'un jeu de donn\u00e9es d\u00e9di\u00e9</li>
<li>Conception d'un pipeline d'inversion sur Stable Diffusion</li>
<li>Reproduction d'une m\u00e9thode de d\u00e9tection de r\u00e9f\u00e9rence (NS-DSer)</li>
<li>D\u00e9veloppement d'une approche de d\u00e9tection par deep learning</li>
<li>Entra\u00eenement et \u00e9valuation de classifieurs (CNN, SVM, Random Forest, FLD, etc.)</li>
<li>Conduite de l'\u00e9valuation des performances et de l'analyse exp\u00e9rimentale</li>
</ul>
<p>Le d\u00e9tail complet est sur la page <a href="research/generative-steganography.html">Recherche</a>.</p>
"""
        tech_p = """
<p><strong>Stage informatique, District Commercial Naftal, Tizi-Ouzou (2024)</strong> \u2014 analyse du syst\u00e8me d'information de l'entreprise, \u00e9valuation des processus m\u00e9tier, \u00e9tude de la gestion de l'information d'entreprise, rapport de stage technique.</p>
<p><strong>Projet de fin d'\u00e9tudes de Licence (2024)</strong> \u2014 Application de gestion d'une huilerie (Python/PyQt5, Qt Designer, MySQL), avec Idir Rebhi : mod\u00e9lisation UML et m\u00e9moire \u00e9crit.</p>
<p>Projets de master et projets personnels s\u00e9lectionn\u00e9s \u2014 voir la page <a href="projects.html">Projets</a> pour le d\u00e9tail, les collaborateurs et les liens.</p>
"""
        pub_p = "<p>Aucune publication pour le moment. Cette section sera mise \u00e0 jour si le m\u00e9moire donne lieu \u00e0 une soumission en conf\u00e9rence ou en revue.</p>"

    body = """
<div class="section-head reveal">
  <p class="eyebrow">{eyebrow}</p>
  <h2>{title}</h2>
  <p>{desc}</p>
</div>
<div class="reveal">
  <a class="btn primary" href="{cv_pdf}" target="_blank" rel="noopener noreferrer">{download} {dl_icon}</a>
</div>
<div class="grid cols-2" style="grid-template-columns: .85fr 1.15fr; align-items:start; gap:2.2rem; margin-top:2.4rem;">
  <aside>
    <div class="panel reveal"><p class="panel-title">{core_skills}</p>{skills_tags}</div>
    <div class="panel reveal"><p class="panel-title">{tools}</p>{tools_tags}</div>
    <div class="panel reveal"><p class="panel-title">{math}</p>{math_tags}</div>
    <div class="panel reveal"><p class="panel-title">{languages}</p><ul class="definition-list" style="list-style:none;">{langs}</ul></div>
  </aside>
  <div class="prose reveal">
    <h2>{education}</h2>
    {edu}
    <h2>{research_h}</h2>
    {research_p}
    <h2>{tech_exp}</h2>
    {tech_p}
    <h2>{publications}</h2>
    {pub_p}
  </div>
</div>
""".format(eyebrow=t["cv_eyebrow"], title=t["cv_title"], desc=t["cv_desc"], download=t["download"], dl_icon=icon("download"),
           cv_pdf=cv_pdf_href, core_skills=t["core_skills"], skills_tags=tags_html(CV["core_skills"]),
           tools=t["tools"], tools_tags=tags_html(CV["tools"]), math=t["math"], math_tags=tags_html(CV["math"]),
           languages=t["languages"], langs=langs_html, education=t["education"], edu=edu,
           research_h=t["research_h"], research_p=research_p, tech_exp=t["tech_exp"], tech_p=tech_p,
           publications=t["publications"], pub_p=pub_p)
    title = "%s \u2014 %s" % (t["cv_title"], SITE_NAME)
    page = page_shell(lang, depth, "cv", "cv.html", title, t["cv_desc"], body)
    write(("fr/cv.html" if lang == "fr" else "cv.html"), page)

# ---------------------------------------------------------------------------
# CONTACT
# ---------------------------------------------------------------------------
def build_contact(lang, depth):
    t = L[lang]
    body = """
<div class="section-head reveal">
  <p class="eyebrow">{eyebrow}</p>
  <h2>{title}</h2>
  <p>{desc}</p>
</div>
<div class="grid cols-2 reveal">
  <div class="panel">
    <p class="eyebrow">{email_label}</p>
    <h3 style="margin-top:.3rem;">{email_title}</h3>
    <p style="margin-top:.6rem;">{email_body}</p>
    <div style="margin-top:1.2rem;"><a class="btn primary" href="mailto:{email}">{mail_icon} {email}</a></div>
  </div>
  <div class="panel">
    <p class="eyebrow">{profiles}</p>
    <div class="actions" style="margin-top:1rem;">
      <a class="btn" href="{gh}" target="_blank" rel="noopener noreferrer">{github_icon} GitHub</a>
      <a class="btn" href="{kg}" target="_blank" rel="noopener noreferrer">{kaggle_icon} Kaggle</a>
      <a class="btn" href="{li}" target="_blank" rel="noopener noreferrer">{linkedin_icon} LinkedIn</a>
    </div>
  </div>
</div>
<div class="panel reveal" style="margin-top:1.1rem;">
  <p class="panel-title">{form_title}</p>
  <p style="margin-top:-.6rem; margin-bottom:1.1rem;">{form_desc}</p>
  <form class="form-grid" id="contact-form" data-email="{email}">
    <div class="field"><label for="f-name">{f_name}</label><input id="f-name" type="text" required></div>
    <div class="field"><label for="f-email">{f_email}</label><input id="f-email" type="email" required></div>
    <div class="field"><label for="f-message">{f_message}</label><textarea id="f-message" required></textarea></div>
    <div>
      <button type="submit" class="btn primary">{f_send} {arrow}</button>
      <p class="form-note mono" id="form-note" hidden>{f_note}</p>
    </div>
  </form>
</div>
""".format(eyebrow=t["contact_eyebrow"], title=t["contact_title"], desc=t["contact_desc"],
           email_label=t["email_label"], email_title=t["email_title"], email_body=t["email_body"],
           email=EMAIL, mail_icon=icon("mail"), profiles=t["profiles"],
           gh="https://github.com/siham-larbi", kg="https://www.kaggle.com/sihamlarbi", li="https://linkedin.com/in/siham-larbi",
           github_icon=icon("github"), kaggle_icon=icon("kaggle"), linkedin_icon=icon("linkedin"),
           form_title=t["form_title"], form_desc=t["form_desc"], f_name=t["f_name"], f_email=t["f_email"],
           f_message=t["f_message"], f_send=t["f_send"], arrow=icon("arrow"), f_note=t["f_note"])
    title = "%s \u2014 %s" % (t["contact_title"], SITE_NAME)
    page = page_shell(lang, depth, "contact", "contact.html", title, t["contact_desc"], body)
    write(("fr/contact.html" if lang == "fr" else "contact.html"), page)

# ---------------------------------------------------------------------------
# Run
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    for lang, depth in (("en", 0), ("fr", 1)):
        build_home(lang, depth)
        build_about(lang, depth)
        build_research_list(lang, depth)
        build_projects_list(lang, depth)
        build_cv(lang, depth)
        build_contact(lang, depth)
        build_research_detail(lang, depth + 1)
        for pr in PROJECTS:
            build_project_detail(pr, lang, depth + 1)
    print("Build complete.")
