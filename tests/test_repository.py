# ./tests/test_repository.py

from infrastructure.database.initializer import DatabaseInitializer
from infrastructure.database.unit_of_work import DuckDBUnitOfWork
from infrastructure.scrapers.inria_scraper import InriaScraper


def test_save_scraped_theses():

    DatabaseInitializer.initialize()

    scraper = InriaScraper()

    theses = scraper.scrape()

    assert len(theses) > 0

    with DuckDBUnitOfWork() as uow:

        uow.theses.delete_all()

        for thesis in theses:

            uow.theses.save(thesis)

    with DuckDBUnitOfWork() as uow:

        stored = uow.theses.get_all()

        assert len(stored) == len(theses)

        assert uow.theses.count() == len(theses)