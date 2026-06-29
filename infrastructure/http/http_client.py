# ./infrastructure/http/http_client.py

from requests import Session

from config.settings import settings


class HttpClient:
    """Simple HTTP client."""

    def __init__(self) -> None:
        self.session = Session()

        self.session.headers.update(
            {
                "User-Agent": settings.user_agent,
            }
        )

    def get(self, url: str) -> str:

        response = self.session.get(
            url,
            timeout=settings.request_timeout,
        )

        response.raise_for_status()

        return response.text