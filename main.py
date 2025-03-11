import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import io

st.set_page_config(page_title="InsightPlot - Data Visualization App", layout="wide")
st.title("📊 InsightPlot - Automated Data Visualization & Analysis")

# Sidebar Navigation
st.sidebar.header("Navigation")
menu = st.sidebar.radio("Go to", ["Upload & View Data", "Visualize Data", "Data Insights"])

# Upload CSV file
uploaded_file = st.sidebar.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    
    if menu == "Upload & View Data":
        st.write("### Sample Data")
        st.dataframe(df)
        
        st.write("### Data Summary")
        st.write(df.describe())
        
        st.write("### Missing Values")
        st.write(df.isnull().sum())

    elif menu == "Visualize Data":
        plot_type = st.sidebar.selectbox("Select a visualization type:", 
                                         ["Bar Chart", "Scatter Plot", "Histogram", "Box Plot", "Line Plot", "Heatmap", "Pairplot"])
        
        x_col = st.sidebar.selectbox("Select X-axis:", df.columns)
        y_col = st.sidebar.selectbox("Select Y-axis:", df.columns) if plot_type not in ["Histogram", "Heatmap", "Pairplot"] else None
        
        fig, ax = plt.subplots(figsize=(10, 6))
        
        if plot_type == "Bar Chart":
            sns.barplot(x=df[x_col], y=df[y_col], ax=ax, palette="viridis")
        elif plot_type == "Scatter Plot":
            sns.scatterplot(x=df[x_col], y=df[y_col], ax=ax, hue=df[x_col], palette="coolwarm")
        elif plot_type == "Histogram":
            sns.histplot(df[x_col], bins=20, kde=True, ax=ax, color="blue")
        elif plot_type == "Box Plot":
            sns.boxplot(x=df[x_col], y=df[y_col], ax=ax, palette="pastel")
        elif plot_type == "Line Plot":
            sns.lineplot(x=df[x_col], y=df[y_col], ax=ax, marker="o", linestyle="-", color="red")
        elif plot_type == "Heatmap":
            plt.figure(figsize=(10,6))
            sns.heatmap(df.select_dtypes(include=['number']).corr(), annot=True, cmap="coolwarm", linewidths=0.5)
            st.pyplot(plt)
            st.stop()
        elif plot_type == "Pairplot":
            st.write("### Pairplot")
            st.pyplot(sns.pairplot(df, diag_kind="kde", palette="coolwarm"))
            st.stop()
        
        ax.set_title(f"{plot_type} of {y_col} vs {x_col}")
        ax.set_xlabel(x_col)
        ax.set_ylabel(y_col)
        st.pyplot(fig)
    
    elif menu == "Data Insights":
        st.write("### Unique Value Counts")
        st.write(df.nunique())
        
        st.write("### Correlation Matrix")
        st.write(df.select_dtypes(include=['number']).corr())
        
        # Download processed data
        buffer = io.BytesIO()
        df.to_csv(buffer, index=False)
        buffer.seek(0)
        st.download_button("Download Processed Data", buffer, file_name="processed_data.csv", mime="text/csv")