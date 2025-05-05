import streamlit as st

# Set the page configuration
st.set_page_config(page_title="Contract Management System", layout="wide")
st.title("📄 Business Contract Management System")

# Sidebar with authentication & webhook configuration
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
        "confidentiality": st.text_input("Confidentiality Webhook URL"),
        # Add other contract webhooks as necessary
    }

    st.markdown("---")
    st.caption("ℹ️ Configure webhook URLs in your n8n workflow first")
    
    # Sidebar listing all 116 contract pages
    st.header("📜 Contract Pages")
    contract_pages = [
        ("01_Partnership_Agreement", "Partnership Agreement"),
        ("02_Employment_Agreement", "Employment Agreement"),
        ("03_Service_Agreement", "Service Agreement"),
        ("04_Non_Disclosure_Agreement", "Non-Disclosure Agreement (NDA)"),
        ("05_Freelance_Agreement", "Freelance Agreement"),
        ("06_Lease_Agreement", "Lease Agreement"),
        ("07_Distribution_Agreement", "Distribution Agreement"),
        ("08_Investment_Agreement", "Investment Agreement"),
        ("09_Consulting_Agreement", "Consulting Agreement"),
        ("10_Joint_Venture_Agreement", "Joint Venture Agreement"),
        ("11_Sponsorship_Agreement", "Sponsorship Agreement"),
        ("12_Licensing_Agreement", "Licensing Agreement"),
        ("13_Sales_Agreement", "Sales Agreement"),
        ("14_Confidentiality_Agreement", "Confidentiality Agreement"),
        ("15_Equity_Sharing_Agreement", "Equity Sharing Agreement"),
        ("16_Shareholder_Agreement", "Shareholder Agreement"),
        ("17_Business_Sale_Agreement", "Business Sale Agreement"),
        ("18_Membership_Agreement", "Membership Agreement"),
        ("19_Purchase_Agreement", "Purchase Agreement"),
        ("20_Real_Estate_Agreement", "Real Estate Agreement"),
        ("21_Leverage_Agreement", "Leverage Agreement"),
        ("22_Wholesale_Contract", "Wholesale Contract"),
        ("23_Installment_Agreement", "Installment Agreement"),
        ("24_Real_Estate_Option_Agreement", "Real Estate Option Agreement"),
        ("25_Asset_Transfer_Agreement", "Asset Transfer Agreement"),
        ("26_Conditional_Sale_Agreement", "Conditional Sale Agreement"),
        ("27_Purchase_Option_Agreement", "Purchase Option Agreement"),
        ("28_Escrow_Agreement", "Escrow Agreement"),
        ("29_Financing_Agreement", "Financing Agreement"),
        ("30_Deferred_Payment_Agreement", "Deferred Payment Agreement"),
        ("31_Lease_Option_Agreement", "Lease Option Agreement"),
        ("32_Rent_And_Sale_Agreement", "Rent and Sale Agreement"),
        ("33_Security_Agreement", "Security Agreement"),
        ("34_Management_Agreement", "Management Agreement"),
        ("35_Agent_Agreement", "Agent Agreement"),
        ("36_Real_Estate_Flipping_Agreement", "Real Estate Flipping Agreement"),
        ("37_Power_Of_Attorney_Agreement", "Power of Attorney Agreement"),
        ("38_Contract_Assignment_Agreement", "Contract Assignment Agreement"),
        ("39_Buyer_Agreement", "Buyer Agreement"),
        ("40_Seller_Agreement", "Seller Agreement"),
        ("41_Loan_Agreement", "Loan Agreement"),
        ("42_Purchase_Sale_Agreement", "Purchase Sale Agreement"),
        ("43_Investment_Contract", "Investment Contract"),
        ("44_Real_Estate_Sale_Agreement", "Real Estate Sale Agreement"),
        ("45_Shareholder_Agreement", "Shareholder Agreement"),
        ("46_Co_Signing_Agreement", "Co-Signing Agreement"),
        ("47_Mortgage_Option_Agreement", "Mortgage Option Agreement"),
        ("48_Funding_Agreement", "Funding Agreement"),
        ("49_Equity_Agreement", "Equity Agreement"),
        ("50_Funding_Agreement", "Funding Agreement"),
        ("51_Wholesale_Purchase_Agreement", "Wholesale Purchase Agreement"),
        ("52_Real_Estate_Investor_Agreement", "Real Estate Investor Agreement"),
        ("53_Personal_Guarantee_Agreement", "Personal Guarantee Agreement"),
        ("54_Foreclosure_Agreement", "Foreclosure Agreement"),
        ("55_Capital_Agreement", "Capital Agreement"),
        ("56_Home_Sale_Agreement", "Home Sale Agreement"),
        ("57_Real_Estate_Option_Purchase_Agreement", "Real Estate Option Purchase Agreement"),
        ("58_Property_Management_Agreement", "Property Management Agreement"),
        ("59_Residential_Rental_Agreement", "Residential Rental Agreement"),
        ("60_Commercial_Lease_Agreement", "Commercial Lease Agreement"),
        ("61_Real_Estate_Lease_Agreement", "Real Estate Lease Agreement"),
        ("62_Residential_Sale_Agreement", "Residential Sale Agreement"),
        ("63_Tenant_Landlord_Agreement", "Tenant Landlord Agreement"),
        ("64_Property_Rent_Agreement", "Property Rent Agreement"),
        ("65_Lease_Purchase_Agreement", "Lease Purchase Agreement"),
        ("66_Mortgage_Contract", "Mortgage Contract"),
        ("67_Property_Sale_Agreement", "Property Sale Agreement"),
        ("68_Broker_Agreement", "Broker Agreement"),
        ("69_Real_Estate_Agent_Agreement", "Real Estate Agent Agreement"),
        ("70_Estate_Sale_Agreement", "Estate Sale Agreement"),
        ("71_Financing_Real_Estate_Agreement", "Financing Real Estate Agreement"),
        ("72_Agent_Broker_Agreement", "Agent Broker Agreement"),
        ("73_Payment_Agreement", "Payment Agreement"),
        ("74_Financial_Structure_Agreement", "Financial Structure Agreement"),
        ("75_Investor_Agreement", "Investor Agreement"),
        ("76_Rental_Option_Agreement", "Rental Option Agreement"),
        ("77_Sale_Purchase_Agreement", "Sale Purchase Agreement"),
        ("78_Rent_Sale_Agreement", "Rent Sale Agreement"),
        ("79_Equity_Participation_Agreement", "Equity Participation Agreement"),
        ("80_Capital_Partnership_Agreement", "Capital Partnership Agreement"),
        ("81_Payment_Plan_Agreement", "Payment Plan Agreement"),
        ("82_Business_Purchase_Agreement", "Business Purchase Agreement"),
        ("83_Investing_Agreement", "Investing Agreement"),
        ("84_Credit_Option_Agreement", "Credit Option Agreement"),
        ("85_Supplier_Agreement", "Supplier Agreement"),
        ("86_Real_Estate_Transaction_Agreement", "Real Estate Transaction Agreement"),
        ("87_Real_Estate_Fund_Agreement", "Real Estate Fund Agreement"),
        ("88_Equity_Purchase_Agreement", "Equity Purchase Agreement"),
        ("89_Acquisition_Agreement", "Acquisition Agreement"),
        ("90_Property_Development_Agreement", "Property Development Agreement"),
        ("91_Rental_Property_Agreement", "Rental Property Agreement"),
        ("92_Real_Estate_Investment_Agreement", "Real Estate Investment Agreement"),
        ("93_Short_Term_Lease_Agreement", "Short Term Lease Agreement"),
        ("94_Seller_Financing_Agreement", "Seller Financing Agreement"),
        ("95_Real_Estate_Profit_Sharing_Agreement", "Real Estate Profit Sharing Agreement"),
        ("96_Rent_Lease_Agreement", "Rent Lease Agreement"),
        ("97_Real_Estate_Refinance_Agreement", "Real Estate Refinance Agreement"),
        ("98_Mortgage_Loan_Agreement", "Mortgage Loan Agreement"),
        ("99_Investment_Real_Estate_Agreement", "Investment Real Estate Agreement"),
        ("100_Loan_Agreement", "Loan Agreement"),
        ("101_Equity_Share_Agreement", "Equity Share Agreement"),
        ("102_Land_Purchase_Agreement", "Land Purchase Agreement"),
        ("103_Financing_Purchase_Agreement", "Financing Purchase Agreement"),
        ("104_Property_Option_Agreement", "Property Option Agreement"),
        ("105_Loan_Contract", "Loan Contract"),
        ("106_Rental_Investment_Agreement", "Rental Investment Agreement"),
        ("107_Estate_Investment_Agreement", "Estate Investment Agreement"),
        ("108_Lease_Option_Agreement", "Lease Option Agreement"),
        ("109_Vendor_Contract_Agreement", "Vendor Contract Agreement"),
        ("110_Flipping_Agreement", "Flipping Agreement"),
        ("111_Cash_Sale_Agreement", "Cash Sale Agreement"),
        ("112_Rent_And_Sell_Agreement", "Rent and Sell Agreement"),
        ("113_Equity_Sharing_Agreement", "Equity Sharing Agreement"),
        ("114_Property_Management_Agreement", "Property Management Agreement"),
        ("115_Contract_Assignment_Agreement", "Contract Assignment Agreement"),
        ("116_Mortgage_Option_Agreement", "Mortgage Option Agreement")
    ]

    # Loop through contract pages to create links
    for page_filename, page_name in contract_pages:
        st.markdown(f"[{page_name}]({page_filename})")
        
# Main content
st.header("Welcome to the Contract Management System")

st.write("""
    This system allows you to manage various business contracts. Please use the sidebar to navigate through different contract types and input your data.
""")
