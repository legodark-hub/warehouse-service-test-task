# Сервис для управления складом

Этот проект представляет собой сервис для управления складом, разработанный на Python с использованием FastAPI. Он предоставляет RESTful API для управления складами и отслеживания перемещений товаров. Сервис также включает в себя Kafka consumer для асинхронной обработки событий перемещения.

## Ключевые технологии

- **Бэкенд:** Python, FastAPI
- **База данных:** SQLAlchemy с Alembic для миграций
- **Обмен сообщениями:** FastStream с Kafka
- **Валидация данных:** Pydantic

## Структура проекта

```
├── alembic/           # Скрипты миграций Alembic
├── src/
│   ├── api/           # Эндпоинты REST API (роутеры и сервисы)
│   ├── consumers/     # Потребители сообщений Kafka
│   ├── database/      # Настройка SQLAlchemy и управление сессиями
│   ├── models/        # Модели SQLAlchemy ORM
│   ├── repositories/  # Паттерн "Репозиторий" для доступа к данным
│   ├── schemas/       # Схемы Pydantic для запросов/ответов API
│   └── utils/         # Вспомогательные модули (Unit of Work и т.д.)
├── tests/             # Тесты для приложения
├── alembic.ini        # Конфигурация Alembic
├── requirements.txt   # Зависимости Python
└── README.md
```

## Установка и настройка

1. **Клонируйте репозиторий:**

    ```bash
    git clone https://github.com/legodark-hub/warehouse-service-test-task.git
    cd warehouse-service-test-task
    ```

2. **Создайте и активируйте виртуальное окружение:**

    ```bash
    python -m venv .venv
    source .venv/bin/activate  
    # Для Windows: .venv\Scripts\activate
    ```

3. **Установите зависимости:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Настройте переменные окружения:**
    Создайте файл `.env` и укажите необходимые значения.

    Пример `.env` файла:
    ```
    MODE=DEV
    DB_NAME=your_db_name
    DB_HOST=localhost
    DB_PORT=5432
    DB_USER=your_db_user
    DB_PASS=your_db_password
    ```

## Миграции базы данных

Проект использует Alembic для управления миграциями схемы базы данных.

- Чтобы создать новую миграцию:

    ```bash
    alembic revision --autogenerate -m "Ваше сообщение о миграции"
    ```

- Чтобы применить миграции:

    ```bash
    alembic upgrade head
    ```

## Запуск приложения

Для запуска сервера разработки FastAPI выполните команду:

```bash
uvicorn src.main:app --reload
```

Документация API будет доступна по адресу `http://127.0.0.1:8000/docs`.

## Эндпоинты API

Приложение предоставляет следующие основные роутеры API:

- `/warehouse`: Эндпоинты для управления складами (создание, чтение, обновление, удаление).
- `/movement`: Эндпоинты для отслеживания перемещений товаров.

## Потребитель Kafka

Сервис включает в себя consumer Kafka, управляемого FastStream, для обработки событий, связанных с перемещением товаров, таких как поступления и отправки. Логика потребителя находится в каталоге `src/consumers/`.
