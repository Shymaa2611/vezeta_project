# Generated by Django 4.2.3 on 2023-07-22 09:14

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pages', '0012_doctor_data_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor_review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stars', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.doctor_data')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'doctor')},
                'index_together': {('user', 'doctor')},
            },
        ),
    ]
