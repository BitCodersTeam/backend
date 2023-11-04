from django.urls import path

from .views.guilds.add import add_guild
from .views.testing import test

urlpatterns = [
    path('test', test),
    #guilds
    path('guild/add', add_guild)
]