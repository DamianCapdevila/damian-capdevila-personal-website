import streamlit as st
import utilities.helper
from assets.about_resources import *

col1, col2 = st.columns(2, gap='small', vertical_alignment="top")

with col1:
    st.image(HEADSHOT_URL, output_format="PNG", width=)
with col2:
    st.title("Damián Capdevila", anchor=False)
    st.write(UVP_MAIN_TEXT)
    st.write(f"*{UVP_EXPLANATION_TEXT}*")
        
st.subheader("Providing Services", divider=True)

st.write("*Are you ready to start your transition into software engineering?*")
col5, col6, col7 = st.columns(3, gap='small', vertical_alignment="center")
with col5:
    if st.button("📈 FREE Initial Consultation!", type="primary", help="**Book a free initial consultation!**"):
        st.switch_page("pages/services.py")
with col6:
    st.link_button("💡 See Actionable Advice", url=ACTIONABLE_STEPS_URL, type="secondary", help="**See 8 steps to begin your transition!**")

utilities.helper.faq()

st.write("")
st.subheader("About Me", divider=True)
st.write(ABOUT_ME_TEXT)

with st.expander(label="**Experience**", icon="👨‍🏭"):
    st.write("")

    with st.container(border=False):
        st.write(EXPERIENCE_TEXT)
    
        st.write(f"- For further details, you can visit my [LinkedIn Profile]({LINKEDIN_PROFILE_URL}) 😎")
        st.write("")

with st.expander("**Education**", icon="👨‍🎓"):
    st.subheader("Formal Education", divider=True)
    st.write(EDUCATION_TEXT)

    st.subheader("Relevant Courses", divider=True)
    st.write(COURSES_TEXT)

with st.expander(label="**Skills**", icon="🛠"):
    st.write("")
    st.write(SKILLS_TEXT)
    st.write("")

st.write("")
utilities.helper.call_to_action()
utilities.helper.faq()

#Disclaimer
st.write("---")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")

utilities.helper.footer()