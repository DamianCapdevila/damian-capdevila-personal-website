import streamlit as st
import requests 
import re
from assets.contact_resources import *

def is_valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

@st.dialog("✉ Contact Me")
def contact_form():
    with st.form(FORM_TITLE): 
        name = st.text_input(NAME_LABEL, placeholder=NAME_PLACEHOLDER)
        email = st.text_input(EMAIL_LABEL, placeholder=EMAIL_PLACEHOLDER)
        message = st.text_area(MESSAGE_LABEL, placeholder=MESSAGE_PLACEHOLDER)
        col1, col2, col3 = st.columns(3, gap="large")
        with col2:
            submit_button = st.form_submit_button(SUBMIT_BUTTON_TEXT, type=SUBMIT_BUTTON_TYPE, use_container_width=True)

        if submit_button:
            with st.spinner("Sending message..."):
                # Input validation
                if not name:
                    st.warning(VALIDATION_WARNING_NAME)
                elif not email:
                    st.warning(VALIDATION_WARNING_EMAIL)
                elif not is_valid_email(email):
                    st.warning(VALIDATION_WARNING_VALID_EMAIL)
                elif not message:
                    st.warning(VALIDATION_WARNING_MESSAGE)
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
                            st.success(SUCCESS_MESSAGE)
                        else:
                            st.error(ERROR_MESSAGE)
                    except requests.exceptions.RequestException as e:
                        st.error(ERROR_MESSAGE_WITH_EXCEPTION.format(e))