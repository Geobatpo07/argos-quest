# ./ui/components/layout.py

import streamlit as st


def page(
    title: str,
    icon: str = "",
    description: str | None = None,
) -> None:
    """Render a standard page header."""

    if icon:
        st.title(f"{icon} {title}")
    else:
        st.title(title)

    if description:
        st.caption(description)

    st.divider()


def section(title: str) -> None:
    """Render a section title."""

    st.subheader(title)