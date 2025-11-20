# Final Project — DATS 2102: Data Visualization for Data Science

> A capstone demonstrating your end‑to‑end visualization workflow: question → data → wrangling → analysis → visuals → narrative.

---

## 🎯 Purpose & Scope

The final project synthesizes everything you’ve learned across the course. You will identify a compelling question, gather/curate data, apply rigorous wrangling, design effective visualizations (static and/or interactive), and communicate clear insights for a non‑expert audience.

---

## ✅ Learning Objectives

By the end, you will be able to:

- Frame an analytical question and select appropriate data sources.
- Apply robust **pandas** wrangling (selection/filtering, sorting, groupby+aggregation, joins/merges, tidy reshaping).
- Design visuals aligned to purpose: distributions, comparisons, relationships, uncertainty (Weeks 3–11).
- Integrate specialized techniques as appropriate: **mapping** (Week 8), **color & accessibility** (Week 9), **ML/NLP visualizations** (Week 12).
- Communicate a coherent data story with clear text, labels, and annotations (Week 7).
- Ensure reproducibility and ethical, accessible practice throughout.

---

## 🧵 Project Tracks (Mix thoughtfully)

- **A. Data Story (EDA to Insight):** A narrative with 6–10 well‑designed figures revealing a substantive finding.
- **B. Map‑Based Analysis:** Spatial joins/classification; 2+ choropleths and at least one interactive map (Folium/Plotly). Discuss projection/CRS choices.
- **C. Interactive Mini‑Dashboard:** A focused multi‑view interface (Plotly, Panel, or simple Jupyter widgets) with linked visuals and annotations.
- **D. ML/NLP Visualization:** Train a simple model; show feature importance, confusion matrix/ROC, and an NLP visualization (word cloud or topic clusters).

---

## 📦 Required Deliverables (submit all)

1. **Jupyter Notebook(s)** with narrative markdown and all figures.

2. **Quarto rendered HTML(s) of the notebook(s).**

3. **A data folder or data access instructions** (URLs, retrieval scripts). If restricted, include a synthetic sample and schema.

4. **Data dictionary** (variables, units, definitions, any transformations).

5. **Slide deck (7–8 minutes)**  for in‑class presentation (PDF or PPTX).

6. A recorded short **video/audio (1 to 3 minutes)** for demonstrating your work (e.g., using Zoom).

7. **Optional:** publish your work via GitHub Pages or Quarto Pub and include the URL in the submission. 

---

## 🗓️ Milestones & Timeline

- **Finals Week:** In‑class presentation + final submission of all artifacts.

---

## 🔍 Data Sources (suggested)

- **Open Data DC**, **Our World in Data**, **Gapminder**, **FiveThirtyEight**, World Bank, BLS/BEA, NOAA, US DOT BTS, or vetted institutional repositories.
- Your own research/organizational data (ensure permission and anonymization if needed).

> **Cite all datasets with links and access dates** in your README and slides.

---

## 🧰 Allowed Tools

- **Core:** Python (pandas, numpy, matplotlib, seaborn, plotly), Jupyter/Quarto.
- **Spatial (optional):** geopandas, folium, mapclassify.
- **ML/NLP (optional):** scikit‑learn, wordcloud, BERTopic (or similar).
- **Design & accessibility:** ColorBrewer/Colorcet, contrast checkers; adhere to Week 9 guidance.

---

## 🧪 Quality Expectations

- **Audience‑appropriate** explanations; avoid jargon without definitions.
- **Effective encodings** and **color choices**; legends/direct labels; informative titles and captions.
- **Uncertainty** shown where appropriate (error bars, bands, bootstrap summaries).
- **Accessibility:** palette choices that remain interpretable with color‑vision deficiencies; sufficient contrast; alt text in slides where feasible.
- **Reproducibility:** clean execution top‑to‑bottom; deterministic seeds; clear env instructions.
- **Ethics:** respect license/terms; anonymize sensitive fields; discuss limitations and potential biases.

---

## 🧮 Grading Rubric (40 pts total)

- **Problem Framing & Relevance (5 pts):** Clear question, audience, and motivation.
- **Data Acquisition & Ethics (4 pts):** Credible sources, citations, permissions/privacy considerations.
- **Wrangling & Reproducibility (6 pts):** Correct, readable code using selection/sorting, groupby+agg, joins, tidy reshaping; runnable notebook & env notes.
- **Visualization Quality & Variety (10 pts):** Appropriate chart choices (distributions, comparisons, relationships, uncertainty; maps/ML/NLP as relevant), labeling/annotations, narrative flow.
- **Analysis & Insight (7 pts):** Sound reasoning, limitations addressed, meaningful takeaways.
- **Communication & Writing (4 pts):** Clarity of markdown narrative, captions, and organization; slide design.
- **Presentation & Q&A (4 pts):** Timing, delivery, visual clarity, ability to answer questions.

---

## 🗣️ Presentation Guidelines (7–8 minutes)

- Open with the problem and why it matters (≤ 60 seconds).
- Show **3–5 strongest visuals**; narrate what the viewer should notice.
- Include at least one slide on **methods/wrangling** (brief) and one on **limitations & next steps**.
- End with a **single insight slide** (one sentence + supporting figure).

---

## 🤝 Collaboration, AI, and Academic Integrity

- Follow course **AI policy**: AI tools may assist with **scaffolding** (formatting code, minor debugging, grammar). They may **not** fabricate results or replace your own analysis/interpretation. Disclose any AI assistance in the README.
- Cite all data, code snippets, and external visuals. Plagiarism or undisclosed AI‑generated work violates university policy.

---

## ✅ Submission Checklist

Before submitting on Blackboard, ensure:

- Your project has fulfilled all the basic requirements listed above.
- Used Quarto to render the notebook into HTML and zip the files for submission.
- Double-check the visualizations and your reflections in the HTML are properly organized and displayed.
- Do not forget the README file, the slides, and the short video/audio

---

## 💡 Tips for Success

- Start with a sketch of your story and a list of figures you’ll need.
- Iterate: rough plots → refine encodings/labels → polish.
- Prefer fewer, better figures over many similar ones.
- Keep code cells small and well‑commented; use functions where helpful.

