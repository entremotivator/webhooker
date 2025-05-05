# utils/webhook.py
import streamlit as st
import requests

def send_to_webhook(contract_type, data, api_key, webhook_urls):
    url = webhook_urls.get(contract_type)
    if not url:
        st.error(f"No webhook URL configured for '{contract_type}'")
        return

    headers = {"Authorization": f"Bearer {api_key}"}
    try:
        response = requests.post(url, json=data, headers=headers, timeout=10)
        if response.status_code == 200:
            st.success("✅ Contract submitted successfully!")
            st.json(response.json())
        else:
            st.error(f"🚨 Submission failed: {response.text}")
    except Exception as e:
        st.error(f"🔌 Connection error: {str(e)}")
