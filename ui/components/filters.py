# ./ui/components/filters.py

import streamlit as st


def select_filter(
    label: str,
    options: list[str],
) -> str:

    return st.selectbox(
        label,
        options,
    )