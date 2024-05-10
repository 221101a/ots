# Generated by Django 4.2.5 on 2024-01-24 09:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("online_test", "0003_remove_test_paper_id_alter_test_paper_q_id"),
    ]

    operations = [
        migrations.CreateModel(
            name="Profile",
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
                ("fathers_name", models.CharField(default="", max_length=30)),
                ("mothers_name", models.CharField(default="", max_length=30)),
                ("phone", models.CharField(default="", max_length=10)),
                ("email", models.CharField(default="", max_length=30)),
                ("address", models.CharField(default="", max_length=50)),
                (
                    "username",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="online_test.user",
                    ),
                ),
            ],
        ),
    ]
