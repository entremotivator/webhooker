# pages/4_NDA.py
import streamlit as st
from utils.webhook import send_to_webhook

st.header("🛡️ Non-Disclosure Agreement")

with st.form("nda_form"):
    party_a = st.text_input("Disclosing Party")
    party_b = st.text_input("Receiving Party")
    purpose = st.text_area("Purpose of Disclosure", height=100)
    duration = st.selectbox("Confidentiality Duration", ["1 year", "2 years", "5 years", "Indefinite"])

    if st.form_submit_button("Submit NDA"):
        contract_data = {
            "type": "nda",
            "disclosing_party": party_a,
            "receiving_party": party_b,
            "purpose": purpose,
            "duration": duration
        }
        send_to_webhook("nda", contract_data, st.session_state['api_key'], st.session_state['webhook_urls'])
