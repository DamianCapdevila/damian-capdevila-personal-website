import streamlit as st
from utilities.footer import footer
from forms.contact import contact_form

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

LINKEDIN_REVIEW_URL = "https://cal.com/damiancapdevila/linkedin-profile-review"
LINKEDIN_REVIEW_DURATION = "30"
LINKEDIN_REVIEW_PRICE = "35"

CONTAINER_HEIGHT = 438

st.subheader("💻 Services", divider=True)
st.write("*To speed up your transition to software engineering, book consultation sessions that adapt to your schedule!*")
st.caption("""<p>Questions? See <a href="#FAQ">FAQ Section</a></p>""", unsafe_allow_html=True)
col1, col2 = st.columns(2, gap='small')
col3, col4 = st.columns(2, gap='small')

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
        """)
        st.link_button("BOOK INITIAL CONSULTATION", type="primary", use_container_width=True, url=INITIAL_CONSULTATION_URL)

# Resume Review/Writing
with col3:
    with st.container(height=CONTAINER_HEIGHT, border=True):
        st.subheader("**Resume Review/Writing**", anchor=False)
        st.write(f"⏳ Duration: {RESUME_REVIEW_DURATION} minutes")
        st.write(f"💶 Price: {RESUME_REVIEW_PRICE} Euros")
        st.write(f"""
        **📄 What We Do:**
        - Thoroughly review your current resume with feedback tailored for software engineering roles.
        - Help craft a new resume that emphasizes your transferable skills and experience.
        - Make your CV ATS-proof.
        """)
        st.link_button("BOOK RESUME REVIEW", type="primary", use_container_width=True, url=RESUME_REVIEW_URL)

# Regular Consultation
with col2:
    with st.container(height=CONTAINER_HEIGHT, border=True):
        st.subheader("**Regular Consultation**", anchor=False)
        st.write(f"⏳ Duration: {REGULAR_CONSULTATION_DURATION} minutes")
        st.write(f"💶 Price: {REGULAR_CONSULTATION_PRICE} Euros")
        st.write("""
        **📈 What We Do:**
        - Provide ongoing support after the initial consultation.
        - Assess your current transition status.
        - Assist with coding challenges, interview preparation, and career development planning.
        """)
        st.link_button("BOOK REGULAR CONSULTATION", type="primary", use_container_width=True, url=REGULAR_CONSULTATION_URL)

# Resume Review/Writing
with col4:
    with st.container(height=CONTAINER_HEIGHT, border=True):
        st.subheader("**LinkedIn Profile Review**", anchor=False)
        st.write(f"⏳ Duration: {LINKEDIN_REVIEW_DURATION} minutes")
        st.write(f"💶 Price: {LINKEDIN_REVIEW_PRICE} Euros")
        st.write(f"""
        **📄 What We Do:**
        - Carefully review your current LinkedIn profile with feedback tailored for software engineering roles.
        - Enhance the profile to make opportunities come to you.
        - Help you build a personal brand.
        """)
        st.link_button("BOOK LINKEDIN REVIEW", type="primary", use_container_width=True, url=LINKEDIN_REVIEW_URL)

st.subheader("FAQ", anchor="FAQ", divider=True)
# FAQ 1
with st.expander("**How do I know if these services are right for me?**"):
    st.write("""
    *If you're an engineer from a different field, such as automation, and you're considering a transition to software engineering, my services are designed for you. During the initial consultation, we discuss your background and career goals to ensure that the services align with your needs. My goal is to help you make a smooth transition into the software engineering field.*
    """)

# FAQ 2
with st.expander("**How many consultations does it typically take?**"):
    st.write("""
    *The number of consultations depends on your individual needs and how quickly you progress. Some clients might require just one or two sessions for specific guidance, while others may benefit from ongoing support over several months. We can discuss a customized plan during the initial consultation.*
    """)

# FAQ 3
with st.expander("**How long does it usually take to transition into software engineering?**"):
    st.write("""
    *The time it takes to transition into software engineering varies depending on your current skills, the time you can dedicate to learning, and the specific area of software engineering you're targeting. On average, it could take anywhere from a few months to a year with consistent effort and the right guidance.*
    """)

# FAQ 4
with st.expander("**What programming language should I start with?**"):
    st.write("""
    *The best programming language to start with depends on your career goals. If you're interested in web development, Python and JavaScript are popular choices. For systems programming, C++ might be more suitable. During our consultations, I can help you choose the right language based on your background and objectives.*
    """)

# FAQ 5
with st.expander("**What payment methods do you accept?**"):
    st.write("""
    *I accept various payment methods, including credit/debit cards, PayPal, and bank transfers. If you have any specific requirements or preferences, feel free to discuss them during our consultation.*
    """)

# FAQ 6
with st.expander("**What is the difference between an initial and a regular consultation?**"):
    st.write("""
    *The initial consultation is designed to understand your background, career goals, and create a tailored roadmap for your transition into software engineering. The regular consultations are follow-up sessions where we assess your progress, tackle any challenges you're facing, and continue to refine your transition plan.*
    """)

st.subheader("Further Assistance", divider=True)
st.write("*In case you have questions that are not listed in the FAQ, feel free to ask my assistant. If you prefer talking to a human, contact me!*")

col5, col6, col7, col8 = st.columns([1, 4, 4, 1], gap="medium")

with col6:
  if st.button("🤖 Ask my assistant", type="primary", use_container_width=True):
    st.switch_page("pages/chat.py")

with col7:
  if st.button("✉️ Contact me!", type="primary", use_container_width=True):
    contact_form()

st.write("---")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")

footer()