# -*- coding: iso-8859-15 -*-

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response

from Django.mediacenter.models import *

import httplib, os

MediaCenterDB = 'django-mediacenter'
CacheFolder = "/var/www/Django/mediacenter/cache"


def CacheProperties():
	try:					# Use Cache ?
		use = (Settings.objects.using(MediaCenterDB).get(property="UseCache") == "True")
	except:
		use = True
	if use:
		use = "checked";

	try:					# Cache expires after x days
		expires = int(Settings.objects.using(MediaCenterDB).get(property="CacheExpires"))
	except:
		expires = 14

	Cached = os.listdir(CacheFolder)
	titles = len(Cached)			# number of files in Cache Folder

	size = 0
	for f in Cached:			# add up size of all files
		size += os.path.getsize(CacheFolder+"/"+f)
	size = size/1024/1024			# size in MB

	return {'UseCache':use, 'CacheExpires':expires, 'CachedTitles':titles, 'CachedSize':size}


def ClearCache( request ):
	# delete all files in CacheFolder
	return HttpResponse("Cache cleared.", "text/html")


def SetupCache( request ):

	def setup(p, v):
		try:
			for PreviousSetting in Settings.objects.using(MediaCenterDB).filter(property=p):
				PreviousSetting.delete()
		except:
			pass
		Settings.objects.using(MediaCenterDB).create(property=p, value=str(v))

	setup("UseCache", request.GET.__contains__("Use"))
	setup("CacheExpires", request.GET.get("Expires"))

	return HttpResponse("Cache set up.", "text/html")

