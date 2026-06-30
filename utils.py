"""
Utility functions for Campus Placement Prediction
"""

from pathlib import Path

import joblib
import pandas as pd
import streamlit as st

from config import (
    DATASET_PATH,
    MODEL_PATH,
    ENCODER_PATH,
    FEATURE_COLUMNS_PATH,
    STYLE_PATH,
)


# ======================================================
# CSS Loader
# ======================================================

def load_css():
    """Load custom CSS."""
    if STYLE_PATH.exists():
        with open(STYLE_PATH, "r", encoding="utf-8") as css:
            st.markdown(
                f"<style>{css.read()}</style>",
                unsafe_allow_html=True,
            )


# ======================================================
# Dataset Loader
# ======================================================

@st.cache_data
def load_dataset():
    """Load placement dataset."""
    return pd.read_csv(DATASET_PATH)


# ======================================================
# Model Loader
# ======================================================

@st.cache_resource
def load_model():
    """Load trained ML model."""
    return joblib.load(MODEL_PATH)


@st.cache_resource
def load_encoders():
    """Load saved encoders."""
    return joblib.load(ENCODER_PATH)


@st.cache_resource
def load_feature_columns():
    """Load feature column order."""
    return joblib.load(FEATURE_COLUMNS_PATH)


# ======================================================
# Download CSV
# ======================================================

def dataframe_to_csv(df: pd.DataFrame):
    """Convert dataframe to CSV bytes."""
    return df.to_csv(index=False).encode("utf-8")


# ======================================================
# Placement Label
# ======================================================

def placement_label(value):
    """
    Convert prediction into readable label.
    """

    if value in [1, "Placed"]:
        return "Placed"

    return "Not Placed"


# ======================================================
# Metric Card
# ======================================================

def metric_card(title, value):
    """
    Display metric card.
    """

    st.metric(title, value)


# ======================================================
# Data Summary
# ======================================================

def dataset_summary(df):
    """
    Return dataset summary.
    """

    return {
        "Rows": df.shape[0],
        "Columns": df.shape[1],
        "Missing": int(df.isnull().sum().sum()),
        "Duplicates": int(df.duplicated().sum()),
    }


# ======================================================
# Numeric Columns
# ======================================================

def numeric_columns(df):
    return df.select_dtypes(include="number").columns.tolist()


# ======================================================
# Categorical Columns
# ======================================================

def categorical_columns(df):
    return df.select_dtypes(include="object").columns.tolist()


# ======================================================
# Validation
# ======================================================

def validate_percentage(value, field_name):
    """
    Validate percentage fields.
    """

    if value < 0 or value > 100:
        raise ValueError(
            f"{field_name} must be between 0 and 100."
        )


# ======================================================
# Footer
# ======================================================

def footer():
    st.markdown("---")
    st.caption(
        "Campus Placement Prediction • Streamlit • Machine Learning"
    )