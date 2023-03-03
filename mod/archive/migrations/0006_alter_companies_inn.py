# Generated by Django 4.1.7 on 2023-02-28 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("archive", "0005_companies_alter_acts_number_alter_acts_title_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="companies",
            name="inn",
            field=models.IntegerField(max_length=10, unique=True, verbose_name="ИНН"),
        ),
    ]