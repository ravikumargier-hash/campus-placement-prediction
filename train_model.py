"""
Train Campus Placement Prediction Model
"""

import joblib
import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

from config import (
    DATASET_PATH,
    MODEL_PATH,
    ENCODER_PATH,
    FEATURE_COLUMNS_PATH,
)


# ======================================================
# Load Dataset
# ======================================================

print("Loading dataset...")

df = pd.read_csv(DATASET_PATH)

# ======================================================
# Drop unnecessary columns
# ======================================================

columns_to_drop = []

if "sl_no" in df.columns:
    columns_to_drop.append("sl_no")

if "salary" in df.columns:
    columns_to_drop.append("salary")

df.drop(columns=columns_to_drop, inplace=True)

# ======================================================
# Encode categorical columns
# ======================================================

encoders = {}

categorical_columns = df.select_dtypes(include="object").columns.tolist()

# Don't encode target yet
categorical_columns.remove("status")

for column in categorical_columns:
    encoder = LabelEncoder()
    df[column] = encoder.fit_transform(df[column])
    encoders[column] = encoder

# Encode target
target_encoder = LabelEncoder()
df["status"] = target_encoder.fit_transform(df["status"])
encoders["status"] = target_encoder

# ======================================================
# Split Features / Target
# ======================================================

X = df.drop("status", axis=1)
y = df["status"]

feature_columns = list(X.columns)

# ======================================================
# Train/Test Split
# ======================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y,
)

# ======================================================
# Train Model
# ======================================================

model = RandomForestClassifier(
    n_estimators=200,
    random_state=42,
)

model.fit(X_train, y_train)

# ======================================================
# Evaluation
# ======================================================

predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print("=" * 50)
print(f"Model Accuracy : {accuracy:.4f}")
print("=" * 50)

print(classification_report(y_test, predictions))

# ======================================================
# Save Artifacts
# ======================================================

joblib.dump(model, MODEL_PATH)
joblib.dump(encoders, ENCODER_PATH)
joblib.dump(feature_columns, FEATURE_COLUMNS_PATH)

print("\nFiles Saved Successfully:")
print(f"✓ {MODEL_PATH}")
print(f"✓ {ENCODER_PATH}")
print(f"✓ {FEATURE_COLUMNS_PATH}")