# -*- coding: iso-8859-15 -*-

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response

from Django.mediacenter.models import *

MediaCenterDB = 'django-mediacenter'

def Listing( request ):
	params = {}
	params["Titles"] = []
	for S in Radio.objects.using(MediaCenterDB).all():
		params["Sender"].append( export_title(S) )
	return render_to_response("Radio.html", params)

def Logo( request ):
	ID = request.GET.get("ID")
	try:
		Icon = DB.objects.using(MediaCenterDB).get( id=ID ).Logo
		mime = "image/jpeg"
	except:
		Icon = open("/var/www/Django/mediacenter/static/system-search.png", "r").read()
		mime = "image/png"
	return HttpResponse( Icon, mimetype=mime )

