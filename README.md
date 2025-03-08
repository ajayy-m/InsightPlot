# InsightPlot 📈 - Automated Visualization

InsightPlot is an automated data visualization tool built with Streamlit. It allows users to upload a CSV file and automatically generate insightful plots—such as bar charts, scatter plots, and histograms—without writing any code.

## Features

- **CSV Upload:** Easily upload your CSV file and preview a sample of your data.
- **Automated Column Detection:** Automatically detects available columns and allows you to select the appropriate ones for visualization.
- **Multiple Visualization Types:** Choose from Bar Chart, Scatter Plot, or Histogram.
- **Customizable Plots:** Generates plots with titles, labels, and color palettes using Seaborn.
- **Interactive Web App:** Built with Streamlit, making it easy to deploy and share.

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/insightplot.git
   cd insightplot
   ```

2. **Install Dependencies:**

   Ensure you have Python installed. Then install the required libraries:

   ```bash
   pip install streamlit pandas matplotlib seaborn
   ```

## Usage

1. **Run the Streamlit App:**

   ```bash
   streamlit run insight_plot.py
   ```

2. **Upload Your CSV File:**

   Once the app launches in your browser, upload your CSV file using the file uploader widget.

3. **Select Visualization Options:**

   Choose your desired visualization type and the columns for the X and Y axes (if applicable).

4. **View the Generated Plot:**

   The app will display your selected plot along with basic customization such as title and labels.

## Contributing

Contributions are welcome! If you have ideas or improvements, please create an issue or submit a pull request.

## License

This project is licensed under the [Apache 2.0](LICENSE).

```
