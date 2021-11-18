from django.urls import path
from . import views

urlpatterns = [
    path('popular/', views.popular),
    path('top_rated/', views.top_rated),
    path('genres/ids/', views.genre_ids),
    path('genres/<int:genre_id>/', views.genres),
    path('<int:movie_id>/', views.movie_detail),
    # path('loaddata/', views.loaddata),
    # path('loaddata2/', views.loaddata2),
]
