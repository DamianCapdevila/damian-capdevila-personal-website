import streamlit as st

# URLs, durations, and prices for booking services
INITIAL_CONSULTATION_URL = "https://cal.com/damiancapdevila/initial-consultation"
INITIAL_CONSULTATION_DURATION = "45"
INITIAL_CONSULTATION_PRICE = "50"

RESUME_REVIEW_URL = "https://cal.com/damiancapdevila/resume-review-writing"
RESUME_REVIEW_DURATION = "45"
RESUME_REVIEW_PRICE = "50"

REGULAR_CONSULTATION_URL = "https://cal.com/damiancapdevila/regular-consultation"
REGULAR_CONSULTATION_DURATION = "60"
REGULAR_CONSULTATION_PRICE = "100"

CONTAINER_HEIGHT = 498

st.title("My Services")
col1, col2 = st.columns(2, gap='small')

# Initial Consultation
with col1:
    with st.container(height=CONTAINER_HEIGHT, border=True):
        st.subheader("**Initial Consultation**", anchor=False)
        st.write(f"⏳ Duration: {INITIAL_CONSULTATION_DURATION} minutes")
        st.write(f"💶 Price: {INITIAL_CONSULTATION_PRICE} Euros")
        st.write("""
        **🔎 What We Do:**
        - Discuss your background, experience, and career goals.
        - Assess your strengths and areas to focus on for your transition to software engineering.
        - Define a roadmap for your transition.
                 
        **Special Offer:** Free for the first five customers to help you get started without any cost.
        """)
        st.link_button("BOOK INITIAL CONSULTATION", type="primary", use_container_width=True, url=INITIAL_CONSULTATION_URL)

# Resume Review/Writing
with col2:
    with st.container(height=CONTAINER_HEIGHT, border=True):
        st.subheader("**Resume Review/Writing**", anchor=False)
        st.write(f"⏳ Duration: {RESUME_REVIEW_DURATION} minutes")
        st.write(f"💶 Price: {RESUME_REVIEW_PRICE} Euros")
        st.write(f"""
        **📄 What We Do:**
        - Thoroughly review your current resume with feedback tailored for software engineering roles.
        - Help craft a new resume that emphasizes your transferable skills and experience.
        - Make your CV ATS-proof.
        
        **Special Offer:** Free for the first five customers to help you get started without any cost.
        """)
        st.link_button("BOOK RESUME REVIEW", type="primary", use_container_width=True, url=RESUME_REVIEW_URL)

col3, col4 = st.columns(2, gap='small')

# Regular Consultation
with col3:
    with st.container(height=CONTAINER_HEIGHT, border=True):
        st.subheader("**Regular Consultation**", anchor=False)
        st.write(f"⏳ Duration: {REGULAR_CONSULTATION_DURATION} minutes")
        st.write(f"💶 Price: {REGULAR_CONSULTATION_PRICE} Euros")
        st.write("""
        **📈 What We Do:**
        - Provide ongoing support after the initial consultation.
        - Assess your current transition status.
        - Assist with coding challenges, interview preparation, and career development planning.
        - Get access to all support material to help your transition.
        """)
        st.write("")
        st.link_button("BOOK REGULAR CONSULTATION", type="primary", use_container_width=True, url=REGULAR_CONSULTATION_URL)
