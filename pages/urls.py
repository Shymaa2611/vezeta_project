from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns=[
    path('',view=views.doctor_list,name='doctor_list'),
    path('doctor_detail/<int:pk>/',view=views.doctor_detail,name='doctor_detail'),
    path('update_post/<int:pk>/',views.update_post.as_view(),name='update_post'),
    path('delete_post/<int:pk>/',views.delete_post.as_view(),name='delete_post'),
    path('signUp/',views.signUp.as_view(),name='signUp'),
    path('blog_list/',views.blog_list.as_view(),name='blog_list'),
    path('blog_detail/<int:pk>/',views.blog_detail.as_view(),name='blog_detail'),
    path('appointment/',views.appointment.as_view(),name='appointment'),
    path('update_profile/<int:pk>/',views.update_profile.as_view(),name='update_profile'),
    path('profile/<int:pk>/',views.profile.as_view(),name='profile'),
    path('present/',views.present.as_view(),name='present'),
    path('add_posts/',views.add_posts.as_view(),name='add_posts'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    path('login/',auth_views.LoginView.as_view(template_name='authentication/login.html'),name='login'),
]
