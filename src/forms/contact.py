import streamlit as st
import requests 
import re

GOOGLE_APPS_SEND_EMAIL_SCRIPT_URL = 'https://script.google.com/macros/s/AKfycbzSIJs3dvcsAhLugSSIkRGUWeQavN3T81K52mgJwmUnv7di9exBMN5OSLQvmr39JnJHzA/exec'

def is_valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

@st.dialog("✉ Contact Me")
def contact_form():
    with st.form("Contact Me"): 
        name = st.text_input("Name", placeholder="Jane Doe")
        email = st.text_input("Email", placeholder="someone@example.com")
        message = st.text_area("Message", placeholder="What´s your strategy for career transitioning?")
        col1, col2, col3 = st.columns(3, gap="large")
        with col2:
            submit_button = st.form_submit_button("Submit", type="primary", use_container_width=True)

        if submit_button:
            with st.spinner("Sending message..."):
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