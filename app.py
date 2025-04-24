import streamlit as st
import requests

API_URL = "http://localhost:8000"

st.set_page_config(page_title="Zeta Portal", layout="centered")
st.title("Zeta - Self-Service Portal")

username = st.text_input("Enter your username:")

# --------------------- CHECK BALANCE ---------------------
if st.button("Check Balance") and username:
    res = requests.get(f"{API_URL}/balance/{username}")
    if res.status_code == 200 and 'balance' in res.json():
        st.success(f"Current Balance: ${res.json()['balance']}")
    else:
        st.error("❌ User not found or error retrieving balance.")

# --------------------- LOAN APPLICATION ---------------------
st.markdown("---")
st.header("Apply for Loan")

with st.form("loan_form"):
    name = st.text_input("Full Name")
    age = st.number_input("Age", min_value=18, max_value=100)
    income = st.number_input("Annual Income ($)", step=1000.0)
    credit = st.number_input("Credit Score", min_value=300, max_value=900)
    submitted = st.form_submit_button("Check Eligibility")

    if submitted:
        payload = {"name": name, "age": age, "annual_income": income, "credit_score": credit}
        res = requests.post(f"{API_URL}/loan-eligibility/", json=payload)
        result = res.json()
        st.success(f"{result['name']}, you are **{result['recommendation']}** (Score: {result['score']})")

# --------------------- DISPUTE HISTORY ---------------------
st.markdown("---")
st.header("Dispute History")

if st.button("View Disputes") and username:
    res = requests.get(f"{API_URL}/disputes/{username}")
    data = res.json()
    if not data:
        st.info("No disputes found.")
    else:
        for d in data:
            st.markdown(f"""
            **{d['title']}**  
            {d['description']}  
            Status: `{d['status']}` | Raised On: `{d['raised_on']}`  
            ---""")
