## Setup

Первое, что нужно сделать, это клонироать репозиторий:
```angular2html
$ https://github.com/leondav1/api_engine.git
$ cd api_engine
```
Создайте виртуальную среду для установки зависимостей и активируйте ее:
```angular2html
$ python -m venv env
$ source env/bin/activate
```
Затем установите зависимости:
```angular2html
(env)$ pip install -r requirements.txt
```
Теперь необходимо настроить базу данных.
Вместо стандартных настроек
```angular2html
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```
вставьте следующий код:
```angular2html
DATABASES = {'default': env.db('DATABASE_URL')}
```
Создайте файл .env, добавьте одну настройку DEBUG=True и переходите к пункту создания миграций:
```angular2html
touch .env
sudo nano .env
DEBUG=True
```
#### Настройка базы PostgreSQL.
Установите базу данных PostgreSQL, если её у вас ещё нет.
1. Откройте консоль PostgreSQL
```angular2html
sudo -u postgres psql postgres
```
2. Затем задайте пароль администратора БД
```angular2html
\password postgres
```
3. Далее необходимо создать и настроить пользователя, при помощи которого будем соединяться с БД. Ну и также укажем значения по умолчанию для кодировки, уровня изоляции транзакции и временного пояса
```angular2html
create user <имя пользователя> with password '<пароль>';
alter role <имя пользователя> set client_encoding to 'utf8';
alter role <имя пользователя> set default_transaction_isolation to 'read committed';
alter role <имя пользователя> set timezone to 'UTC';
```
Временной поям можете указать свой, согласно файла settings.py.
4. Создайте базу для проекта и выйдите из консоли
```angular2html
create database <имя БД> owner <имя пользователя>;
\q
```
5. И последнее, необходимо настроить раздел DATABASES конфигурационного файла проекта settings.py
Нам понадобится файл .env. Создадим его в консоли и добавим пару настроек.
В DATABASE_URL укажем настройки для подключения к БД:
```angular2html
touch .env
sudo nano .env
DEBUG=True
DATABASE_URL=psql://<имя пользователя>:password@127.0.0.1:5432/<имя БД>
```
Осталось создать и применить миграции:
```angular2html
python manage.py makemigrations
python manage.py migrate
```
Создаём суперпользователя:
```angular2html
python manage.py createsuperuser
```
Запускаем сервер:
```angular2html
python manage.py runserver
```

### Немного об API
Вместо аутентификации в каждый запрос необходимо добавлять номер телефона пользователя
Через админку добавим пользователя c номером 89199998877:
```angular2html
http://127.0.0.1:8000/api/stores/?phone=89199998877
```
Получение списка Торговых точек привязанных к конкретному номеру телефона:
```angular2html
http://127.0.0.1:8000/api/stores/?phone=89199998877
```
Вывести список посещений Торговых точек по конкретному номеру телефона. GET запрос:
```angular2html
http://127.0.0.1:8000/api/visit/?phone=89199998877
```
Выполнить посещение Торговой точки. POST запрос:
```angular2html
http://127.0.0.1:8000/api/visit/?phone=89199998877
```
Параметры POST запроса:
```angular2html
{
    "store": 1,
    "latitude": 56.855638,
    "longtitude": 35.878198
}
где store - id торговой точки;
    latitude, longtitude - координаты торговой точки.
```
