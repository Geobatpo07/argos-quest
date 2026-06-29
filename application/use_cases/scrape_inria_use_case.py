# ./app/use_cases/scrape_inria_use_case.py

from infrastructure.database.unit_of_work import DuckDBUnitOfWork
from infrastructure.scrapers.inria_scraper import InriaScraper


class ScrapeInriaUseCase:
    """Scrape all Inria PhD opportunities and persist them."""

    def __init__(
        self,
        scraper: InriaScraper | None = None,
    ) -> None:

        self.scraper = scraper or InriaScraper()

    def execute(self) -> int:

        theses = self.scraper.scrape()

        with DuckDBUnitOfWork() as uow:

            uow.theses.delete_all()

            uow.theses.save_all(theses)

            uow.commit()

        return len(theses)