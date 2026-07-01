# ./application/use_cases/get_all_theses_use_case.py

from infrastructure.database.unit_of_work import (
    DuckDBUnitOfWork,
)


class GetAllThesesUseCase:

    def execute(self):

        with DuckDBUnitOfWork() as uow:

            return uow.theses.get_all()