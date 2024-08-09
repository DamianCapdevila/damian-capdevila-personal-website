import streamlit as st
import requests 
import re

GOOGLE_APPS_SEND_EMAIL_SCRIPT_URL = 'https://script.google.com/macros/s/AKfycbz4Z1u9vGxFcKNYZg0ANFkPMHu764Mjr5k5Ynhqh-QlsJZ7J0VESbsSmNTJ_407ExMB/exec'

def is_valid_email(email):
    # Simple regex for validating an email address
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

@st.dialog("Contact Me")
def contact_form():
    with st.form("Contact Me"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message")
        submit_button = st.form_submit_button("Submit")

        if submit_button:
            # Input validation
            if not name:
                st.warning("⚠️ Please enter your name.")
            elif not email:
                st.warning("⚠️ Please enter your email.")
            elif not is_valid_email(email):
                st.warning("⚠️ Please enter a valid email address.")
            elif not message:
                st.warning("⚠️ Please enter your message.")
            else:
                # Data is valid, send it to Google Apps Script
                data = {
                    "name": name,
                    "email": email,
                    "message": message
                }
                try:
                    response = requests.post(GOOGLE_APPS_SEND_EMAIL_SCRIPT_URL, json=data)
                    if response.status_code == 200:
                        st.success("💌 Message sent!")
                    else:
                        st.error("❌ Failed to send message. Please try again later.")
                except requests.exceptions.RequestException as e:
                    st.error(f"❌ Failed to send message. Error: {e}")