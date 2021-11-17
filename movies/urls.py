from django.urls import path
from . import views


urlpatterns = [
    # path('', views.index, name='index'),
    path('loaddata/', views.loaddata),
    path('loaddata2/', views.loaddata2),
]
