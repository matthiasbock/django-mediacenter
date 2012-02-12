# -*- coding: iso-8859-15 -*-

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response

def Playlist(request):
	return render_to_response('Playlist.html')

def HTML5_Player(URL):
	# e.g. http://video-js.zencoder.com/oceans-clip.ogv
	return '<video name=Player id=Player src="'+URL+'" autobuffer autoplay controls />'

def Player(request):
	params = {}
	if 'Link' in request.GET.keys():
		params['Link'] = request.GET.get('Link')
	return render_to_response('Player.html', params)
