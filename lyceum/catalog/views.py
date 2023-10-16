from django.http import HttpResponse


def item_list(request):
    return HttpResponse("<body>Список элементов<body/>")


def item_detail(request, id_elem):
    return HttpResponse("<body>Подробно элемент<body/>")


def number(request, n):
    return HttpResponse(f"<body>{n}<body/>")
