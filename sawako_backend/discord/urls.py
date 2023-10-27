from django.urls import path
from .views.testing import test

urlpatterns = [
    path('test/', test)
]