import argparse
import sys

from tabulate import tabulate

from cli_validator import validate_args
from reader import read_csv_files
from reports.factory import get_average_rating


def parse_arguments(argv=None):
    """
    Разбирает аргументы командной строки и делегирует низкоуровневую фильтрацию
    модулю validate_args.

    После предварительной фильтрации остаются только разрешённые ключи:
      - --files с одним или несколькими CSV-файлами
      - --report с одним значением из reports.factory.REPORTS/choices

    Все остальные аргументы (неизвестные ключи, не-CSV файлы, неизвестные значения
    после --report) игнорируются с выводом предупреждений.

    :param argv: список аргументов (по умолчанию sys.argv[1:])
    :return: argparse.Namespace с полями:
        - .files: список CSV-файлов
        - .report: выбранный тип отчета
    :raises ValueError: если после --report не передано корректное значение или
                        если отсутствует хотя бы один из обязательных аргументов
                        (--files и --report)

    Пример запуска:

        poetry run python main.py \
            --files products1.csv products2.csv virus.exe --wrong-parameter \
            --report average-rating something --useless.csv another-virus.exe

    После работы validate_args и parse_arguments останется:

        Namespace(
            files=['products1.csv', 'products2.csv'],
            report='average-rating'
        )
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--files",
        nargs="+",
        required=True,
        help="Paths to CSV files",
    )
    parser.add_argument(
        "--report",
        required=True,
        choices=[
            "average-rating",
        ],
        help="Report type",
    )
    return parser.parse_args(argv)


def main():
    raw_arguments = sys.argv[1:]
    validated_arguments = validate_args(raw_arguments)
    parsed_arguments = parse_arguments(validated_arguments)

    csv_data = read_csv_files(parsed_arguments.files)
    csv_report = get_average_rating(parsed_arguments.report)
    table = csv_report.generate(csv_data)

    print(tabulate(table, headers=["Brand", "Average Rating"], tablefmt="github"))


if __name__ == "__main__":
    main()
