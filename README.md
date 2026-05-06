<div align="center">
    
# Тестирование приложения DemoQA

<strong>Python • Selenium</strong>

[![Python](https://img.shields.io/badge/Python-3.14-blue?logo=python)](https://www.python.org/)
[![Pytest](https://img.shields.io/badge/Pytest-9.0-orange?logo=pytest)](https://docs.pytest.org/)
[![Selenium](https://img.shields.io/badge/Selenium-4.43-brightgreen?logo=selenium)](https://www.selenium.dev/)
[![Allure](https://img.shields.io/badge/Allure-2.15-purple?logo=allure)](https://allurereport.org/)
</div>

------------------------------------------------------------------------

## 📌 О проекте
Автоматизация тестирования веб-приложения [**DemoQA**](https://demoqa.com/).  

📋 Чек-лист тестирования:\
👉 https://github.com/iivanitskiy/demoqa-tests/blob/main/check-list.md

------------------------------------------------------------------------

### Ключевые возможности:

✅ **UI тесты** – Selenium.  
✅ **API тесты** – Requests для проверки эндпоинтов.  
✅ **Автоматическая генерация отчетов** – Allure с шагами, скриншотами и вложениями.  
✅ **Конфигурирование** – гибкая настройка через `configuration/`.  
✅ **Тестовые данные** – вынесены в отдельную директорию (`test_data/`).

------------------------------------------------------------------------

## 🛠️ Технологический стек

| Инструмент | Назначение |
|----------|------------|
| **Python** | Написание тестов |
| **Pytest** | Фреймворк для запуска тестов |
| **Selenium** | Управление браузером для UI-тестов |
| **Requests** | Выполнение HTTP-запросов для API-тестов |
| **Allure** | Генерация детальных отчетов |
| **Page Object Model** | Паттерн для структурирования UI-локаторов и логики |

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
