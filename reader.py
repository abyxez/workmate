import csv

from reports.base import Row


def read_csv_files(paths: list[str]) -> list[Row]:
    """
    Считывает CSV файлы и возвращает список Row.

    :param paths: список путей к CSV файлам
    :return: список Row
    """
    final = []

    for path in paths:
        with open(path, newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                final.append(Row(**row))
    return final
