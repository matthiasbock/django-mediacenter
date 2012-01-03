# -*- coding: iso-8859-15 -*-

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response

from Django.mediacenter.models import *

MediaCenterDB = 'django-mediacenter'

def Listing( request ):
	params = {}
	params["Stations"] = Radio.objects.using(MediaCenterDB).all().order_by("frequency")
	return render_to_response("Radio.html", params)

def Icon( request ):
	return HttpResponse( Radio.objects.using(MediaCenterDB).get( id=request.GET.get("ID") ).logo, mimetype="image" )

