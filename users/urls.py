from django.urls import path, include
from django.conf.urls import url
from . import views
from .views import CreateMessageView
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('view_profile/', TemplateView.as_view(template_name='users/profileview.html'), name='view_profile'),
    path('profile/', views.userprofile, name='profile'),
    path('', include('django.contrib.auth.urls')),
    path('create_message/', CreateMessageView.as_view(success_url='/users/message'), name = "create_message"),
    path('notification/', views.usernotification, name='notification'),
    path('message/', views.usermessage, name='message'),


]
