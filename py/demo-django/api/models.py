from django.db import models


class Profile(models.Model):
    """
    Model representing a user profile.
    """
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    data = models.JSONField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"


class Note(models.Model):
    """
    Model representing a note, owned by a user profile.
    """
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='notes')
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Note: {self.title} by {self.profile.user.username}"