# ./tests/test_scrape_inria_use_case.py

from application.use_cases.scrape_inria_use_case import (
    ScrapeInriaUseCase,
)
from infrastructure.database.initializer import (
    DatabaseInitializer,
)
from infrastructure.database.unit_of_work import (
    DuckDBUnitOfWork,
)


def test_scrape_inria_use_case():

    DatabaseInitializer.initialize()

    use_case = ScrapeInriaUseCase()

    imported = use_case.execute()

    assert imported > 0

    with DuckDBUnitOfWork() as uow:

        assert uow.theses.count() == imported

        theses = uow.theses.get_all()

        assert len(theses) == imported

        assert theses[0].title

        assert theses[0].url