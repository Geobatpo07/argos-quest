# ./infrastructure/database/connection.py

from pathlib import Path
from typing import Any

import duckdb

from config.settings import settings


class DuckDBConnection:
    """Wrapper around a DuckDB connection."""

    def __init__(self) -> None:

        database_path = Path(settings.database_path)
        database_path.parent.mkdir(parents=True, exist_ok=True)

        self._connection = duckdb.connect(str(database_path))

    # ---------------------------------------------------------
    # Query API
    # ---------------------------------------------------------

    def execute(self, query: str, params: tuple | list | None = None):

        if params is None:
            return self._connection.execute(query)

        return self._connection.execute(query, params)

    def executemany(
        self,
        query: str,
        params: list[tuple],
    ) -> None:

        self._connection.executemany(query, params)

    def fetchone(self):

        return self._connection.fetchone()

    def fetchall(self):

        return self._connection.fetchall()

    # ---------------------------------------------------------
    # Transactions
    # ---------------------------------------------------------

    def begin(self) -> None:

        self._connection.execute("BEGIN TRANSACTION")

    def commit(self) -> None:

        self._connection.commit()

    def rollback(self) -> None:

        try:
            self._connection.rollback()
        except duckdb.TransactionException:
            # aucune transaction active
            pass

    # ---------------------------------------------------------
    # Connection
    # ---------------------------------------------------------

    def close(self) -> None:

        self._connection.close()