# Week 10 — Relationships & Modeling

> Visualizing relationships, correlations, and model fits to understand data patterns and predictive insights.

---

## 📖 Background & Motivation

Beyond distributions and comparisons, data visualization can help us understand **relationships** between variables and evaluate **model performance**. This week introduces how to visualize bivariate relationships, regression fits, residuals, and uncertainty, providing the foundation for interpreting linear and non‑linear trends.

Students will learn how to use scatterplots, trend lines, confidence intervals, and diagnostic plots to explore patterns and assess model fit, combining statistical modeling with visual storytelling.

---

## 🔎 Learning Objectives

- Create scatterplots to explore relationships between two or more variables.
- Visualize regression lines and confidence intervals.
- Understand correlation vs. causation and potential pitfalls.
- Evaluate model residuals visually to check fit and assumptions.
- Communicate model performance and uncertainty through effective visualization.

---

## 📚 Readings & Resources

- *Fundamentals of Data Visualization* — chapters on relationships & uncertainty.
- Seaborn: [regplot and lmplot](https://seaborn.pydata.org/tutorial/regression.html)
- Statsmodels: [OLS Regression](https://www.statsmodels.org/stable/examples/notebooks/generated/ols.html)
- [Visualizing Statistical Models](https://clauswilke.com/dataviz/statistical-models.html)

**Sample Data Sources:**

- Penguins dataset (bill length vs. flipper length)
- Housing price dataset (price vs. area)
- Gapminder (GDP vs. life expectancy)

---

## 🛠️ Setup Checklist

Ensure your environment includes:

```bash
pip install numpy pandas matplotlib seaborn statsmodels scikit-learn
```

**`scikit-learn` is on this list for the datasets, not for modeling.** We use it
only to fetch Ames and California housing; the regression itself is Statsmodels.
Both datasets are also cached as CSVs in the week 10 folder, so the notebooks run
without a network connection.

---

## 🧭 Lecture Outline

### Session 1 (75 min — Theory Focus)

1. Understanding relationships: correlation vs. causation (10 min)
2. Scatterplots and trend lines — visualizing associations (15 min)
3. Simple regression and confidence intervals (20 min)
4. Interpreting model fit and residuals visually (20 min)
5. Visual pitfalls: spurious correlation, overfitting, and omitted variables (10 min)
6. **Download** [everything for this week as one zip](week10/week10.zip) — both notebooks plus the `data/` folder they read from
7. Or the [modeling notebook](week10/Week10_relationships_modeling.ipynb) on its own, with [`ames.csv`](week10/data/ames.csv) and [`california.csv`](week10/data/california.csv) saved into a `data/` folder beside it

### Session 2 (75 min — Hands-on Focus)

1. Creating scatterplots with regression fits in Seaborn (20 min)
2. Adding confidence intervals and customizing aesthetics (15 min)
3. Building an OLS regression model with Statsmodels (20 min)
4. Visualizing residuals and diagnostic plots (15 min)
5. Mini‑workshop: interpret one key relationship in your dataset (5 min)
6. Continue in the same [modeling notebook](week10/Week10_relationships_modeling.ipynb) — it covers both sessions
7. A **Working version of linked plotly plot** can be [downloaded here](week10/linked_plotly_plots.ipynb)

---

## 💻 Starter Notebook Snippets

### Scatterplot with regression fit

```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("data/ames.csv")

sns.regplot(data=df, x="GrLivArea", y="SalePrice",
            scatter_kws={"alpha": 0.5}, line_kws={"color": "firebrick"})
plt.xlabel("Above-grade living area (sq ft)")
plt.ylabel("Sale price ($)")
plt.title("Living area vs sale price, Ames IA")
plt.show()
```

### One line per group

```python
two = df[df["HouseStyle"].isin(["1Story", "2Story"])]
sns.lmplot(data=two, x="GrLivArea", y="SalePrice", hue="HouseStyle",
           height=4.5, aspect=1.3, scatter_kws={"alpha": 0.5})
plt.show()
```

Two stories of the same square footage sell for **less** than one story of the
same square footage, and the slopes differ. A single pooled line hides both.

### Correlation matrix heatmap

```python
num = df[["SalePrice", "GrLivArea", "OverallQual", "TotalBsmtSF",
          "GarageArea", "LotArea", "YearBuilt"]]
sns.heatmap(num.corr(numeric_only=True), annot=True, fmt=".2f",
            cmap="vlag", center=0, square=True)
plt.title("Correlation matrix")
plt.show()
```

A **diverging** palette centered at zero, because the sign matters — Week 9
applied. A sequential palette would make -0.4 and +0.4 look like different
magnitudes.

### Regression with Statsmodels

```python
import statsmodels.api as sm

X = sm.add_constant(df["GrLivArea"])
model = sm.OLS(df["SalePrice"], X).fit()
print(model.summary())
```

### Residual plot — the most important plot of the week

```python
sns.residplot(data=df, x="GrLivArea", y="SalePrice", lowess=True,
              scatter_kws={"alpha": 0.5},
              line_kws={"color": "firebrick", "lw": 2})
plt.axhline(0, color="gray", lw=1)
plt.ylabel("Residual ($)")
plt.title("Residuals vs the predictor")
plt.show()
```

If a straight line described the data well, this would be a shapeless band
around zero. It is not: the spread widens with house size and the smoother
bends. Both are the model telling you something the scatterplot did not.

### When n is large: overplotting

```python
ca = pd.read_csv("data/california.csv")   # 20,640 block groups

fig, axes = plt.subplots(1, 3, figsize=(14, 4), sharey=True)
axes[0].scatter(ca["MedInc"], ca["MedHouseVal"], s=12)
axes[1].scatter(ca["MedInc"], ca["MedHouseVal"], s=6, alpha=0.08, color="steelblue")
hb = axes[2].hexbin(ca["MedInc"], ca["MedHouseVal"], gridsize=45, cmap="Blues", mincnt=1)
plt.colorbar(hb, ax=axes[2], label="block groups")
plt.show()
```

The plain scatter shows the *extent* of the data and nothing about its
*density*. Once the overplotting clears, a hard ceiling appears: 965 block
groups (4.7%) were capped at exactly $500,001.

---

## ⚖️ Where a variable comes from

Before the hands-on, we spend about fifteen minutes on a dataset we are **not**
using: Boston Housing, the standard regression teaching set for forty years,
removed from scikit-learn in version 1.2.

Its `black` column does not store the proportion of Black residents per town.
It stores `1000 * (Bk - 0.63) ** 2` — a squared term asserting that home values
rise as a town's Black population moves away from 63% in either direction. That
is a hypothesis somebody built into the data, not a measurement.

We check the formula ourselves, plot what it does, and find that undoing the
transform **reverses the sign** of the correlation with home value.

**Download** the [ethics case notebook](week10/Week10_ethics_dataset_case.ipynb)

The habit it is meant to build: read the data dictionary before you plot, and
plot the variable itself — not only its relationship to your outcome.

---

## 🧪 In-Class Activity

- Create scatterplots for multiple variable pairs and interpret patterns.
- Build a simple regression model and visualize fit and residuals.
- Discuss what model visualization reveals beyond summary statistics.
- Explore an example of spurious correlation and discuss implications.

---

## 🏠 Homework

1. Select a dataset of your choice (Try to avoid using integrated dataset).
2. Produce the following:
      - One **scatterplot** with regression fit and confidence interval.
      - One **correlation matrix heatmap**.
      - One **residual plot** illustrating model fit or deviation.
3. Include a brief interpretation (200–300 words) explaining:
      - What relationships you observed.
      - How visualization helped confirm or question your assumptions.
4. Submit `.ipynb` and `.html`.

**Rubric (10 pts)**

- Correct implementation of regression and correlation plots (4)
- Quality of interpretation and insights (3)
- Clarity of visualizations and labeling (2)
- Code reproducibility and documentation (1)

---

## 🧩 Optional Extensions

- Add multiple regression and visualize partial effects.
- Compare linear vs. non-linear fits.
- Visualize prediction intervals and uncertainty bands.
- Explore pairplots for multivariate relationships.

---

## ✅ Submission Checklist

Before submitting, make sure:

- Your assignment has fulfilled all the basic requirements listed above.

- Use Quarto to render the notebook into HTML and zip the files for submission.

- Double-check the visualizations and your reflections in the HTML are properly organized and displayed.

