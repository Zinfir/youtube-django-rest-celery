from videos.models import KeyWord, Video
from rest_framework import serializers


class KeyWordSerializer(serializers.ModelSerializer):
    """Key word serializer"""

    class Meta:
        model = KeyWord
        fields = ('created_on', 'updated_on', 'title', 'description')

    def create(self, validated_data):
         return KeyWord.objects.create(**validated_data)


class VideoSerializer(serializers.ModelSerializer):
    """Video serializer"""

    class Meta:
        model = Video
        fields = ('created_on', 'updated_on', 'title', 'link', 'key', 'description')