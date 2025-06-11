import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load('random_forest_model.pkl') 

# Title
st.title("Malaria Incidence Predictor")

# Input form
year = st.number_input("Enter Year", min_value=2000, max_value=2030, step=1)
cases = st.number_input("Enter Previous Year Cases")
rainfall = st.number_input("Enter Rainfall Amount")
temperature = st.number_input("Enter Temperature")

# Prediction
if st.button("Predict"):
    input_df = pd.DataFrame({
        'Year': [year],
        'Cases_Previous': [cases],
        'Rainfall': [rainfall],
        'Temperature': [temperature]
    })
    prediction = model.predict(input_df)
    st.success(f"Predicted Malaria Incidence: {prediction[0]:.2f}")
