# Generated by Django 4.1.2 on 2022-12-26 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_wings_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wings',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]
