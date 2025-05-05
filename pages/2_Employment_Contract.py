import streamlit as st
import requests

st.title("👔 Employment Contract")

api_key = st.sidebar.text_input("API Key", type="password")
webhook_url = st.sidebar.text_input("Employment Webhook URL")

def send_to_webhook(data):
    if not webhook_url:
        st.error("Webhook URL is missing.")
        return
    try:
        res = requests.post(webhook_url, json=data, headers={"Authorization": f"Bearer {api_key}"})
        if res.status_code == 200:
            st.success("✅ Contract sent successfully.")
            st.json(res.json())
        else:
            st.error(f"Error: {res.status_code} - {res.text}")
    except Exception as e:
        st.error(f"Request failed: {str(e)}")

with st.form("employment_form"):
    employee_name = st.text_input("Employee Name")
    job_title = st.selectbox("Position", ["Manager", "Developer", "Designer", "Analyst", "Intern"])
    start_date = st.date_input("Start Date")
    salary = st.number_input("Annual Salary", min_value=20000, step=1000)
    benefits = st.multiselect("Benefits", ["Health Insurance", "PTO", "401k", "Stock Options"])

    if st.form_submit_button("Submit Employment Contract"):
        data = {
            "type": "employment",
            "employee": employee_name,
            "job_title": job_title,
            "start_date": str(start_date),
            "salary": salary,
            "benefits": benefits
        }
        send_to_webhook(data)
