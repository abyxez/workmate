from collections import defaultdict
from statistics import mean

from .base import BaseReport, Report, Row


class AverageRating(BaseReport):
    def generate(self, data: list[Row]) -> list[Report]:
        """
        Вычисляет средний рейтинг по брендам и возвращает отсортированный список.
        :param data: список Row с данными CSV
        :return: список Report, отсортированных по average_rating по убыванию
        """
        ratings = defaultdict(list)
        for row in data:
            ratings[row.brand].append(row.rating)

        result = [
            Report(brand=brand, average_rating=round(mean(values), 2))
            for brand, values in ratings.items()
        ]
        return sorted(result, key=lambda x: x.average_rating, reverse=True)
