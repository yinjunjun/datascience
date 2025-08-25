# Week 1 — Getting Started

> A Quarto/Panel-style module page for DATS 2102, implemented in Python/Jupyter.

---

## 📖 Background & Motivation

Data visualization is the bridge between raw data and human understanding. In data science, visualizations are not just decorative — they are powerful analytical tools that help reveal patterns, outliers, and trends that might remain hidden in tables or statistical summaries.

Well-designed visualizations can:

- Tell compelling, evidence-based stories that influence decision-making.
- Make complex concepts easier to grasp for diverse audiences.
- Identify and expose errors or inconsistencies in data during the exploratory stage.
- Enable collaboration between technical and non-technical stakeholders.

**Applications span across domains:**

- **Public health:** Tracking disease spread with interactive dashboards.
- **Climate science:** Mapping temperature anomalies over decades.
- **Business analytics:** Visualizing customer behavior or sales performance.
- **Machine learning:** Understanding model performance through ROC curves, feature importance charts, or clustering visualizations.

As data science projects grow in size and complexity, the ability to craft clear, truthful, and impactful visuals becomes as important as building the models themselves.

---

## 🔎 Learning Objectives

- Set up a reliable Python environment for data visualization.
- Navigate Jupyter Notebook/Lab and basic notebook hygiene (headings, code vs. markdown, restart & run all).
- Load and inspect tabular data with `pandas`.
- Produce the first charts with `matplotlib` and `seaborn`.

---

## 📚 Readings & Resources

- [JupyterLab User Guide](https://jupyterlab.readthedocs.io)
- [Python Tutorial](https://docs.python.org/3/tutorial/)
- [Pandas](https://pandas.pydata.org/docs/)
- [Matplotlib Pyplot](https://matplotlib.org/stable/tutorials/introductory/pyplot.html)
- [Seaborn Tutorials](https://seaborn.pydata.org/tutorial.html)

**Sample Data Sources for Practice:**

- [Seaborn Built-in Datasets](https://seaborn.pydata.org/generated/seaborn.load_dataset.html)
- [Kaggle Datasets](https://www.kaggle.com/datasets)
- [FiveThirtyEight Data](https://data.fivethirtyeight.com/)
- [Our World in Data](https://ourworldindata.org/)
- [Open Data DC](https://opendata.dc.gov/)
- [UCI Machine Learning Repository](https://archive.ics.uci.edu/)
- [data.gov](https://www.data.gov/)
- [GeoPandas Sample Datasets](https://geopandas.org/en/stable/getting_started/introduction.html#sample-data)

---

## 🛠️ Setup Checklist

1. **Install** Anaconda or Miniconda.
2. **Create/activate** environment:
   ```bash
   conda create -n dataviz python=3.12 -y
   conda activate dataviz
   ```
3. **Install libraries** (CPU-friendly baseline):
   ```bash
   pip install pandas numpy matplotlib seaborn plotly altair geopandas
   ```
4. **Launch JupyterLab**:
   ```bash
   jupyter lab
   ```
5. (Optional) IDEs you can use: VS Code, PyCharm, Sublime Text; or run in Google Colab.

**Troubleshooting**

- If `geopandas` fails on Windows, try `conda install -c conda-forge geopandas`.
- If Jupyter can’t see the env, run: `python -m ipykernel install --user --name dataviz --display-name "Python (dataviz)"`.

---

## 🧭 Lecture Outline

1. Course overview & syllabus tour
2. Why visualization in data science? (truthfulness, clarity, audience)
3. Notebook workflow: cells, markdown, restart & run all, saving
4. First dataset in `pandas` (CSV → DataFrame → quick EDA)
5. First plots: `matplotlib` bar/line; `seaborn` scatter/hist

---

## 💻 Starter Notebook Snippets

### Load a tiny dataset

```python
import pandas as pd

cities = pd.DataFrame({
    "city": ["DC", "NY", "LA", "Chicago", "Houston"],
    "population": [712_816, 8_336_817, 3_898_747, 2_746_388, 2_304_580]
})

cities.head()
```

### First charts (matplotlib → seaborn)

```python
import matplotlib.pyplot as plt
import seaborn as sns

# Matplotlib bar chart
plt.bar(cities["city"], cities["population"])
plt.title("Population by City")
plt.xlabel("City"); plt.ylabel("Population")
plt.show()

# Seaborn bar chart
sns.barplot(data=cities, x="city", y="population")
plt.title("Population by City (Seaborn)")
plt.show()
```

### Quick EDA helpers

```python
cities.describe(include="all")
print("Missing values by column:\n", cities.isna().sum())
```

---

## 🧪 In-Class Activity

Using `seaborn.load_dataset("penguins")`:

- Make a scatterplot of **flipper\_length\_mm vs body\_mass\_g** colored by **species**.
- Add axis labels, a title, and a legend with a better title.
- Try a `seaborn.pairplot` to see relationships across multiple variables.

**Hints**

```python
penguins = sns.load_dataset("penguins").dropna()
ax = sns.scatterplot(data=penguins, x="flipper_length_mm", y="body_mass_g", hue="species")
ax.set(title="Penguins: Flipper vs Body Mass", xlabel="Flipper length (mm)", ylabel="Body mass (g)")
```

---

## 🏠 Homework (Due before Week 2)

1. Set up your environment and confirm you can open/run notebooks.
2. Import a **CSV of your choice** and submit one notebook that includes:
   - A short markdown description of the dataset (source, what, who, when).
   - Top 5 rows, `.info()`, and `.describe()`.
   - One **bar** or **histogram** plot, and one **scatter** plot.
   - A brief paragraph reflecting on one insight + one limitation of the data.
3. Export notebook to HTML (`File → Save and Export Notebook As`) and upload both `.ipynb` and `.html`.

**Rubric (10 pts)**

- Reproducible environment & clean notebook structure (2)
- Correct loading/inspection & basic EDA (3)
- Two charts with sensible labels/titles (3)
- Insight + limitation reflection (2)

---

## 🧩 Optional Extensions

- Try the same chart in both `matplotlib` and `seaborn`; note the pros/cons you observe.
- Install `altair` (a declarative statistical visualization library for Python, built on top of Vega-Lite, useful for creating interactive charts with minimal code) and create the same scatterplot with tooltips.
- If you’re comfortable with maps, test your `geopandas` install (`geopandas.datasets.get_path('naturalearth_lowres')`).

---

## ✅ Submission Checklist

This section, for example, lists everything you should verify before submitting your work for Week 1.

-

