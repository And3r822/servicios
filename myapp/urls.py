from django.urls import path
from . import views  # Importa todas las vistas desde el directorio actual

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('', views.home, name='home'),  # Define tu vista home
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logout_view, name='logout'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
]