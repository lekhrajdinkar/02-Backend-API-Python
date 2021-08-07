from . import views
from django.urls import path

urlpatterns = [
    path('hello', views.hello),
    path('hello-string', views.hello_string)
]