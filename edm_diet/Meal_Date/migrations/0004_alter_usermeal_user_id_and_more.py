# Generated by Django 4.2 on 2024-01-03 01:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Meal_Date", "0003_alter_usermeal_user_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="usermeal",
            name="user_id",
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name="usermealevaluation",
            name="user_id",
            field=models.CharField(max_length=255),
        ),
    ]
