# -*- coding: iso-8859-15 -*-

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response

def Playlist(request):
	return render_to_response('Playlist.html')

def resolve(url):
	from urlparser import splitURL
	Protocol, Host, Site = splitURL(url)
	s = Host.split(".")
	domain = '.'.join(s[len(s)-2:]).lower()
	middle = s[len(s)-2]

	from robot import Robot
	import shared
	shared.r = Robot()
	shared.URL = url
	shared.filename = ""
	resolver = __import__(middle).resolver
	resolver()
	return shared.URL

def embed(URL):
	return '<video src="'+URL+'" style="width: 100%; height=100%;" autobuffer=1 autoplay=1 controls=1 />'
#	return '<object type="application/x-oleobject" standby="Loading Player ...">' \
#		+ '<embed type="application/x-mplayer2" src="'+URL+'" pluginspage="http://mplayerplug-in.sourceforge.net/" displaysize="1" showstatusbar="1" autosize="1" showpositioncontrols="1" showaudiocontrols="1" showcontrols="1" animationatstart="1" transparentatstart="0" autostart="1" />' \
#		+ '</object>'

def Player(request):
	params = {}
	if 'Link' in request.GET.keys():
		params['Link'] = request.GET.get('Link')
		params['Player'] = embed(resolve(params['Link']))
	return render_to_response('Player.html', params)

def GetDirectLink(request):
	return HttpResponse(resolve(request.GET.get('url')))

