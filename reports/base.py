from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class Row:
    name: str
    brand: str
    price: float
    rating: float

    def __post_init__(self):
        self.price = float(self.price)
        self.rating = float(self.rating)

        if not (0 <= self.rating <= 5):
            raise ValueError(f"Incorrect rating: {self.rating}")

        if self.price < 0:
            raise ValueError(f"Price can not be negative: {self.price}")


@dataclass
class Report:
    brand: str
    average_rating: float


class BaseReport(ABC):
    @abstractmethod
    def generate(self, data: list) -> list:
        """
        Основной метод отчета: принимает данные и возвращает их в форме, пригодной для отображения или сохранения.

        Метод не реализован в базовом классе и должен быть переопределен в потомках.
        Конкретный тип входных и выходных данных определяется наследником.

        :param data: список входных данных
        :return: список элементов отчета, структура которых зависит от конкретного потомка
        """
        pass  # pragma: no cover
