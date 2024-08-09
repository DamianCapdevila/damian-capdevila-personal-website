import streamlit as st
from forms.contact import contact_form

col1, col2 = st.columns(2, gap='small', vertical_alignment="center")

with col1:
    st.image("../src/assets/Damian.jpeg", width=330)
with col2:
    st.title("Damian Capdevila", anchor=False)
    st.write("Software Engineer, helping companies worldwide create vuluable products!")
    if st.button("📩 Lets talk!"):
        contact_form()