import streamlit as st
import pandas as pd
from prediction import predict

st.set_page_config(
    page_title="Placement Predictor",
    page_icon="🎯",
    layout="wide"
)

st.title("🎯 Campus Placement Prediction")

st.markdown(
    """
Fill in the student's details below to predict whether the student is
likely to be placed.
"""
)

with st.form("prediction_form"):

    col1, col2 = st.columns(2)

    with col1:

        gender = st.selectbox(
            "Gender",
            ["M", "F"]
        )

        ssc_p = st.number_input(
            "SSC Percentage",
            0.0,
            100.0,
            70.0
        )

        ssc_b = st.selectbox(
            "SSC Board",
            ["Central", "Others"]
        )

        hsc_p = st.number_input(
            "HSC Percentage",
            0.0,
            100.0,
            70.0
        )

        hsc_b = st.selectbox(
            "HSC Board",
            ["Central", "Others"]
        )

        hsc_s = st.selectbox(
            "HSC Stream",
            ["Commerce", "Science", "Arts"]
        )

    with col2:

        degree_p = st.number_input(
            "Degree Percentage",
            0.0,
            100.0,
            70.0
        )

        degree_t = st.selectbox(
            "Degree Type",
            ["Sci&Tech", "Comm&Mgmt", "Others"]
        )

        workex = st.selectbox(
            "Work Experience",
            ["Yes", "No"]
        )

        etest_p = st.number_input(
            "Employability Test %",
            0.0,
            100.0,
            70.0
        )

        specialisation = st.selectbox(
            "MBA Specialisation",
            ["Mkt&HR", "Mkt&Fin"]
        )

        mba_p = st.number_input(
            "MBA Percentage",
            0.0,
            100.0,
            70.0
        )

    submitted = st.form_submit_button(
        "🚀 Predict Placement"
    )
#part 2
if submitted:

    student = {
        "gender": gender,
        "ssc_p": ssc_p,
        "ssc_b": ssc_b,
        "hsc_p": hsc_p,
        "hsc_b": hsc_b,
        "hsc_s": hsc_s,
        "degree_p": degree_p,
        "degree_t": degree_t,
        "workex": workex,
        "etest_p": etest_p,
        "specialisation": specialisation,
        "mba_p": mba_p
    }

    prediction, probability = predict(student)

    confidence = probability * 100

    st.divider()

    if prediction == 1:
        st.success("🎉 Student is likely to be PLACED")
    else:
        st.error("❌ Student is likely to be NOT PLACED")

    st.metric(
        "Prediction Confidence",
        f"{confidence:.2f}%"
    )

    st.progress(min(int(confidence), 100))

    st.info(f"Model Confidence : {confidence:.2f}%")

    result = pd.DataFrame({
        "Prediction": ["Placed" if prediction == 1 else "Not Placed"],
        "Confidence": [confidence]
    })

    st.download_button(
        "⬇ Download Prediction",
        result.to_csv(index=False),
        "prediction.csv",
        "text/csv"
    )