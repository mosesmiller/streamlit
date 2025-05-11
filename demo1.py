import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Title of the app
st.title("Seaborn Plot of Tips Dataset")

# Load the dataset
tips = sns.load_dataset("tips")

# Sidebar options
st.sidebar.header("Customize Plot")
x_col = st.sidebar.selectbox("X-axis", tips.columns)
y_col = st.sidebar.selectbox("Y-axis", tips.select_dtypes(include='number').columns)

# Create the plot
st.subheader(f"Scatter Plot: {x_col} vs {y_col}")
fig, ax = plt.subplots()
sns.scatterplot(data=tips, x=x_col, y=y_col, ax=ax)
st.pyplot(fig)
