import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load('random_forest_model.pkl') 

# Title
st.title("Malaria Incidence Predictor")

# Input form
year = st.number_input("Enter Year", min_value=1990, max_value=2030, step=1)
cases = st.number_input("Malaria cases reported")
bednets = st.number_input("Use of insecticide-treated bed nets (% under 5)")
fever_treatment = st.number_input("Children with fever receiving antimalarial drugs (%)")
ipt = st.number_input("IPT for pregnant women (%)")
water = st.number_input("Safe drinking water access (%)")
sanitation = st.number_input("Safe sanitation access (%)")

# Prediction
if st.button("Predict"):
    input_df = pd.DataFrame({
        'Use of insecticide-treated bed nets (% of under-5 population)': [bednets],
        'Children with fever receiving antimalarial drugs (% of children under age 5 with fever)': [fever_treatment],
        'Intermittent preventive treatment (IPT) of malaria in pregnancy (% of pregnant women)': [ipt],
        'People using safely managed drinking water services (% of population)': [water],
        'People using safely managed sanitation services (% of population)': [sanitation],
        'Malaria cases reported': [cases],
        'Year': [year]
    })

    prediction = model.predict(input_df)
    st.success(f"Predicted Malaria Incidence: {prediction[0]:.2f}")
