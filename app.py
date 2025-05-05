import streamlit as st
import requests

# Page configuration
st.set_page_config(page_title="Contract Management System", layout="wide")

# Sidebar settings
with st.sidebar:
    st.header("🔐 Authentication & Webhook Configuration")
    api_key = st.text_input("API Key", type="password", help="Your secure API key for authentication")

    webhook_urls = {
        "partnership": st.text_input("Partnership Webhook URL"),
        "employment": st.text_input("Employment Webhook URL"),
        "service": st.text_input("Service Webhook URL"),
        "nda": st.text_input("NDA Webhook URL"),
        "freelance": st.text_input("Freelance Webhook URL")
    }

    st.markdown("---")
    st.caption("ℹ️ Make sure all webhooks are correctly set in your n8n workflow")

# Webhook sending utility
def send_to_webhook(contract_type, data):
    url = webhook_urls.get(contract_type)
    if not url:
        return st.error(f"No webhook URL configured for '{contract_type}'")

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

# Partnership Agreement
def partnership_contract():
    with st.form("partnership_form"):
        st.header("🤝 Partnership Agreement")
        col1, col2 = st.columns(2)
        with col1:
            p1_name = st.text_input("Partner 1 Name")
            p1_address = st.text_input("Partner 1 Address")
            p1_contribution = st.number_input("Partner 1 Contribution ($)", min_value=1000)
        with col2:
            p2_name = st.text_input("Partner 2 Name", key="p2_name")
            p2_address = st.text_input("Partner 2 Address", key="p2_address")
            p2_contribution = st.number_input("Partner 2 Contribution ($)", min_value=1000, key="p2_contrib")

        if st.form_submit_button("Submit Partnership Agreement"):
            contract_data = {
                "type": "partnership",
                "partners": [
                    {"name": p1_name, "address": p1_address, "contribution": p1_contribution},
                    {"name": p2_name, "address": p2_address, "contribution": p2_contribution}
                ]
            }
            send_to_webhook("partnership", contract_data)

# Employment Contract
def employment_contract():
    with st.form("employment_form"):
        st.header("👔 Employment Contract")
        col1, col2 = st.columns([2, 1])
        with col1:
            employee_name = st.text_input("Employee Name")
            job_title = st.selectbox("Job Title", ["Manager", "Developer", "Designer", "Analyst"])
        with col2:
            start_date = st.date_input("Start Date")
            salary = st.number_input("Annual Salary ($)", min_value=30000, step=5000)

        benefits = st.multiselect("Benefits", ["Health Insurance", "401(k)", "Stock Options", "PTO"])

        if st.form_submit_button("Submit Employment Contract"):
            contract_data = {
                "type": "employment",
                "employee": employee_name,
                "position": job_title,
                "start_date": str(start_date),
                "salary": salary,
                "benefits": benefits
            }
            send_to_webhook("employment", contract_data)

# Service Agreement
def service_contract():
    with st.form("service_form"):
        st.header("🔧 Service Agreement")
        client_name = st.text_input("Client Name")
        service_desc = st.text_area("Service Description", height=150)
        col1, col2, col3 = st.columns(3)
        with col1:
            payment_terms = st.selectbox("Payment Terms", ["Net 30", "50% Advance", "Milestone"])
        with col2:
            duration = st.number_input("Contract Duration (months)", min_value=1, max_value=36)
        with col3:
            termination_clause = st.checkbox("Include Termination Clause")

        if st.form_submit_button("Submit Service Agreement"):
            contract_data = {
                "type": "service",
                "client": client_name,
                "description": service_desc,
                "payment_terms": payment_terms,
                "duration": duration,
                "termination_clause": termination_clause
            }
            send_to_webhook("service", contract_data)

# NDA Agreement
def nda_contract():
    with st.form("nda_form"):
        st.header("🛡️ Non-Disclosure Agreement")
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
            send_to_webhook("nda", contract_data)

# Freelance Agreement
def freelance_contract():
    with st.form("freelance_form"):
        st.header("🧑‍💻 Freelance Agreement")
        freelancer = st.text_input("Freelancer Name")
        client = st.text_input("Client Name", key="freelance_client")
        scope = st.text_area("Scope of Work", height=120)
        rate = st.number_input("Hourly Rate ($)", min_value=10)
        deadline = st.date_input("Project Deadline")

        if st.form_submit_button("Submit Freelance Agreement"):
            contract_data = {
                "type": "freelance",
                "freelancer": freelancer,
                "client": client,
                "scope_of_work": scope,
                "hourly_rate": rate,
                "deadline": str(deadline)
            }
            send_to_webhook("freelance", contract_data)

# Page selection
pages = {
    "Partnership Agreement": partnership_contract,
    "Employment Contract": employment_contract,
    "Service Agreement": service_contract,
    "Non-Disclosure Agreement": nda_contract,
    "Freelance Agreement": freelance_contract
}

# App layout
st.title("📄 Business Contract Management System")
st.subheader("Easily create and submit contracts to your automation workflows")
selected_page = st.sidebar.selectbox("Choose Contract Type", list(pages.keys()))
pages[selected_page]()
