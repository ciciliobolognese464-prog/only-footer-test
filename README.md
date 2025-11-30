# Автотесты футера сайта only.digital

Проект содержит автотесты для проверки наличия футера и ключевых элементов на нескольких страницах сайта only.digital.

## Что проверяется

Тесты проверяют на следующих страницах:
- Главная страница (https://only.digital/)
- Страница проектов (https://only.digital/projects)
- Страница компании (https://only.digital/company)

Для каждой страницы проверяется:
- Видимость футера
- Наличие текста "© 2014 - 2025"
- Наличие элемента "Политика конфиденциальности"

## Установка и запуск

1. Создать и активировать виртуальное окружение (по желанию):
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # Linux/Mac
   source venv/bin/activate
   ```

2. Установить зависимости:
   ```bash
   pip install -r requirements.txt
   ```

3. Установить браузеры Playwright:
   ```bash
   python -m playwright install
   ```

4. Запустить тесты:
   ```bash
   pytest
   ```


