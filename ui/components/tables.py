# ./ui/components/tables.py

import pandas as pd
import streamlit as st


def dataframe(
    df: pd.DataFrame,
) -> None:

    st.dataframe(
        df,
        hide_index=True,
        width="stretch",
    )