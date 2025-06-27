#!/usr/bin/env python3
"""Client for Django foo-demo.
"""
from functools import cache

import niquests
import urllib


BASE_URL = 'http://localhost:8000/api'

PROFILES_URL = f'{BASE_URL}/profiles'
NOTES_URL = f'{BASE_URL}/notes'


def get_profiles():
    """Get Profiles as JSON."""
    response = niquests.get(PROFILES_URL)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f'Error fetching profiles: {response.status_code} - {response.text}')


def get_profile(profile_id):
    """Get a single Profile by ID."""
    response = niquests.get(f'{PROFILES_URL}/{profile_id}')
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f'Error fetching profile {profile_id}: {response.status_code} - {response.text}')


def get_notes():
    """Get Notes as JSON."""
    response = niquests.get(NOTES_URL)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f'Error fetching notes: {response.status_code} - {response.text}')


def get_notes_by_profile(profile_id):
    """Get Notes for a specific Profile."""
    response = niquests.get(f'{NOTES_URL}?profile={profile_id}')
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f'Error fetching notes for profile {profile_id}: {response.status_code} - {response.text}')


@cache
def username_from_url(url):
    if url:
        user_response = niquests.get(url)
        if user_response.status_code == 200:
            return user_response.json().get('username', 'Unknown')

    return 'Unknown'


def main():
    profiles = get_profiles()

    print(f"{len(profiles.get('results', []))} Profile(s):")

    for profile in profiles.get('results', []):
        print(f"ID: {profile['id']}, User: {username_from_url(profile.get('user'))}, Bio: {profile['bio']}")

    profile_id = profiles['results'][0]['id'] if profiles.get('results') else None

    if profile_id:
        profile = get_profile(profile_id)
        username = username_from_url(profile.get('user'))

        print(f"\nProfile Details for ID {profile_id}:")
        print(f"User: {username}, Bio: {profile['bio']}, Location: {profile['location']}, Birth Date: {profile['birth_date']}")

        notes = get_notes_by_profile(profile_id)
        count = notes.get('count', 0)

        if count > 0:
            print(f"[{len(notes['results'])}/{count}] Notes for Profile ID {profile_id}:")
        else:
            print(f"\n{len(notes['results'])} Notes for Profile ID {profile_id}:")

        for note in notes.get('results', []):
            print(f"Title: {note['title']}, Content: {note['content']}, Created At: {note['created_at']}")


if __name__ == '__main__':
    main()
