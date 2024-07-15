# Generated by Django 4.2.14 on 2024-07-13 01:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("authentication", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Notification",
            fields=[
                (
                    "notification_id",
                    models.AutoField(primary_key=True, serialize=False),
                ),
                ("type", models.CharField(max_length=10)),
                ("message", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "user_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="notifications",
                        to="authentication.user",
                    ),
                ),
            ],
        ),
    ]