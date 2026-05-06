# Автоматизация тестирования DemoQA

📍 https://demoqa.com/

------------------------------------------------------------------------

## 📌 О проекте

Пет-проект по автоматизации тестирования веб-приложения **DemoQA**.\
Включает в себя:

-   UI тесты (Selenium)
-   API тесты (Requests)
-   Генерацию отчетов (Allure)

📋 Чек-лист тестирования:\
👉 https://github.com/iivanitskiy/demoqa-tests/blob/main/check-list.md

------------------------------------------------------------------------

## 🚀 Быстрый старт

### 1. Клонирование репозитория

``` bash
git clone https://github.com/iivanitskiy/demoqa-tests.git
cd demoqa-tests
```

### 2. Установка зависимостей

``` bash
pip install -r requirements.txt
```

### 3. Запуск тестов

#### UI тесты

``` bash
pytest tests/ui
```

#### API тесты

``` bash
pytest tests/api
```

#### Все тесты

``` bash
pytest tests
```

------------------------------------------------------------------------

## 📊 Отчеты

Для просмотра Allure-отчета выполните:

``` bash
allure serve allure_results
```

------------------------------------------------------------------------

## 📁 Структура проекта

    project/
    │
    ├── api/              # API клиенты (Page Object / service layer)
    ├── allure_results/   # результаты выполнения тестов
    ├── configuration/    # конфигурации и настройки
    ├── locators/         # локаторы элементов UI
    ├── page/             # Page Object модели
    ├── reports/          # отчеты
    ├── screenshots/      # скриншоты при падениях тестов
    ├── test_data/        # тестовые данные
    ├── tests/            # тесты (UI / API)
    └── utils/            # вспомогательные утилиты

------------------------------------------------------------------------

## 🛠️ Технологический стек

-   **Python**
-   **Pytest**
-   **Selenium**
-   **Requests**
-   **Allure Reports**