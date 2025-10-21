# CSV Reader Reports

Простой Python-проект для генерации отчетов из CSV файлов.  

## Установка зависимостей

Проект использует [Poetry](https://python-poetry.org/) для управления зависимостями.

### Клонируем репозиторий
```bash
git clone https://github.com/yourusername/workmate.git
cd workmate
```

### Устанавливаем зависимости через Poetry
```bash
poetry install
```

### Пример запуска скрипта
```bash
poetry run python main.py --files file1.csv file2.csv --report average-rating
```

### Проверить покрытие с помощью pytest
```bash
poetry run pytest --cov=reports
```

Примечание для ревьюера:

Тесты не покрывают main.py ( сборка приложения ), cli_validator.py ( рассмотрены краевые случаи, а файлы всегда валидны ) и reader.py ( нет смысла проверять работу Python ). Посчитал, что для тестов reports/ на 100% будет достаточно.
