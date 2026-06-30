"""
Campus Placement Prediction
Main Application
"""

import streamlit as st

from config import (
    APP_TITLE,
    APP_ICON,
    APP_LAYOUT,
    VERSION,
    AUTHOR,
)

from utils import load_css

# -------------------------------------------------------
# Page Configuration
# -------------------------------------------------------

st.set_page_config(
    page_title=APP_TITLE,
    page_icon=APP_ICON,
    layout=APP_LAYOUT,
    initial_sidebar_state="expanded",
)

# -------------------------------------------------------
# Load CSS
# -------------------------------------------------------

load_css()

# -------------------------------------------------------
# Sidebar
# -------------------------------------------------------

st.sidebar.title("🎓 Campus Placement")

st.sidebar.success("Navigation")

st.sidebar.info(
    """
Use the navigation menu above to access:

🏠 Home

📊 Dataset

📈 Visualizations

🎯 Placement Predictor

📉 Model Performance

ℹ About
"""
)

st.sidebar.markdown("---")

st.sidebar.caption(f"Version : {VERSION}")
st.sidebar.caption(f"Developer : {AUTHOR}")

# -------------------------------------------------------
# Landing Page
# -------------------------------------------------------

st.title("🎓 Campus Placement Prediction System")

st.markdown(
    """
Welcome to the **Campus Placement Prediction System**.

This application predicts whether a student is likely to be placed
using a trained Machine Learning model.
"""
)

st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    st.info(
        """
### 📊 Dataset

Explore the placement dataset.

✔ Search

✔ Statistics

✔ Download
"""
    )

with col2:
    st.success(
        """
### 🤖 Prediction

Predict placement.

✔ Single Prediction

✔ Batch Prediction

✔ Confidence Score
"""
    )

with col3:
    st.warning(
        """
### 📈 Analytics

Visualize data.

✔ Charts

✔ Heatmaps

✔ Feature Analysis
"""
    )

st.divider()

st.subheader("🚀 Application Features")

features = [
    "Interactive Dashboard",
    "Placement Prediction",
    "Dataset Explorer",
    "Interactive Plotly Charts",
    "Model Performance",
    "Download Prediction Reports",
    "Batch CSV Prediction",
]

for feature in features:
    st.markdown(f"✅ {feature}")

st.divider()

st.subheader("📁 Project Structure")

st.code(
"""
Campus Placement Prediction/

├── app.py
├── config.py
├── utils.py
├── train_model.py
├── prediction.py
│
├── pages/
│
├── Dataset/
│
├── Model/
│
└── assets/
"""
)

st.success(
    "Use the left sidebar to navigate through the application."
)

st.markdown("---")

st.caption(
    "Campus Placement Prediction • Streamlit • Scikit-Learn • Plotly"
)