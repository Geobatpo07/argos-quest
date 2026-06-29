# ./domain/entities/application.py

from datetime import datetime
from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class Application(BaseModel):
    id: UUID = Field(default_factory=uuid4)

    thesis_id: UUID

    status: str = "Draft"

    sent_at: datetime | None = None

    interview_date: datetime | None = None

    notes: str | None = None