from django.shortcuts import render
import os
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from .serializer import MemberSerializer
from .models import Member

# Create your views here.


def get_members(request):
    f = {}
    if not os.environ['SHOW_STAGING']:
        f.update({'staging': False})
    data = MemberSerializer(Member.objects.filter(**f)).data
    return HttpResponse(JSONRenderer().render(data), content_type='application/json')