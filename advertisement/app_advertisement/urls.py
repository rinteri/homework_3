from django.urls import path
from .views import index, ind

urlpatterns = [
    path('', index),
    path('start', ind)
]