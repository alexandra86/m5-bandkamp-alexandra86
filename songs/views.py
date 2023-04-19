from rest_framework.generics import ListCreateAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Song
from .serializers import SongSerializer
from albums.models import Album


class SongView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    serializer_class = SongSerializer
    lookup_url_kwarg = "album_id"

    def get_queryset(self):
        album_id = self.kwargs.get(self.lookup_url_kwarg)
        song = Song.objects.filter(album_id=album_id)
        return song

    def perform_create(self, serializer: SongSerializer):
        album_id = self.kwargs.get(self.lookup_url_kwarg)
        album = Album.objects.get(id=album_id)
        serializer.save(album=album)
