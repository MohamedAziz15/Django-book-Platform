from django.contrib import admin
from django.urls import path
from .views import book_list,book_detail

from .api import book_list_api, book_detail_api , BookListAPI,BookDetailAPI

urlpatterns = [
    path("",book_list),
    path('<slug:slug>',book_detail),



    # path('api/list', book_list_api),
    # path('api/list/<int:id>',book_detail_api),




    path('api/list', BookListAPI.as_view()),
    # path('api/list/<int:id>',BookDetailAPI.as_view()),
    path('api/list/<int:pk>',BookDetailAPI.as_view()),

]






