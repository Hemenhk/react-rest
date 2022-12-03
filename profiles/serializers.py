from rest_framework import serializers
from .models import Profile

"""
Create serializer and add a Meta class that specifies which fields
can be accessed by the user.
"""


class ProfilesSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Profile
        fields = [
                'id', 'owner', 'created_at', 'updated_at', 'name',
                'content', 'image', 'is_owner'
                ]