# ./infrastructure/database/unit_of_work.py

from infrastructure.database.connection import (
    DuckDBConnection,
)

from infrastructure.repositories.duckdb_thesis_repository import (
    DuckDBThesisRepository,
)


class DuckDBUnitOfWork:

    def __init__(self):

        self.connection = DuckDBConnection()

        self.theses = DuckDBThesisRepository(
            self.connection
        )

    def __enter__(self):

        return self

    def commit(self):

        self.connection.commit()

    def rollback(self):

        self.connection.rollback()

    def __exit__(
        self,
        exc_type,
        exc_val,
        exc_tb,
    ):

        if exc_type:

            self.rollback()

        else:

            self.commit()

        self.connection.close()