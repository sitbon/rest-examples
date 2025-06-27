from django.contrib import admin

from .models import Profile
from .models import Note

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """
    Admin interface for the Profile model.
    """
    list_display = ('user', 'bio', 'location', 'birth_date', 'notes_count')
    search_fields = ('user__username', 'bio', 'location', 'notes__title', 'notes__content')
    list_filter = ('birth_date',)
    ordering = ('user__username',)

    def notes_count(self, obj):
        """
        Returns the count of notes associated with the profile.
        """
        return obj.notes.count()

    def get_queryset(self, request):
        """
        Override to include related user data in the queryset.
        """
        return super().get_queryset(request).select_related('user')


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    """
    Admin interface for the Note model.
    """
    list_display = ('title', 'profile', 'created_at', 'updated_at')
    search_fields = ('title', 'content', 'profile__user__username')
    list_filter = ('created_at', 'updated_at')
    ordering = ('-created_at',)

    def get_queryset(self, request):
        """
        Override to include related profile data in the queryset.
        """
        return super().get_queryset(request).select_related('profile')
