# ./ui/pages/settings.py

from config.settings import settings

from ui.components.layout import page


def show_settings():

    page(
        title="Settings",
        icon="⚙️",
        description="Application configuration.",
    )

    import streamlit as st

    st.write("Application")

    st.code(settings.app_name)

    st.write("Database")

    st.code(settings.database_path)