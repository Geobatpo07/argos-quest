# ./application/bootstrap.py

from infrastructure.database.initializer import DatabaseInitializer


def bootstrap() -> None:
    """
    Initialize the application.
    """

    DatabaseInitializer.initialize()