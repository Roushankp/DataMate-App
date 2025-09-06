import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Datamate - Your Data Companion",
    page_icon="📊",
    layout="wide"
)

# Title and description
st.title("📊 Datamate - Your Data Companion")
st.write("Welcome to Datamate! Explore the following tools to simplify your data analysis and machine learning tasks.")

# App descriptions
st.subheader("Available Features")
st.write("""
1. **Chat with CSV**: Interact with your CSV files using natural language. Ask questions, filter data, and get insights instantly.
2. **Text to SQL generator**: Upload a dataset and ask questions in plain English — the app generates and runs SQL queries.         
3. **Data Visualizer**: Upload any dataset and visualize it using 2D and 3D plots.         
4. **Merge Spreadsheets**: Combine multiple spreadsheets into one seamless dataset for easy analysis.
5. **Exploratory Data Analysis (EDA)**: Perform in-depth exploratory data analysis on uploaded datasets. Visualize data distributions, correlations, and more.
6. **Compare ML Algorithms (Regression)**: Compare the performance of various machine learning algorithms for regression problem statements.
7. **Hyperparameter Tuning (Regression)**: Optimize your regression models by tuning hyperparameters for better performance.
""")

# Sidebar for navigation
st.sidebar.title("Navigation")
st.sidebar.write("Select a feature from the list above to get started.")

# Footer
st.write("---")
st.write("Made with ❤️ by Amritanshu Bhardwaj")
st.write("© 2025 Datamate. All rights reserved.")