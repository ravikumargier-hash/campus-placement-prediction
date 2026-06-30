import streamlit as st
import pandas as pd
from pathlib import Path

# ---------------------------------------------------
# Page Configuration
# ---------------------------------------------------
st.set_page_config(
    page_title="Dataset Explorer",
    page_icon="📊",
    layout="wide"
)

# ---------------------------------------------------
# Load Dataset
# ---------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
DATASET_PATH = BASE_DIR / "Dataset" / "Placement_Data_Full_Class.csv"

@st.cache_data
def load_data():
    return pd.read_csv(DATASET_PATH)

df = load_data()

# ---------------------------------------------------
# Header
# ---------------------------------------------------
st.title("📊 Dataset Explorer")

st.markdown(
    """
Explore the Campus Placement dataset used for model training.
Search records, inspect columns, identify missing values,
and download the dataset.
    """
)

# ---------------------------------------------------
# Dataset Information
# ---------------------------------------------------
c1, c2, c3, c4 = st.columns(4)

c1.metric("Rows", df.shape[0])
c2.metric("Columns", df.shape[1])
c3.metric("Missing Values", int(df.isnull().sum().sum()))
c4.metric("Duplicate Rows", int(df.duplicated().sum()))

st.divider()

# ---------------------------------------------------
# Search Dataset
# ---------------------------------------------------
st.subheader("🔍 Search Dataset")

search = st.text_input(
    "Search any value",
    placeholder="Example: M, Science, Placed"
)

filtered_df = df.copy()

if search:
    mask = filtered_df.astype(str).apply(
        lambda x: x.str.contains(search, case=False, na=False)
    ).any(axis=1)

    filtered_df = filtered_df[mask]

st.dataframe(
    filtered_df,
    use_container_width=True,
    height=450
)

# ---------------------------------------------------
# Download CSV
# ---------------------------------------------------
st.download_button(
    label="⬇ Download Dataset",
    data=filtered_df.to_csv(index=False),
    file_name="placement_dataset.csv",
    mime="text/csv"
)

st.divider()

# ---------------------------------------------------
# Dataset Information
# ---------------------------------------------------
st.subheader("📋 Column Information")

info = pd.DataFrame({
    "Column": df.columns,
    "Data Type": df.dtypes.astype(str),
    "Missing": df.isnull().sum().values,
    "Unique Values": df.nunique().values
})

st.dataframe(
    info,
    use_container_width=True
)

# ---------------------------------------------------
# Missing Values
# ---------------------------------------------------
st.divider()

st.subheader("❗ Missing Values")

missing = pd.DataFrame({
    "Column": df.columns,
    "Missing Count": df.isnull().sum().values,
    "Missing %": (
        df.isnull().sum().values / len(df) * 100
    ).round(2)
})

st.dataframe(
    missing,
    use_container_width=True
)

# ---------------------------------------------------
# Statistical Summary
# ---------------------------------------------------
st.divider()

st.subheader("📈 Statistical Summary")

st.dataframe(
    df.describe(include="all"),
    use_container_width=True
)

# ---------------------------------------------------
# Categorical Columns
# ---------------------------------------------------
st.divider()

st.subheader("🏷 Categorical Columns")

categorical = df.select_dtypes(include="object").columns.tolist()

selected = st.selectbox(
    "Choose a Column",
    categorical
)

value_counts = (
    df[selected]
    .value_counts()
    .reset_index()
)

value_counts.columns = [selected, "Count"]

st.dataframe(
    value_counts,
    use_container_width=True
)

# ---------------------------------------------------
# Numeric Columns
# ---------------------------------------------------
st.divider()

st.subheader("📊 Numeric Summary")

numeric = df.select_dtypes(include="number")

selected_num = st.selectbox(
    "Select Numeric Column",
    numeric.columns
)

st.write(numeric[selected_num].describe())

st.success("Dataset Explorer Loaded Successfully ✅")