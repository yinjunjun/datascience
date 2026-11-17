# Week 11 — Uncertainty & Error Visualization

> Communicating uncertainty, variability, and confidence through effective visual representations.

---

## 📖 Background & Motivation

Data visualizations often emphasize what is known—but communicating what is **uncertain** is equally critical for honest and transparent storytelling. This week explores how to represent statistical uncertainty, variability, and measurement error using visual design. Students will learn how to use error bars, confidence bands, sampling distributions, and bootstrap visualizations to convey uncertainty clearly and responsibly.

---

## 🔎 Learning Objectives

- Understand the sources of uncertainty in data and models.
- Differentiate between standard deviation, standard error, and confidence interval.
- Visualize uncertainty with error bars, ribbons, and confidence bands.
- Communicate uncertainty effectively without misleading interpretation.
- Apply resampling or bootstrapping methods for visual inference.

---

## 📚 Readings & Resources

- *Fundamentals of Data Visualization* — Chapter on uncertainty.
- [Why We Should Visualize Uncertainty (Nature)](https://www.nature.com/articles/d41586-020-00548-9)
- [Seaborn confidence intervals documentation](https://seaborn.pydata.org/tutorial/regression.html#statistical-estimation-and-bootstrapping)
- [Visualizing Uncertainty (Information is Beautiful)](https://informationisbeautiful.net/visualizations/visualizing-uncertainty/)

**Sample Data Sources:**

- Ames, Iowa home sales (the Week 10 data) — used in the hands-on notebook
- Simulated sample means and bootstraps
- Gapminder GDP data (yearly changes)
- Experimental datasets (e.g., survey or sensor data)

---

## 🛠️ Setup Checklist

Ensure your environment includes:

```bash
pip install numpy pandas matplotlib seaborn scipy scikit-learn plotly altair
```

The hands-on notebook uses `scikit-learn` for resampling and for the bootstrap regression fits, `plotly` for the interactive ensemble plot, and `altair` for one optional section.

Verify that Seaborn is configured to display confidence intervals and that Matplotlib renders error bars correctly.

---

## 🧭 Lecture Outline

### Session 1 (Theory Focus)

1. What is uncertainty? Sources in data collection and modeling
2. Standard deviation, standard error, and confidence intervals
3. Visual metaphors for uncertainty (error bars, ribbons, shaded regions)
4. Common pitfalls: false precision, overlapping intervals, and transparency
5. Case studies: how media and research visualize uncertainty

### Session 2 (Hands-on Focus)

1. Plotting error bars with Seaborn and Matplotlib
2. Adding confidence bands around regression lines
3. Simulating sampling distributions and bootstrap intervals
4. Improve one of your previous plots by including uncertainty
5. **Download** the hands-on [Jupyter Notebook](week11/week11_uncertainty_visualization.ipynb). It uses the Ames home sales from Week 10 and loads them from the course site, or from [`ames.csv`](week11/data/ames.csv) saved into a `data/` folder beside it.

---

## 💻 Starter Notebook Snippets

### Adding error bars

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Simulated means and standard errors
groups = ['A','B','C','D']
means = [20, 23, 25, 22]
se = [1.5, 2.0, 1.2, 1.8]

plt.bar(groups, means, yerr=se, capsize=5, color='steelblue')
plt.title('Bar chart with error bars')
plt.ylabel('Mean value')
plt.show()
```

### Group means with a 95% confidence interval

```python
import seaborn as sns

df = pd.read_csv("data/ames.csv")

# Six groups of homes by living area, each with about the same number of homes
df["area_bin"] = pd.qcut(df["GrLivArea"], q=6, duplicates="drop")

sns.barplot(data=df, x="area_bin", y="SalePrice", errorbar=('ci', 95), capsize=.15)
plt.xticks(rotation=15, ha="right")
plt.xlabel("Living area (sq ft) — quantile bins")
plt.ylabel("Sale price ($)")
plt.title("Mean Sale Price by Living Area with 95% CI")
plt.show()
```

The interval on the last bar is the widest: the largest homes vary the most in
price, so their mean is the least certain.

### Confidence band around a regression line

```python
ci = 95     # try 70, then 99, and watch the band change width

g = sns.lmplot(data=df, x="GrLivArea", y="SalePrice", ci=ci,
               height=4.5, aspect=1.4, scatter_kws={"alpha": 0.5})
g.fig.suptitle(f"Regression with {ci}% Confidence Interval", y=1.03)
plt.show()
```

The band is the uncertainty in the **line**, not in where one home will fall. It
is narrow in the middle, where most homes are, and widens toward the large homes.

### Bootstrap sampling distribution

```python
from sklearn.utils import resample

means = []
for i in range(1000):
    sample = resample(df["SalePrice"], random_state=i)
    means.append(sample.mean())

sns.histplot(means, kde=True, bins=30)
plt.axvline(np.mean(means), color='red', linestyle='--', label='Bootstrap mean')
plt.xlabel("Mean sale price ($)")
plt.title("Bootstrap Distribution of Mean Sale Price (1000 resamples)")
plt.legend()
plt.show()
```

Each resample draws 1,460 homes from the data with replacement and records the
mean. The spread of those 1,000 means shows how much the average would move if
we had sampled a different set of homes.

---

## 🧪 In-Class Activity

- Compare bar charts with and without error bars — what changes in interpretation?
- Explore how sample size affects confidence interval width.
- Visualize a bootstrap sampling distribution and discuss its meaning.
- Redesign a visualization from your earlier project to include uncertainty representation.

---

## 🏠 Homework

1. Select a dataset of your choice (or use one from a prior week).
2. Produce:
      - One **bar or line chart** with error bars or confidence bands.
      - One **bootstrap visualization** or sampling distribution.
      - A short (200–300 words) reflection on how uncertainty affects the interpretation of your results.
3. Submit `.ipynb` and `.html`.

**Rubric (10 pts)**

- Correct calculation and visualization of uncertainty (4)
- Clarity and labeling of intervals/bands (2)
- Quality of interpretation and reflection (3)
- Reproducibility and documentation (1)

---

## 🧩 Optional Extensions

- Compare 68%, 90%, and 95% confidence intervals visually.
- Add uncertainty bands to model predictions from Statsmodels.
- Visualize uncertainty in map-based data (e.g., population margins of error).

---

## ✅ Submission Checklist

Before submitting, make sure:

- Your assignment has fulfilled all the basic requirements listed above.

- Use Quarto to render the notebook into HTML and zip the files for submission.

- Double-check the visualizations and your reflections in the HTML are properly organized and displayed.
