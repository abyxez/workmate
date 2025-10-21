from .average import AverageRating


REPORTS = [
    "average-rating",
]


def get_average_rating(name: str):
    """
    Возвращает объект отчета по имени.

    :param name: Тип отчета ("average-rating", ...)
    :return: Экземпляр класса отчета
    :raises ValueError: если имя неизвестно
    """
    if name in REPORTS:
        if name == "average-rating":
            return AverageRating()
        elif (
            name == "average-price"
        ):  # Архитектура позволяет быстро добавлять новые отчёты
            ...
    raise ValueError(f"Unknown report type: {name}")
