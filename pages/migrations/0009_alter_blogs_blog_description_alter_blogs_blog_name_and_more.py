# Generated by Django 4.1.7 on 2023-06-21 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0008_blogs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='blog_description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='blogs',
            name='blog_name',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='doctor_data',
            name='Specialist_doctor',
            field=models.CharField(choices=[('جلدية', 'جلدية'), ('اسنان', 'اسنان'), ('اطفال حديثة الولادة', 'اطفال حديثة الولادة'), ('مخ و اعصاب', 'مخ و اعصاب'), ('نفسي', 'نفسي'), ('نساء و توليد', 'نساء و توليد'), ('عظام', 'عظام')], max_length=200),
        ),
        migrations.AlterField(
            model_name='doctor_data',
            name='address',
            field=models.CharField(choices=[('القاهرة', 'القاهرة'), ('القاهرة', 'المنصورة'), ('المنيا', 'المنيا'), ('السويس', 'السويس'), ('دمياط', 'دمياط'), ('اسيوط', 'اسيوط')], max_length=200),
        ),
    ]
