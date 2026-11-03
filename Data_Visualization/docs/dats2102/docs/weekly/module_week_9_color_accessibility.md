# Week 9 — Color & Accessibility

> Understanding color theory, palette selection, and accessibility best practices in data visualization.

---

## 📖 Background & Motivation

Color is one of the most powerful and expressive tools in visualization. It can highlight differences, show magnitude, encode categories, or evoke emotion—but it can also **distort, confuse, or exclude** if not used carefully. This module explores color theory, perceptual uniformity, and accessibility guidelines to ensure your visuals communicate effectively to all audiences.

We will discuss the use of color in sequential, diverging, and categorical scales, and how to design visualizations that remain interpretable for viewers with color vision deficiencies.

---

## 🔎 Learning Objectives

- Distinguish between **sequential**, **diverging**, and **categorical** color schemes.
- Select appropriate palettes based on data type and context.
- Apply color theory concepts (hue, saturation, luminance) to improve legibility.
- Use color tools to ensure accessibility for all users.
- Test visualizations for color blindness and accessibility compliance.

---

## 📚 Readings & Resources

- *Fundamentals of Data Visualization* — chapters on color and perception.
- [ColorBrewer2](https://colorbrewer2.org/) — tool for choosing effective color schemes.
- [Colorcet](https://colorcet.holoviz.org/index.html) - Perceptually accurate 256-color colormaps
- [Adobe Color](https://color.adobe.com/create/color-wheel) — create custom palettes.
- [Coblis — Color Blindness Simulator](https://www.color-blindness.com/coblis-color-blindness-simulator/)
- [Accessible Data Visualization Guide (W3C)](https://www.w3.org/WAI/tutorials/images/complex/)
- [Seaborn color palettes documentation](https://seaborn.pydata.org/tutorial/color_palettes.html)

**Sample Data Sources:**

- Gapminder dataset (for categorical and quantitative mapping)
- U.S. demographic data (for diverging and sequential maps)
- Simulated survey data (for categorical comparison)

---

## 🛠️ Setup Checklist

Ensure your environment includes everything the notebook imports:

```bash
pip install numpy pandas matplotlib seaborn colorcet plotly altair vega_datasets geopandas mapclassify
```

**Don't skip `mapclassify`.** The notebook never imports it by name, but GeoPandas
needs it the moment you pass `scheme="Quantiles"` or `scheme="FisherJenks"` to
`.plot()`. Without it those calls fail with an error that does not mention the
missing package.

Confirm you can load the sample datasets (`seaborn`, `vega_datasets`, `plotly.express`
all download theirs on first use, so you need a network connection) and that
`data/map_us_only.geojson` and `data/unemployment.csv` sit next to the notebook.

---

## 🧭 Lecture Outline

### Session 1 (Theory + Hands-on)

1. Introduction: Why color matters in visualization
2. Color theory basics — hue, saturation, brightness
3. Types of color schemes — sequential, diverging, categorical
4. Color perception & accessibility — common pitfalls
5. Experiment with Seaborn and Matplotlib color palettes
6. Apply ColorBrewer and Colorcet palettes to the previous week’s map visualizations
7. Classification and class breaks — quantile vs equal-interval vs Fisher-Jenks
8. **Download** the [Jupyter Notebook and Data](week9/week9.zip)

---

## 💻 Starter Notebook Snippets

These are taken from the course notebook (`Week09_Color_Accessibility_Demos.ipynb`
in the download above), so you can follow along or run them on your own data.

### 1. Match the palette to the data type

```python
import numpy as np
import matplotlib.pyplot as plt

# Sequential: one direction, low to high
data_seq = np.outer(np.linspace(0, 1, 120), np.ones(120))
plt.imshow(data_seq, aspect="auto", cmap="viridis")
plt.title("Sequential colormap: viridis (ordered data)")
plt.colorbar()
plt.show()

# Diverging: a meaningful midpoint at 0
data_div = np.outer(np.linspace(-1, 1, 120), np.ones(120))
plt.imshow(data_div, aspect="auto", cmap="coolwarm")
plt.title("Diverging colormap: coolwarm (deviation around 0)")
plt.colorbar()
plt.show()
```

### 2. Check text contrast against WCAG

```python
def srgb_to_linear(c):
    """One sRGB channel (0-255) -> linear light (0-1).

    WCAG defines luminance on linear light, so the gamma has to come off first.
    """
    c = c / 255.0
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4


def rel_luminance(rgb):
    r, g, b = (srgb_to_linear(v) for v in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast_ratio(fg, bg):
    L1, L2 = rel_luminance(fg), rel_luminance(bg)
    hi, lo = max(L1, L2), min(L1, L2)
    return (hi + 0.05) / (lo + 0.05)


contrast_ratio((33, 33, 33), (255, 255, 255))     # 16.10 -> passes
contrast_ratio((150, 150, 150), (255, 255, 255))  #  2.96 -> fails (needs 4.5)
```

### 3. Simulate color vision deficiency

```python
import numpy as np

def srgb_to_linear_arr(c):
    return np.where(c <= 0.04045, c / 12.92, ((c + 0.055) / 1.055) ** 2.4)


def linear_to_srgb_arr(c):
    c = np.clip(c, 0, 1)
    return np.where(c <= 0.0031308, c * 12.92, 1.055 * c ** (1 / 2.4) - 0.055)


# Vienot, Brettel & Mollon (1999). The matrix is only valid in LINEAR light,
# so undo the sRGB gamma first -- skipping that step overstates the damage and
# can make a safe palette look as bad as a risky one.
DEUTERANOPIA = np.array([[ 0.2920, 0.7054, -0.0003],
                         [ 0.2934, 0.7089,  0.0000],
                         [-0.0209, 0.0272,  0.9922]])


def simulate_cvd(rgb, M):
    """rgb: array of floats 0-1, shape (..., 3)."""
    lin = srgb_to_linear_arr(np.asarray(rgb, float))
    out = np.clip(lin.reshape(-1, 3) @ M.T, 0, 1).reshape(np.shape(rgb))
    return np.clip(linear_to_srgb_arr(out), 0, 1)
```

Run it on a red/green pair and a blue/orange pair and compare how far apart the
two colors stay. Red and green collapse into two olives; blue and orange do not.

### 4. Class breaks change the map

```python
import pandas as pd
import geopandas as gpd

polys = gpd.read_file("data/map_us_only.geojson")
attrs = pd.read_csv("data/unemployment.csv")
g = pd.merge(polys, attrs, left_on="GEO_ID", right_on="Geo_GEO_ID", how="left")
g = g.to_crs("ESRI:102003")          # equal-area projection

# Social Explorer table A17002. The unemployment rate is
# unemployed / civilian labor force -- NOT a share of total population.
g["unemp_rate"] = g["SE_A17002_006"] / g["SE_A17002_004"] * 100

for scheme in ("EqualInterval", "Quantiles", "FisherJenks"):
    ax = g.plot(column="unemp_rate", cmap="OrRd", scheme=scheme, k=5,
                legend=True, edgecolor="white", linewidth=0.2)
    ax.set_title(scheme)
    ax.set_axis_off()
```

Same data, same palette, three different maps. Say in your caption which
classification you used and why.

---

## 🧪 In-Class Activity

- Create 3 mini visualizations (one sequential, one diverging, one categorical) using Seaborn.
- Use ColorBrewer to test and adjust color schemes.
- Simulate color blindness and discuss readability.
- Redesign a prior week’s map or chart with improved accessibility.

---

## 🏠 Homework

1. Choose one of your visualizations from a previous week and redesign it to improve color and accessibility.
2. Include:
      - One **before-and-after comparison** of color schemes.
      - Discussion (150–250 words) of how your new design improves clarity and inclusivity.
      - Verification of color accessibility (using simulator or contrast tool).
3. Submit `.ipynb` and `.html`.

**Rubric (10 pts)**

- Appropriate use of color schemes (3)
- Accessibility testing and discussion (3)
- Clarity and improvement of redesigned visual (2)
- Reproducibility and documentation (2)

---

## 🧩 Optional Extensions

- Explore `colorcet` for perceptually uniform colormaps.
- Create a color legend that works both in grayscale and color.
- Compare the performance of different palettes in color‑blind simulation.

---

## ✅ Submission Checklist

Before submitting, make sure:

- Your assignment has fulfilled all the basic requirements listed above.

- Use Quarto to render the notebook into HTML and zip the files for submission.

- Double-check the visualizations and your reflections in the HTML are properly organized and displayed.
