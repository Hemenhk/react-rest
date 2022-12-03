from rest_framework import serializers
from .models import Profile

"""
Create serializer and add a Meta class that specifies which fields
can be accessed by the user.
"""


class ProfilesSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Profile
        fields = [
                'id', 'owner', 'created_at', 'updated_at', 'name',
                'content', 'image'
                ]