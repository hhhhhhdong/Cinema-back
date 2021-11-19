from django.urls import path
from . import views

urlpatterns = [
    path('user/<int:user_id>/', views.get_by_user),
    path('movie/<int:movie_id>/', views.get_create_by_movie),
]
