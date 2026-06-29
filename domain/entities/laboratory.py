# ./domain/entities/laboratory.py

from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class Laboratory(BaseModel):
    id: UUID = Field(default_factory=uuid4)

    name: str

    city: str | None = None

    country: str | None = None

    website: str | None = None