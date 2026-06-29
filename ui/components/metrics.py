# ./ui/components/metrics.py

import streamlit as st


def metric(
    label: str,
    value,
):

    st.metric(
        label=label,
        value=value,
    )