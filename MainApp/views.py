from django.shortcuts import render
from django.http import HttpResponse

author = {
    'Имя': 'Иван',
    'Фамилия': 'Иванов',
    'Отчество': 'Петрович',
    'Телефон': '8-923-600-01-02',
    'Почта': 'vasya@mail.ru'
}

all_items = [
{"id": 1, "name": "Кроссовки abibas" ,"quantity":5},
{"id": 2, "name": "Куртка кожаная" ,"quantity":2},
{"id": 5, "name": "Coca-cola 1 литр" ,"quantity":12},
{"id": 7, "name": "Картофель фри" ,"quantity":0},
{"id": 8, "name": "Кепка" ,"quantity":124}
]

def home(request):
    #print(f"{vars(request) = }")
    text = """
    <h1>"Изучаем Django"</h1>
    <strong>Автор</strong>: <i>Чернышов Д.Д.</i>"""
    return HttpResponse(text)

def about(request):
    text = f"""
    Имя: <b>{author["Имя"]}</b><br>
    Фамилия: <b>{author["Фамилия"]}</b><br>
    Отчество: <b>{author["Отчество"]}</b><br>
    Телефон: <b>{author["Телефон"]}</b><br>
    Почта: <b>{author["Почта"]}</b><br>"""
    return HttpResponse(text)

def item(request, id):
    for item in all_items:
        if item["id"] == id:
            text = f"""
            id: <b>{item["id"]}</b><br>
            name: <b>{item["name"]}</b><br>
            quantity: <b>{item["quantity"]}</b><br>
            <b><a href="/items">Назад к списку товаров</a></b><br>"""
            return HttpResponse(text)
    text = f"<b>Товар с id={id} не найден</b>"
    return HttpResponse(text)
    
def items(request):
    text = ""
    for item in all_items:
        text += f"""
            id: <b>{item["id"]}</b><br>
            name: <b><a href="/item/{item["id"]}">{item["name"]}</a></b><br>
            quantity: <b>{item["quantity"]}</b><br>"""
        text += "<br>"
    return HttpResponse(text)