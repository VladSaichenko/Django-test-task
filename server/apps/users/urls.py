from django.urls import path, include

from apps.users import views

urlpatterns = [
    path('profile/<int:id>', include('allauth.urls'))
]
