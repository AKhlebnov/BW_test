## Описание проекта

Тестовое задание - небольшое Django-приложение, которое состоит из двух частей:
1. API для работы с продуктами (создание и получение списка).
2. Страница на HTML с использованием JavaScript для отправки данных на API и отображения продуктов.

### Технологии

- Python 3.9
- Django 4.2
- SQLite3
- HTML
- JavaScript

### Установка

Для запуска приложения проделайте следующие шаги:

1. Склонируйте репозиторий.
```
git clone git@github.com:AKhlebnov/BW_test.git
```
2. Перейдите в папку с кодом и создайте виртуальное окружение:
```
python -m venv venv
```
3. Активируйте виртуальное окружение:
На Windows:
```
venv\Scripts\activate
```
На macOS/Linux:
```
source venv/bin/activate
```
4. Установите зависимости:
```
python -m pip install -r requirements.txt
```
5. Выполните миграции:
```
python manage.py migrate
```
6. Соберите статические файлы:
```
python manage.py collectstatic
```
7. Создайте суперпользователя:
```
python manage.py createsuperuser
```
8. Запустите сервер:
```
python manage.py runserver
```
9. Перейдите в браузере по адресу:
```
http://127.0.0.1:8000/products/
```