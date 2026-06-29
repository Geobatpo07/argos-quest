# ./infrastructure/database/initializer.py

from infrastructure.database.migration_runner import (
    MigrationRunner,
)


class DatabaseInitializer:

    @staticmethod
    def initialize():

        MigrationRunner().run()