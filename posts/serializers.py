from rest_framework import serializers
from .models import Post
from rest_framework.serializers import ValidationError
from accounts.serializers import UserSerializer

class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only = True)

    class Meta:
        model = Post
        fields = ("id", "caption","image","user", "created_at", "updated_at")

    def validate_caption(self,value):
        if len(value.strip())< 5:
            raise ValidationError(
                "caption must be atleast 5 characters"
            )
        return value

class SimplePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("id", "caption")