import streamlit as st
import pandas as pd
from pathlib import Path

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="Campus Placement Prediction",
    page_icon="🎓",
    layout="wide"
)

# -----------------------------
# Load Dataset
# -----------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
DATASET_PATH = BASE_DIR / "Dataset" / "Placement_Data_Full_Class.csv"

df = pd.read_csv(DATASET_PATH)

# -----------------------------
# Custom CSS
# -----------------------------
st.markdown("""
<style>
.big-title{
    font-size:42px;
    font-weight:bold;
    color:#1565C0;
}
.subtitle{
    color:#555;
    font-size:18px;
}
.card{
    background:#f8f9fa;
    border-radius:12px;
    padding:20px;
    box-shadow:0px 2px 8px rgba(0,0,0,0.08);
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# Header
# -----------------------------
st.markdown(
    "<div class='big-title'>🎓 Campus Placement Prediction System</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='subtitle'>Machine Learning based Student Placement Predictor</div>",
    unsafe_allow_html=True
)

st.write("")

# -----------------------------
# Metrics
# -----------------------------
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Students", len(df))

with col2:
    st.metric("Features", len(df.columns))

with col3:
    placed = (df["status"] == "Placed").sum()
    st.metric("Placed", placed)

with col4:
    not_placed = (df["status"] == "Not Placed").sum()
    st.metric("Not Placed", not_placed)

st.divider()

# -----------------------------
# Overview
# -----------------------------
left, right = st.columns([2, 1])

with left:
    st.subheader("Project Overview")

    st.write("""
This application predicts whether a student is likely to be placed
based on:

- SSC Percentage
- HSC Percentage
- Degree Percentage
- Employability Test
- MBA Percentage
- Work Experience
- Specialisation
- Academic Background

The application uses a Machine Learning model trained on historical
campus placement data.
""")

with right:
    st.info(
        """
### Technology Stack

- Python
- Streamlit
- Scikit-learn
- Pandas
- Plotly
- Joblib
"""
    )

st.divider()

# -----------------------------
# Dataset Preview
# -----------------------------
st.subheader("Dataset Preview")

st.dataframe(df.head(), use_container_width=True)

st.divider()

# -----------------------------
# Quick Statistics
# -----------------------------
st.subheader("Dataset Summary")

st.dataframe(df.describe(), use_container_width=True)

st.success("Use the left sidebar to explore the remaining pages.")