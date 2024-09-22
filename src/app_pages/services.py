import streamlit as st
import utilities.helper
from forms.contact import contact_form
from assets.string_constants.services_resources import *
from app_pages.routes import *

st.subheader(SERVICES_SUBHEADER, divider=True)
st.write(SERVICES_INTRO_TEXT)
st.caption(SERVICES_FAQ_TEXT, unsafe_allow_html=True)
col1, col2 = st.columns(2, gap='small')
col3, col4 = st.columns(2, gap='small')

# Initial Consultation
with col1:
    with st.container(height=CONTAINER_HEIGHT, border=True):
        st.subheader(INITIAL_CONSULTATION_SUBHEADER, anchor=False)
        st.write(DURATION_TEXT.format(INITIAL_CONSULTATION_DURATION))
        st.write(PRICE_TEXT.format(INITIAL_CONSULTATION_PRICE))
        st.write(INITIAL_CONSULTATION_TEXT)
        st.link_button(BOOK_INITIAL_CONSULTATION_TEXT, type="primary", use_container_width=True, url=INITIAL_CONSULTATION_URL)

# Resume Review/Writing
with col3:
    with st.container(height=CONTAINER_HEIGHT, border=True):
        st.subheader(RESUME_REVIEW_SUBHEADER, anchor=False)
        st.write(DURATION_TEXT.format(RESUME_REVIEW_DURATION))
        st.write(PRICE_TEXT.format(RESUME_REVIEW_PRICE))
        st.write(RESUME_REVIEW_TEXT)
        st.link_button(BOOK_RESUME_REVIEW_TEXT, type="primary", use_container_width=True, url=RESUME_REVIEW_URL)

# Regular Consultation
with col2:
    with st.container(height=CONTAINER_HEIGHT, border=True):
        st.subheader(REGULAR_CONSULTATION_SUBHEADER, anchor=False)
        st.write(DURATION_TEXT.format(REGULAR_CONSULTATION_DURATION))
        st.write(PRICE_TEXT.format(REGULAR_CONSULTATION_PRICE))
        st.write(REGULAR_CONSULTATION_TEXT)
        st.link_button(BOOK_REGULAR_CONSULTATION_TEXT, type="primary", use_container_width=True, url=REGULAR_CONSULTATION_URL)

# LinkedIn Profile Review
with col4:
    with st.container(height=CONTAINER_HEIGHT, border=True):
        st.subheader(LINKEDIN_REVIEW_SUBHEADER, anchor=False)
        st.write(DURATION_TEXT.format(LINKEDIN_REVIEW_DURATION))
        st.write(PRICE_TEXT.format(LINKEDIN_REVIEW_PRICE))
        st.write(LINKEDIN_REVIEW_TEXT)
        st.link_button(BOOK_LINKEDIN_REVIEW_TEXT, type="primary", use_container_width=True, url=LINKEDIN_REVIEW_URL)

st.subheader("FAQ", anchor="FAQ", divider=True)
# FAQ 1
with st.expander(FAQ_1_QUESTION):
    st.write(FAQ_1_ANSWER)

# FAQ 2
with st.expander(FAQ_2_QUESTION):
    st.write(FAQ_2_ANSWER)

# FAQ 3
with st.expander(FAQ_3_QUESTION):
    st.write(FAQ_3_ANSWER)

# FAQ 4
with st.expander(FAQ_4_QUESTION):
    st.write(FAQ_4_ANSWER)

# FAQ 5
with st.expander(FAQ_5_QUESTION):
    st.write(FAQ_5_ANSWER)

# FAQ 6
with st.expander(FAQ_6_QUESTION):
    st.write(FAQ_6_ANSWER)

st.subheader(FURTHER_ASSISTANCE_SUBHEADER, divider=True)
st.write(FURTHER_ASSISTANCE_TEXT)

col5, col6, col7, col8 = st.columns([1, 4, 4, 1], gap="medium")

with col6:
    if st.button(ASK_ASSISTANT_BUTTON_TEXT, type="secondary", use_container_width=True):
        st.switch_page(CHAT_PAGE_ROUTE)

with col7:
    if st.button(CONTACT_ME_BUTTON_TEXT, type="primary", use_container_width=True):
        contact_form()

st.write("")
utilities.helper.call_to_action()

st.write("---")
st.write("")
st.write("")
st.write("")
st.write("")

utilities.helper.footer()