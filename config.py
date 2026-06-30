"""
Configuration file for Campus Placement Prediction
"""

from pathlib import Path

# --------------------------------------------------
# Project Directories
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent

DATASET_DIR = BASE_DIR / "Dataset"
MODEL_DIR = BASE_DIR / "Model"
ASSETS_DIR = BASE_DIR / "assets"
PAGES_DIR = BASE_DIR / "pages"

# --------------------------------------------------
# Dataset
# --------------------------------------------------

DATASET_PATH = DATASET_DIR / "Placement_Data_Full_Class.csv"

# --------------------------------------------------
# Saved Model Files
# --------------------------------------------------

MODEL_PATH = MODEL_DIR / "model.pkl"
ENCODER_PATH = MODEL_DIR / "encoders.pkl"
FEATURE_COLUMNS_PATH = MODEL_DIR / "feature_columns.pkl"

# --------------------------------------------------
# Assets
# --------------------------------------------------

STYLE_PATH = ASSETS_DIR / "style.css"

# --------------------------------------------------
# Application
# --------------------------------------------------

APP_TITLE = "🎓 Campus Placement Prediction"

APP_ICON = "🎓"

APP_LAYOUT = "wide"

VERSION = "2.0"

AUTHOR = "Sharma J"