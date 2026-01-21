import streamlit as st
import pandas as pd
import joblib

# Page config
st.set_page_config(page_title="Customer Churn Prediction", layout="centered")

# Title
st.title("📊 Customer Churn Prediction App")
st.write("Predict whether a customer is likely to churn using Machine Learning")

# Load model
model = joblib.load("churn_model.pkl")
features = joblib.load("model_features.pkl")


# User inputs
gender = st.selectbox("Gender", ["Male", "Female"])
senior = st.selectbox("Senior Citizen", ["Yes", "No"])
partner = st.selectbox("Partner", ["Yes", "No"])
dependents = st.selectbox("Dependents", ["Yes", "No"])
tenure = st.slider("Tenure (Months)", 0, 72, 12)
monthly_charges = st.number_input("Monthly Charges", min_value=0.0, value=70.0)

# Convert inputs
data = {
    "Gender": 1 if gender == "Male" else 0,
    "Senior Citizen": 1 if senior == "Yes" else 0,
    "Partner": 1 if partner == "Yes" else 0,
    "Dependents": 1 if dependents == "Yes" else 0,
    "Tenure Months": tenure,
    "Monthly Charges": monthly_charges
}

input_df = pd.DataFrame([data])
input_df = pd.get_dummies(input_df)
input_df = input_df.reindex(columns=features, fill_value=0)

# Prediction
if st.button("Predict Churn"):
    probability = model.predict_proba(input_df)[0][1]
    prediction = model.predict(input_df)[0]

    st.metric("Churn Probability", f"{probability * 100:.2f}%")

    if prediction == 1:
        st.error("⚠️ Customer is likely to churn")
    else:
        st.success("✅ Customer is likely to stay")
