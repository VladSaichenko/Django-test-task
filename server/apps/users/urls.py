from django.urls import path, include

from apps.users import views

urlpatterns = [
    path('profile/', views.profile, name='profile'),
]
