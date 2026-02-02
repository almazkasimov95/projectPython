# AQA Automation Framework (Python + Playwright + Pytest)

## 🛠️ Технологии
- Python 3.10+
- Playwright (Chromium)
- Pytest
- Allure
- GitHub Actions

## ▶️ Запуск
1. `pip install -r requirements.txt`
2. `playwright install chromium`
3. `pytest tests/ --alluredir=./allure-results`
4. `allure serve ./allure-results`

## 🧪 Тесты
- UI: вход в систему (the-internet.herokuapp.com)
- API: CRUD-операции (jsonplaceholder.typicode.com)

![Allure Report](allure-report.png)

