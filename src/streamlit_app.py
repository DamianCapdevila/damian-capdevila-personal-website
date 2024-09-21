import streamlit as st
from forms.contact import contact_form
from utilities.helper import sidebar_footer
import os

# Function to get absolute path
def get_absolute_path(relative_path):
    return os.path.abspath(os.path.join(os.path.dirname(__file__), relative_path))

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

# Construct the absolute path to the image
image_path = get_absolute_path("assets/background-removed.png")

# Verify if the image exists before setting the logo
if os.path.exists(image_path):
    st.logo(image_path)
else:
    st.error(f"Logo image not found at {image_path}")

# Navigation setup:
pg = st.navigation(
    {
        "Introduction": [about_page, chat_page],
        "Services": [services_page],
    }
)

sidebar_footer()

# Run the navigation:
pg.run()