import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

# -------------------------------------------------
# Page Configuration
# -------------------------------------------------
st.set_page_config(
    page_title="Visualizations",
    page_icon="📈",
    layout="wide"
)

# -------------------------------------------------
# Load Dataset
# -------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
DATASET_PATH = BASE_DIR / "Dataset" / "Placement_Data_Full_Class.csv"

@st.cache_data
def load_data():
    return pd.read_csv(DATASET_PATH)

df = load_data()

st.title("📈 Interactive Dashboard")

st.markdown(
    "Explore the Campus Placement dataset through interactive visualizations."
)

# -------------------------------------------------
# Sidebar Filters
# -------------------------------------------------
st.sidebar.header("Filters")

gender = st.sidebar.multiselect(
    "Gender",
    options=df["gender"].unique(),
    default=df["gender"].unique()
)

status = st.sidebar.multiselect(
    "Placement Status",
    options=df["status"].unique(),
    default=df["status"].unique()
)

filtered = df[
    (df["gender"].isin(gender))
    &
    (df["status"].isin(status))
]

# -------------------------------------------------
# Row 1
# -------------------------------------------------
col1, col2 = st.columns(2)

with col1:

    fig = px.pie(
        filtered,
        names="status",
        title="Placement Distribution",
        hole=0.45
    )

    st.plotly_chart(fig, use_container_width=True)

with col2:

    fig = px.bar(
        filtered,
        x="gender",
        color="status",
        barmode="group",
        title="Placement by Gender"
    )

    st.plotly_chart(fig, use_container_width=True)

# -------------------------------------------------
# Row 2
# -------------------------------------------------
col1, col2 = st.columns(2)

with col1:

    fig = px.histogram(
        filtered,
        x="degree_p",
        nbins=20,
        color="status",
        title="Degree Percentage Distribution"
    )

    st.plotly_chart(fig, use_container_width=True)

with col2:

    fig = px.box(
        filtered,
        x="status",
        y="etest_p",
        color="status",
        title="Employability Test Score"
    )

    st.plotly_chart(fig, use_container_width=True)

# -------------------------------------------------
# Row 3
# -------------------------------------------------
col1, col2 = st.columns(2)

with col1:

    fig = px.scatter(
        filtered,
        x="ssc_p",
        y="hsc_p",
        color="status",
        size="degree_p",
        hover_data=["gender"],
        title="SSC vs HSC"
    )

    st.plotly_chart(fig, use_container_width=True)

with col2:

    fig = px.violin(
        filtered,
        y="mba_p",
        color="status",
        box=True,
        title="MBA Percentage"
    )

    st.plotly_chart(fig, use_container_width=True)

# -------------------------------------------------
# Salary Distribution
# -------------------------------------------------
st.subheader("Salary Distribution")

salary = filtered.dropna(subset=["salary"])

fig = px.histogram(
    salary,
    x="salary",
    nbins=25,
    title="Salary Histogram"
)

st.plotly_chart(fig, use_container_width=True)

# -------------------------------------------------
# Correlation Heatmap
# -------------------------------------------------
st.subheader("Correlation Matrix")

numeric = filtered.select_dtypes(include="number")

corr = numeric.corr()

fig = px.imshow(
    corr,
    text_auto=".2f",
    aspect="auto",
    color_continuous_scale="Blues"
)

st.plotly_chart(fig, use_container_width=True)

# -------------------------------------------------
# Category Analysis
# -------------------------------------------------
st.subheader("Category Analysis")

column = st.selectbox(
    "Select Category",
    [
        "degree_t",
        "hsc_s",
        "specialisation",
        "workex"
    ]
)

value_counts = filtered[column].value_counts().reset_index()
value_counts.columns = [column, "count"]

fig = px.bar(
    value_counts,
    x=column,
    y="count",
    color=column,
    title=f"{column} Distribution"
)

st.plotly_chart(fig, use_container_width=True)

# -------------------------------------------------
# Summary Metrics
# -------------------------------------------------
st.divider()

c1, c2, c3, c4 = st.columns(4)

c1.metric("Students", len(filtered))
c2.metric("Placed", (filtered["status"]=="Placed").sum())
c3.metric("Not Placed", (filtered["status"]=="Not Placed").sum())

avg_salary = salary["salary"].mean() if not salary.empty else 0
c4.metric("Average Salary", f"{avg_salary:,.0f}")

st.success("Interactive Dashboard Loaded Successfully")