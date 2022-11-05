from rest_framework import serializers
from musicapp.models import Artiste, Song, Lyric
#from rest_framework.response import Response
#from rest_framework.views import APIView
import pysnooper


class LyricSerializer(serializers.ModelSerializer):
    
    #song = serializers.StringRelatedField()
    

    class Meta:
        model = Lyric
        fields = ('song_id', 'content')

class SongSerializer(serializers.ModelSerializer):
    
    #artiste = serializers.StringRelatedField()
    #lyric = LyricSerializer(many=True, required=False)

    class Meta:
        model = Song
        fields = ('title', 'date_released', 'likes', 'artiste_id')

class ArtisteSerializer(serializers.ModelSerializer):
    
    #song = SongSerializer(many=True, required=False)
    
    class Meta:
        model = Artiste
        fields = ('id', 'first_name', 'last_name', 'age')