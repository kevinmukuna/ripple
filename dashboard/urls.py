from django.urls import path
from . import views

urlpatterns = [
    path('delete_user', views.deleteUser, name='delete-user'),
    path('user_delete', views.confirmDeleteUser, name='confirm-delete-user')
]
