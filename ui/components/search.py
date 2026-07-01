# ./ui/components/search.py

import streamlit as st


def search_box(
    placeholder: str = "Search...",
) -> str:

    return st.text_input(
        label="Search",
        placeholder=placeholder,
        label_visibility="collapsed",
    )