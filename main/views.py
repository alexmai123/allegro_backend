from django.shortcuts import render
import os
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from .serializer import MemberSerializer, EventSerializer
from .models import Member, Event

# Create your views here.


def get_members(request):
    f = {}
    if not os.environ.get('SHOW_STAGING'):
        f.update({'staging': False})
    data = MemberSerializer(Member.objects.filter(**f), many=True).data
    return HttpResponse(JSONRenderer().render(data), content_type='application/json')


def get_event(request):
    f = {}
    if not os.environ.get('SHOW_STAGING'):
        f.update({'staging': False})
    data = EventSerializer(Event.objects.filter(**f), many=True).data
    return HttpResponse(JSONRenderer().render(data), content_type='application/json')

