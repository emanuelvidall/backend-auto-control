from django.urls import path
from .views import UserListCreateView, UserUpdateView, UserDeleteView

urlpatterns = [
  path('users/', UserListCreateView.as_view(), name='user-list-create')
]