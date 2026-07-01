# ./ui/pages/sources.py

import pandas as pd

from application.services.scraper_registry import (
    ScraperRegistry,
)

from ui.components.layout import page
from ui.components.tables import dataframe


def show_sources():

    page(
        title="Sources",
        icon="🏛️",
        description="Configured scraping sources.",
    )

    rows = []

    for scraper in ScraperRegistry.get_all():

        rows.append(
            {
                "Source": scraper.__class__.__name__,
                "Status": "Available",
            }
        )

    dataframe(
        pd.DataFrame(rows)
    )