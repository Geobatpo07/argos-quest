# ./app.py

import streamlit as st

from ui.pages.dashboard import show_dashboard

st.set_page_config(
    page_title="Argos Quest",
    page_icon="⛵",
    layout="wide",
)

show_dashboard()