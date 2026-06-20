import streamlit as st
import pandas as pd
import joblib

model = joblib.load("../Model/sales_model.pkl")

st.set_page_config(
    page_title="Predictive Analytics Dashboard",
    layout="wide"
)

st.title("📈 Predictive Analytics Using Historical Data")

st.write(
    "Predict Future Sales Using Historical Data"
)

year = st.number_input(
    "Enter Year",
    2020,
    2035,
    2026
)

month = st.number_input(
    "Enter Month",
    1,
    12,
    1
)

day = st.number_input(
    "Enter Day",
    1,
    31,
    1
)

if st.button("Predict"):

    data = pd.DataFrame({
        "Year":[year],
        "Month":[month],
        "Day":[day]
    })

    prediction = model.predict(data)

    st.success(
        f"Predicted Sales = ${prediction[0]:.2f}"
    )