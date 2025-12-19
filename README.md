# Netflix Клон на Django

## Быстрый старт

1. **Клонируйте репозиторий:**
   ```
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
   ```
2. **Создайте и активируйте виртуальное окружение:**
   ```
   python -m venv .venv
   .venv\Scripts\activate  # Windows
   source .venv/bin/activate  # Linux/Mac
   ```
3. **Установите зависимости:**
   ```
   pip install -r requirements.txt
   ```
4. **Выполните миграции базы данных:**
   ```
   python manage.py migrate
   ```
5. **Запустите сервер:**
   ```
   python manage.py runserver
   ```
6. **Откройте сайт:**
   Перейдите в браузере по адресу http://127.0.0.1:8000/

## Примечания
- Для входа и регистрации используйте страницы /login и /signup.
- Для добавления фильмов в избранное используйте кнопку "Добавлено".
- Все команды выполняйте из корневой папки проекта.
