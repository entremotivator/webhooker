# Home.py
import streamlit as st

st.set_page_config(page_title="Contract Management System", layout="wide")
st.title("📄 Business Contract Management System")

with st.sidebar:
    st.header("🔐 Authentication & Webhook Configuration")
    st.session_state['api_key'] = st.text_input("API Key", type="password")
    st.session_state['webhook_urls'] = {
        "partnership": st.text_input("Partnership Webhook URL"),
        "employment": st.text_input("Employment Webhook URL"),
        "service": st.text_input("Service Webhook URL"),
        "nda": st.text_input("NDA Webhook URL"),
        "freelance": st.text_input("Freelance Webhook URL"),
        "lease": st.text_input("Lease Webhook URL"),
        "distribution": st.text_input("Distribution Webhook URL"),
        "investment": st.text_input("Investment Webhook URL"),
        "consulting": st.text_input("Consulting Webhook URL"),
        "joint_venture": st.text_input("Joint Venture Webhook URL"),
        "sponsorship": st.text_input("Sponsorship Webhook URL"),
        "licensing": st.text_input("Licensing Webhook URL"),
        "sales": st.text_input("Sales Webhook URL"),
        "confidentiality": st.text_input("Confidentiality Webhook URL")
    }
    st.markdown("---")
    st.caption("ℹ️ Configure webhook URLs in your n8n workflow first")
