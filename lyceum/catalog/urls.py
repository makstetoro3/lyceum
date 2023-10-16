from lyceum.catalog import converters
from django.urls import path, re_path, register_converter
from . import views

register_converter(converters.FourDigitIntConverter, "number")

urlpatterns = [
    path("", views.item_list),
    path("<int:id_elem>", views.item_detail),
    re_path("^re/(?P<n>[0-9]+)$", views.number),
    path("converter/<number:n>", views.number),
]
