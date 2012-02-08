# -*- coding: iso-8859-15 -*-

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response

from Django.mediacenter.models import *

MediaCenterDB = 'django-mediacenter'

# http://imdbpy.sourceforge.net/?page=docs
import httplib, os, imdb
from operator import itemgetter

def Listing( request ):
	cols = 4
	params = {}
	params["rows"] = []
	col = cols
	for M in Movies.objects.using(MediaCenterDB).all().order_by("original_title"):
		col += 1
		if col > cols:
			col = 1
			params["rows"].append( [] )
		params["rows"][len(params["rows"])-1].append( M )
	return render_to_response("Movies.html", params)


def Icon( request ):
	try:
		Icon = Movies.objects.using(MediaCenterDB).get( id=request.GET.get("ID") ).icon
		mime = "image/jpeg"
	except:
		Icon = open("/usr/share/icons/gnome/256x256/actions/system-search.png", "r").read()
		mime = "image/png"
	return HttpResponse( Icon, mimetype=mime )


def Search( request ):
	params = {}
	query = request.GET.get("query")

	ia = imdb.IMDb()
	params["movies"] = []
	for item in ia.search_movie( query ):
		original = item['title']
		german = ''
		if 'akas' in item.data:
			for aka in item.data['akas']:
				if aka.find("Germany (imdb display title)") > -1:
					german = aka.split(":")[0]
		params["movies"].append( {'original':original.encode('ascii'), 'german':german, 'year':item.data['year'], 'movieID':item.movieID} )

	get = itemgetter('year')			# sort by column "year"
	params["movies"].sort( key=get, reverse=True )

	params["pictures"] = GooglePictures( query+' movie' ).Links[:6]

	return render_to_response("SearchMovie.html", params)


def AddMovie( request ):

	if request.POST.get("URL") is not None and request.POST.get("URL") != "":
		URL = request.POST.get("URL").replace("http://","")
		host = URL.split("/")[0]
		site = URL.replace( host, "" )
		connection = httplib.HTTPConnection( host )
		connection.request("GET", site)
		Picture = connection.getresponse().read()
		connection.close()
	else:
		Picture = None

	Movies.objects.using(MediaCenterDB).create( original_title=request.POST.get("Original"), german_title=request.POST.get("German"), year=request.POST.get("Year"), icon=Picture )
	return HttpResponseRedirect(".")


def AddStream( request ):

	if request.method == "GET":
		params = {}
		ID = request.GET.get("ID")
		params["Title"] = Movies.objects.using(MediaCenterDB).get( id=ID )
		return render_to_response("AddURL.html", params)

	elif request.method == "POST":
		Streams.objects.using(MediaCenterDB).create( title=request.POST.get("ID"), url=request.POST.get("URL") )
		return HttpResponseRedirect(".")


