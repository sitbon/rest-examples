"""Django management command to generate notes for all users.
"""
from django.core.management.base import BaseCommand

from api.models import Profile, Note

class Command(BaseCommand):
    help = 'Generate notes for all users'

    def add_arguments(self, parser):
        parser.add_argument(
            'count',
            type=int,
            help='Number of notes to generate for each user (default: 1)'
        )

    def handle(self, *args, **kwargs):
        count = kwargs['count']

        profiles = Profile.objects.all()

        for profile in profiles:
            for i in range(count):
                Note.objects.create(
                    profile=profile,
                    title=f"Note {i + 1} for {profile.user.username}",
                    content=f"This is the content of note {i + 1} for user {profile.user.username}."
                )

        self.stdout.write(self.style.SUCCESS('Successfully generated notes for all users.'))
