from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.shortcuts import get_object_or_404, render_to_response
import json

def root(request):
    print "voodoo"
    return render_to_response('light.html')
