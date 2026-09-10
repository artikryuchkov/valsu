# Учебный сайт на Django

Страница демонстрации без входа, сбора данных, аналитики и подключения базы.

## Локальный запуск (PowerShell)

```powershell
python -m venv .venv
.\.venv\Scripts\python -m pip install -r requirements.txt
.\.venv\Scripts\python manage.py runserver
```

Откройте http://127.0.0.1:8000. Остановка: Ctrl+C.

## Публикация на Render

Сначала загрузите обновлённые файлы в GitHub, сохраняя структуру папок.
Файлы manage.py и requirements.txt должны лежать в корне репозитория.
Не загружайте .venv, db.sqlite3, auth.log и старую папку form/static.
.gitignore не удаляет файлы, которые ранее уже попали на GitHub.
Если там есть реальные учётные данные, удалите их также из истории репозитория и смените затронутые пароли.

1. На https://dashboard.render.com создайте New → Web Service.
2. Подключите GitHub и выберите репозиторий с обновлённым проектом.
3. Language: Python 3. Root Directory: пусто, если manage.py в корне.
4. Build Command: `pip install -r requirements.txt && python manage.py collectstatic --noinput`
5. Start Command: `gunicorn fish.wsgi:application --bind 0.0.0.0:$PORT`
6. Добавьте переменную окружения SECRET_KEY — новый случайный ключ. Для его получения локально выполните:
   `.\.venv\Scripts\python -c "import secrets; print(secrets.token_urlsafe(64))"`
   Скопируйте результат в Render, не в файлы проекта.
7. Для учебного сайта выберите Free, если доступен, и нажмите Deploy Web Service.
8. После статуса Live откройте адрес https://имя-сервиса.onrender.com.

База данных, DATABASE_URL и migrate для этой версии не нужны.
На Render DEBUG выключается автоматически; домен берётся из RENDER_EXTERNAL_HOSTNAME.
Бесплатный сервис засыпает после 15 минут без запросов, первый запуск может занять около минуты.
Инструкция хостинга: https://render.com/docs/deploy-django

## Проверки

```powershell
.\.venv\Scripts\python manage.py check
.\.venv\Scripts\python manage.py test
.\.venv\Scripts\python manage.py collectstatic --noinput
```

Старые db.sqlite3, auth.log и ресурсы form/static могут оставаться локально, но приложение их не читает и не публикует. Старая таблица удаляется миграцией 0007 только при её явном применении к старой базе; автоматически старые данные не стирались.
