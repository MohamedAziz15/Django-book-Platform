from rest_framework import serializers
from .models import Author, Book, review

class bookSerlizer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class AuthorSerlizer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'
        


class ReviewSerlizer(serializers.ModelSerializer):
    class Meta:
        model = review
        fields = '__all__'
        





