import streamlit as st
from utilities.helper import sidebar_footer
from app_pages.routes import *
from assets.string_constants.about_resources import HEADSHOT_URL
import os

# Site logo setup:
def get_absolute_path(relative_path):
    return os.path.abspath(os.path.join(os.path.dirname(__file__), relative_path))

# Construct the absolute path to the site logo
logo_image_path = get_absolute_path("assets/images/background-removed.png")

st.set_page_config(page_title="Damián Capdevila - Software Engineer", page_icon=HEADSHOT_URL)

# Multiple pages setup:
about_page = st.Page(
    page = ABOUT_PAGE_ROUTE,
    title = "About Me",
    icon = "📄",
    default = True,
)

services_page = st.Page(
    page = SERVICES_PAGE_ROUTE,
    title = "Services",
    icon = "💻",
)

chat_page = st.Page(
    page = CHAT_PAGE_ROUTE,
    title = "Ask my assistant!",
    icon = "🤖",
)

# Verify if the image exists before setting the site logo
if os.path.exists(logo_image_path):
    st.logo(logo_image_path)
else:
    st.error(f"Logo image not found at {logo_image_path}")

# Navigation setup:
pg = st.navigation(
    {
        "Introduction": [about_page, chat_page],
        "Services": [services_page],
    }
)

# Footer setup:
sidebar_footer()

# Run the navigation:
pg.run()