import os
import django
from django.conf import settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
django.setup()

from faker import Faker
from decimal import Decimal  
from book.models import Book, Author, review
import random


def create_Author(n):
    fake = Faker()
    for i in range(n):
        Author.objects.create(
            name = fake.name(),
            birth_date =fake.date_this_decade(),
            biography = fake.text(),
        )
    print(f'{n} Author was added successfully')


def create_Book(n):
    fake = Faker()
    for i in range(n):
        Book.objects.create(
            title = fake.sentence(),
            Author = Author.objects.all().order_by('?')[0],
            publish_date = fake.date_this_decade(),
            price = fake.pydecimal(left_digits=3, right_digits=2, positive=True),  
        )
    print(f'{n} Book was added successfully')


def create_review(n):
    fake = Faker()
    for i in range(n):
        review.objects.create(
            book=Book.objects.all().order_by('?')[0],
            reviewer_name=fake.name(),
            rating=random.randint(1, 5),
            content=fake.text(),

        )
    print(f'{n} review was added successfully')


# create_Author(20)
create_Book(100)  
create_review(2000)  
