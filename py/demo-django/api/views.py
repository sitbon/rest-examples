from rest_framework import viewsets
from .models import Profile, Note
from .serializers import ProfileSerializer, NoteSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing user profiles.
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def get_queryset(self):
        """
        Override to include related user data in the queryset.
        """
        return super().get_queryset().select_related('user')


class NoteViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing notes.
    """
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def get_queryset(self):
        """
        Override to include related profile data in the queryset.
        """
        return super().get_queryset().select_related('profile')
