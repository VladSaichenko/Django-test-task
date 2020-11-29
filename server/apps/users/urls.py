from django.urls import path

from apps.users import views

urlpatterns = [
    path('profile/', views.profile, name='profile'),
]
