# Generated by Django 4.1.7 on 2023-06-20 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor_data',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
