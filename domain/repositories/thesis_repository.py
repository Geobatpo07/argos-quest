# ./domain/repositories/thesis_repository.py

from abc import ABC, abstractmethod

from domain.entities.thesis import Thesis


class ThesisRepository(ABC):

    @abstractmethod
    def save(self, thesis: Thesis) -> None:
        ...

    @abstractmethod
    def get_all(self) -> list[Thesis]:
        ...

    @abstractmethod
    def delete_all(self) -> None:
        ...

    @abstractmethod
    def save_all(self, theses: list[Thesis]) -> None:
        ...