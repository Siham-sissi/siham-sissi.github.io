# -*- coding: utf-8 -*-

PROFILE = {
    "en": {
        "title": "Applied AI & Computer Vision — M.Sc. Intelligent Computer Systems",
        "lede": "I design and evaluate machine learning systems, from classical pipelines to diffusion-based generative models. My graduate thesis asked how far steganalysis can go once a hidden message is written directly into the image-generation process itself.",
        "location": "Tizi-Ouzou, Algeria",
        "cta_cv": "Open CV",
    },
    "fr": {
        "title": "IA appliquée & Vision par ordinateur — Master Systèmes Informatiques Intelligents",
        "lede": "Je conçois et j'évalue des systèmes de machine learning, des pipelines classiques aux modèles génératifs par diffusion. Mon mémoire de master a posé une question simple : jusqu'où la stéganalyse peut-elle aller lorsque le message caché est écrit directement dans le processus de génération de l'image ?",
        "location": "Tizi-Ouzou, Algérie",
        "cta_cv": "Voir le CV",
    },
}

READOUT = [
    {"val": "99.52%", "lbl_en": "NS-DSer accuracy — Message Concealment", "lbl_fr": "Précision NS-DSer — Message Concealment"},
    {"val": "1.0", "lbl_en": "AUC-ROC on the reproduced baseline", "lbl_fr": "AUC-ROC sur la baseline reproduite"},
    {"val": "57.0%", "lbl_en": "Best result vs. mas-GRDH (tabular + RPCM)", "lbl_fr": "Meilleur résultat vs mas-GRDH (tabulaire + RPCM)"},
    {"val": "2 000", "lbl_en": "Cover/stego samples per technique evaluated", "lbl_fr": "Échantillons cover/stego évalués par technique"},
]

STRIP_EN = ["Machine Learning", "Deep Learning", "Computer Vision", "Generative AI", "Steganalysis", "Diffusion Models", "PyTorch", "Data Pipelines"]
STRIP_FR = ["Machine Learning", "Deep Learning", "Vision par ordinateur", "IA générative", "Stéganalyse", "Modèles de diffusion", "PyTorch", "Pipelines de données"]

RESEARCH_INTERESTS_EN = ["Machine Learning", "Deep Learning", "Computer Vision", "Generative AI", "Steganalysis", "Data Pipelines"]
RESEARCH_INTERESTS_FR = ["Machine Learning", "Deep Learning", "Vision par ordinateur", "IA générative", "Stéganalyse", "Pipelines de données"]

QUICK_FACTS_EN = [
    "M2 Intelligent Computer Systems, Univ. Mouloud Mammeri de Tizi-Ouzou — class of 2026",
    "Thesis on steganalysis of diffusion-generated images, with Idir Rebhi, supervised by S. Sadi and T. Hedir",
    "Reproduced the NS-DSer baseline at 99.52% accuracy on Message Concealment (AUC-ROC 1.0)",
    "Pipeline, notebooks and datasets published on GitHub, Kaggle and Colab",
]
QUICK_FACTS_FR = [
    "M2 Systèmes Informatiques Intelligents, Univ. Mouloud Mammeri de Tizi-Ouzou — promotion 2026",
    "Mémoire sur la stéganalyse d'images générées par diffusion, avec Idir Rebhi, encadré par S. Sadi et T. Hedir",
    "Reproduction de la baseline NS-DSer à 99,52% de précision sur Message Concealment (AUC-ROC 1.0)",
    "Pipeline, notebooks et jeux de données publiés sur GitHub, Kaggle et Colab",
]

ABOUT_EN = [
    "I hold a Master's degree in Intelligent Computer Systems from Université Mouloud Mammeri de Tizi-Ouzou, where I focused on building AI-driven solutions to concrete problems. If there's one habit that defines how I work, it's starting from the question rather than the tool: I try to pin down exactly what a method can and cannot do before I trust it.",
    "That habit is the whole premise of my graduate thesis, <em>\"Detecting steganography from generative models: distinguishing steganographic images from synthetic images.\"</em> Diffusion models can now embed a secret message directly while an image is being generated, instead of hiding it inside a picture that already exists — so the usual question (\"was this image modified?\") stops making sense. Together with Idir Rebhi, under the supervision of M. Samy Sadi and Mlle Hedir Tassadit, I worked on reproducing the NS-DSer detection method on Stable Diffusion 2.1 and testing it against embedding techniques with very different resistance to detection.",
    "Most of the applied projects on this site — the REST API, the facial recognition pipeline, the IoT system — were also built with Idir Rebhi, and a few with Nouria Benamara and Mohamed Amine Terdjemane. Each project page lists exactly who worked on what.",
    "Outside the thesis, I like taking things apart to understand them: implementing a neural network or a classic ML algorithm from scratch before reaching for a library, then carrying that understanding into systems that actually run — APIs, connected devices, desktop tools. I get more out of a project when I'm building it with someone else.",
]
ABOUT_FR = [
    "Je suis titulaire d'un Master en Systèmes Informatiques Intelligents de l'Université Mouloud Mammeri de Tizi-Ouzou, où je me suis concentrée sur la construction de solutions fondées sur l'IA pour des problèmes concrets. S'il y a une habitude qui définit ma façon de travailler, c'est de partir de la question plutôt que de l'outil : je cherche à cerner précisément ce qu'une méthode peut et ne peut pas faire avant de lui faire confiance.",
    "Cette habitude est tout le point de départ de mon mémoire de master, « Détection de stéganographie issue de modèles génératifs : distinction entre images stéganographiées et images synthétiques ». Les modèles de diffusion peuvent désormais intégrer un message secret directement pendant la génération de l'image, au lieu de le dissimuler dans une image déjà existante — la question habituelle (« cette image a-t-elle été modifiée ? ») cesse alors d'avoir un sens. Avec Idir Rebhi, sous la direction de M. Samy Sadi et Mlle Hedir Tassadit, j'ai travaillé à la reproduction de la méthode de détection NS-DSer sur Stable Diffusion 2.1, puis à son évaluation face à des techniques d'intégration présentant des résistances très différentes à la détection.",
    "La plupart des projets appliqués présentés ici — l'API REST, le pipeline de reconnaissance faciale, le système IoT — ont également été réalisés avec Idir Rebhi, et certains avec Nouria Benamara et Mohamed Amine Terdjemane. Chaque fiche projet précise qui a travaillé sur quoi.",
    "En dehors du mémoire, j'aime démonter les choses pour les comprendre : implémenter un réseau de neurones ou un algorithme de ML classique à la main avant de me tourner vers une bibliothèque, puis réinvestir cette compréhension dans des systèmes qui tournent réellement — API, objets connectés, outils de bureau. Je progresse davantage sur un projet quand je le construis à plusieurs.",
]

