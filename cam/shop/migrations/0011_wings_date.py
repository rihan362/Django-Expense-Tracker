# Generated by Django 4.1.2 on 2023-01-18 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_remove_wings_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='wings',
            name='date',
            field=models.TextField(null=True),
        ),
    ]