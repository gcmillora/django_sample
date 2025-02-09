from django.urls import path
from .views.repository import RepositoryApiView, RepositoryDetailApiView
from .views.user import UserView

urlpatterns = [
    path("repository/", RepositoryApiView.as_view()),
    path("repository/<str:name>", RepositoryDetailApiView.as_view()),
    path("user/", UserView.as_view()),
]
