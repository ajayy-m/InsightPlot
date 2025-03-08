import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Upload CSV file
st.title("InsightPlot - Automated Visualization")
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file:
    # Read CSV
    df = pd.read_csv(uploaded_file)
    
    # Show sample data
    st.write("### Sample Data")
    st.write(df.head())

    # Select visualization type
    plot_type = st.selectbox("Select a visualization type:", ["Bar Chart", "Scatter Plot", "Histogram"])

    # Automatically detect columns
    x_col = st.selectbox("Select X-axis:", df.columns)
    y_col = st.selectbox("Select Y-axis:", df.columns) if plot_type != "Histogram" else None

    # Generate plot
    fig, ax = plt.subplots()

    if plot_type == "Bar Chart":
        sns.barplot(x=df[x_col], y=df[y_col], ax=ax, palette="viridis")
        ax.set_title(f"{y_col} vs {x_col}")
        ax.set_xlabel(x_col)
        ax.set_ylabel(y_col)

    elif plot_type == "Scatter Plot":
        sns.scatterplot(x=df[x_col], y=df[y_col], ax=ax, hue=df[x_col], palette="coolwarm")
        ax.set_title(f"Scatter Plot of {y_col} vs {x_col}")
        ax.set_xlabel(x_col)
        ax.set_ylabel(y_col)

    elif plot_type == "Histogram":
        sns.histplot(df[x_col], bins=20, kde=True, ax=ax, color="blue")
        ax.set_title(f"Distribution of {x_col}")
        ax.set_xlabel(x_col)
        ax.set_ylabel("Frequency")

    # Show the plot
    st.pyplot(fig)
