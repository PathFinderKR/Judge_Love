from rest_framework import serializers
from .models import Story

# 사연 시리얼라이저 정의
class StorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = ['id', 'author', 'recipient', 'text', 'response', 'created_at', 'updated_at']
