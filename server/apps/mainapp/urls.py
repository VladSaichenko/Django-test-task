from django.urls import path

from apps.mainapp import views


urlpatterns = [
    path('', views.homepage, name='homepage')
]
