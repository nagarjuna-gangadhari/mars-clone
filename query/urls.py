from django.urls import path
from .views import *


urlpatterns = [
    path('query/', ChatConsumer.as_asgi())
]