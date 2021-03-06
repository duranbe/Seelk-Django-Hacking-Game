# Generated by Django 2.2.5 on 2021-02-21 16:41

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("alerts", "0002_alert_linked_user"),
    ]

    operations = [
        migrations.CreateModel(
            name="TimeAlert",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                ("base_asset", models.CharField(max_length=3)),
                ("quote_asset", models.CharField(max_length=3)),
                (
                    "when_alert",
                    models.CharField(
                        choices=[("ABV", "Above"), ("BLW", "Below")],
                        default="Above",
                        max_length=3,
                    ),
                ),
                ("is_activated", models.BooleanField()),
                ("date_created", models.DateTimeField(auto_now=True)),
                ("time_delta", models.DurationField()),
                (
                    "percentage",
                    models.FloatField(
                        validators=[
                            django.core.validators.MinValueValidator(0.0),
                            django.core.validators.MaxValueValidator(100.0),
                        ]
                    ),
                ),
                (
                    "linked_user",
                    models.ForeignKey(
                        editable=False,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["date_created"],
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="ValueAlert",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                ("base_asset", models.CharField(max_length=3)),
                ("quote_asset", models.CharField(max_length=3)),
                (
                    "when_alert",
                    models.CharField(
                        choices=[("ABV", "Above"), ("BLW", "Below")],
                        default="Above",
                        max_length=3,
                    ),
                ),
                ("is_activated", models.BooleanField()),
                ("date_created", models.DateTimeField(auto_now=True)),
                ("coin_value", models.DecimalField(decimal_places=15, max_digits=25)),
                (
                    "linked_user",
                    models.ForeignKey(
                        editable=False,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["date_created"],
                "abstract": False,
            },
        ),
        migrations.DeleteModel(
            name="Alert",
        ),
    ]
