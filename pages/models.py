from django.db import models
category=[('القاهرة','القاهرة'),
          ('القاهرة','المنصورة') ,
          ('المنيا','المنيا') ,
          ('السويس','السويس'),
          ('دمياط','دمياط'),
          ('اسيوط','اسيوط')
          ]
specialist=[
   ('جلدية','جلدية'),('اسنان','اسنان'),('اطفال حديثة الولادة','اطفال حديثة الولادة'),('مخ و اعصاب','مخ و اعصاب'),
   ('نفسي','نفسي'),('نساء و توليد','نساء و توليد'),('عظام','عظام')
]
class doctor_data(models.Model):
    doctor_name=models.CharField(max_length=100)
    subtitle=models.CharField(max_length=100)
    Specialist_doctor=models.CharField(max_length=200,choices=specialist)
    address=models.CharField(max_length=200,choices=category)
    address_detail=models.CharField(max_length=200)
    price=models.IntegerField(default=0)
    Waiting_time=models.TimeField(blank=True,null=True)
    working_hours=models.IntegerField(default=0)
    number_phone=models.CharField(max_length=12)
    doctor_info=models.CharField(max_length=500,blank=True,null=True)
    doctor_service=models.CharField(max_length=1000,blank=True,null=True)

class comments(models.Model):
    comment_writer_name=models.CharField(max_length=200)
    comment_writer_email=models.CharField(max_length=500)
    comment_message=models.TextField()
class posts(models.Model):
    post_name=models.CharField(max_length=100)
    post_content=models.TextField()
    post_time_created=models.CharField(max_length=100)
    post_date_created=models.CharField(max_length=100)
class appoint(models.Model):
    patient_name=models.CharField(max_length=100)
    patient_phone_number=models.CharField(max_length=12)
    day_want=models.CharField(max_length=100)

class blogs(models.Model):
    blog_name=models.CharField(max_length=500)
    blog_description=models.TextField()
    publish_day=models.CharField(max_length=100)
    publish_date=models.DateField()
    publish_time=models.TimeField()
