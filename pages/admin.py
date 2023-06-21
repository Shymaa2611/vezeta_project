from django.contrib import admin
from .models import doctor_data,comments,posts,appoint,blogs
admin.site.register(doctor_data)
admin.site.register(comments)
admin.site.register(posts)
admin.site.register(appoint)
admin.site.register(blogs)