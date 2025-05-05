import streamlit as st
import requests

st.title("🤝 Partnership Agreement")

# Sidebar config
api_key = st.sidebar.text_input("API Key", type="password")
webhook_url = st.sidebar.text_input("Partnership Webhook URL")

def send_to_webhook(data):
    if not webhook_url:
        st.error("Please provide a valid webhook URL.")
        return
    try:
        res = requests.post(webhook_url, json=data, headers={"Authorization": f"Bearer {api_key}"})
        if res.status_code == 200:
            st.success("✅ Submitted successfully!")
            st.json(res.json())
        else:
            st.error(f"Failed: {res.status_code} - {res.text}")
    except Exception as e:
        st.error(f"Request error: {str(e)}")

with st.form("partnership_form"):
    st.subheader("Partner 1")
    p1_name = st.text_input("Partner 1 Name")
    p1_address = st.text_input("Partner 1 Address")
    p1_contribution = st.number_input("Partner 1 Contribution", min_value=0.0)

    st.subheader("Partner 2")
    p2_name = st.text_input("Partner 2 Name")
    p2_address = st.text_input("Partner 2 Address")
    p2_contribution = st.number_input("Partner 2 Contribution", min_value=0.0)

    submitted = st.form_submit_button("Submit Partnership Agreement")
    if submitted:
        data = {
            "type": "partnership",
            "partners": [
                {"name": p1_name, "address": p1_address, "contribution": p1_contribution},
                {"name": p2_name, "address": p2_address, "contribution": p2_contribution}
            ]
        }
        send_to_webhook(data)
