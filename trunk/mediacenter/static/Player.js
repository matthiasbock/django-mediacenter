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

function play(URL) {
	link = resolve(URL);
	parent.Player.document.getElementById('Player').innerHTML = '<embed id=embed src="'+link+'" onload="embedLoaded();" type="application/x-mplayer2"><\/embed><small>'+link;
	}

function stop() {
	document.getElementById('Player').innerHTML = '';
	}
