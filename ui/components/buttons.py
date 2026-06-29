# ./ui/components/buttons.py

import streamlit as st


def sync_button():

    return st.button(
        "🔄 Synchroniser les offres",
        use_container_width=True,
    )