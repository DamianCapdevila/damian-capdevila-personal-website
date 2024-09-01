import streamlit as st
from forms.contact import contact_form
from utilities.footer import sidebar_footer

# Multiple pages setup:

about_page = st.Page(
    page = "pages/about.py",
    title = "About Me",
    icon = "📄",
    default = True,
)

services_page = st.Page(
    page = "pages/services.py",
    title = "Services",
    icon = "💻",
)

chat_page = st.Page(
    page = "pages/chat.py",
    title = "Ask my assistant!",
    icon = "🤖",
)

st.logo("assets/background-removed.png")
#Navigation setup:
pg = st.navigation(
    {
        "Introduction": [about_page, chat_page],
        "Services": [services_page],
    }
)

sidebar_footer()

#Run the navigation:
pg.run()