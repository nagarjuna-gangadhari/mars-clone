from django.urls import path
from .views import *
from .viewset import *


urlpatterns = [
    path('login/', LoginPageView.as_view()),
    path('sign-up/', RegisterView.as_view()),
    path('logout/', logout_view),
    # ---------------------------
    path('profile/', UserProfileViewSet.as_view({'get':'get'})),
    path('location/', LocationViewset.as_view({'get':'get'})),
    
    
]