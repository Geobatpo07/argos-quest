# ./tests/test_database.py

# ./tests/test_database.py

from domain.entities.thesis import Thesis
from domain.enums.source import Source

from infrastructure.database.connection import DuckDBConnection
from infrastructure.database.initializer import DatabaseInitializer
from infrastructure.database.migration_runner import MigrationRunner
from infrastructure.database.unit_of_work import DuckDBUnitOfWork


EXPECTED_COLUMNS = {
    "id",
    "title",
    "reference",
    "source",
    "organization",
    "laboratory",
    "team",
    "city",
    "country",
    "domain",
    "funding",
    "deadline",
    "summary",
    "description",
    "url",
    "score",
    "is_active",
    "scraped_at",
    "created_at",
}


def test_database_infrastructure():

    # ------------------------------------------------------------------
    # Database initialization
    # ------------------------------------------------------------------

    DatabaseInitializer.initialize()

    connection = DuckDBConnection()

    # ------------------------------------------------------------------
    # Migration executed
    # ------------------------------------------------------------------

    versions = connection.execute(
        """
        SELECT version
        FROM schema_version
        """
    ).fetchall()

    assert len(versions) == len(
        MigrationRunner()._available_migrations()
    )

    # ------------------------------------------------------------------
    # Thesis table exists
    # ------------------------------------------------------------------

    tables = connection.execute(
        """
        SHOW TABLES
        """
    ).fetchall()

    tables = {table[0] for table in tables}

    assert "thesis" in tables

    # ------------------------------------------------------------------
    # Thesis schema
    # ------------------------------------------------------------------

    rows = connection.execute(
        """
        DESCRIBE thesis
        """
    ).fetchall()

    columns = {
        row[0]
        for row in rows
    }

    assert columns == EXPECTED_COLUMNS

    connection.close()

    # ------------------------------------------------------------------
    # Repository
    # ------------------------------------------------------------------

    with DuckDBUnitOfWork() as uow:

        uow.theses.delete_all()

        thesis = Thesis(
            title="Scientific Machine Learning",
            source=Source.INRIA,
            organization="Inria",
            laboratory="Inria",
            url="https://inria.fr",
        )

        uow.theses.save(thesis)

        uow.commit()

    # ------------------------------------------------------------------
    # Read
    # ------------------------------------------------------------------

    with DuckDBUnitOfWork() as uow:

        theses = uow.theses.get_all()

    assert len(theses) == 1

    assert theses[0].title == thesis.title

    assert theses[0].source == Source.INRIA

    assert theses[0].organization == "Inria"

    assert theses[0].laboratory == "Inria"

    assert theses[0].url == thesis.url