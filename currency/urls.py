from django.urls import path
from .views import convert_currency

urlpatterns = [
    path("convert/", convert_currency, name="convert-currency"),
]
