# ./application/services/statistics_service.py

from __future__ import annotations

import pandas as pd

from application.services.dataframe_service import (
    DataFrameService,
)


class StatisticsService:
    """
    Computes application statistics.
    """

    def __init__(self):

        self._df: pd.DataFrame = DataFrameService.load()

    @property
    def dataframe(self) -> pd.DataFrame:

        return self._df.copy()

    def thesis_count(self) -> int:

        return len(self._df)

    def source_count(self) -> int:

        if self._df.empty:
            return 0

        return self._df["source"].dropna().nunique()

    def organization_count(self) -> int:

        if self._df.empty:
            return 0

        return self._df["organization"].dropna().nunique()

    def laboratory_count(self) -> int:

        if self._df.empty:
            return 0

        return self._df["laboratory"].dropna().nunique()

    def city_count(self) -> int:

        if self._df.empty:
            return 0

        return self._df["city"].dropna().nunique()

    def nearest_deadline(self) -> str:

        if self._df.empty:
            return "-"

        deadlines = self._df["deadline"].dropna()

        if deadlines.empty:
            return "-"

        return deadlines.min().strftime("%d/%m/%Y")

    def dashboard(self) -> dict[str, int | str]:

        return {
            "Theses": self.thesis_count(),
            "Sources": self.source_count(),
            "Organizations": self.organization_count(),
            "Cities": self.city_count(),
            "Next deadline": self.nearest_deadline(),
        }