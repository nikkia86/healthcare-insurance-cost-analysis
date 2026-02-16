import streamlit as st


# MultiPage class handles sidebar navigation
class MultiPage:

    # Initialise app with a name
    def __init__(self, app_name="Dashboard App"):
        self.pages = []
        self.app_name = app_name

    # Add a page (title + function)
    def add_page(self, title, func):
        self.pages.append({
            "title": title,
            "function": func
        })

    # Run selected page
    def run(self):
        st.sidebar.title(self.app_name)

        page = st.sidebar.radio(
            "Navigation",
            self.pages,
            format_func=lambda p: p["title"]
        )

        page["function"]()