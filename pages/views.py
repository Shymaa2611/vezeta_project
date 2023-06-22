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

#def index(request):
#    return render(request,'pages/index.html')

    
class doctor_list(ListView):
     model=doctor_data
     context_object_name='doctor_list'
     template_name='pages/doctor_list.html' 
     
   #  def get_context_data(self, **kwargs):
    #    context = super().get_context_data(**kwargs)

 

      

class doctor_detail(DetailView):
    model=doctor_data
    context_object_name='doctor_detail'
    template_name='pages/doctor_detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['comment'] = comments.objects. all()
        context['form'] =commentForm()
        return context

class CommentCreateView(CreateView):
    model = comments
    form_class =commentForm

    def get_success_URL(self):
        return reverse ('request: detail', kwargs = {'slug':self.object.post.slug})

    def form_valid(self, form):
        post = get_object_or_404(Request, slug = self.kwargs ['slug'])
        Form.instance.post = Request
        return super().form_valid(form)

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

class profile(CreateView):
    model=doctor_data
    form_class=profileForm
    context_object_name='form'
    success_url='/'
    template_name='pages/create_profile.html'