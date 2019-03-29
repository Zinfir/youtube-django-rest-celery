from django.views.generic.list import ListView
from videos.serializers import KeyWordSerializer, VideoSerializer
from videos.models import Video, KeyWord
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet


class KeyWordsView(ModelViewSet):
    """KeyWords viewset"""
    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request):
        keywords = KeyWord.objects.all()
        serializer = KeyWordSerializer(KeyWord, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data.get("data")
        serializer = KeyWordSerializer(data=data)

        if serializer.is_valid(raise_exception=True):
            keyword_saved = serializer.save()

        return Response({"success": "Key word {} created successfully".format(keyword_saved.title)})


class VideoView(ModelViewSet):
    """Video viewset"""
    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request):
        key = request.GET.get('key')
        videos = Video.objects.filter(title=key)
        serializer = KeyWordSerializer(KeyWord, many=True)
        return Response(serializer.data)
