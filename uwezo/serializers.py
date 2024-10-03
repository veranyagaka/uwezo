# myapp/serializers.py
from rest_framework import serializers
from .models import Relationship, Post, Like, Comment

class RelationshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Relationship
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    likes = serializers.StringRelatedField(many=True, read_only=True)  # Include likes info
    comments = serializers.StringRelatedField(many=True, read_only=True)  # Include comments info

    class Meta:
        model = Post
        fields = '__all__'

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
