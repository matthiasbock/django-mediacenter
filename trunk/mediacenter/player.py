# -*- coding: iso-8859-15 -*-

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response

def Playlist(request):
	return render_to_response('Playlist.html')

def getVideoURL(url):
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

def embed_HTML5(URL):
	return '<audio src="'+URL+'" style="width: 100%; height=100%;" autobuffer=1 autoplay=1 controls=1 />'

def embed_object(URL):
	return '<object standby="Loading Player ..." data="'+URL+'" type="application/x-mplayer2"></object>'
#	return '<object type="application/x-oleobject" standby="Loading Player ...">' \
#		+ '<embed type="application/x-mplayer2" src="'+URL+'" pluginspage="http://mplayerplug-in.sourceforge.net/" displaysize="1" showstatusbar="1" autosize="1" showpositioncontrols="1" showaudiocontrols="1" showcontrols="1" animationatstart="1" transparentatstart="0" autostart="1" />' \
#		+ '</object>'

def ResourceCached(URL):
	# query database
	return

def StartATjob(cmd):
	from subprocess import Popen, PIPE
	filename = '/tmp/atjob'
	open(filename, 'w').write(cmd)
	p = Popen('at now + 1 min -f '+filename).wait()

def LoadToCache(URL, DirectLink):
	StartATjob('cd /tmp\nwget ...')
	#...

def LoadFromCache(request):
	resource = request.GET.get('resource')
	#...
	#File from database
	File = None
	return File

def Player(request):
	params = {}
	if 'Link' in request.GET.keys():
		params['Link'] = request.GET.get('Link')
		if True in [key in params['Link'] for key in ['youtube', 'myvideo']]:
#			URL = ResourceCached(params['Link'])
#			if URL is None:
			URL = getVideoURL(params['Link'])
#				LoadToCache(params['Link'], URL)
#			else:
#				URL = 'LoadFromCache?resource='+params['Link']
			params['Player'] = embed_HTML5(URL)
		else:
			params['Player'] = embed_object(params['Link'])
	return render_to_response('Player.html', params)


