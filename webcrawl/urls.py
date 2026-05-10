from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_search, name='movie_search'),
    path('all_search/', views.movie_all_search, name='movie_all_search'),
    path('qry_search/', views.movie_qry_search, name='movie_qry_search'),
]