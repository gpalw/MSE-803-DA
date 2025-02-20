import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
print("Current working directory:", os.getcwd())


def plot_data(df, mode="histogram"):
    """
    Generate data visualization plots.

    Parameters:
        df (pd.DataFrame): The dataset to be visualized.
        mode (str): "histogram" - Generate 4 histograms.
                    "mixed" - Generate 4 different types of plots.
    """
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))

    if mode == "histogram":
        # 🎯 **Mode 1: Generate 4 histograms**
        for i, column in enumerate(df.columns[:4]):  # Select the first 4 columns
            ax = axes.flatten()[i]  # Select subplot position
            df[column].hist(
                bins=30, alpha=0.7, edgecolor="black", ax=ax, color="orange"
            )
            ax.set_title(f"Histogram ({column})")

    elif mode == "mixed":
        # 🎯 **Mode 2: Generate 4 different types of plots**
        # Histogram
        df["Normal_Distribution"].hist(
            bins=30, alpha=0.7, edgecolor="black", ax=axes[0, 0], color="orange"
        )
        axes[0, 0].set_title("Histogram (Normal Distribution)")

        # Box Plot
        sns.boxplot(
            data=df[["Normal_Distribution", "Uniform_Distribution"]],
            ax=axes[0, 1],
            palette="Oranges",
        )
        axes[0, 1].set_title("Box Plot (Normal & Uniform)")

        # Scatter Plot
        axes[1, 0].scatter(
            df["Normal_Distribution"],
            df["Exponential_Distribution"],
            alpha=0.5,
            color="orange",
            edgecolors="black",
        )
        axes[1, 0].set_xlabel("Normal Distribution")
        axes[1, 0].set_ylabel("Exponential Distribution")
        axes[1, 0].set_title("Scatter Plot")

        # Violin Plot
        sns.violinplot(
            data=df[["Poisson_Distribution"]], ax=axes[1, 1], palette="Oranges"
        )
        axes[1, 1].set_title("Violin Plot (Poisson Distribution)")

    else:
        raise ValueError("Invalid mode. Use 'histogram' or 'mixed'.")

    # Adjust layout and display
    plt.tight_layout()
    plt.show()


# Load dataset
file_path = "Sample_Data_for_Activity (1).csv"
df = pd.read_csv(file_path)

# Generate 4 histograms
plot_data(df, mode="histogram")

# Generate 4 different types of plots
plot_data(df, mode="mixed")
