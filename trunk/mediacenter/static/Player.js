/*
	http://www.w3schools.com/xml/xml_http.asp
	https://developer.mozilla.org/en/JSON
*/

function resolve(URL) {
	xmlHttp = new XMLHttpRequest();
	xmlHttp.open("GET", "/Django/proxy/resolve?URL="+URL, false);
	xmlHttp.send();
	return xmlHttp.responseText;
	}

function extractplayer(URL) {
	xmlHttp = new XMLHttpRequest();
	xmlHttp.open("GET", "/Django/proxy/extractplayer?URL="+URL, false);
	xmlHttp.send();
	return xmlHttp.responseText;
	}

function insertplayer(player) {
	parent.Player.document.getElementById('Player').innerHTML = player;
	}

function play(URL) {
	 insertplayer(	'<object id="MediaPlayer" height="220" width="220" type="application/x-oleobject" standby="Loading Player ...">'
			+ '<embed name="MediaPlayer" type="application/x-mplayer2" src="'+URL+'" pluginspage="http://mplayerplug-in.sourceforge.net/" width="220" height="220" displaysize="0" showstatusbar="1" autosize="0" showpositioncontrols="0" showaudiocontrols="1" showcontrols="true" animationatstart="0" autostart="1" transparentatstart="1" />'
			+ '</object>' );
	}

function stop() {
	document.getElementById('Player').innerHTML = '';
	}
