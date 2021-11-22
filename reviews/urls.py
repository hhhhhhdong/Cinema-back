from django.urls import path
from . import views

urlpatterns = [
    path('recommend/', views.recommend),
    path('<int:review_id>/likes/', views.likes),
    path('user/<int:user_id>/', views.get_by_user),
    path('movie/<int:movie_id>/', views.get_create_by_movie),
    path('<int:review_id>/comments/', views.comments_create),
    path('<int:review_id>/comments/<int:comment_id>/', views.comments_delete),
    path('<int:review_id>/', views.reviews_get_update_delete),
]
