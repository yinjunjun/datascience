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

Ensure your environment includes:

```bash
pip install seaborn matplotlib colorcet pandas
```

Confirm you can load sample datasets and apply color palettes using Seaborn and Matplotlib.

---

## 🧭 Lecture Outline

### Session 1 (75 min — Theory Focus)

1. Introduction: Why color matters in visualization (10 min)
2. Color theory basics — hue, saturation, brightness (15 min)
3. Types of color schemes — sequential, diverging, categorical (20 min)
4. Color perception & accessibility — common pitfalls (15 min)
5. Demonstration: testing palettes with simulators and contrast checkers (15 min)

### Session 2 (75 min — Hands-on Focus)

1. Experiment with Seaborn and Matplotlib color palettes (20 min)
2. Create side-by-side examples: good vs poor palette use (20 min)
3. Apply ColorBrewer and Colorcet palettes to the previous week’s map visualizations (20 min)
4. Workshop: redesign one of your past charts for color accessibility (15 min)

---

## 💻 Starter Notebook Snippets

### Using Seaborn palettes

```python
import seaborn as sns
import matplotlib.pyplot as plt

# Sequential palette
sns.palplot(sns.color_palette("Blues", 8))
plt.title("Sequential palette example")

# Diverging palette
sns.palplot(sns.diverging_palette(220, 20, n=8))
plt.title("Diverging palette example")

# Categorical palette
sns.palplot(sns.color_palette("Set2", 8))
plt.title("Categorical palette example")
plt.show()
```

### Applying color palettes to a chart

```python
penguins = sns.load_dataset("penguins").dropna()
sns.scatterplot(data=penguins, x="flipper_length_mm", y="body_mass_g", hue="species", palette="Set2")
plt.title("Categorical color palette example")
plt.show()
```

### Testing color palettes for accessibility

```python
# Example: simulate grayscale or color blindness
import matplotlib.colors as mcolors
import numpy as np

# Convert to grayscale to check luminance contrast
img = np.linspace(0, 1, 256).reshape(1, -1)
plt.imshow(img, cmap="viridis", aspect="auto")
plt.title("Luminance contrast check (Viridis)")
plt.axis('off')
plt.show()
```

---

## 🧪 In-Class Activity

- Create 3 mini visualizations (one sequential, one diverging, one categorical) using Seaborn.
- Use ColorBrewer to test and adjust color schemes.
- Simulate color blindness and discuss readability.
- Redesign a prior week’s map or chart with improved accessibility.

---

## 🏠 Homework (Due next Thursday, Oct 30)

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
