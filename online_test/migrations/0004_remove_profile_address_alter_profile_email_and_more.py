# Generated by Django 4.2.5 on 2024-02-28 09:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("online_test", "0003_alter_profile_username"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="profile",
            name="address",
        ),
        migrations.AlterField(
            model_name="profile",
            name="email",
            field=models.CharField(default="not filled", max_length=30),
        ),
        migrations.AlterField(
            model_name="profile",
            name="fathers_name",
            field=models.CharField(default="not filled", max_length=30),
        ),
        migrations.AlterField(
            model_name="profile",
            name="mothers_name",
            field=models.CharField(default="not filled", max_length=30),
        ),
        migrations.AlterField(
            model_name="profile",
            name="phone",
            field=models.CharField(default="not filled", max_length=10),
        ),
        migrations.AlterField(
            model_name="profile",
            name="username",
            field=models.ForeignKey(
                max_length=20,
                on_delete=django.db.models.deletion.CASCADE,
                primary_key=True,
                serialize=False,
                to="online_test.user",
            ),
        ),
    ]
