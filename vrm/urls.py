from django.urls import path, include
from .views import home_views
from .viewsets import UserViewSet


urlpatterns = [
    path('', home_views.Home.as_view()),
    path('api/v1/profile/', UserViewSet.as_view({'get': 'get'})),   
]