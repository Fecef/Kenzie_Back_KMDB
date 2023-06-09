# Generated by Django 4.1 on 2023-03-02 18:52

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Review",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "stars",
                    models.PositiveSmallIntegerField(
                        choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]
                    ),
                ),
                ("review", models.TextField()),
                ("spoilers", models.BooleanField(blank=True, default=False, null=True)),
            ],
            options={
                "ordering": ("stars",),
            },
        ),
    ]
