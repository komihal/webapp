# Generated by Django 4.1.7 on 2023-02-23 07:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("archive", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(old_name="Contract", new_name="Contracts",),
        migrations.AlterModelOptions(
            name="contracts",
            options={"verbose_name": "Договор", "verbose_name_plural": "Договоры"},
        ),
    ]