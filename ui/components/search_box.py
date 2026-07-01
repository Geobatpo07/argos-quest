# ./ui/components/search_box.py

import streamlit as st


def search_box():

    return st.text_input(
        "🔍 Rechercher une thèse",
        placeholder="Machine Learning...",
    )