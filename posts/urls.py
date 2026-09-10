from django.urls import path
from posts import views

urlpatterns = [
    path("create/", views.PostAPIView.as_view()),
    path("List/", views.PostListAPIView.as_view()),
    path("feed/", views.UserFeedAPIView.as_view()),

    # To get individiual data

    path("List/<int:pk>/", views.PostListAPIDetailedView.as_view()),
    path("Like/<int:pk>/", views.PostLikeAPIView.as_view()),
]
