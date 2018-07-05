from rest_framework import serializers
from .models import Member, Role, Event
import requests


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ('name')


class MemberSerializer(serializers.ModelSerializer):
    roles = RoleSerializer(many=True)
    class Meta:
        model = Member
        fields = ('name', 'description', 'pro_pic', 'active', 'year', 'section', 'roles')


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('title', 'description', 'created', 'picture', 'staging')
