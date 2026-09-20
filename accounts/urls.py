from django.urls import path
from accounts import views
urlpatterns = [
    path('register/', views.RegistrationAPIView.as_view()),
    path('login/', views.LoginAPIView.as_view()),
    path('profile/', views.ProfileAPIView.as_view()),
    path('follow/<int:user_id>/', views.FollowAPIView.as_view()),
    path('unfollow/<int:user_id>/', views.UnfollowAPIView.as_view()),
]