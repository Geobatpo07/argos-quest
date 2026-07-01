# ./ui/pages/theses.py

import pandas as pd

from application.use_cases.get_all_theses_use_case import (
    GetAllThesesUseCase,
)

from ui.components.layout import page
from ui.components.search import search_box
from ui.components.tables import dataframe


def show_theses():

    page(
        title="Theses",
        icon="📚",
        description="Browse all available PhD opportunities.",
    )

    keyword = search_box(
        "Search a thesis..."
    )

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

    df = pd.DataFrame(
        [
            {
                "Title": thesis.title,
                "Organization": thesis.organization,
                "City": thesis.city,
                "Deadline": thesis.deadline,
            }
            for thesis in theses
        ]
    )

    dataframe(df)