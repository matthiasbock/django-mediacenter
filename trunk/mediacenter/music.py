# -*- coding: iso-8859-15 -*-

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response

from Django.globals import *
from Django.mediacenter.models import *
from Django.mediacenter.cache import CacheProperties

import httplib


# exportiert ein Template-übergebbares Dictionary für diesen Title-Eintrag

def export_title( T ):
	URLs = []
	for URL in Urls.objects.using(MediaCenterDB).filter( title=T.id ):
#		URLs.append( { "url":URL.url+"&use=cache", "hoster":"Local" } )
		URLs.append( { "url":URL.url, "hoster":URL.url.replace("http://","").replace(".","/").split("/")[1] } )
	for local in Locals.objects.using(MediaCenterDB).filter( title=T.id ):
		URLs.append( { "url":FileBase.File( ID=local.filebaseid ).FullPath(), "hoster":"FileBase" } )
	Track = T.track
	if Track == 0:
		Track = ""
	return { "id":T.id, "composer":T.composer, "performer":T.performer, "album":T.album, "track":Track, "title":T.title, "URLs":URLs }

# end helper functions


def TitleList( request ):
	if request.method == "GET":
		params = {}
		params.update( CacheProperties() )
		params["Titles"] = []
		for T in Titles.objects.using(MediaCenterDB).all().order_by('album','track','composer','performer','title'):
			params["Titles"].append( export_title(T) )
		return render_to_response("Music.html", params)
	elif request.method == "POST":
		try:
			Track = int(request.POST.get("Track"))
		except:
			Track = 0
		Titles.objects.using(MediaCenterDB).create( composer=request.POST.get("Composer"), performer=request.POST.get("Performer"), album=request.POST.get("Album"), track=Track, title=request.POST.get("Title") )
		T = Titles.objects.using(MediaCenterDB).get( composer=request.POST.get("Composer"), performer=request.POST.get("Performer"), album=request.POST.get("Album"), title=request.POST.get("Title") )
		if request.POST.get("URL") != "":
			Urls.objects.using(MediaCenterDB).create( title=T.id, url=request.POST.get("URL") )
		return HttpResponseRedirect( "Performer?Name="+request.POST.get("Performer") )


def AddURL( request ):			# POST event from AddURL div
	Urls.objects.using(MediaCenterDB).create( title=request.POST.get("ID"), url=request.POST.get("URL") )
	return HttpResponseRedirect("Performer?Name="+Titles.objects.using(MediaCenterDB).get( id=request.POST.get("ID") ).performer)


def PerformerList( request ):
	params = {}
	params.update( CacheProperties() )
	cols = 6
	Performer = []
	for T in Titles.objects.using(MediaCenterDB).all().order_by( 'performer' ):
		if not T.performer in Performer and T.performer != "":
			Performer.append( T.performer )
	params["rows"] = []
	col = cols
	for P in Performer:
		col += 1
		if col > cols:
			col = 1
			params["rows"].append( { "cols":[] } )
		params["rows"][len(params["rows"])-1]["cols"].append( P )
	return render_to_response("Performers.html", params)


def Performer( request ):
	try:
		Name = request.GET.get("Name")
	except:
		Name = "None"
	params = {}
	params.update( CacheProperties() )
	params["Performer"] = Name
	params["Titles"] = []
	for T in Titles.objects.using(MediaCenterDB).filter( performer=Name ).order_by( 'album','track','composer','title' ):
		params["Titles"].append( export_title(T) )
	return render_to_response("Performer.html", params)


def PerformerIcon( request ):
	if request.method == "GET":						# pass Performer Icon from DB
		try:
			Name = request.GET.get("Name")
		except:
			Name = "None"
		try:
			Icon = Performers.objects.using(MediaCenterDB).get( name=Name ).icon
			mime = "image/jpeg"
		except:
			Icon = open("/var/www/Django/mediacenter/static/system-search.png", "r").read()
			mime = "image/png"
		return HttpResponse( Icon, mimetype=mime )

	elif request.method == "POST":						# download and store new Performer Icon in DB
		_Performer = request.POST.get("Performer")
		URL = request.POST.get("URL").replace("http://","")
		host = URL.split("/")[0]
		site = URL.replace( host, "" )
		connection = httplib.HTTPConnection( host )
		connection.request("GET", site)
		response = connection.getresponse()
		_Picture = response.read()
		connection.close()
		try:
			Performers.objects.using(MediaCenterDB).get( name=_Performer ).delete()
		except:
			pass
		Performers.objects.using(MediaCenterDB).create( name=_Performer, icon=_Picture )
		return HttpResponseRedirect("Performer?Name="+_Performer)

