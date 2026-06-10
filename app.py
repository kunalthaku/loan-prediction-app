import streamlit as st
import joblib

model = joblib.load("loan_model.pkl")

st.title("Loan Prediction System")

income = st.number_input("Enter Income", min_value=0)
loan_amount = st.number_input("Enter Loan Amount", min_value=0)
credit_score = st.number_input("Enter Credit Score", min_value=0)

if st.button("Predict"):

    prediction = model.predict(
        [[income, loan_amount, credit_score]]
    )

    if prediction[0] == 1:
        st.success("Loan Approved")
    else:
        st.error("Loan Rejected")