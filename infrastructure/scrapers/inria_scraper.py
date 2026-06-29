# ./infrastructure/scrapers/inria_scraper.py

from datetime import datetime
from urllib.parse import urljoin

from selectolax.parser import HTMLParser

from domain.entities.thesis import Thesis
from domain.enums.source import Source
from infrastructure.http.http_client import HttpClient
from infrastructure.scrapers.base_scraper import BaseScraper


class InriaScraper(BaseScraper):
    """Scraper for Inria PhD opportunities."""

    BASE_URL = "https://jobs.inria.fr"

    URL = (
        "https://jobs.inria.fr/public/classic/fr/offres"
        "?filtre=doctorants"
    )

    def __init__(self) -> None:
        self.client = HttpClient()

    def _fetch_document(self) -> HTMLParser:
        html = self.client.get(self.URL)
        return HTMLParser(html)

    @staticmethod
    def _extract_cards(document: HTMLParser):
        return document.css("li.resultats")

    @staticmethod
    def _extract_metadata(card):

        metadata = {
            "reference": None,
            "city": None,
            "team": None,
            "deadline": None,
        }

        for li in card.css("li"):

            text = li.text(separator=" ", strip=True)

            if "Job reference" in text:
                metadata["reference"] = (
                    text.replace("Job reference", "")
                    .replace(":", "")
                    .strip()
                )

            elif "Town/city" in text:
                metadata["city"] = (
                    text.replace("Town/city", "")
                    .replace(":", "")
                    .strip()
                )

            elif "Inria Team" in text:
                metadata["team"] = (
                    text.replace("Inria Team", "")
                    .replace(":", "")
                    .strip()
                )

        time_node = card.css_first("time")

        if (
            time_node is not None
            and "datetime" in time_node.attributes
        ):
            metadata["deadline"] = datetime.strptime(
                time_node.attributes["datetime"],
                "%Y-%m-%d",
            ).date()

        return metadata

    @classmethod
    def _parse_card(cls, card) -> Thesis:

        title_node = card.css_first("h2 a")

        if title_node is None:
            raise ValueError("Unable to parse Inria card.")

        title = title_node.text(strip=True)

        href = title_node.attributes.get("href", "")

        url = urljoin(
            cls.BASE_URL,
            href,
        )

        metadata = cls._extract_metadata(card)

        description = card.text(
            separator="\n",
            strip=True,
        )

        return Thesis(
            title=title,
            source=Source.INRIA,
            organization="Inria",
            laboratory="Inria",
            city=metadata["city"],
            country="France",
            team=metadata["team"],
            reference=metadata["reference"],
            deadline=metadata["deadline"],
            description=description,
            url=url,
        )

    @classmethod
    def _build_theses(cls, cards) -> list[Thesis]:

        theses = []

        for card in cards:

            try:
                theses.append(cls._parse_card(card))
            except Exception:
                continue

        return theses

    def scrape(self) -> list[Thesis]:

        document = self._fetch_document()

        cards = self._extract_cards(document)

        return self._build_theses(cards)