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

def faq():
    st.caption("""<p>Questions? See <a href="services#FAQ" target="_self">FAQ Section</a></p>""", unsafe_allow_html=True)

def add_vertical_space(num_lines: int = 1):
    """
    Adds vertical space using Streamlit's write function.
    
    Args:
    num_lines (int): Number of lines of vertical space to add. Defaults to 1.
    """
    for _ in range(num_lines):
        st.write("")