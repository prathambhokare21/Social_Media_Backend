from django.shortcuts import render
from .serializers import RegistartionSerializer,LoginSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from .models import User
from django.shortcuts import get_object_or_404
from rest_framework import status
# Create your views here.

class RegistrationAPIView(APIView):
    def post(self,request):
        serializer = RegistartionSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
class LoginAPIView(APIView):
    def post(self,request):
        serializer = LoginSerializer(data = request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            user = authenticate(username=username,password=password)

            if user:
                refresh = RefreshToken.for_user(user)
                access = refresh.access_token
                return Response({'refresh':str(refresh), 'access':str(access)},status=status.HTTP_200_OK)
            else:
                return Response({"message":"Invalid_Credentials"}, status=status.HTTP_401_UNAUTHORIZED)
            
class ProfileAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        return Response({"username":request.user.username}, status=status.HTTP_200_OK)

class FollowAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request,user_id):
        user_to_follow = get_object_or_404(User,id=user_id)

        if request.user == user_to_follow:
            return Response(
                {"message": "You cannot follow yourself"},
                status=status.HTTP_400_BAD_REQUEST
            )
        if request.user.following.filter(id=user_to_follow.id).exists():
            return Response(
                {"message": "You are already following this user"},
                status=status.HTTP_400_BAD_REQUEST
            )
        request.user.following.add(user_to_follow)

        return Response(
            {"message": "User followed successfully"},
            status=status.HTTP_200_OK
    )

class UnfollowAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, user_id):
        user_to_unfollow = get_object_or_404(User, id=user_id)

        if request.user == user_to_unfollow:
            return Response(
                {"message": "You cannot unfollow yourself"},
                status=status.HTTP_400_BAD_REQUEST
            )

        if not request.user.following.filter(id=user_to_unfollow.id).exists():
            return Response(
                {"message": "You are not following this user"},
                status=status.HTTP_400_BAD_REQUEST
            )

        request.user.following.remove(user_to_unfollow)

        return Response(
            {"message": "User unfollowed successfully"},
            status=status.HTTP_200_OK
        )