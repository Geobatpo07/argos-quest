# ./ui/pages/theses.py

import streamlit as st

from application.use_cases.get_all_theses_use_case import (
    GetAllThesesUseCase,
)

from ui.components.search_box import search_box
from ui.components.thesis_table import thesis_table


def show_theses():

    st.title("📚 Thèses")

    keyword = search_box()

    theses = (
        GetAllThesesUseCase()
        .execute()
    )

    if keyword:

        keyword = keyword.lower()

        theses = [
            thesis
            for thesis in theses
            if keyword in thesis.title.lower()
        ]

    thesis_table(theses)