import streamlit as st
import requests

BASE = "http://localhost:8000"

st.title("Zeta Transaction Test UI")

user = st.text_input("User ID", value="sanjana")

if st.button("Check Balance"):
    res = requests.get(f"{BASE}/balance/{user}")
    st.json(res.json())

amount = st.number_input("Amount", min_value=1.0, step=10.0)

if st.button("Credit"):
    res = requests.post(f"{BASE}/credit", json={"user_id": user, "amount": amount})
    st.json(res.json())

if st.button("Debit"):
    res = requests.post(f"{BASE}/debit", json={"user_id": user, "amount": amount})
    st.json(res.json())
