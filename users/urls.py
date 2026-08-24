from django.urls import path
from .views import users

urlpatterns = [
    path("users/", users, name="user"),
    path("users/<int:id>/", users,name='user1')
]