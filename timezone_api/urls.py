from timezone_api import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter

# http://127.0.0.1:8000/tz/data/
# http://127.0.0.1:8000/tz/timezone-view-set
router = DefaultRouter()
router.register('timezone-view-set', views.TimezoneViewSet, basename='timezone-view-set-basename')

urlpatterns = [
    path('data/', views.TimezomeAPI.as_view()),
    path('', include(router.urls))
]