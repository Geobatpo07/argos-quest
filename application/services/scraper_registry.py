# ./app/services/scraper_registry.py

from infrastructure.scrapers.inria_scraper import InriaScraper


class ScraperRegistry:
    """Registry of all available scrapers."""

    @staticmethod
    def get_all():

        return [
            InriaScraper(),
        ]