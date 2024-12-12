# Generated by Django 5.1.4 on 2024-12-12 08:58

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="SentimentHistory",
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
                ("user_input", models.TextField()),
                ("sentiment", models.CharField(max_length=50)),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
