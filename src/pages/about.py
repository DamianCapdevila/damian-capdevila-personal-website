import streamlit as st
import utilities.helper
from assets.about_resources import *

# Headshot, UVP and Name
col1, col2 = st.columns(2, gap='small', vertical_alignment="top")

with col1:
    st.image(HEADSHOT_URL, output_format="PNG", width=HEADSHOT_WIDTH)
with col2:
    st.title(TITLE_TEXT, anchor=False)
    st.write(UVP_MAIN_TEXT)
    st.write(f"*{UVP_EXPLANATION_TEXT}*")

# Call to Action
st.subheader(SERVICES_SUBHEADER, divider=True)

st.write(SERVICES_QUESTION)
col5, col6, col7 = st.columns(3, gap='small', vertical_alignment="center")
with col5:
    if st.button(CONSULTATION_BUTTON_TEXT, type="primary", help=CONSULTATION_BUTTON_HELP):
        st.switch_page("pages/services.py")
with col6:
    st.link_button(ACTIONABLE_ADVICE_BUTTON_TEXT, url=ACTIONABLE_STEPS_URL, type="secondary", help=ACTIONABLE_ADVICE_BUTTON_HELP)

utilities.helper.faq()

# About Me
st.write("")
st.subheader(ABOUT_ME_SUBHEADER, divider=True)
st.write(ABOUT_ME_TEXT.format(TRANSITION_STORY_URL))

with st.expander(label=EXPERIENCE_LABEL, icon="👨‍🏭"):
    st.write("")
    with st.container(border=False):
        st.write(EXPERIENCE_TEXT)
        st.write(LINKEDIN_PROFILE_TEXT.format(LINKEDIN_PROFILE_URL))
        st.write("")

with st.expander(EDUCATION_LABEL, icon="👨‍🎓"):
    st.subheader(FORMAL_EDUCATION_SUBHEADER, divider=True)
    st.write(EDUCATION_TEXT)

    st.subheader(RELEVANT_COURSES_SUBHEADER, divider=True)
    st.write(COURSES_TEXT)

with st.expander(label=SKILLS_LABEL, icon="🛠"):
    st.write("")
    st.write(SKILLS_TEXT)
    st.write("")

# Call to Action
st.write("")
utilities.helper.call_to_action()
utilities.helper.faq()

# Disclaimer
utilities.helper.add_vertical_space(5)  # This will add 5 blank lines
utilities.helper.footer()