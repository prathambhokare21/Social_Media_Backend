from django.urls import path
from comments import views

urlpatterns = [
    path("comment/<int:pk>/", views.CommentAPIView.as_view() ),

    # For List Comment
    path("comments/<int:pk>/", views.CommentsDetailedAPIView.as_view()),
    path("update/<int:pk>/", views.CommentUpdateView.as_view())
]
