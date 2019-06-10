"""
high level support for doing this and that.
"""
from rest_framework import serializers
from testApp.models import Note

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Note
        fields="__all__"
