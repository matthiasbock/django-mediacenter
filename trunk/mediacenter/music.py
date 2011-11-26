# -*- coding: iso-8859-15 -*-

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response

from Django.mediacenter.models import *

MediaCenterDB = 'django-mediacenter'

def index(request):
	return render_to_response('MediaCenter.html')

def export_title( T ):			# exportiert ein Template-übergebbares Dictionary für diesen Title-Eintrag
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


def TitleList( request ):
	if request.method == "GET":						# return a list of all titles
		params = {}
		params["Titles"] = []
		for T in Titles.objects.using(MediaCenterDB).all().order_by('album','track','composer','performer','title'):
			params["Titles"].append( export_title(T) )
		return render_to_response("Music.html", params)

	elif request.method == "POST":						# add a new title
		try:
			Track = int(request.POST.get("Track"))
		except:
			Track = 0
		Titles.objects.using(MediaCenterDB).create( composer=request.POST.get("Composer"), performer=request.POST.get("Performer"), album=request.POST.get("Album"), track=Track, title=request.POST.get("Title") )
		T = Titles.objects.using(MediaCenterDB).get( composer=request.POST.get("Composer"), performer=request.POST.get("Performer"), album=request.POST.get("Album"), title=request.POST.get("Title") )
		if request.POST.get("URL") != "":
			Urls.objects.using(MediaCenterDB).create( title=T.id, url=request.POST.get("URL") )
		return HttpResponseRedirect("Details?Database=Performers&Name="+request.POST.get("Performer"))


def AddURL( request ):			# POST event from AddURL div
	Urls.objects.using(MediaCenterDB).create( title=request.POST.get("ID"), url=request.POST.get("URL") )
	return HttpResponseRedirect("Details?Database=Performers&Name="+Titles.objects.using(MediaCenterDB).get( id=request.POST.get("ID") ).performer)


def IconListing( request ):
	params = {}

	Database = request.GET.get("Database")
	params['Prefix'] = Database[:-1]		# Composer, Performer, Album
	orderby = params['Prefix'].lower()		# composer, performer, album

	if Database == "Composers":
		params['Title'] = 'Komponisten'
	elif Database == "Performers":
		params['Title'] = 'Künstler'
	elif Database == "Albums":
		params['Title'] = 'Alben'

	cols = 6
	results = []
	for T in Titles.objects.using(MediaCenterDB).all().order_by(orderby):
		if Database == "Composers":
			if T.composer != "" and not T.composer in results:
				results.append( T.composer )
		elif Database == "Performers":
			if T.performer != "" and not T.performer in results:
				results.append( T.performer )
		elif Database == "Albums":
			if T.album != "" and not T.album in results:
				results.append( T.album )

	params["rows"] = []				# arrange as Icons in multiple columns and rows
	col = cols
	for R in results:
		col += 1
		if col > cols:
			col = 1
			params["rows"].append( { "cols":[] } )
		params["rows"][len(params["rows"])-1]["cols"].append(R)

	return render_to_response("IconListing.html", params)


def Details( request ):
	params = {}

	Database = request.GET.get("Database")
	Name = request.GET.get("Name")

	params['Name'] = Name
	params['Prefix'] = Database[:-1]	# Composer, Performer, Album
	params[params['Prefix']] = Name		# Composer=Name, Performer=Name, Album=Name

	if Database == "Composers":
		results = Titles.objects.using(MediaCenterDB).filter( composer=Name )
	elif Database == "Performers":
		results = Titles.objects.using(MediaCenterDB).filter( performer=Name )
	elif Database == "Albums":
		results = Titles.objects.using(MediaCenterDB).filter( album=Name )

	params["Titles"] = []
	for T in results.order_by( 'album','track','composer','title' ):
		params["Titles"].append( export_title(T) )

	return render_to_response("Details.html", params)


def Icon( request ):
	if request.method == "GET":						# pass Icon from DB
		Database = request.GET.get("Database")
		Name = request.GET.get("Name")
		try:
			if Database == "Composers":
				DB = Composers
			elif Database == "Performers":
				DB = Performers
			elif Database == "Albums":
				DB = Albums
			Icon = DB.objects.using(MediaCenterDB).get( name=Name ).icon
			mime = "image/jpeg"
		except:
			Icon = open("/var/www/Django/mediacenter/static/system-search.png", "r").read()
			mime = "image/png"
		return HttpResponse( Icon, mimetype=mime )

	elif request.method == "POST":						# download and store new Icon in DB
		Database	= request.POST.get("Database")
		Name		= request.POST.get("Name")
		URL		= request.POST.get("URL").replace("http://","")
		host		= URL.split("/")[0]
		site		= URL.replace( host, "" )

		connection = httplib.HTTPConnection( host )
		connection.request("GET", site)
		response = connection.getresponse()
		Picture = response.read()
		connection.close()

		if Database == "Composers":
			DB = Composers
		elif Database == "Performers":
			DB = Performers
		elif Database == "Albums":
			DB = Albums

		try:
			DB.objects.using(MediaCenterDB).get( name=Name ).delete()	# delete old Icon, if present
		except:
			pass
		DB.objects.using(MediaCenterDB).create( name=Name, icon=Picture )

		return HttpResponseRedirect("Details?Database="+Database+"&Name="+Name)