AT_A_GLANCE = {
    "en": {"title": "Name", "location": "Location", "focus": "Focus", "focus_val": "Machine learning, computer vision, generative AI, steganalysis", "languages": "Languages", "languages_val": "Kabyle, French, Arabic, English"},
    "fr": {"title": "Nom", "location": "Localisation", "focus": "Domaine", "focus_val": "Machine learning, vision par ordinateur, IA générative, stéganalyse", "languages": "Langues", "languages_val": "Kabyle, français, arabe, anglais"},
}

# ---------------------------------------------------------------------------
# Research (thesis)
# ---------------------------------------------------------------------------
RESEARCH = {
    "slug": "generative-steganography",
    "date": "2026",
    "status_en": "M.Sc. thesis, defended 2026",
    "status_fr": "Mémoire de master, soutenu en 2026",
    "title_en": "Signal in the Noise: Detecting Steganography in Diffusion-Generated Images",
    "title_fr": "Un signal dans le bruit : détecter la stéganographie dans les images générées par diffusion",
    "summary_en": "Master's thesis: once a hidden message is written into the generation process itself, can steganalysis still separate a clean image from a compromised one?",
    "summary_fr": "Mémoire de master : une fois le message caché intégré au processus de génération lui-même, la stéganalyse peut-elle encore distinguer une image saine d'une image compromise ?",
    "tags": ["Steganalysis", "Diffusion Models", "Generative AI", "Computer Vision", "Deep Learning"],
    "collaborators": ["Idir Rebhi"],
    "links": [
        {"label_en": "Download the thesis (PDF, FR)", "label_fr": "Télécharger le mémoire (PDF)", "url": "/documents/memoire-larbi-rebhi-steganographie-generative.pdf"},
        {"label_en": "GitHub — DStegan", "label_fr": "GitHub — DStegan", "url": "https://github.com/RebhiIdir/DStegan.git"},
        {"label_en": "Kaggle — NS-DSer baseline", "label_fr": "Kaggle — baseline NS-DSer", "url": "https://www.kaggle.com/code/idirrebhi/nsdser"},
    ],
    "image": "/images/research-pipeline.svg",
    "body_en": """
<h2>Starting point</h2>
<p>"Détection de stéganographie issue de modèles génératifs : distinction entre images stéganographiées et images synthétiques" — a Master's thesis in Intelligent Computer Systems at Université Mouloud Mammeri de Tizi-Ouzou, carried out with Idir Rebhi and supervised by M. Samy Sadi and Mlle Hedir Tassadit.</p>
<p>Diffusion models made it possible to write a secret message directly into the noise that seeds an image, rather than hiding it inside a picture that already exists. That single shift breaks the usual steganalysis premise — there is no clean original to compare against, because the image was never anything but generated. This thesis measures how much of that hidden signal survives, and under which conditions it stops being detectable at all.</p>

<h2>Why it's a hard problem</h2>
<p>DM-GIS (Diffusion Model-based Generative Image Steganography) folds the secret message into the latent noise that the diffusion process denoises into a picture. <strong>NS-DSer</strong>, the current reference method, inverts that diffusion trajectory to recover the latent noise and checks whether it still looks statistically Gaussian — a departure from Gaussian is the tell. That test catches naive embedding easily, but a technique built specifically to preserve the Gaussian distribution, such as <strong>Gaussian Shading</strong>, removes the tell almost entirely. The open question we set out to answer: how far can detection be pushed once the embedding is designed to hide from it?</p>

<h2>How we approached it</h2>
<ul>
<li><strong>Reproducing the baseline.</strong> NS-DSer rebuilt end to end on Stable Diffusion 2.1: PF-ODE inversion with a Heun discrete scheduler, v-prediction-to-epsilon conversion, and a 10-feature statistical vector (spatial + DCT) extracted from the recovered noise.</li>
<li><strong>Testing against contrasting techniques.</strong> Two embedding methods with very different profiles: <strong>Message Concealment (MC)</strong>, a direct/naive approach, and <strong>mas-GRDH</strong>, built to preserve the noise distribution.</li>
<li><strong>Trying a learned detector.</strong> A convolutional network trained directly on the latent noise residuals, to see whether learned spatial patterns beat the hand-crafted statistics.</li>
<li><strong>Widening the feature and model search.</strong> Logistic Regression, XGBoost, SVM (RBF), ExtraTrees and a stacking ensemble on the 10-feature space, then the same models augmented with <strong>RPCM</strong> descriptors (phase correlation between channels) recovered after the VAE decoder.</li>
<li><strong>Evaluation protocol.</strong> 2,000 samples per technique (1,000 cover / 1,000 stego), accuracy / F1 / ROC-AUC as the headline metrics, and a train/test split built to avoid leakage.</li>
</ul>

<h2>What the numbers show</h2>
<table>
<thead><tr><th>Method</th><th>Technique tested</th><th>Accuracy</th><th>Notes</th></tr></thead>
<tbody>
<tr><td>NS-DSer (baseline)</td><td>Message Concealment</td><td><strong>99.52%</strong></td><td>AUC-ROC 1.0 — matches the original paper and validates the reproduction</td></tr>
<tr><td>NS-DSer (baseline)</td><td>mas-GRDH</td><td><strong>≈52%</strong></td><td>Barely above chance — the distribution-preserving design works as intended</td></tr>
<tr><td>CNN (learned detector)</td><td>mas-GRDH</td><td><strong>≈50%</strong></td><td>Learned features don't recover a signal either</td></tr>
<tr><td>Logistic Regression / XGBoost</td><td>mas-GRDH</td><td><strong>≈52.5%</strong></td><td>On the 10-feature statistical space</td></tr>
<tr><td>Stacking ensemble</td><td>mas-GRDH</td><td><strong>46.0%</strong> (AUC 0.43)</td><td>Overfits the noise and fails to generalize</td></tr>
<tr><td><strong>Tabular + RPCM features</strong> (penalized Logistic Regression)</td><td>mas-GRDH</td><td><strong>57.0%</strong> (F1 0.552, ROC-AUC 0.550)</td><td>The strongest result of the study — a faint but real signal above chance</td></tr>
</tbody>
</table>
<p>The gap between the two rows tells the real story: naive embedding is caught almost perfectly, while a distribution-preserving technique pushes every method we tried — including the CNN — down toward chance level. The one setup that broke through combined noise statistics with RPCM descriptors, hinting that inter-channel phase correlations retain a faint trace of the hidden message even after the VAE decoder reconstructs the image.</p>

<h2>Open threads</h2>
<ul>
<li>Run the inversion pipeline on real photographs, not just synthetic images, to separate sensor noise from generation noise.</li>
<li>Check whether the findings generalize to other diffusion architectures beyond Stable Diffusion (Midjourney, DALL·E 3).</li>
<li>Move from <em>detecting</em> the hidden channel to <em>neutralizing</em> it — for instance a short diffusion/denoising pass combined with a quaternion-based micro-perturbation, in the spirit of Adversarial Diffusion Sanitization.</li>
</ul>

<h2>Reproducibility</h2>
<p>The pipeline, notebooks and generated datasets are public. Reproducing the environment isn't one-click (some hardware-specific dependencies), but every step is documented:</p>
<ul>
<li><strong>GitHub</strong> — <a href="https://github.com/RebhiIdir/DStegan.git" target="_blank" rel="noopener noreferrer">github.com/RebhiIdir/DStegan</a></li>
<li><strong>Kaggle</strong> — <a href="https://www.kaggle.com/code/idirrebhi/nsdser" target="_blank" rel="noopener noreferrer">NS-DSer baseline notebook</a></li>
<li><strong>Google Colab</strong> — <a href="https://colab.research.google.com/drive/1VayTd9MSf_RxZmBAg9sTLwXmzXzBpSDL?usp=sharing" target="_blank" rel="noopener noreferrer">mas-GRDH dataset generation</a></li>
<li><strong>Google Colab</strong> — <a href="https://colab.research.google.com/drive/1r7A-xs2FrWvubkwBnHGWmOcWfun3WmaE?usp=sharing" target="_blank" rel="noopener noreferrer">CNN extension &amp; UNet hooks</a></li>
<li><strong>Google Colab</strong> — <a href="https://colab.research.google.com/drive/1O4siaNVnEL5UEvyOH_7e1hvkTKlUGgGp?usp=sharing" target="_blank" rel="noopener noreferrer">Gaussian Shading test data generation</a></li>
<li><strong>Datasets</strong> — <a href="https://drive.google.com/drive/folders/13-byY7SyrEgkCZvn-GYbNgRFf3-3WUAf?usp=sharing" target="_blank" rel="noopener noreferrer">cover and stego images (Google Drive)</a></li>
</ul>

<h2>Reference</h2>
<p>J. Zhu, Z. Chen, J. Liu, L. Yang, Y. Zhou, W. Luo, and X. Xie, "Rethinking Security of Diffusion-based Generative Steganography," arXiv:2602.10219, February 2026.</p>
""",
    "body_fr": """
<h2>Point de départ</h2>
<p>« Détection de stéganographie issue de modèles génératifs : distinction entre images stéganographiées et images synthétiques » — mémoire de master en Systèmes Informatiques Intelligents à l'Université Mouloud Mammeri de Tizi-Ouzou, réalisé avec Idir Rebhi et encadré par M. Samy Sadi et Mlle Hedir Tassadit.</p>
<p>Les modèles de diffusion permettent désormais d'écrire un message secret directement dans le bruit qui amorce la génération d'une image, plutôt que de le dissimuler dans une image déjà existante. Ce changement remet en cause le principe même de la stéganalyse classique : il n'existe plus d'original « propre » auquel se comparer, puisque l'image n'a jamais été autre chose que générée. Ce mémoire mesure la part de ce signal caché qui subsiste, et dans quelles conditions il cesse tout simplement d'être détectable.</p>

<h2>Pourquoi c'est difficile</h2>
<p>La DM-GIS (stéganographie générative fondée sur les modèles de diffusion) intègre le message secret dans le bruit latent que le processus de diffusion transforme, par débruitage, en image. <strong>NS-DSer</strong>, la méthode de référence actuelle, inverse cette trajectoire de diffusion pour retrouver le bruit latent et vérifie s'il conserve une distribution statistiquement gaussienne — un écart à la gaussienne trahit la présence d'un message. Ce test repère facilement une intégration naïve, mais une technique conçue spécifiquement pour préserver la distribution gaussienne, comme <strong>Gaussian Shading</strong>, efface presque entièrement cet indice. La question à laquelle nous voulions répondre : jusqu'où peut-on pousser la détection lorsque l'intégration est justement conçue pour s'y soustraire ?</p>

<h2>Notre démarche</h2>
<ul>
<li><strong>Reproduction de la baseline.</strong> NS-DSer reconstruit de bout en bout sur Stable Diffusion 2.1 : inversion PF-ODE avec un scheduler discret de Heun, conversion v-prediction vers epsilon, et un vecteur statistique à 10 descripteurs (domaine spatial + DCT) extrait du bruit récupéré.</li>
<li><strong>Confrontation à deux techniques opposées.</strong> <strong>Message Concealment (MC)</strong>, une intégration directe et naïve, et <strong>mas-GRDH</strong>, conçue pour préserver la distribution du bruit.</li>
<li><strong>Un détecteur appris.</strong> Un réseau convolutif entraîné directement sur les résidus de bruit latent, pour voir si des motifs spatiaux appris font mieux que les statistiques construites à la main.</li>
<li><strong>Élargir la recherche de modèles et de descripteurs.</strong> Régression logistique, XGBoost, SVM (RBF), ExtraTrees et un ensemble par stacking sur l'espace à 10 descripteurs, puis les mêmes modèles enrichis de descripteurs <strong>RPCM</strong> (corrélation de phase entre canaux) récupérés après le décodeur VAE.</li>
<li><strong>Protocole d'évaluation.</strong> 2 000 échantillons par technique (1 000 cover / 1 000 stego), précision / F1 / ROC-AUC comme métriques principales, et un découpage train/test conçu pour éviter toute fuite de données.</li>
</ul>

<h2>Ce que montrent les chiffres</h2>
<table>
<thead><tr><th>Méthode</th><th>Technique testée</th><th>Précision</th><th>Remarques</th></tr></thead>
<tbody>
<tr><td>NS-DSer (baseline)</td><td>Message Concealment</td><td><strong>99,52%</strong></td><td>AUC-ROC 1.0 — conforme à l'article original, valide la reproduction</td></tr>
<tr><td>NS-DSer (baseline)</td><td>mas-GRDH</td><td><strong>≈52%</strong></td><td>À peine au-dessus du hasard — la préservation de la distribution fonctionne comme prévu</td></tr>
<tr><td>CNN (détecteur appris)</td><td>mas-GRDH</td><td><strong>≈50%</strong></td><td>Les caractéristiques apprises ne récupèrent pas non plus de signal</td></tr>
<tr><td>Régression logistique / XGBoost</td><td>mas-GRDH</td><td><strong>≈52,5%</strong></td><td>Sur l'espace statistique à 10 descripteurs</td></tr>
<tr><td>Ensemble par stacking</td><td>mas-GRDH</td><td><strong>46,0%</strong> (AUC 0,43)</td><td>Sur-apprend le bruit, ne généralise pas</td></tr>
<tr><td><strong>Descripteurs tabulaires + RPCM</strong> (régression logistique pénalisée)</td><td>mas-GRDH</td><td><strong>57,0%</strong> (F1 0,552, ROC-AUC 0,550)</td><td>Le meilleur résultat de l'étude — un signal ténu mais réel au-dessus du hasard</td></tr>
</tbody>
</table>
<p>L'écart entre les deux lignes raconte l'essentiel : une intégration naïve est repérée presque parfaitement, tandis qu'une technique préservant la distribution ramène toutes les méthodes testées — y compris le CNN — près du niveau du hasard. La seule configuration à franchir ce plafond combinait statistiques de bruit et descripteurs RPCM, ce qui suggère que les corrélations de phase entre canaux conservent une trace ténue du message caché, même après reconstruction par le décodeur VAE.</p>

<h2>Pistes ouvertes</h2>
<ul>
<li>Appliquer le pipeline d'inversion à de vraies photographies, et non plus seulement à des images synthétiques, pour séparer bruit de capteur et bruit de génération.</li>
<li>Vérifier si les résultats se généralisent à d'autres architectures de diffusion que Stable Diffusion (Midjourney, DALL·E 3).</li>
<li>Passer de la <em>détection</em> du canal caché à sa <em>neutralisation</em> — par exemple un court cycle de diffusion/débruitage combiné à une micro-perturbation à base de quaternions, dans l'esprit de l'Adversarial Diffusion Sanitization.</li>
</ul>

<h2>Reproductibilité</h2>
<p>Le pipeline, les notebooks et les jeux de données générés sont publics. L'environnement ne se reproduit pas en un clic (certaines dépendances liées au matériel), mais chaque étape est documentée :</p>
<ul>
<li><strong>GitHub</strong> — <a href="https://github.com/RebhiIdir/DStegan.git" target="_blank" rel="noopener noreferrer">github.com/RebhiIdir/DStegan</a></li>
<li><strong>Kaggle</strong> — <a href="https://www.kaggle.com/code/idirrebhi/nsdser" target="_blank" rel="noopener noreferrer">notebook baseline NS-DSer</a></li>
<li><strong>Google Colab</strong> — <a href="https://colab.research.google.com/drive/1VayTd9MSf_RxZmBAg9sTLwXmzXzBpSDL?usp=sharing" target="_blank" rel="noopener noreferrer">génération du jeu de données mas-GRDH</a></li>
<li><strong>Google Colab</strong> — <a href="https://colab.research.google.com/drive/1r7A-xs2FrWvubkwBnHGWmOcWfun3WmaE?usp=sharing" target="_blank" rel="noopener noreferrer">extension CNN &amp; hooks UNet</a></li>
<li><strong>Google Colab</strong> — <a href="https://colab.research.google.com/drive/1O4siaNVnEL5UEvyOH_7e1hvkTKlUGgGp?usp=sharing" target="_blank" rel="noopener noreferrer">génération des données de test Gaussian Shading</a></li>
<li><strong>Datasets</strong> — <a href="https://drive.google.com/drive/folders/13-byY7SyrEgkCZvn-GYbNgRFf3-3WUAf?usp=sharing" target="_blank" rel="noopener noreferrer">images cover et stego (Google Drive)</a></li>
</ul>

<h2>Référence</h2>
<p>J. Zhu, Z. Chen, J. Liu, L. Yang, Y. Zhou, W. Luo, et X. Xie, « Rethinking Security of Diffusion-based Generative Steganography », arXiv:2602.10219, février 2026.</p>
""",
}

