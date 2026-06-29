# ./infrastructure/database/migration_runner.py

from datetime import UTC, datetime
from pathlib import Path

from infrastructure.database.connection import DuckDBConnection


class MigrationRunner:
    """Runs SQL migrations."""

    MIGRATIONS_DIR = (
        Path(__file__).parent / "migrations"
    )

    def __init__(self) -> None:

        self.connection = DuckDBConnection()

    # ---------------------------------------------------------
    # Public API
    # ---------------------------------------------------------

    def run(self) -> None:

        self._initialize_schema_version()

        available = self._available_migrations()

        applied = self._applied_versions()

        pending = [
            migration
            for migration in available
            if migration.stem not in applied
        ]

        if not pending:
            return

        self.connection.begin()

        try:

            for migration in pending:

                self._apply(migration)

            self.connection.commit()

        except Exception:

            self.connection.rollback()

            raise

        finally:

            self.connection.close()

    # ---------------------------------------------------------
    # Initialization
    # ---------------------------------------------------------

    def _initialize_schema_version(self) -> None:

        self.connection.execute(
            """
            CREATE TABLE IF NOT EXISTS schema_version
            (
                version VARCHAR PRIMARY KEY,
                applied_at TIMESTAMP NOT NULL
            )
            """
        )

    # ---------------------------------------------------------
    # Discovery
    # ---------------------------------------------------------

    def _available_migrations(self) -> list[Path]:

        return sorted(
            self.MIGRATIONS_DIR.glob("*.sql")
        )

    def _applied_versions(self) -> set[str]:

        rows = self.connection.execute(
            """
            SELECT version
            FROM schema_version
            """
        ).fetchall()

        return {row[0] for row in rows}

    # ---------------------------------------------------------
    # Apply
    # ---------------------------------------------------------

    def _apply(self, migration: Path) -> None:

        sql = migration.read_text(
            encoding="utf-8"
        )

        self.connection.execute(sql)

        self.connection.execute(
            """
            INSERT INTO schema_version
            (
                version,
                applied_at
            )
            VALUES (?, ?)
            """,
            (
                migration.stem,
                datetime.now(UTC),
            ),
        )