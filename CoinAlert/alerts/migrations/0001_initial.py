# Generated by Django 2.2.5 on 2021-02-19 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Alert",
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
                ("coin_value", models.DecimalField(decimal_places=15, max_digits=25)),
                ("is_activated", models.BooleanField()),
                ("date_created", models.DateTimeField(auto_now=True)),
            ],
        ),
    ]