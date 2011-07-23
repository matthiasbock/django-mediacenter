# -*- coding: iso-8859-15 -*-

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response

from Django.globals import *
from Django.mediacenter.models import *

#import FileBase
import httplib, os

def export_title( T ):				# exportiert ein Template-übergebbares Dictionary für diesen Title-Eintrag
	URLs = []
	for URL in Urls.objects.using( MusicBaseDB ).filter( title=T.id ):
#		URLs.append( { "url":URL.url+"&use=cache", "hoster":"Local" } )
		URLs.append( { "url":URL.url, "hoster":URL.url.replace("http://","").replace(".","/").split("/")[1] } )
	for local in Locals.objects.using( MusicBaseDB ).filter( title=T.id ):
		URLs.append( { "url":FileBase.File( ID=local.filebaseid ).FullPath(), "hoster":"FileBase" } )
	Track = T.track
	if Track == 0:
		Track = ""
	return { "id":T.id, "composer":T.composer, "performer":T.performer, "album":T.album, "track":Track, "title":T.title, "URLs":URLs }


def TitleList( request ):
	if request.method == "GET":
		params = {}
		params["Titles"] = []
		for T in Titles.objects.using( MusicBaseDB ).all().order_by('album','track','composer','performer','title'):
			params["Titles"].append( export_title(T) )
		return render_to_response("Music.html", params)
	elif request.method == "POST":
		try:
			Track = int(request.POST.get("Track"))
		except:
			Track = 0
		Titles.objects.using( MusicBaseDB ).create( composer=request.POST.get("Composer"), performer=request.POST.get("Performer"), album=request.POST.get("Album"), track=Track, title=request.POST.get("Title") )
		T = Titles.objects.using( MusicBaseDB ).get( composer=request.POST.get("Composer"), performer=request.POST.get("Performer"), album=request.POST.get("Album"), title=request.POST.get("Title") )
		if request.POST.get("URL") != "":
			Urls.objects.using( MusicBaseDB ).create( title=T.id, url=request.POST.get("URL") )
		return HttpResponseRedirect( "Performer?Name="+request.POST.get("Performer") )


def AddOnlineMusic( request ):

	if request.method == "GET":
		params = {}
		ID = request.GET.get("ID")
		params["Title"] = Titles.objects.using( MusicBaseDB ).get( id=ID )
		return render_to_response("AddOnlineMusic.html", params)

	elif request.method == "POST":
		Urls.objects.using( MusicBaseDB ).create( title=request.POST.get("ID"), url=request.POST.get("URL") )
		return HttpResponseRedirect("Performer?Name="+Titles.objects.using( MusicBaseDB ).get( id=request.POST.get("ID") ).performer)


def LocalMusic( request ):
	#...
	return render_to_response("Search")


def AddLocalMusic( request ):

	if request.method == "GET":
		params = {}
#		ID = request.GET.get("ID") 			blablablabla
#		params["Title"] = Titles.objects.using( MusicBaseDB ).get( id=ID )
		return render_to_response("AddLocal.html", params)

	elif request.method == "POST":
#		Urls.objects.using( MusicBaseDB ).create( title=request.POST.get("ID"), url=request.POST.get("URL") )
		# nur editieren, erzeugt ist es schon
		return HttpResponseRedirect("Performer?Name="+Titles.objects.using( MusicBaseDB ).get( id=request.POST.get("ID") ).performer)


def LocalUpgrade( request ):
	# finde alle Dateien im Verzeichnis, ist ein unbekannter Dateiname/FileSize dabei, MD5 erstellen
	# ist die MD5 bekannt, DB korrigieren, ist die MD5 nicht bekannt -> neuer Eintrag und Edit-Link
	params = {}
	folder = "/home/user/Music"
	params["new"] = []
	for root, dirs, files in os.walk( folder ):
		for name in files:
			fname = os.path.join( root, name )
			fsize = os.path.getsize( fname )
			try:
				Locals.objects.using( MusicBaseDB ).find( filename=fname, filesize=fsize )
			except:
				new = Locals.objects.using( MusicBaseDB ).create( filename=fname, filesize=fsize, md5=largefileMD5(fname) )
				params["new"].append( new.id )
	return render_to_response("NewLocals.html", params)


def PerformerList( request ):

	cols = 6

	params = {}
	Performer = []
	for T in Titles.objects.using( MusicBaseDB ).all().order_by( 'performer' ):
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

	if request.method == "GET":
		try:
			Name = request.GET.get("Name")
		except:
			Name = "None"
		params = {}
		params["Performer"] = Name
		params["Titles"] = []
		for T in Titles.objects.using( MusicBaseDB ).filter( performer=Name ).order_by( 'album','track','composer','title' ):
			params["Titles"].append( export_title(T) )
		return render_to_response("Performer.html", params)

	elif request.method == "POST":						# store new picture to database
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
			Performers.objects.using( MusicBaseDB ).get( name=_Performer ).delete()
		except:
			pass
		Performers.objects.using( MusicBaseDB ).create( name=_Performer, icon=_Picture )
		return HttpResponseRedirect("Performer?Name="+_Performer)


def PerformerIcon( request ):
	try:
		Name = request.GET.get("Name")
	except:
		Name = "None"
	try:
		Icon = Performers.objects.using( MusicBaseDB ).get( name=Name ).icon
		mime = "image/jpeg"
	except:
		Icon = open("/usr/share/icons/gnome/256x256/actions/system-search.png", "r").read()
		mime = "image/png"
	return HttpResponse( Icon, mimetype=mime )


