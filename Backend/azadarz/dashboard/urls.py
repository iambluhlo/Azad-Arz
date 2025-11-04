from django.urls import path
from .views import admin_stats

urlpatterns = [
    path('admin-stats/', admin_stats, name='admin-stats'),
]
