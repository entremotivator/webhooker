import streamlit as st
import requests

st.title("🔧 Service Agreement")

api_key = st.sidebar.text_input("API Key", type="password")
webhook_url = st.sidebar.text_input("Service Webhook URL")

def send_to_webhook(data):
    if not webhook_url:
        st.error("Missing webhook URL.")
        return
    try:
        res = requests.post(webhook_url, json=data, headers={"Authorization": f"Bearer {api_key}"})
        if res.status_code == 200:
            st.success("✅ Service Agreement sent.")
            st.json(res.json())
        else:
            st.error(f"Webhook failed: {res.status_code} - {res.text}")
    except Exception as e:
        st.error(f"Error: {str(e)}")

with st.form("service_form"):
    client_name = st.text_input("Client Name")
    service_desc = st.text_area("Service Description", height=150)
    payment_terms = st.selectbox("Payment Terms", ["Net 30", "50% Upfront", "Milestone-Based"])
    duration_months = st.number_input("Duration (months)", min_value=1, max_value=36)
    termination_clause = st.checkbox("Include Termination Clause")

    if st.form_submit_button("Submit Service Agreement"):
        data = {
            "type": "service",
            "client": client_name,
            "description": service_desc,
            "payment_terms": payment_terms,
            "duration": duration_months,
            "termination_clause": termination_clause
        }
        send_to_webhook(data)
