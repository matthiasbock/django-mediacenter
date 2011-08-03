# -*- coding: iso-8859-15 -*-

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response

from Django.globals import *
from Django.mediacenter.models import *

import httplib, os

CacheFolder = "/var/www/Django/proxy/cache"


def CacheProperties():
	Cached = os.listdir(CacheFolder)
	titles = len(Cached)
	size = 0
	for f in Cached:
		size += os.path.getsize(CacheFolder+"/"+f)
	size = size/1024/1024	# size in MB
	return {'CachedTitles':titles, 'CachedSize':size}


def ClearCache( request ):
	# delete all files in CacheFolder
	return HttpResponse("Cache cleared.", "text/html")


def SetupCache( request ):
	Use = request.GET.__contains__("Use")
	Expires = request.GET.get("Expires")
	return HttpResponse("Cache set up.", "text/html")

