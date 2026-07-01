# ./ui/components/alerts.py

import streamlit as st


def success(message: str):

    st.success(message)


def warning(message: str):

    st.warning(message)


def error(message: str):

    st.error(message)