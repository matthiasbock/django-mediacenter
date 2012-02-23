#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

def resolver():
	import shared
	r = shared.r
	r.GET(shared.URL)

	from htmlparser import between
	s = shared.URL.split("/")
	MyVideoID = s[len(s)-2]
	img_src = between(r.Page, "<img id='i"+MyVideoID+"' src='", "'").replace("http://","")
	folder = "/".join( img_src.split("/")[1:4] )
	shared.URL = "http://is3.myvideo.de/"+folder+"/"+MyVideoID+".flv"

def straddle(page):
	from htmlparser import straddle as replace_content
	return replace_content(page, "<div id='player_container'>")

if __name__ == "__main__":
	from retrieve import main
	main()

