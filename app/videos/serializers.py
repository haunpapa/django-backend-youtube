from rest_framework import serializers
from .models import Video
from users.serializers import UserSerializer
from comments.serializers import CommentSerializer

class VideoListSerializer(serializers.ModelSerializer):

    user = UserSerializer(read_only=True) # Video(FK)

    class Meta:
        model = Video
        fields = '__all__'


class VideoDetailSerializer(serializers.ModelSerializer):

    user = UserSerializer(read_only=True) # Video(FK)

    comment_set = CommentSerializer(read_only=True, many=True)

    class Meta:
        model = Video
        fields = '__all__'