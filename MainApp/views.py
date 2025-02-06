from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from .models import Item
from django.core.exceptions import ObjectDoesNotExist

author = {
    'name': 'Иван',
    'surname': 'Иванов',
    'lastname': 'Петрович',
    'phone': '8-923-600-01-02',
    'email': 'vasya@mail.ru'
}

# items = [
# {"id": 1, "name": "Кроссовки abibas" ,"quantity":5},
# {"id": 2, "name": "Куртка кожаная" ,"quantity":2},
# {"id": 5, "name": "Coca-cola 1 литр" ,"quantity":12},
# {"id": 7, "name": "Картофель фри" ,"quantity":0},
# {"id": 8, "name": "Кепка" ,"quantity":124}
# ]

def home(request):
    """Модуль 1"""
    #print(f"{vars(request) = }")
    #text = """
    #<h1>"Изучаем Django"</h1>
    #<strong>Автор</strong>: <i>Чернышов Д.Д.</i>"""
    #return HttpResponse(text)

    """Модуль 2"""
    context = {
        "name": "Chernyshov Danila Dmitrievich",
        "email": "my_email@mail.ru"
    }
    return render(request, "index.html", context)

def about(request):
    """Модуль 1"""
    # text = f"""
    # Имя: <b>{author["Имя"]}</b><br>
    # Фамилия: <b>{author["Фамилия"]}</b><br>
    # Отчество: <b>{author["Отчество"]}</b><br>
    # Телефон: <b>{author["Телефон"]}</b><br>
    # Почта: <b>{author["Почта"]}</b><br>"""
    #return HttpResponse(text)

    """Модуль 2"""
    context = {
        "author": author
    }
    return render(request, "about.html", context)

def get_item(request, item_id):
    """Модуль 1"""
    # for item in items:
    #     if item["id"] == item_id:
    #         text = f"""
    #         id: <b>{item["id"]}</b><br>
    #         name: <b>{item["name"]}</b><br>
    #         quantity: <b>{item["quantity"]}</b><br>
    #         <b><a href="/items">Назад к списку товаров</a></b><br>"""
    #         return HttpResponse(text)
    # text = f"<b>Товар с id={item_id} не найден</b>"
    # return HttpResponse(text)

    """Модуль 2"""
    # for item in items:
    #     if item["id"] == item_id:
    #         return render(request, "item.html", item)
    #return HttpResponseNotFound(f"<b>Товар с id={item_id} не найден</b>")

    """Модуль 3"""
    colors = []
    try:
        item = Item.objects.get(pk=item_id)
        if item.colors.exists():
            colors = item.colors.all()
    except ObjectDoesNotExist:  
        return HttpResponseNotFound(f"<b>Товар с id={item_id} не найден</b>")
    else:
        context = {
            "item": item,
            "colors": colors
        }
        return render(request, "item.html", context)
    
def get_items(request):
    """Модуль 1"""
    # text = """<h1>Список товаров</h1><ol>"""
    # for item in items:
    #     text += f"""<li><a href="/item/{item["id"]}">{item["name"]}</a></li>"""
    #     #text += f"""
    #         #id: <b>{item["id"]}</b><br>
    #         #name: <b><a href="/item/{item["id"]}">{item["name"]}</a></b><br>
    #         #quantity: <b>{item["quantity"]}</b><br>"""
    #     #text += "<br>"
    # text += "</ol>"
    #return HttpResponse(text)

    """Модуль 2"""
    #context = {
    #    "items": items
    #}
    #return render(request, "items.html", context)

    """Модуль 3"""
    items = Item.objects.all()
    context = {
        "items": items
    }
    return render(request, "items.html", context)