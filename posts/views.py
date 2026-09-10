from django.shortcuts import render
from .serializers import PostSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Post
from .permissions import IsOwnerOrReadOnly
from django.shortcuts import get_object_or_404
from .pagination import PostPagination
from rest_framework.filters import SearchFilter
from rest_framework.filters import OrderingFilter
# Create your views here.


class PostAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self,request):
        serializer = PostSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save(user = request.user)

            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status= status.HTTP_201_CREATED)

class PostListAPIView(APIView):
    permission_classes = [IsAuthenticated]
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = ['caption']
    ordering_fields = ['id','created_at']
    def get(self,request):
        posts = Post.objects.all()
        search_filter = SearchFilter()
        filter_posts = search_filter.filter_queryset(request,posts,self)
        ordering_filter = OrderingFilter()
        ordering_post = ordering_filter.filter_queryset(request,filter_posts,self)
        paginator= PostPagination()
        page = paginator.paginate_queryset(ordering_post,request)
        serializer= PostSerializer(page, many=True)
        return paginator.get_paginated_response(serializer.data)
    
#Primary key based operation
class PostListAPIDetailedView(APIView):
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    def get(self,request,pk):
        posts = Post.objects.get(pk=pk)
        serializer = PostSerializer(posts)
        return Response(serializer.data)

    def put(self,request,pk):
        posts = Post.objects.get(pk=pk)
        self.check_object_permissions(request,posts)
        serializer = PostSerializer(posts, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        posts = Post.objects.get(pk=pk)
        self.check_object_permissions(request,posts)
        print(request.user)
        if request.user != posts.user:
            return Response({"message": "You are not allowed to delete this post."}, status=status.HTTP_403_FORBIDDEN)
        
        posts.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PostLikeAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request,pk):
        posts = get_object_or_404(Post, pk=pk)
        if posts.likes.filter(id= request.user.id).exists():
            posts.likes.remove(request.user)
            return Response({"message": "Post unliked successfully"}, status=status.HTTP_200_OK)
        else:
            posts.likes.add(request.user)

            return Response({"message": "Post liked successfully"}, status=status.HTTP_200_OK)
    

#UserFeed

class UserFeedAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        following_users = request.user.following.all()
        posts = Post.objects.filter(user__in =following_users)
        serializer = PostSerializer(posts,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)