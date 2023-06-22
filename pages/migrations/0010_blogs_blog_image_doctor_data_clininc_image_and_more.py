# Generated by Django 4.1.7 on 2023-06-22 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0009_alter_blogs_blog_description_alter_blogs_blog_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogs',
            name='blog_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='doctor_data',
            name='clininc_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='doctor_data',
            name='doctor_image',
            field=models.ImageField(default='', upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='posts',
            name='post_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
