from .serilizer import bookSerlizer
from .models import Book,Author,review
from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

@api_view(['GET'])
def book_list_api(request):
    books = Book.objects.all()
    data = bookSerlizer(books,many=True).data
    return Response({"message":"success","status":200,"Books":data})


@api_view(['GET'])
def book_detail_api(request,id):
    book = Book.objects.get(id=id)
    data = bookSerlizer(book,many=False).data
    return Response({"message":"success","status":200,"Book":data})




class BookListAPI(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = bookSerlizer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filterset_fields  = ['title','Author']
    search_fields = ['title', 'Author','price']
    ordering_fields = ['price', 'publish_date']





class BookDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = bookSerlizer






