from django.urls import path, include
from .views import create_user, get_all_users, get_user, update_user, delete_user, send_email

urlpatterns = [
    path('users/', get_all_users, name='all_users'),
    path('users/create/', create_user, name='create_user'),
    path('users/<int:pk>/', get_user, name='get_user'),
    path('users/<int:pk>/update/', update_user, name='update_user'),
    path('users/<int:pk>/delete/', delete_user, name='delete_user'),
    path('send-email/', send_email, name='send_email'),
]