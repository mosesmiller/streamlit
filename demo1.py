# app.py

import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

# Set Streamlit page config
st.set_page_config(page_title="Seaborn Tips Plot", layout="wide")

# Title and description
st.title("Seaborn Plot of the Tips Dataset")
st.markdown("Explore different relationships in the classic `tips` dataset using Seaborn.")

# Load the dataset
@st.cache_data
def load_data():
    return sns.load_dataset("tips")

tips = load_data()

# Sidebar controls
st.sidebar.header("Plot Customization")
x_axis = st.sidebar.selectbox("X-axis", tips.columns, index=tips.columns.get_loc("total_bill"))
y_axis = st.sidebar.selectbox("Y-axis", tips.select_dtypes(include="number").columns, index=tips.select_dtypes(include="number").columns.get_loc("tip"))
hue = st.sidebar.selectbox("Hue (color by)", ["None"] + list(tips.select_dtypes(include="object").columns))

# Create the plot
fig, ax = plt.subplots(figsize=(10, 6))
if hue != "None":
    sns.scatterplot(data=tips, x=x_axis, y=y_axis, hue=hue, ax=ax)
else:
    sns.scatterplot(data=tips, x=x_axis, y=y_axis, ax=ax)

ax.set_title(f"{y_axis} vs {x_axis}", fontsize=14)
st.pyplot(fig)
