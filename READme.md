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