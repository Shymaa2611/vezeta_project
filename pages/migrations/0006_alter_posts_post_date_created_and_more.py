# Generated by Django 4.1.7 on 2023-06-21 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_posts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='post_date_created',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='posts',
            name='post_time_created',
            field=models.CharField(max_length=100),
        ),
    ]
