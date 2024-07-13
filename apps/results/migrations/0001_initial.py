# Generated by Django 4.2.14 on 2024-07-13 01:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("quiz", "0001_initial"),
        ("authentication", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Result",
            fields=[
                ("result_id", models.AutoField(primary_key=True, serialize=False)),
                ("score", models.IntegerField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "quiz_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="results",
                        to="quiz.quiz",
                    ),
                ),
                (
                    "user_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="results",
                        to="authentication.user",
                    ),
                ),
            ],
        ),
    ]
