from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Profile, Note


User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the User model.
    """
    queryset = User.objects.all()

    class Meta:
        model = User
        fields = list({'id', User.USERNAME_FIELD, User.EMAIL_FIELD})
        read_only_fields = fields


class ProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for the Profile model.
    """
    user = serializers.HyperlinkedRelatedField(
        queryset=User.objects.all(),
        view_name='user-detail'
    )

    class Meta:
        model = Profile
        fields = '__all__'
        read_only_fields = ['id']


class NoteSerializer(serializers.ModelSerializer):
    """
    Serializer for the Note model.
    """
    # profile = ProfileSerializer()
    profile = serializers.HyperlinkedRelatedField(
        queryset=Profile.objects.all(),
        view_name='profile-detail'
    )

    class Meta:
        model = Note
        fields = ['id', 'profile', 'title', 'content', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']
