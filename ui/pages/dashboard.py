# ./ui/pages/dashboard.py

import streamlit as st

from application.services.statistics_service import (
    StatisticsService,
)

from application.services.synchronization_service import (
    SynchronizationService,
)

from ui.components.buttons import sync_button
from ui.components.metrics import metric


def show_dashboard():

    st.title("⛵ Argos Quest")

    st.divider()

    if sync_button():

        with st.spinner(
            "Synchronisation..."
        ):

            imported = (
                SynchronizationService()
                .synchronize()
            )

        st.success(
            f"{imported} offres importées."
        )

    count = (
        StatisticsService()
        .thesis_count()
    )

    metric(
        "Nombre de thèses",
        count,
    )