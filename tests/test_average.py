import csv
import random
import tempfile

import pytest

from reports.average import AverageRating
from reports.base import Row


def make_random_csv(num_rows: int, num_brands: int = 10) -> str:
    """

    :param num_rows:
    :param num_brands:
    :return:
    """
    temporary_file = tempfile.NamedTemporaryFile(
        delete=False, suffix=".csv", mode="w", newline="", encoding="utf-8"
    )
    writer = csv.writer(temporary_file)
    writer.writerow(["name", "brand", "price", "rating"])
    brands = [f"brand_{brand}" for brand in range(num_brands)]

    for row in range(num_rows):
        name = f"product_{row}"
        brand = random.choice(brands)
        price = round(random.uniform(10, 1000), 2)
        rating = round(random.uniform(0, 5), 2)
        writer.writerow([name, brand, price, rating])

    temporary_file.close()
    return temporary_file.name


def load_random_csv(file_path: str) -> list[Row]:
    rows = []

    with open(file_path, newline="", encoding="utf-8 ") as file:
        reader = csv.DictReader(file)
        for row in reader:
            rows.append(
                Row(
                    name=row["name"],
                    brand=row["brand"],
                    price=float(row["price"]),
                    rating=float(row["rating"]),
                )
            )
    return rows


@pytest.mark.parametrize(
    "rows_count, brands_count",
    [
        (10, 3),
        (100, 10),
        (1000, 50),
    ],
)
def test_average_rating_automatic(rows_count, brands_count):
    """Проверяет корректность и скорость на большом объёме данных"""
    csv_path = make_random_csv(rows_count, brands_count)
    data = load_random_csv(csv_path)
    report = AverageRating().generate(data)

    brands_in_data = set(row.brand for row in data)
    brands_in_report = set(row.brand for row in report)
    assert brands_in_data == brands_in_report

    ratings = [row.average_rating for row in report]
    assert ratings == sorted(ratings, reverse=True)

    assert all(5 >= row.average_rating >= 0 for row in report)


def test_average_rating_manual():
    """Проверяет точное усреднение на контролируемых данных"""
    data = [
        Row("iPhone", "apple", 999, 4.3),
        Row("Macbook", "apple", 1999, 5.0),
        Row("S23", "samsung", 899, 4.8),
        Row("S22", "samsung", 799, 4.1),
    ]

    result = AverageRating().generate(data)
    assert len(result) == 2

    apple = next(row for row in result if row.brand == "apple")
    samsung = next(row for row in result if row.brand == "samsung")

    assert apple.average_rating == round((5.0 + 4.3) / 2, 2)
    assert samsung.average_rating == round((4.8 + 4.1) / 2, 2)

    print(f"result: {result}")
