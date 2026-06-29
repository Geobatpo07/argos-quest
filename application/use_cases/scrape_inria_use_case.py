# ./app/use_cases/scrape_inria_use_case.py

from application.services.synchronization_service import (
    SynchronizationService,
)


class ScrapeInriaUseCase:

    def execute(self):

        return (
            SynchronizationService()
            .synchronize()
        )