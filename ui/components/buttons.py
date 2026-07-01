# ./ui/components/buttons.py

import streamlit as st


def primary_button(
    label: str,
    icon: str | None = None,
    key: str | None = None,
) -> bool:

    return st.button(
        label,
        icon=icon,
        key=key,
        type="primary",
        width="stretch",
    )


def secondary_button(
    label: str,
    icon: str | None = None,
    key: str | None = None,
) -> bool:

    return st.button(
        label,
        icon=icon,
        key=key,
        width="stretch",
    )