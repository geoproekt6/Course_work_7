<H1>
    <center>
        Course Work 7 
    </center>
</H1>



<p align="center">
    <a href=""><img alt="Documentation" src="https://img.shields.io/badge/django-4.2-green"></a>
    <a href="https://pypi.org/project/djangorestframework/"><img alt="Documentation" src="https://img.shields.io/badge/DRF-3.14.0-red"></a>
</p>

______

<H3>
    <center>
        Установка
    </center>
</H3>

1. Клонировать проект

```bash
git clone git@github.com:AndrewDyakonow/Course_work_7.git
```

2. Развернуть виртуальное окружение

```bash
python -m venv venv
```

3. Активировать виртуальное окружение

```bash
source venv/bin/activate
```

4. Установить зависимости

```bash
pip install -r requirements.txt
```

5. запустить отладочный веб-сервер

```bash
python manage.py runserver
```

6. Запустить Worker

```bash
celery -A config worker -l INFO
```

7. Запустить планировщик Celery beat

```bash
celery -A config beat -l INFO
```
