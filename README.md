# FirstDjango_0402025

## Instruction

1. python3 -m venv django_venv

2. source django_venv/bin/activated

3. pip3 install -r requirements.txt

4. python manage.py migrate

5. python manage.py runserver

## Запуск ipython в контексте приложений Django
```
    python manage.py shell_plus --ipython
```

## Выгрузить данные из БД
```
    python manage.py dumpdata MainApp --indent 4 > ./fixtures/items.json

    python manage.py dumpdata MainApp.item --indent 4 > ./fixtures/only_items.json
```

## Загрузить данные из БД
```
    python manage.py loaddata ./fixtures/items.json
```

## Дополнительно

1. Полезное дополнения для шаблнов `Django`
```
    ext isntall baptisteo.vscode-django
```

2. Добавить в settings.json
```
"emmet.includeLanguages": {
    " django-html": "html",
},
"files.assocoations": {
    "*.html": "django-html",
}
```