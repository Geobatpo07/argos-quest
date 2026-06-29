# ./application/services/statistics_service.py

from infrastructure.database.unit_of_work import (
    DuckDBUnitOfWork,
)


class StatisticsService:
    """Database statistics."""

    def thesis_count(self) -> int:

        with DuckDBUnitOfWork() as uow:

            return uow.theses.count()