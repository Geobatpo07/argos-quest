# ./app.py

import streamlit as st

from ui.components.sidebar import sidebar

from ui.pages.analytics import show_analytics
from ui.pages.dashboard import show_dashboard
from ui.pages.settings import show_settings
from ui.pages.sources import show_sources
from ui.pages.theses import show_theses


# ---------------------------------------------------------------------
# Page configuration
# ---------------------------------------------------------------------

st.set_page_config(
    page_title="Argos Quest",
    page_icon="⛵",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------------------------------------------------------------------
# Sidebar
# ---------------------------------------------------------------------

sidebar()

# ---------------------------------------------------------------------
# Navigation
# ---------------------------------------------------------------------

navigation = st.navigation(
    {
        "Explore": [
            st.Page(
                show_dashboard,
                title="Dashboard",
                icon="🏠",
                default=True,
            ),
            st.Page(
                show_theses,
                title="Theses",
                icon="📚",
            ),
            st.Page(
                show_analytics,
                title="Analytics",
                icon="📈",
            ),
        ],
        "Configuration": [
            st.Page(
                show_sources,
                title="Sources",
                icon="🏛️",
            ),
            st.Page(
                show_settings,
                title="Settings",
                icon="⚙️",
            ),
        ],
    }
)

# ---------------------------------------------------------------------
# Run application
# ---------------------------------------------------------------------

navigation.run()