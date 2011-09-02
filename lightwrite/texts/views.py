from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.shortcuts import get_object_or_404, render_to_response
from django.core import serializers

from lightwrite.texts.models import Text, TextForm

import json
import random
import string 

def root(request):
    wash = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(9))
    return HttpResponseRedirect('/' + wash) 

def write(request, wash):
    return render_to_response('light.html', {'wash': wash,})

def json_get_text(request, wash):
    t = Text.objects.filter(wash=wash)
    if (len(t)==0):
        t = Text(wash=wash)
        t.text = '\n\nWelcome to LightWrite!\nby Gun.io\n\nLightWrite is a web-based clone of WriteRoom - it\'s a place to write your thoughts without any distractions.\n\nTo use LightWrite, just start typing! You can move your mouse over the bottom of the page to save your text or export to a file. \n\nTo enter fullscreen mode, just press F11.'
        t.save() 
    data = serializers.serialize("json", t)
    return HttpResponse(data, mimetype='application/json')
