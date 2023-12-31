# Generated by Django 4.1.7 on 2023-06-21 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_comments'),
    ]

    operations = [
        migrations.CreateModel(
            name='posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_name', models.CharField(max_length=100)),
                ('post_content', models.TextField()),
                ('post_time_created', models.TimeField()),
                ('post_date_created', models.DateField()),
            ],
        ),
    ]
