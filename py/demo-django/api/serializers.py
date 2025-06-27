from rest_framework import serializers
from .models import Profile, Note


class ProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for the Profile model.
    """
    class Meta:
        model = Profile
        fields = '__all__'
        read_only_fields = ['id', 'user']


class NoteSerializer(serializers.ModelSerializer):
    """
    Serializer for the Note model.
    """
    profile = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Note
        fields = '__all__'
        read_only_fields = ['id', 'profile', 'created_at', 'updated_at']
