from django.contrib import admin
from django.urls import path
from core import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('add-assignment/', views.add_assignment, name='add_assignment'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='core/logout.html'), name='logout'),
    path('check-in/', views.wellness_check_in, name='check_in'),
    path('calendar/', views.calendar_view, name='calendar_view'),
    path('analytics/', views.mood_analytics, name='mood_analytics'),
]
