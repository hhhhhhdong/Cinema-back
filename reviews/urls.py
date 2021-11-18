from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_by_user),
    path('<int:movie_id>/', views.get_create_by_movie),
]
