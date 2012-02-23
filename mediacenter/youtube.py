#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

def resolver():
	import shared
	r = shared.r
	r.GET(shared.URL)

	from htmlparser import between, unescape
	from urllib import unquote

	shared.filename = between(r.Page, '<title>', '</title>')+'.flv'
	watch = between(r.Page, '<object', '</object>', include=True).replace('>','>\n')
	player = between(watch, 'name="movie" value="', '"')
	flashvars = between(watch, 'name="flashvars" value="', '"')

	def fmt_stream_map(var):
		v = var.split('&')[0]	# first parameter, discard "quality=medium" etc.
		urls = unquote(v)[4:]	# without "url="
		return urls

	_flashvars = flashvars.replace('&amp;',"'").split("'")
	for var in _flashvars:
		s = var.split('=')
		key = s[0]
		if key == 'url_encoded_fmt_stream_map':		# that's the interesting part
			_values = unquote(s[1]).split(',')
			values = [fmt_stream_map(_values[i]) for i in range(len(_values))]
			print str(len(values))+' URLs:\n'+str(values)

	try:
		shared.URL = values[0]		# get the first URL in the list
	except:
		shared.URL = ''

def straddle(page):
	from htmlparser import straddle as replace_content
	return replace_content(page, '<div id="watch-video-container">')

if __name__ == "__main__":
	from retrieve import main
	main()

