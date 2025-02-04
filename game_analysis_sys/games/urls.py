from django.urls import path
from . import views  # Import views from the current directory

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('add-user/', views.add_user, name='add_user'),  # Add user page
    path('games/', views.game_records, name='game_records'),  # Game records
    path('points/', views.points_records, name='point_records'),  # Point records
]
