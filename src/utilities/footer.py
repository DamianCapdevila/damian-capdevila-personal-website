import streamlit as st

FOOTER_TEXT = """
        <div style="text-align: center;">
            <p>Made with 💪🏼 by <a href="https://linkedin.com/in/damiancapdevila" target="_blank">Damian Capdevila</a></p>
            <p><b>Damian Capdevila, LLC</b> - All rights reserved</p>
        </div>
        """

def footer():
    st.markdown(FOOTER_TEXT, unsafe_allow_html=True)

def sidebar_footer():
    st.sidebar.markdown(FOOTER_TEXT, unsafe_allow_html=True)

def call_to_action():
    # Call to Action - Book an appointment
    st.subheader("🗓️ Book an Appointment", divider=True)
    st.write("*Start your transition into software engineering **for free!***")
    if st.button("📈 FREE Initial Consultation!", key="Footer call to action", type="primary", help="**Book a free initial consultation!**"):
        st.switch_page("pages/services.py")