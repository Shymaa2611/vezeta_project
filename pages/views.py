from audioop import reverse
from typing import Any, Dict
from urllib.request import Request
from django.db import models
from django.db.models.query import QuerySet
from django.forms import Form
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render,redirect
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView,TemplateView,View,FormView
from .models import doctor_data,posts,appoint,blogs,comments
from .forms import commentForm,postForm,appointForm,profileForm
from django.contrib.auth.forms import UserCreationForm

def doctor_list(request):
     name=None
     Specialist_doctor=None
     search=doctor_data.objects.all()
     if 'search_name' in request.GET:
            name=request.GET['search_name']
            if name:
                search=search.filter(doctor_name__icontains=name)

     if 'specilization' in request.GET:
          Specialist_doctor=request.GET['specilization']
          if  Specialist_doctor:
             search=search.filter(Specialist_doctor__icontains=Specialist_doctor)
         
     context={
         'doctor_list':search
     }
     return render(request,'pages/doctor_list.html',context) 
     

def doctor_detail(request,pk):
     if request.method=='POST':
         add_Comment=commentForm(request.POST,request.FILES)
         if add_Comment.is_valid():
             add_Comment.save()
     context={
         'form':commentForm(),
         'doctor_detail':doctor_data.objects.get(id=pk)
     }
     return render(request,'pages/doctor_detail.html',context)

class signUp(CreateView):
    form_class=UserCreationForm
    context_object_name='form'
    success_url='/'
    template_name='authentication/signup.html'


class add_posts(CreateView):
   model=posts
   form_class=postForm
   context_object_name='form'
   success_url='/'
   template_name='pages/add_post.html'

class update_post(UpdateView):
   model=posts
   form_class=postForm
   context_object_name='form'
   success_url='/'
   template_name='pages/update_post.html'

class delete_post(DeleteView):
    model=posts
    template_name='pages/delete_post.html'
    success_url='/'      
class appointment(CreateView):
    model=appoint
    form_class=appointForm
    template_name='pages/appointment.html'
    context_object_name='form'
    success_url='/' 

class blog_list(ListView):
    model=blogs
    context_object_name='blog'
    template_name='pages/blog_list.html'
class blog_detail(DetailView):
    model=blogs
    context_object_name='blog_detail'
    template_name='pages/blog_detail.html'

class update_profile(UpdateView):
    model=doctor_data
    form_class=profileForm
    context_object_name='form'
    success_url='/'
    template_name='pages/update_profile.html'

class profile(DeleteView):
    model=doctor_data
    context_object_name='data'
    success_url='/'
    template_name='pages/profile.html'
class present(CreateView):
    model=doctor_data
    context_object_name='form'
    success_url='/'
    template_name='pages/present_yourself.html'
