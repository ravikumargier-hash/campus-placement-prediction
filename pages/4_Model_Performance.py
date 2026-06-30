import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report
)
from sklearn.preprocessing import LabelEncoder

import plotly.express as px

# --------------------------------------------------
# Page Config
# --------------------------------------------------

st.set_page_config(
    page_title="Model Performance",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Model Performance Dashboard")

# --------------------------------------------------
# Load Dataset
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

DATASET = BASE_DIR / "Dataset" / "Placement_Data_Full_Class.csv"
MODEL = BASE_DIR / "Model" / "model.pkl"

df = pd.read_csv(DATASET)

# --------------------------------------------------
# Preprocessing
# --------------------------------------------------

df = df.drop(columns=["sl_no", "salary"])

categorical = [
    "gender",
    "ssc_b",
    "hsc_b",
    "hsc_s",
    "degree_t",
    "workex",
    "specialisation",
    "status"
]

for col in categorical:
    encoder = LabelEncoder()
    df[col] = encoder.fit_transform(df[col])

X = df.drop("status", axis=1)
y = df["status"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=5
)

# --------------------------------------------------
# Load Model
# --------------------------------------------------

model = joblib.load(MODEL)

prediction = model.predict(X_test)

# --------------------------------------------------
# Metrics
# --------------------------------------------------

accuracy = accuracy_score(y_test, prediction)
precision = precision_score(y_test, prediction)
recall = recall_score(y_test, prediction)
f1 = f1_score(y_test, prediction)

c1, c2, c3, c4 = st.columns(4)

c1.metric("Accuracy", f"{accuracy:.2%}")
c2.metric("Precision", f"{precision:.2%}")
c3.metric("Recall", f"{recall:.2%}")
c4.metric("F1 Score", f"{f1:.2%}")

st.divider()

# --------------------------------------------------
# Confusion Matrix
# --------------------------------------------------

st.subheader("Confusion Matrix")

cm = confusion_matrix(y_test, prediction)

cm_df = pd.DataFrame(
    cm,
    columns=["Predicted No", "Predicted Yes"],
    index=["Actual No", "Actual Yes"]
)

fig = px.imshow(
    cm_df,
    text_auto=True,
    color_continuous_scale="Blues"
)

st.plotly_chart(fig, use_container_width=True)

# --------------------------------------------------
# Classification Report
# --------------------------------------------------

st.subheader("Classification Report")

report = classification_report(
    y_test,
    prediction,
    output_dict=True
)

report_df = pd.DataFrame(report).transpose()

st.dataframe(report_df, use_container_width=True)

# --------------------------------------------------
# Feature Importance
# --------------------------------------------------

st.subheader("Feature Importance")

if hasattr(model, "feature_importances_"):

    importance = pd.DataFrame({
        "Feature": X.columns,
        "Importance": model.feature_importances_
    })

    importance = importance.sort_values(
        "Importance",
        ascending=False
    )

    fig = px.bar(
        importance,
        x="Importance",
        y="Feature",
        orientation="h",
        title="Important Features"
    )

    st.plotly_chart(fig, use_container_width=True)

else:

    st.info("Current model does not provide feature importance.")

st.success("Model evaluation completed successfully.")