from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
	(r'^MediaCenter/$',				"Django.mediacenter.music.forward"),

	(r'^MediaCenter/Music/$',			"Django.mediacenter.music.TitleList"),
	(r'^MediaCenter/Music/AddURL$',			"Django.mediacenter.music.AddURL"),
	(r'^MediaCenter/Music/IconListing$',		"Django.mediacenter.music.IconListing"),
	(r'^MediaCenter/Music/Details$',		"Django.mediacenter.music.Details"),
	(r'^MediaCenter/Music/Icon$',			"Django.mediacenter.music.Icon"),
	(r'^MediaCenter/Music/Player$',			"Django.mediacenter.player.index"),

	(r'^MediaCenter/Movies/$',			"Django.mediacenter.movies.Listing"),
	(r'^MediaCenter/Movies/Icon$',			"Django.mediacenter.movies.Icon"),
	(r'^MediaCenter/Movies/Search$',		"Django.mediacenter.movies.Search"),
	(r'^MediaCenter/Movies/AddMovie$',		"Django.mediacenter.movies.AddMovie"),
	(r'^MediaCenter/Movies/AddStream$',		"Django.mediacenter.movies.AddStream"),
	(r'^MediaCenter/static/(?P<path>.*)$',		'django.views.static.serve', {'document_root': '/var/www/Django/mediacenter/static', 'show_indexes': True}),
)

