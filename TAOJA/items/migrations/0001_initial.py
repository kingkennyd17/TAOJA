# Generated by Django 5.1 on 2024-08-13 11:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("categories", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Item",
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
                ("name", models.CharField(max_length=100)),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("stock", models.IntegerField(default=0)),
                ("description", models.TextField(blank=True)),
                ("published_date", models.DateTimeField(auto_now_add=True)),
                (
                    "subcategory",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="items",
                        to="categories.subcategory",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Accessory",
            fields=[
                (
                    "item_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="items.item",
                    ),
                ),
                ("compatibility", models.CharField(max_length=100)),
                ("material", models.CharField(max_length=100)),
                ("color", models.CharField(max_length=50)),
            ],
            bases=("items.item",),
        ),
        migrations.CreateModel(
            name="Phone",
            fields=[
                (
                    "item_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="items.item",
                    ),
                ),
                ("screen_size", models.CharField(max_length=50)),
                ("ram", models.CharField(max_length=50)),
                ("rom", models.CharField(max_length=50)),
                ("battery_capacity", models.CharField(max_length=50)),
                ("camera_resolution", models.CharField(max_length=50)),
            ],
            bases=("items.item",),
        ),
        migrations.CreateModel(
            name="SmartDevice",
            fields=[
                (
                    "item_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="items.item",
                    ),
                ),
                ("type", models.CharField(max_length=50)),
                ("compatibility", models.CharField(max_length=100)),
                ("battery_life", models.CharField(max_length=50)),
                ("features", models.TextField()),
            ],
            bases=("items.item",),
        ),
        migrations.CreateModel(
            name="Tablet",
            fields=[
                (
                    "item_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="items.item",
                    ),
                ),
                ("screen_size", models.CharField(max_length=50)),
                ("storage", models.CharField(max_length=50)),
                ("battery_life", models.CharField(max_length=50)),
                ("operating_system", models.CharField(max_length=50)),
            ],
            bases=("items.item",),
        ),
    ]
