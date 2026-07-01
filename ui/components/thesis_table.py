# ./ui/components/thesis_table.py

import pandas as pd
import streamlit as st

from domain.entities.thesis import Thesis


def thesis_table(theses: list[Thesis]):

    dataframe = pd.DataFrame(
        [
            {
                "Titre": thesis.title,
                "Organisation": thesis.organization,
                "Ville": thesis.city,
                "Échéance": thesis.deadline,
            }
            for thesis in theses
        ]
    )

    st.dataframe(
        dataframe,
        use_container_width=True,
        hide_index=True,
    )