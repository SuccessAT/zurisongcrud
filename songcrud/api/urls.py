from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'songs', SongViewSet, basename='song')
router.register(r'songlist', TryViews, basename='songList')
router.register(r'artistes', ArtisteViewSet, basename='artiste')

urlpatterns = router.urls
