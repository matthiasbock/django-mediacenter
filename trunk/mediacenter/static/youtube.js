function GET(url) {
	xmlHttp = new XMLHttpRequest();
	xmlHttp.open("GET", url, false);
	xmlHttp.send();
	return xmlHttp.responseText;
	}

function between(haystack, before, after) {
	p = haystack.indexOf(before);
	if ( p === false ) return '';			// before not found, return empty string
	p += before.length;
	q = haystack.indexOf(after, p);
	if ( q === false ) return haystack.substr(p);	// after not found, return everyting after after
	return haystack.substring(p, q);
	}

function youtube(url) {
	label = document.getElementById('label');
	label.innerHTML = 'GET ...';
	page = GET(url);
	alert(page);
	label.innerHTML = 'Parsing ...';
	object = between(page, '<object', '</object>');
	alert(object);
	player = between(object, 'name="movie" value="', '"');
	alert(player);
	flashvars = between(object, 'name="flashvars" value="', '"').replace('&amp;',"'").split("'");
	alert(flashvars);

	function fmt_stream_map(variable) {
		v = variable.split('&')[0];	// only "url=" is interesting , discard "quality=medium" ...
		urls = unescape(v).substr(4);	// without "url=", only the link!
		return urls;
		}

	label.innerHTML = 'Searching URLs ...';
	values = Array('failed');

	for (i=0; i<flashvars.length; i++) {
		variable = flashvars[i];
		s = variable.split('=');
		key = s[0];
		if (key == 'url_encoded_fmt_stream_map') {
			_values = unescape(s[1]).split(',');
			values = new Array(len(_values));
			for (i=0; i<_values.length; i++) {
				values[i] = fmt_stream_map(_values[i]);
				alert(values[i]);
				}
			}
		}

	return values[0];	// return the first URL in the list
	}

function resolve(url) {
	if ( url.indexOf('youtube.') !== false ) {
		res = youtube(url);
		document.body.innerHTML = '\n<video name=Player id=Player style="width:'+document.body.offsetWidth+'px; height:'+document.body.offsetHeight+'px;" src="'+res+'" autobuffer autoplay controls />\n';
		}
	else	document.body.innerHTML = 'Sorry, hoster not supported';
	}
