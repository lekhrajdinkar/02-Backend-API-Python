from django.urls import path
from timezone_api import views

urlpatterns = [
    path('codes/', views.TimezomeAPI.as_view())

]