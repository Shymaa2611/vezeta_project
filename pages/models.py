from typing import Iterable, Optional
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.utils.text import slugify
from django.core.validators import MaxValueValidator,MinValueValidator

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
    user=models.OneToOneField(User,on_delete=models.CASCADE,blank=True,null=True)
    doctor_name=models.CharField(max_length=100)
    subtitle=models.CharField(max_length=100)
    doctor_image=models.ImageField()
    clininc_image=models.ImageField()
    Specialist_doctor=models.CharField(max_length=200,choices=specialist)
    address=models.CharField(max_length=200,choices=category)
    address_detail=models.CharField(max_length=200)
    price=models.IntegerField(default=0)
    Waiting_time=models.TimeField(blank=True,null=True)
    working_hours=models.IntegerField(default=0)
    number_phone=models.CharField(max_length=12)
    doctor_info=models.CharField(max_length=500,blank=True,null=True)
    doctor_service=models.CharField(max_length=1000,blank=True,null=True)
    slug=models.SlugField(blank=True,null=True)
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug=slugify(self.user.username)
            super(doctor_data,self).save(*args,**kwargs)
    def __str__(self):
        return self.slug
def create_profile(sender,**kwargs):
    if kwargs['created']:
        user_profile=doctor_data.objects.create(user=kwargs['instance'])
post_save.connect(create_profile,sender=User)


class comments(models.Model):
    comment_writer_name=models.CharField(max_length=200)
    comment_writer_email=models.CharField(max_length=500)
    comment_message=models.TextField()
class posts(models.Model):
    post_name=models.CharField(max_length=100)
    post_content=models.TextField()
    post_image=models.ImageField(blank=True,null=True)
    post_time_created=models.CharField(max_length=100)
    post_date_created=models.CharField(max_length=100)
class appoint(models.Model):
    patient_name=models.CharField(max_length=100)
    patient_phone_number=models.CharField(max_length=12)
    day_want=models.CharField(max_length=100)

class blogs(models.Model):
    blog_name=models.CharField(max_length=500)
    blog_description=models.TextField()
    blog_image=models.ImageField(blank=True,null=True)
    publish_day=models.CharField(max_length=100)
    publish_date=models.DateField()
    publish_time=models.TimeField()

class Doctor_review(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    doctor=models.ForeignKey(doctor_data,on_delete=models.CASCADE)
    stars=models.IntegerField(default=0,validators=[MinValueValidator(0),MaxValueValidator(5)])
    class Meta:
        unique_together=(('user','doctor'))
        index_together=(('user','doctor'))