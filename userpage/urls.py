from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home_view, name='home'),
    path('register/', views.register_view, name='register'),
    path('success/', views.success_view, name='success'),
    path('records/', views.view_users, name='view_users'),
]
