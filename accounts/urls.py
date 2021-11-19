from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from . import views


urlpatterns = [
    path('get/', views.get),
    path('signup/', views.signup),
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
    path('<int:user_id>/follow/', views.follow),
    path('<username>/', views.profile),
]