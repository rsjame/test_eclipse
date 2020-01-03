from django.shortcuts import render_to_response
from learn2.models import Eploee

def index(req):
    emp=Eploee.objects.all()
    return render_to_response('index.html',locals())