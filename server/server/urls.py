from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from videos.views import KeyWordsView, VideoView
from django.contrib import admin

router = DefaultRouter()
router.register('videos', VideoView)
router.register('keywords', KeyWordsView)

urlpatterns = [
    path('api/', include((router.urls, 'videos'), namespace='api')),
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]
