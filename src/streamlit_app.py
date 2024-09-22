import streamlit as st
from utilities.helper import sidebar_footer
from app_pages.routes import *
import os

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

# Site logo setup:

# Function to get absolute path
def get_absolute_path(relative_path):
    return os.path.abspath(os.path.join(os.path.dirname(__file__), relative_path))

# Construct the absolute path to the site logo
image_path = get_absolute_path("assets/images/background-removed.png")

# Verify if the image exists before setting the site logo
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

# Footer setup:
sidebar_footer()

# Run the navigation:
pg.run()