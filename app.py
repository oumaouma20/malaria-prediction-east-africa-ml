import streamlit as st
import pandas as pd
import joblib


# Load the model
model = joblib.load('random_forest_model.pkl')


st.title("Malaria Incidence Predictor")

# Input fields for the features
year = st.number_input("Year", min_value=1990, max_value=2100, step=1)
cases = st.number_input("Malaria cases reported", min_value=0.0)
bed_nets = st.number_input("Use of insecticide-treated bed nets (% under 5)", min_value=0.0, max_value=100.0)
antimalarial = st.number_input("Children with fever receiving antimalarial drugs (%)", min_value=0.0, max_value=100.0)
ipt = st.number_input("IPT for pregnant women (%)", min_value=0.0, max_value=100.0)
water = st.number_input("Safe drinking water access (%)", min_value=0.0, max_value=100.0)
sanitation = st.number_input("Safe sanitation access (%)", min_value=0.0, max_value=100.0)

# Prepare input for prediction
input_df = pd.DataFrame([{
    'Year': year,
    'Malaria cases reported': cases,
    'Use of insecticide-treated bed nets (% of under-5 population)': bed_nets,
    'Children with fever receiving antimalarial drugs (% of children under age 5 with fever)': antimalarial,
    'Intermittent preventive treatment (IPT) of malaria in pregnancy (% of pregnant women)': ipt,
    'People using safely managed drinking water services (% of population)': water,
    'People using safely managed sanitation services (% of population)': sanitation
}])

# Make prediction
if st.button("Predict"):
    prediction = model.predict(input_df)
    st.success(f"Predicted Malaria Incidence: {prediction[0]:.2f} per 1,000 at risk")
