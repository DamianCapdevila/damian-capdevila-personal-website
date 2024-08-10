import streamlit as st
from forms.contact import contact_form

col1, col2 = st.columns(2, gap='small', vertical_alignment="top")



with col1:
    st.image("../src/assets/Damian-sin fondo-verde.png", width=330)
with col2:
    
    st.write('\n')
    st.title("Damian Capdevila", anchor=False)
    st.write("Software Engineer, helping companies worldwide create vuluable products!")
    col3, col4 = st.columns(2, gap='small', vertical_alignment="center")
    with col3:
        if st.button("📩 Send me an email!"):
            contact_form()
    with col4:
        if st.button("🤖 Ask my assistant!"):
            st.switch_page("pages/chat.py")