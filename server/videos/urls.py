from videos.views import KeyWordsView, VideoView
from django.urls import path, re_path

app_name = 'videos'

urlpatterns = [
    re_path(r'^videos/(?P<key>\w+)/$', VideoView.as_view(), name='video_list'),
    path('keywords/', KeyWordsView.as_view(), name='keys'),
]
