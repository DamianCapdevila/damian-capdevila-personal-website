import streamlit as st

# Multiple pages setup:

about_page = st.Page(
    page = "pages/about.py",
    title = "About Me",
    icon = "📄",
    default = True,
)

projects_page = st.Page(
    page = "pages/projects.py",
    title = "My Projects",
    icon = "💻",
)

chat_page = st.Page(
    page = "pages/chat.py",
    title = "Ask my assistant!",
    icon = "🤖",
)


#Navigation setup:
pg = st.navigation(
    {
        "Introduction": [about_page],
        "Experience": [chat_page, projects_page],
    }
)


st.sidebar.text("Made with ❤ by Damian Capdevila")

#Run the navigation:
pg.run()