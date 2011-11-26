# -*- coding: iso-8859-15 -*-

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response

def Playlist(request):
	return render_to_response('Playlist.html')

def Player(request):
	return render_to_response('Player.html')
