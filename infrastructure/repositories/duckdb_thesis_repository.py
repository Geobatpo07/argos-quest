# ./infrastructure/repositories/duckdb_thesis_repository.py

from domain.entities.thesis import Thesis
from domain.enums.source import Source
from domain.repositories.thesis_repository import ThesisRepository


class DuckDBThesisRepository(ThesisRepository):
    """DuckDB implementation of the ThesisRepository."""

    INSERT_SQL = """
                 INSERT INTO thesis
                 (
                     id,
                     title,
                     reference,
                     source,
                     organization,
                     laboratory,
                     team,
                     city,
                     country,
                     domain,
                     funding,
                     deadline,
                     summary,
                     description,
                     url,
                     score,
                     is_active,
                     scraped_at,
                     created_at
                 )
                 VALUES
                     (
                         ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
                     ) \
                 """

    def __init__(self, connection):
        self.connection = connection

    def _to_row(self, thesis: Thesis) -> tuple:
        return (
            str(thesis.id),
            thesis.title,
            thesis.reference,
            thesis.source.value if isinstance(thesis.source, Source) else thesis.source,
            thesis.organization,
            thesis.laboratory,
            thesis.team,
            thesis.city,
            thesis.country,
            thesis.domain,
            thesis.funding,
            thesis.deadline,
            thesis.summary,
            thesis.description,
            str(thesis.url),
            thesis.score,
            thesis.is_active,
            thesis.scraped_at,
            thesis.created_at,
        )

    def save(self, thesis: Thesis) -> None:

        self.connection.execute(
            self.INSERT_SQL,
            self._to_row(thesis),
        )

    def save_all(self, theses: list[Thesis]) -> None:

        self.connection.executemany(
            self.INSERT_SQL,
            [self._to_row(thesis) for thesis in theses],
        )

    def get_all(self) -> list[Thesis]:

        rows = self.connection.execute(
            """
            SELECT
                id,
                title,
                reference,
                source,
                organization,
                laboratory,
                team,
                city,
                country,
                domain,
                funding,
                deadline,
                summary,
                description,
                url,
                score,
                is_active,
                scraped_at,
                created_at
            FROM thesis
            ORDER BY scraped_at DESC
            """
        ).fetchall()

        theses = []

        for row in rows:

            theses.append(
                Thesis.model_validate(
                    {
                        "id": row[0],
                        "title": row[1],
                        "reference": row[2],
                        "source": Source(row[3]),
                        "organization": row[4],
                        "laboratory": row[5],
                        "team": row[6],
                        "city": row[7],
                        "country": row[8],
                        "domain": row[9],
                        "funding": row[10],
                        "deadline": row[11],
                        "summary": row[12],
                        "description": row[13],
                        "url": row[14],
                        "score": row[15],
                        "is_active": row[16],
                        "scraped_at": row[17],
                        "created_at": row[18],
                    }
                )
            )

        return theses

    def delete_all(self) -> None:

        self.connection.execute(
            """
            DELETE FROM thesis
            """
        )

    def count(self) -> int:

        return self.connection.execute(
            """
            SELECT COUNT(*)
            FROM thesis
            """
        ).fetchone()[0]