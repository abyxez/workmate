from reports.factory import REPORTS

ALLOWED_ARGUMENTSS = {
    "--files",
    "--report",
}


def validate_args(arguments: list[str]) -> list[str]:
    """
    Проверяет список аргументов и оставляет только разрешённые.
    Фильтрует неразрешённые ключи и игнорирует не-CSV файлы после --files.
    Проверяет на наличие обязательных аргументов для запуска скрипта.
    По ТЗ считаем, что содержимое файлов валидно и
    что хотя бы один .csv файл будет передан.

    :param arguments: sys.argv[1:]
    :return: отфильтрованный список аргументов
    """
    filtered = []
    count = 0

    while count < len(arguments):
        argument = arguments[count]

        if argument not in ALLOWED_ARGUMENTSS:
            print(f"Ignoring unknown argument type: {argument}")
            count += 1
            continue

        filtered.append(argument)
        count += 1

        if argument == "--files":
            while count < len(arguments) and not arguments[count].startswith("--"):
                name_of_file = arguments[count]

                if name_of_file.lower().endswith(".csv"):
                    filtered.append(name_of_file)
                else:
                    print(f"Ignoring non-CSV file: {name_of_file}")
                count += 1

        elif argument == "--report":
            if count >= len(arguments):
                raise ValueError(f"Expected a report type after --report")

            while count < len(arguments) and not arguments[count].startswith("--"):
                report_value = arguments[count]

                if report_value in REPORTS:
                    filtered.append(report_value)
                else:
                    print(
                        f"Ignoring unknown report type: {report_value}, expected one of {REPORTS}"
                    )
                count += 1

    if any(arg not in filtered for arg in ALLOWED_ARGUMENTSS):
        raise ValueError(f"Missing required argument(s): --files and/or --report")

    return filtered
