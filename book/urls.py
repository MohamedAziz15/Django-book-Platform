from django.contrib import admin
from django.urls import path
from .views import book_list,book_detail

from .api import book_list_api, book_detail_api

urlpatterns = [
    path("",book_list),
    path('<slug:slug>',book_detail),



    path('api/list', book_list_api),
    path('api/list/<int:id>',book_detail_api)

]






