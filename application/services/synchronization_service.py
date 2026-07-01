# ./app/services/synchronization_service.py
from application.services.dataframe_service import DataFrameService
from infrastructure.database.unit_of_work import DuckDBUnitOfWork

from application.services.scraper_registry import (
    ScraperRegistry,
)


class SynchronizationService:
    """Synchronize all configured sources."""

    def synchronize(self) -> int:

        theses = []

        for scraper in ScraperRegistry.get_all():

            theses.extend(
                scraper.scrape()
            )

        with DuckDBUnitOfWork() as uow:

            uow.theses.delete_all()

            uow.theses.save_all(theses)

            uow.commit()

            DataFrameService.clear_cache()

        return len(theses)