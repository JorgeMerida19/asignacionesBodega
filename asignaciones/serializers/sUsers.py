from django.contrib.auth.models import User, Group
from django.db.models import fields
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        fields = ['url', 'usarname', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields['url', 'name']