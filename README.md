# Автоматизации тестирования https://demoqa.com/ (В разработке...)


## 🚀 Как начать

### 1. Клонировать репозиторий:
```bash
git clone <your-repo-url>
cd <project-folder>
```

### 2. Установить зависимости:
```bash
pip install -r requirements.txt
```

### 3. Запуск тестов:

- UI тесты:
```bash
pytest tests/ui
```

- API тесты:
```bash
pytest tests/api
```

- Тесты базы данных:
```bash
pytest tests/data_base
```

- Все тесты:
```bash
pytest tests
```

### 4. Просмотр отчета Allure:
```bash
allure serve allure_results
```

---

## 📁 Структура проекта

```
project/
│
├── allure_results/	 # результаты тестов
├── configuration/   # конфигурация проекта
├── locators/        # локаторы элементов
├── page/            # Page Object Model (классы страниц)
├── reports/         # отчеты
├── screenshots/     # скриншоты
├── test_data/       # тестовые данные
├── tests/           # тесты
└── utils/           # утилиты
```

---

## 🛠️ Стек технологий

- Python  
- Pytest  
- Allure  
- Selenium  
- Requests  
