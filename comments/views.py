from django.shortcuts import render
from .serializers import CommentSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Comments
from posts.models import Post
from django.shortcuts import get_object_or_404
from posts.permissions import IsOwnerOrReadOnly
# Create your views here.

# Create Comment
class CommentAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request,pk):
        post = get_object_or_404(Post,pk=pk)
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user, post=post)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#List comments(get)

class CommentsDetailedAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request,pk):
        post = get_object_or_404(Post,pk=pk)
        comment = Comments.objects.filter(post=post)
        serializer = CommentSerializer(comment,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class CommentUpdateView(APIView):
    permission_classes= [IsAuthenticated,IsOwnerOrReadOnly]
    def put(self,request,pk):
        comment = get_object_or_404(Comments,pk=pk)
        self.check_object_permissions(request,comment)
        serializer = CommentSerializer(instance=comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self,request,pk):
        comment = get_object_or_404(Comments, pk=pk)
        self.check_object_permissions(request,comment)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


