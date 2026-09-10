from django.urls import path
from comments import views

urlpatterns = [
    path("Comment/<int:pk>/", views.CommentAPIView.as_view() ),

    # For List Comment
    path("Comments/<int:pk>/", views.CommentsDetailedAPIView.as_view()),
    path("update/<int:pk>/", views.CommentUpdateView.as_view())
]
