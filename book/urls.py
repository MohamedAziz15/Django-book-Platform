from django.contrib import admin
from django.urls import path
from .views import book_list,book_detail

urlpatterns = [
    path("",book_list),
    path('<slug:slug>',book_detail)
]






