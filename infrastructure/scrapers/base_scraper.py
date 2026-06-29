# ./infrastructure/scrapers/base_scraper.py

from abc import ABC, abstractmethod

from domain.entities.thesis import Thesis


class BaseScraper(ABC):

    @abstractmethod
    def scrape(self) -> list[Thesis]:
        """Scrape theses."""