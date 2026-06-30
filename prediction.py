"""
Prediction module for Campus Placement Prediction
"""

import pandas as pd

from utils import (
    load_model,
    load_encoders,
    load_feature_columns,
)

# ======================================================
# Load Saved Objects
# ======================================================

model = load_model()
encoders = load_encoders()
feature_columns = load_feature_columns()


# ======================================================
# Encode One Value
# ======================================================

def encode_value(column, value):
    """
    Encode a categorical value using the saved encoder.
    """

    if column not in encoders:
        return value

    encoder = encoders[column]

    try:
        return encoder.transform([value])[0]
    except ValueError:
        raise ValueError(
            f"Invalid value '{value}' for column '{column}'."
        )


# ======================================================
# Predict Student Placement
# ======================================================

def predict(student_data: dict):
    """
    Predict placement for one student.

    Parameters
    ----------
    student_data : dict

    Returns
    -------
    prediction : int
    probability : float
    """

    data = student_data.copy()

    # Encode categorical fields
    categorical = [
        "gender",
        "ssc_b",
        "hsc_b",
        "hsc_s",
        "degree_t",
        "workex",
        "specialisation",
    ]

    for column in categorical:
        data[column] = encode_value(column, data[column])

    # Create dataframe
    df = pd.DataFrame([data])

    # Match training feature order
    df = df[feature_columns]

    # Prediction
    prediction = model.predict(df)[0]

    # Probability
    if hasattr(model, "predict_proba"):
        probability = float(model.predict_proba(df)[0].max())
    else:
        probability = 1.0

    return prediction, probability


# ======================================================
# Batch Prediction
# ======================================================

def batch_predict(df: pd.DataFrame):
    """
    Predict placement for multiple students.

    Parameters
    ----------
    df : pandas.DataFrame

    Returns
    -------
    pandas.DataFrame
    """

    predictions = []
    confidences = []

    for _, row in df.iterrows():

        pred, prob = predict(row.to_dict())

        predictions.append(
            "Placed" if pred == 1 else "Not Placed"
        )

        confidences.append(round(prob * 100, 2))

    result = df.copy()

    result["Prediction"] = predictions
    result["Confidence (%)"] = confidences

    return result