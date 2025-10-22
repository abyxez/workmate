from collections import defaultdict
from dataclasses import fields
from statistics import mean

from tabulate import tabulate

from .base import BaseReport, BrandAverageRatingReport, Row


class AverageRating(BaseReport):
    def generate(self, data: list[Row]) -> list[BrandAverageRatingReport]:
        """
        Вычисляет средний рейтинг по брендам и возвращает отсортированный список.
        :param data: список Row с данными CSV
        :return: список Report, отсортированных по average_rating по убыванию
        """
        ratings = defaultdict(list)
        for row in data:
            ratings[row.brand].append(row.rating)

        result = [
            BrandAverageRatingReport(brand=brand, average_rating=round(mean(values), 2))
            for brand, values in ratings.items()
        ]
        return sorted(result, key=lambda x: x.average_rating, reverse=True)

    def display(self, reports: list[BrandAverageRatingReport]) -> None:
        """
        Отображает результат работы generate() в формате
        github с использованием атрибутов dataclass.
        """
        if not reports:
            print("No data to display")
            return

        # generate() всегда возвращает определенный list[dataclass], игнорируем статические проверки
        headers = [
            field.name.capitalize().replace("_", " ")
            for field in fields(BrandAverageRatingReport) # type: ignore
        ]

        table = [
            [
                getattr(report, field.name)
                for field in fields(BrandAverageRatingReport)  # type: ignore
            ]
            for report in reports
        ]
        print(tabulate(table, headers=headers, tablefmt="github"))
