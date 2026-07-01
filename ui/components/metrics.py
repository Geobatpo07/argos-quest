# ./ui/components/metrics.py

import streamlit as st


def metrics(values: dict[str, str | int | float]) -> None:

    cols = st.columns(len(values))

    for col, (label, value) in zip(cols, values.items()):

        with col:

            st.metric(
                label=label,
                value=value,
            )