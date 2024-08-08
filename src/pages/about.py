import streamlit as st

col1, col2 = st.columns(2, gap='small', vertical_alignment="center")

with col1:
    st.image("src/assets/Damian.jpeg", width=330)
with col2:
    st.title("Damian Capdevila")
    st.write("Damian")