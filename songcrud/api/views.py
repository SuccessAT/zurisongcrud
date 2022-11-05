from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.db.models import Prefetch
from musicapp.models import Artiste, Song, Lyric
from .serializers import ArtisteSerializer, SongSerializer, LyricSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework import permissions, status, generics, viewsets
# Create your views here.

class SongViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Song.objects.all()
        serial = SongSerializer(queryset, many=True)
        return Response(serial.data)

    def retrieve(self, request, pk=None):
        queryset = Song.objects.all()
        song = get_object_or_404(queryset, pk=pk)
        serial = SongSerializer(song)
        return Response(serial.data)

class ArtisteViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Artiste.objects.all()
        serial = ArtisteSerializer(queryset, many=True)
        return Response(serial.data)

    def retrieve(self, request, pk=None):
        queryset = Artiste.objects.all()
        artiste = get_object_or_404(queryset, pk=pk)
        serial = ArtisteSerializer(artiste)
        return Response(serial.data)

class TryViews(viewsets.ModelViewSet):

    serializer_class = SongSerializer
    queryset = Song.objects.all()

    @action(detail=True, methods=['put'])
    def update_title(self, request, pk=None):
        song = self.get_object()
        serial = SongSerializer(data=request.data)
        if serial.is_valid():
            song.update_title(serial.validated_data['title'])
            song.save()
            return Response({'status': 'title updated'})
        else:
            return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['put'])
    def update_releasedate(self, request, pk=None):
        song = self.get_object()
        serial = SongSerializer(data=request.data)
        if serial.is_valid():
            #song.title(serial.validated_data['title'])
            song.update_releasedate(serial.validated_data['date_released'])
            song.save()
            return Response({'status': 'song details updated'})
        else:
            return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['delete'])
    def delete_song(self, request, pk=None):
        song = self.get_object()
        serial = SongSerializer(data=request.data)
        if serial.is_valid():
            song.delete()
            return Response({'status': 'song deleted'})
        else:
            return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

