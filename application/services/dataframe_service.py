# ./application/services/dataframe_service.py

from __future__ import annotations

import pandas as pd
import streamlit as st

from infrastructure.database.unit_of_work import (
    DuckDBUnitOfWork,
)


class DataFrameService:
    """
    Loads and caches the application dataframe.
    """

    @staticmethod
    @st.cache_data(
        ttl=300,
        show_spinner=False,
    )
    def load() -> pd.DataFrame:
        """
        Load all theses from DuckDB.
        """

        with DuckDBUnitOfWork() as uow:

            theses = uow.theses.get_all()

        return pd.DataFrame(
            [
                {
                    "id": str(thesis.id),
                    "title": thesis.title,
                    "reference": thesis.reference,
                    "source": str(thesis.source),
                    "organization": thesis.organization,
                    "laboratory": thesis.laboratory,
                    "team": thesis.team,
                    "city": thesis.city,
                    "country": thesis.country,
                    "domain": thesis.domain,
                    "funding": thesis.funding,
                    "deadline": thesis.deadline,
                    "summary": thesis.summary,
                    "description": thesis.description,
                    "url": thesis.url,
                    "score": thesis.score,
                    "is_active": thesis.is_active,
                    "scraped_at": thesis.scraped_at,
                    "created_at": thesis.created_at,
                }
                for thesis in theses
            ]
        )

    @staticmethod
    def clear_cache() -> None:
        """
        Invalidate the Streamlit cache.
        """

        DataFrameService.load.clear()