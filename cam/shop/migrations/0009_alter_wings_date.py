# Generated by Django 4.1.2 on 2022-12-27 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_alter_wings_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wings',
            name='date',
            field=models.DateField(blank='True', null='True'),
        ),
    ]