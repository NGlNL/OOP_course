## Проект состоит из двух классов:
### Product:
- название (name)
- описание (description)
- количество в наличии (quantity)
### Category:
- название (name)
- описание (description)
- список товаров категории (products)
Для этих двух классов, добавлена инициализацию так, чтобы каждый параметр был передан при создании объекта и сохранен.

Также у Category
есть два атрибута класса. Доступ к этим атрибутам есть у каждого объекта класса
и в них хранится общая информация для всех объектов. 
Эти атрибуты хранят в себе количество категорий и количество товаров.
Для классов сделали список товаров приватным атрибутом, чтобы к нему нельзя было получить доступ извне.
Атрибуты класса заполняются автоматически при инициализации нового объекта.
Защитили данные, которые не должны быть изменены через публичный доступ, чтобы не нарушилась целостность данных.

## Установка

1. Клонируйте репозиторий:
    ```bash
    git clone https://github.com/your-repo/project-name.git
    ```

2. Перейдите в директорию проекта:
    ```bash
    cd project-name
    ```

3. Установите необходимые зависимости:
    ```bash
    # для первичной установки
     poetry install
    # для обновления
    poetry update
    ```
## Запуск программы
Основная логика проекта заложена в модуле "main.py" которая связывает функциональности между собой.
для того чтобы запустить программу либо запустите файл main.py из директории проекта, либо через консоль
```bash
poetry run python main.py
```
# Тестирование
Для тестирования используйте библиотеку pytest. В проекте включены тесты для всех основных функций.

# Запуск тестов
Убедитесь, что у вас установлен pytest

Запустите тесты из корневой директории проекта:
```bash
pytest
```
### Проект покрыт тестами с использованием pytest. Для запуска тестов выполните команду:

```bash
pytest --cov
```
