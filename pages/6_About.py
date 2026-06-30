import streamlit as st

st.set_page_config(
    page_title="About",
    page_icon="ℹ️",
    layout="wide"
)

st.title("ℹ️ About Campus Placement Prediction System")

st.markdown("""
Welcome to the **Campus Placement Prediction System**.

This project predicts whether a student is likely to be placed in campus recruitment
based on academic performance, work experience, and employability factors.
""")

st.divider()

# ---------------------------------------------------------
# Project Information
# ---------------------------------------------------------

st.header("🎯 Project Objective")

st.write("""
The objective of this project is to assist students and placement officers by
predicting placement outcomes using Machine Learning.

The model analyzes multiple academic and personal factors to estimate the
probability of campus placement.
""")

# ---------------------------------------------------------
# Dataset
# ---------------------------------------------------------

st.header("📊 Dataset")

st.write("""
Dataset contains information such as:

- Gender
- SSC Percentage
- HSC Percentage
- Degree Percentage
- Degree Type
- Employability Test Percentage
- MBA Percentage
- Work Experience
- MBA Specialization
- Placement Status
- Salary
""")

# ---------------------------------------------------------
# Machine Learning Pipeline
# ---------------------------------------------------------

st.header("🤖 Machine Learning Pipeline")

st.markdown("""
1. Data Collection

2. Data Cleaning

3. Label Encoding

4. Feature Selection

5. Train/Test Split

6. Model Training

7. Prediction

8. Model Evaluation
""")

# ---------------------------------------------------------
# Technologies
# ---------------------------------------------------------

st.header("💻 Technologies Used")

c1, c2 = st.columns(2)

with c1:
    st.markdown("""
- Python
- Streamlit
- Pandas
- NumPy
- Scikit-Learn
""")

with c2:
    st.markdown("""
- Plotly
- Matplotlib
- Joblib
- Git
- GitHub
""")

# ---------------------------------------------------------
# Folder Structure
# ---------------------------------------------------------

st.header("📁 Project Structure")

st.code("""
Campus Placement Prediction/

├── app.py
├── prediction.py
├── train_model.py
├── preprocess.py
├── utils.py
├── config.py
├── requirements.txt
│
├── pages/
├── Dataset/
├── Model/
├── Images/
└── assets/
""")

# ---------------------------------------------------------
# Features
# ---------------------------------------------------------

st.header("✨ Features")

st.markdown("""
✅ Interactive Dashboard

✅ Placement Prediction

✅ Dataset Explorer

✅ Interactive Charts

✅ Model Performance

✅ Download Prediction Report

✅ Batch Prediction

✅ Responsive Interface
""")

# ---------------------------------------------------------
# Future Improvements
# ---------------------------------------------------------

st.header("🚀 Future Enhancements")

st.markdown("""
- SHAP Explainability

- XGBoost Model

- Authentication

- Database Integration

- Student Login Portal

- Placement Officer Dashboard

- Cloud Deployment

- REST API
""")

# ---------------------------------------------------------
# Developer
# ---------------------------------------------------------

st.header("👨‍💻 Developer")

st.info("""
Developed as a Machine Learning project using Streamlit.

Designed for:
- Campus Placements
- Academic Demonstrations
- Portfolio Projects
- GitHub Showcase
""")

# ---------------------------------------------------------
# Footer
# ---------------------------------------------------------

st.divider()

st.success("Campus Placement Prediction System © 2026")