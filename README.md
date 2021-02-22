# Seelk-Django-Hacking-Game
Seelk Django Hacking Game

CoinAlert : a simple cryptocurrency notification app

Featuring :

- Alert based on coin value
- Alert based on a X % increase or decrease during a given timeframe
- Email Alert
- Use of CoinApi.io

### Technology

Django, Django Rest Framework, Celery, Redis, SQLITE3 and HTML/CSS/JS

### Django Apps

- users : Manage Users with CRUD and Login/Logout

`api/user` - List

`api/user/{pk}` - CRUD

`api/auth/login` - Login

`api/auth/logout` - Logout

- alerts : Manage Alerts with CRUD

`api/alerts/time` List Time Alerts

`api/alerts/time/{pk}` CRUD Time Alert

`api/alerts/value/` List Value Alerts

`api/alerts/value/{pk}` CRUD Value Alert

- front : only here to be used as a front end for demo purpose only (not suitable for production)

`/` Home and Main Page

`/login` Login Page

`/register` Sign Up Page 

### Config

In settings.py modify SECRET KEY, COINAPI_KEY and all EMAIL variables.
