from django.urls import path
from posts import views

urlpatterns = [
    path("create/", views.PostAPIView.as_view()),
    path("list/", views.PostListAPIView.as_view()),
    path("feed/", views.UserFeedAPIView.as_view()),

    # To get individiual data

    path("list/<int:pk>/", views.PostListAPIDetailedView.as_view()),
    path("like/<int:pk>/", views.PostLikeAPIView.as_view()),
]
