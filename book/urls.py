from django.contrib import admin
from django.urls import path
from .views import book_list,book_detail

from .api import book_list_api, book_detail_api , BookListAPI,BookDetailAPI, AuthorListAPI,AuthorDetailAPI
from .api import reviewListAPI,reviewDetailAPI
urlpatterns = [
    path("",book_list),
    path('<slug:slug>',book_detail),



    # path('api/list', book_list_api),
    # path('api/list/<int:id>',book_detail_api),


    #Books
    path('api/list', BookListAPI.as_view()),
    # path('api/list/<int:id>',BookDetailAPI.as_view()),
    path('api/list/<int:pk>',BookDetailAPI.as_view()),

    
    #Authors
    path('Authors/api/list', AuthorListAPI.as_view()),
    path('Authors/api/list/<int:pk>',AuthorDetailAPI.as_view()),

    #Review
    path('Review/api/list', reviewListAPI.as_view()),
    path('Review/api/list/<int:pk>',reviewDetailAPI.as_view()),



]






