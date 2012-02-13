# -*- coding: iso-8859-15 -*-

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response

def Playlist(request):
	return render_to_response('Playlist.html')

#	 e.g. http://video-js.zencoder.com/oceans-clip.ogv
#	return '<video name=Player id=Player style="width:320px; height:180px;" src="'+URL+'" autobuffer autoplay controls />'

"""
	 insertplayer(	'<object id="MediaPlayer" height="220" width="220" type="application/x-oleobject" standby="Loading Player ...">'
			+ '<embed name="MediaPlayer" type="application/x-mplayer2" src="'+URL+'" pluginspage="http://mplayerplug-in.sourceforge.net/" width="220" height="220" displaysize="0" showstatusbar="1" autosize="0" showpositioncontrols="0" showaudiocontrols="1" showcontrols="true" animationatstart="0" autostart="1" transparentatstart="1" />'
			+ '</object>' );
"""

def Player(request):
	params = {}
	if 'Link' in request.GET.keys():
		params['Link'] = request.GET.get('Link')
	return render_to_response('Player.html', params)

