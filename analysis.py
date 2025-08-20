# 22f3003115@ds.study.iitm.ac.in   <-- Email ID as required

import marimo

__generated_with__ = "0.7.0"
app = marimo.App()


# -------------------------------
# Cell 1: Import data and create raw dataset
# -------------------------------
@app.cell
def raw_data():
    import numpy as np
    import pandas as pd

    # Simulated dataset
    np.random.seed(42)
    df = pd.DataFrame({
        "X": np.linspace(0, 100, 200),
        "Y": np.linspace(0, 100, 200) * 0.5 + np.random.normal(0, 5, 200)
    })
    return df


# -------------------------------
# Cell 2: Interactive filter on X variable
# -------------------------------
@app.cell
def filter_widget():
    import marimo as mo
    slider = mo.ui.slider(0, 100, 10, label="Minimum X value")
    return slider


# -------------------------------
# Cell 3: Filter data (depends on raw_data + filter_widget)
# -------------------------------
@app.cell
def filtered_data(raw_data, filter_widget):
    # Filtering based on slider input
    filtered = raw_data[raw_data["X"] >= filter_widget.value]
    return filtered


# -------------------------------
# Cell 4: Visualization (depends on filtered_data)
# -------------------------------
@app.cell
def plot(filtered_data):
    import matplotlib.pyplot as plt
    import marimo as mo

    fig, ax = plt.subplots()
    ax.scatter(filtered_data["X"], filtered_data["Y"], alpha=0.7)
    ax.set_title("Scatter plot of X vs Y (filtered)")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    mo.pyplot(fig)


# -------------------------------
# Cell 5: Dynamic markdown explanation
# -------------------------------
@app.cell
def explanation(filter_widget, filtered_data):
    import marimo as mo
    mo.md(f"""
    ### Analysis Summary
    - Minimum X chosen: **{filter_widget.value}**
    - Remaining data points: **{len(filtered_data)}**

    This demonstrates how filtering affects the dataset and the observed relationship
    between **X** and **Y**.
    """)


if __name__ == "__main__":
    app.run()