# ---------------------------------------------------------------------------
# Projects
# ---------------------------------------------------------------------------
PROJECTS = [
    {
        "slug": "medical-office-api",
        "date": "2025",
        "featured": True,
        "title_en": "REST API for a Medical Office",
        "title_fr": "API REST pour un cabinet médical",
        "summary_en": "A Java/Spring backend for managing patients, appointments and medical records, secured with JWT.",
        "summary_fr": "Un backend Java/Spring pour gérer patients, rendez-vous et dossiers médicaux, sécurisé par JWT.",
        "tech": ["Java", "Spring", "JAX-RS", "MySQL", "JWT", "REST"],
        "collaborators": ["Idir Rebhi"],
        "links": [{"label_en": "GitHub", "label_fr": "GitHub", "url": "https://github.com/RebhiIdir/ProjetWebServiceREST.git"}],
        "body_en": """
<h2>Brief</h2>
<p>Design a full RESTful service for a medical office — patients, appointments, medical records — with authenticated access and a clean separation between layers.</p>
<h2>Build</h2>
<ul>
<li>Java backend exposing a RESTful API (JAX-RS/Spring).</li>
<li>Endpoints covering the patient, appointment and medical-record lifecycle.</li>
<li>MySQL for persistence.</li>
<li>JWT-based authentication on protected routes.</li>
<li>Endpoint testing and server-side integration via Postman.</li>
</ul>
<h2>Outcome</h2>
<p>A working set of endpoints spanning the full patient/appointment/record lifecycle, exercised end to end with Postman, with authentication enforced wherever it matters.</p>
<h2>What's next</h2>
<p>Automated test coverage, OpenAPI documentation, role-based permissions (doctor / receptionist / admin), and a deployed public instance.</p>
""",
        "body_fr": """
<h2>Objectif</h2>
<p>Concevoir un service RESTful complet pour un cabinet médical — patients, rendez-vous, dossiers médicaux — avec un accès authentifié et une séparation claire des couches applicatives.</p>
<h2>Réalisation</h2>
<ul>
<li>Backend Java exposant une API RESTful (JAX-RS/Spring).</li>
<li>Endpoints couvrant le cycle de vie des patients, des rendez-vous et des dossiers médicaux.</li>
<li>MySQL pour la persistance des données.</li>
<li>Authentification JWT sur les routes protégées.</li>
<li>Tests des endpoints et intégration côté serveur via Postman.</li>
</ul>
<h2>Résultat</h2>
<p>Un ensemble d'endpoints fonctionnels couvrant tout le cycle de vie patient/rendez-vous/dossier, testé de bout en bout avec Postman, avec authentification appliquée là où c'est nécessaire.</p>
<h2>Pistes d'amélioration</h2>
<p>Couverture de tests automatisés, documentation OpenAPI, permissions par rôle (médecin / secrétaire / admin), et une instance publique déployée.</p>
""",
    },
    {
        "slug": "smart-lighting-iot",
        "date": "2025",
        "featured": True,
        "title_en": "Environment-Aware Smart Lighting",
        "title_fr": "Éclairage intelligent piloté par l'environnement",
        "summary_en": "A network of connected sensors that adjusts lighting to environmental conditions, with live monitoring in Grafana.",
        "summary_fr": "Un réseau de capteurs connectés qui adapte l'éclairage aux conditions environnantes, avec supervision en direct sous Grafana.",
        "tech": ["IoT", "ESP32", "Raspberry Pi", "Grafana", "Sensors"],
        "collaborators": ["Idir Rebhi"],
        "links": [
            {"label_en": "GitHub", "label_fr": "GitHub", "url": "https://github.com/RebhiIdir/Projet-IoT.git"},
            {"label_en": "Slides", "label_fr": "Présentation", "url": "https://docs.google.com/presentation/d/1W_NDFf9VynZPt3ZIlj9AXkWTM9l_bB_JQX5AR2c8Ps0/edit?usp=sharing"},
        ],
        "body_en": """
<h2>Brief</h2>
<p>Build a network of connected devices that manages lighting automatically based on ambient conditions, with real-time visibility into the data driving those decisions.</p>
<h2>Build</h2>
<ul>
<li>Sensor nodes on ESP32 microcontrollers.</li>
<li>A Raspberry Pi acting as local hub and gateway.</li>
<li>Live capture and transmission of readings from the nodes to the monitoring stack.</li>
<li>Grafana dashboards for environmental and lighting data.</li>
</ul>
<h2>Outcome</h2>
<p>The system reacts to live environmental readings by adjusting lighting automatically, and every reading is visible in real time through the Grafana dashboards.</p>
<h2>What's next</h2>
<p>Alerting on abnormal readings, more resilient node-to-hub communication, historical trend views, and a publicly reachable dashboard.</p>
""",
        "body_fr": """
<h2>Objectif</h2>
<p>Construire un réseau d'objets connectés qui gère automatiquement l'éclairage selon les conditions ambiantes, avec une visibilité en temps réel sur les données à l'origine de ces décisions.</p>
<h2>Réalisation</h2>
<ul>
<li>Nœuds capteurs sur microcontrôleurs ESP32.</li>
<li>Un Raspberry Pi jouant le rôle de hub local et de passerelle.</li>
<li>Capture et transmission en direct des relevés des nœuds vers la chaîne de supervision.</li>
<li>Tableaux de bord Grafana pour les données environnementales et d'éclairage.</li>
</ul>
<h2>Résultat</h2>
<p>Le système réagit aux relevés environnementaux en direct en ajustant automatiquement l'éclairage, et chaque relevé est visible en temps réel via les tableaux de bord Grafana.</p>
<h2>Pistes d'amélioration</h2>
<p>Alertes sur relevés anormaux, communication nœud-hub plus robuste, vues d'historique et de tendances, et un tableau de bord accessible publiquement.</p>
""",
    },
    {
        "slug": "digit-generation-gan",
        "date": "2025",
        "featured": True,
        "title_en": "Generating Handwritten Digits with a GAN",
        "title_fr": "Génération de chiffres manuscrits avec un GAN",
        "summary_en": "A generative adversarial network trained on MNIST to produce convincing handwritten digits from noise.",
        "summary_fr": "Un réseau antagoniste génératif entraîné sur MNIST pour produire, à partir de bruit, des chiffres manuscrits crédibles.",
        "tech": ["Python", "TensorFlow", "GAN", "Generative AI"],
        "collaborators": ["Idir Rebhi"],
        "links": [
            {"label_en": "Report (PDF)", "label_fr": "Rapport (PDF)", "url": "/documents/rapport-gan-mnist.pdf"},
            {"label_en": "Colab", "label_fr": "Colab", "url": "https://colab.research.google.com/drive/1hyJz0T_4PCdgl1j8UsC1HEyioZEvrNfo?usp=sharing"},
        ],
        "body_en": """
<h2>Brief</h2>
<p>Implement a generative adversarial network able to produce convincing handwritten digits, trained on MNIST.</p>
<h2>Build</h2>
<ul>
<li>Generator and discriminator networks in TensorFlow.</li>
<li>Adversarial training loop alternating generator and discriminator updates.</li>
<li>Qualitative tracking of generated samples across training.</li>
</ul>
<h2>Outcome</h2>
<p>The trained generator produces recognizable handwritten digits from random noise — a first hands-on encounter with generative modeling, ahead of the diffusion-based work in the thesis.</p>
<h2>Link to the thesis</h2>
<p>The earliest stepping stone toward the graduate research: this was the first practical contact with generative models, later extended toward diffusion-based generation and its detection.</p>
""",
        "body_fr": """
<h2>Objectif</h2>
<p>Implémenter un réseau antagoniste génératif capable de produire des chiffres manuscrits crédibles, entraîné sur MNIST.</p>
<h2>Réalisation</h2>
<ul>
<li>Réseaux générateur et discriminateur sous TensorFlow.</li>
<li>Boucle d'entraînement adversarial alternant les mises à jour du générateur et du discriminateur.</li>
<li>Suivi qualitatif des échantillons générés tout au long de l'entraînement.</li>
</ul>
<h2>Résultat</h2>
<p>Le générateur entraîné produit des chiffres manuscrits reconnaissables à partir de bruit aléatoire — un premier contact concret avec la modélisation générative, avant le travail sur la diffusion mené dans le mémoire.</p>
<h2>Lien avec le mémoire</h2>
<p>Le tout premier jalon vers le travail de recherche du master : ce projet a constitué le premier contact pratique avec les modèles génératifs, prolongé ensuite vers la génération par diffusion et sa détection.</p>
""",
    },
    {
        "slug": "facial-recognition",
        "date": "2025",
        "featured": True,
        "title_en": "Facial Recognition Pipeline",
        "title_fr": "Système de reconnaissance faciale",
        "summary_en": "A biometric pipeline covering face detection, feature extraction, model training and evaluation.",
        "summary_fr": "Un pipeline biométrique couvrant détection de visages, extraction de caractéristiques, entraînement et évaluation du modèle.",
        "tech": ["Python", "Computer Vision", "Machine Learning"],
        "collaborators": ["Idir Rebhi", "Nouria Benamara", "Mohamed Amine Terdjemane"],
        "links": [
            {"label_en": "Report (PDF)", "label_fr": "Rapport (PDF)", "url": "/documents/rapport-facial-recognition.pdf"},
            {"label_en": "Colab", "label_fr": "Colab", "url": "https://colab.research.google.com/drive/1Ybj56fBPSgsmG83lN4oUVSytkMtSJ8p2?usp=sharing"},
        ],
        "body_en": """
<h2>Brief</h2>
<p>Build a biometric facial recognition pipeline: detect faces, extract discriminative features, train a recognition model, and evaluate it properly.</p>
<h2>Build</h2>
<ul>
<li>Face detection and image preprocessing.</li>
<li>Feature extraction for face representation.</li>
<li>Model training on labeled face data.</li>
<li>A dedicated testing and evaluation phase.</li>
</ul>
<h2>Outcome</h2>
<p>An end-to-end pipeline from raw images to a trained recognition model, with a separate evaluation phase to measure performance — see the report for full metrics.</p>
<h2>Link to the thesis</h2>
<p>A direct precursor to the graduate research: both projects extract a stable, meaningful signal from image data — visual identity here, latent noise statistics there — through a deep learning pipeline.</p>
""",
        "body_fr": """
<h2>Objectif</h2>
<p>Construire un pipeline biométrique de reconnaissance faciale : détecter les visages, extraire des caractéristiques discriminantes, entraîner un modèle de reconnaissance, puis l'évaluer rigoureusement.</p>
<h2>Réalisation</h2>
<ul>
<li>Détection de visages et prétraitement des images.</li>
<li>Extraction de caractéristiques pour la représentation des visages.</li>
<li>Entraînement du modèle sur des données de visages étiquetées.</li>
<li>Une phase dédiée de test et d'évaluation.</li>
</ul>
<h2>Résultat</h2>
<p>Un pipeline complet, des images brutes jusqu'à un modèle de reconnaissance entraîné, avec une phase d'évaluation distincte pour mesurer la performance — voir le rapport pour les métriques détaillées.</p>
<h2>Lien avec le mémoire</h2>
<p>Un précurseur direct du travail de recherche du master : les deux projets extraient un signal stable et significatif à partir de données image — l'identité visuelle ici, les statistiques de bruit latent là — au travers d'un pipeline de deep learning.</p>
""",
    },
    {
        "slug": "character-recognition",
        "date": "2025",
        "featured": False,
        "title_en": "Handwritten Character Recognition: KNN vs. CNN",
        "title_fr": "Reconnaissance de caractères manuscrits : KNN vs CNN",
        "summary_en": "A side-by-side comparison of K-Nearest Neighbors and a convolutional network on the same recognition task.",
        "summary_fr": "Une comparaison directe entre K-plus-proches-voisins et un réseau convolutif sur la même tâche de reconnaissance.",
        "tech": ["Python", "KNN", "CNN", "Machine Learning"],
        "collaborators": ["Idir Rebhi"],
        "links": [
            {"label_en": "Report (PDF)", "label_fr": "Rapport (PDF)", "url": "/documents/rapport-character-recognition.pdf"},
            {"label_en": "Colab — KNN", "label_fr": "Colab — KNN", "url": "https://colab.research.google.com/drive/1cBHU_dhdKLigD5qXURLS0nL-VRUej9R4?usp=sharing"},
            {"label_en": "Colab — CNN", "label_fr": "Colab — CNN", "url": "https://colab.research.google.com/drive/1fLe75D3sn-UEmDuK7Ws-w-VQCAevm9NR?usp=sharing"},
        ],
        "body_en": """
<h2>Brief</h2>
<p>Put a classical method (K-Nearest Neighbors) head to head with a deep learning approach (CNN) on the same character recognition task, to build intuition for when each is worth its cost.</p>
<h2>Build</h2>
<ul>
<li>A KNN classifier with a tuned distance metric and neighborhood size.</li>
<li>A convolutional network trained on the same dataset.</li>
<li>Side-by-side accuracy and error analysis between the two.</li>
</ul>
<h2>Outcome</h2>
<p>The full comparison, including accuracy figures and error cases for both models, is in the linked report and notebooks.</p>
""",
        "body_fr": """
<h2>Objectif</h2>
<p>Confronter une méthode classique (K-plus-proches-voisins) à une approche de deep learning (CNN) sur la même tâche de reconnaissance de caractères, pour cerner dans quels cas chaque approche vaut son coût.</p>
<h2>Réalisation</h2>
<ul>
<li>Un classifieur KNN avec métrique de distance et voisinage ajustés.</li>
<li>Un réseau convolutif entraîné sur le même jeu de données.</li>
<li>Une analyse comparative de la précision et des erreurs entre les deux approches.</li>
</ul>
<h2>Résultat</h2>
<p>La comparaison complète, avec les taux de précision et les cas d'erreur des deux modèles, est disponible dans le rapport et les notebooks associés.</p>
""",
    },
    {
        "slug": "phylogenetic-trees",
        "date": "2025",
        "featured": False,
        "title_en": "Building Phylogenetic Trees",
        "title_fr": "Construction d'arbres phylogénétiques",
        "summary_en": "An algorithmic implementation for constructing phylogenetic trees from biological sequence data.",
        "summary_fr": "Une implémentation algorithmique pour construire des arbres phylogénétiques à partir de données biologiques.",
        "tech": ["Python", "Algorithms", "Bioinformatics"],
        "collaborators": ["Idir Rebhi", "Nouria Benamara", "Mohamed Amine Terdjemane"],
        "links": [
            {"label_en": "Slides", "label_fr": "Présentation", "url": "https://docs.google.com/presentation/d/1KJmR8K3N3Hu2_LyKrSwdDflu9mqUEiujR9MYB0RNoE0/edit?usp=sharing"},
            {"label_en": "Colab", "label_fr": "Colab", "url": "https://colab.research.google.com/drive/1Em2Km8wxgo7_DOcDVkZxZ7tBYm5y1mh1?usp=sharing"},
        ],
        "body_en": """
<h2>Brief</h2>
<p>Implement the algorithms needed to build phylogenetic trees from biological sequence data, applying graph theory to a bioinformatics problem.</p>
<h2>Build</h2>
<ul>
<li>Distance-based tree construction from biological data.</li>
<li>Graph-based representation and traversal of the resulting trees.</li>
<li>Visualization of the constructed trees.</li>
</ul>
<h2>Outcome</h2>
<p>A working implementation that builds and visualizes phylogenetic trees from input datasets — see the slides and notebook for the algorithmic details.</p>
""",
        "body_fr": """
<h2>Objectif</h2>
<p>Implémenter les algorithmes nécessaires à la construction d'arbres phylogénétiques à partir de données biologiques, en appliquant la théorie des graphes à un problème de bio-informatique.</p>
<h2>Réalisation</h2>
<ul>
<li>Construction d'arbres par méthode fondée sur les distances.</li>
<li>Représentation et parcours des arbres obtenus par théorie des graphes.</li>
<li>Visualisation des arbres phylogénétiques construits.</li>
</ul>
<h2>Résultat</h2>
<p>Une implémentation fonctionnelle capable de construire et de visualiser des arbres phylogénétiques à partir de jeux de données — voir la présentation et le notebook pour le détail algorithmique.</p>
""",
    },
    {
        "slug": "cinema-ontology",
        "date": "2024",
        "featured": False,
        "title_en": "A Cinema Ontology for the Semantic Web",
        "title_fr": "Une ontologie du cinéma pour le Web sémantique",
        "summary_en": "A formal ontology modeling films, people, roles and genres, designed for semantic web integration.",
        "summary_fr": "Une ontologie formelle modélisant films, personnes, rôles et genres, conçue pour le Web sémantique.",
        "tech": ["Ontology", "Semantic Web", "OWL"],
        "collaborators": ["Idir Rebhi"],
        "links": [
            {"label_en": "GitHub", "label_fr": "GitHub", "url": "https://github.com/RebhiIdir/cinema-ontology.git"},
            {"label_en": "Documentation (PDF)", "label_fr": "Documentation (PDF)", "url": "/documents/rapport-ontologie-cinema.pdf"},
        ],
        "body_en": """
<h2>Brief</h2>
<p>Model the domain of cinema — films, people, roles, genres, and how they relate — as a formal ontology suitable for semantic web use.</p>
<h2>Build</h2>
<ul>
<li>Domain analysis and concept modeling for cinema.</li>
<li>Formal ontology definition: classes, properties, relationships.</li>
<li>Design aimed at interoperability with semantic web tooling and queries.</li>
</ul>
<h2>Outcome</h2>
<p>A structured, queryable ontology of the cinema domain, documented and published on GitHub.</p>
""",
        "body_fr": """
<h2>Objectif</h2>
<p>Modéliser le domaine du cinéma — films, personnes, rôles, genres, et leurs relations — sous la forme d'une ontologie formelle adaptée au Web sémantique.</p>
<h2>Réalisation</h2>
<ul>
<li>Analyse du domaine et modélisation des concepts liés au cinéma.</li>
<li>Définition formelle de l'ontologie : classes, propriétés, relations.</li>
<li>Conception pensée pour l'interopérabilité avec les outils et requêtes du Web sémantique.</li>
</ul>
<h2>Résultat</h2>
<p>Une ontologie structurée et interrogeable du domaine du cinéma, documentée et publiée sur GitHub.</p>
""",
    },
    {
        "slug": "oil-mill-management",
        "date": "2024",
        "featured": False,
        "title_en": "Oil Mill Management Software (Bachelor's project)",
        "title_fr": "Logiciel de gestion pour une huilerie (projet de Licence)",
        "summary_en": "A desktop management application for an industrial oil mill, built as a final-year Bachelor's project.",
        "summary_fr": "Une application de bureau pour gérer une huilerie industrielle, réalisée comme projet de fin d'études de Licence.",
        "tech": ["Python", "PyQt5", "Qt Designer", "MySQL", "UML"],
        "collaborators": ["Idir Rebhi"],
        "links": [{"label_en": "GitHub", "label_fr": "GitHub", "url": "https://github.com/RebhiIdir/gestion_logiciels.git"}],
        "body_en": """
<h2>Brief</h2>
<p>Build a desktop management application for an industrial oil mill, as the final-year Bachelor's project in Computer Science, completed as a two-person team.</p>
<h2>Build</h2>
<ul>
<li>Desktop interface built with Python, PyQt5 and Qt Designer.</li>
<li>MySQL database for operational data.</li>
<li>Full UML modeling ahead of implementation.</li>
<li>A written dissertation documenting the design and development process.</li>
</ul>
<h2>Outcome</h2>
<p>A working desktop application covering the mill's core management workflows, delivered together with UML documentation and a final-year report.</p>
""",
        "body_fr": """
<h2>Objectif</h2>
<p>Construire une application de bureau pour gérer une huilerie industrielle, comme projet de fin d'études de Licence en informatique, réalisé en binôme.</p>
<h2>Réalisation</h2>
<ul>
<li>Interface de bureau construite avec Python, PyQt5 et Qt Designer.</li>
<li>Base de données MySQL pour les données opérationnelles.</li>
<li>Modélisation UML complète en amont de l'implémentation.</li>
<li>Un mémoire écrit documentant la démarche de conception et de développement.</li>
</ul>
<h2>Résultat</h2>
<p>Une application de bureau fonctionnelle couvrant les principaux workflows de gestion de l'huilerie, livrée avec sa documentation UML et un rapport de fin d'études.</p>
""",
    },
]

# ---------------------------------------------------------------------------
# CV
# ---------------------------------------------------------------------------
CV = {
    "core_skills": ["Machine Learning", "Deep Learning", "Computer Vision", "NLP", "Generative AI", "PyTorch / TensorFlow", "Scikit-learn / Diffusers", "Stable Diffusion pipelines"],
    "tools": ["PyTorch", "TensorFlow", "Scikit-learn", "Diffusers", "OpenCV", "NLTK", "NumPy", "Pandas", "Matplotlib", "Git & GitHub", "Jupyter Notebook", "Google Colab", "Kaggle", "LaTeX", "Linux/Bash"],
    "math": ["Linear Algebra", "Differential Calculus", "Probability & Statistics", "Optimization"],
    "languages": [
        {"en": "Kabyle — native", "fr": "Kabyle — langue maternelle"},
        {"en": "French — C1", "fr": "Français — C1"},
        {"en": "Arabic — fluent", "fr": "Arabe — courant"},
        {"en": "English — fluent", "fr": "Anglais — courant"},
    ],
}
