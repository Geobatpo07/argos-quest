# ./domain/entities/thesis.py

from datetime import UTC, date, datetime
from uuid import UUID, uuid4

from pydantic import BaseModel, Field, HttpUrl
from domain.enums.source import Source


class Thesis(BaseModel):
    """Represents a PhD opportunity."""

    id: UUID = Field(default_factory=uuid4)

    # Core information
    title: str
    reference: str | None = None

    # Organization
    source: Source = Source.INRIA
    organization: str
    laboratory: str
    team: str | None = None

    # Location
    city: str | None = None
    country: str | None = None

    # Scientific information
    domain: str | None = None
    funding: str | None = None
    deadline: date | None = None

    # Content
    summary: str | None = None
    description: str | None = None

    # Link
    url: HttpUrl

    # Analytics
    score: float = 0.0
    is_active: bool = True

    # Metadata
    scraped_at: datetime = Field(
        default_factory=lambda: datetime.now(UTC)
    )

    created_at: datetime = Field(
        default_factory=lambda: datetime.now(UTC)
    )