# ./tests/test_inria_scraper.py

from domain.enums.source import Source

from infrastructure.scrapers.inria_scraper import (
    InriaScraper,
)


def test_scrape_inria():

    scraper = InriaScraper()

    theses = scraper.scrape()

    assert len(theses) > 0

    for thesis in theses:

        assert thesis.title

        assert thesis.url

        assert thesis.organization == "Inria"

        assert thesis.laboratory == "Inria"

        assert thesis.source == Source.INRIA

        assert thesis.description