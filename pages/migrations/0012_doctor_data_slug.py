# Generated by Django 4.2.3 on 2023-07-22 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0011_doctor_data_user_alter_doctor_data_clininc_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor_data',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
