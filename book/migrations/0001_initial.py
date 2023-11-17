# Generated by Django 4.2.7 on 2023-11-17 07:44

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Author",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("birth_date", models.DateField()),
                ("biography", models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name="Book",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=50)),
                ("publish_date", models.DateField()),
                ("price", models.FloatField()),
                (
                    "Author",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="author_book",
                        to="book.author",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="review",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("reviewer_name", models.CharField(max_length=100)),
                (
                    "rating",
                    models.IntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(
                                1, message="Value must be greater than or equal to 1."
                            ),
                            django.core.validators.MaxValueValidator(
                                5, message="Value must be less than or equal to 5."
                            ),
                        ]
                    ),
                ),
                ("content", models.TextField(max_length=2000)),
                (
                    "book",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="Book_reviews",
                        to="book.book",
                    ),
                ),
            ],
        ),
    ]