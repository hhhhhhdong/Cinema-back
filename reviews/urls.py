from django.urls import path
from . import views

urlpatterns = [
    path('recommend/', views.recommend),
    path('<int:review_id>/likes/', views.likes),
    path('user/<int:user_id>/', views.get_by_user),
    path('movie/<int:movie_id>/', views.get_create_by_movie),
    path('<int:review_pk>/comments/', views.comments_create),
    path('<int:review_pk>/comments/<int:comment_pk>/', views.comments_delete),
]
