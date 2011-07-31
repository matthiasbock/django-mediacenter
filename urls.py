from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
	(r'^MediaCenter/Music/$',			"Django.mediacenter.music.TitleList"),
	(r'^MediaCenter/Music/AddOnlineMusic$',		"Django.mediacenter.music.AddOnlineMusic"),
	(r'^MediaCenter/Music/LocalMusic$',		"Django.mediacenter.music.LocalMusic"),
	(r'^MediaCenter/Music/AddLocalMusic$',		"Django.mediacenter.music.AddLocalMusic"),
	(r'^MediaCenter/Music/Performers$',		"Django.mediacenter.music.PerformerList"),
	(r'^MediaCenter/Music/Performer$',		"Django.mediacenter.music.Performer"),
	(r'^MediaCenter/Music/PerformerIcon$',		"Django.mediacenter.music.PerformerIcon"),
	(r'^MediaCenter/Movies/$',			"Django.mediacenter.movies.Listing"),
	(r'^MediaCenter/Movies/Icon$',			"Django.mediacenter.movies.Icon"),
	(r'^MediaCenter/Movies/Search$',		"Django.mediacenter.movies.Search"),
	(r'^MediaCenter/Movies/AddMovie$',		"Django.mediacenter.movies.AddMovie"),
	(r'^MediaCenter/Movies/AddStream$',		"Django.mediacenter.movies.AddStream"),
	(r'^MediaCenter/static/(?P<path>.*)$',		'django.views.static.serve', {'document_root': '/var/www/Django/mediacenter/static', 'show_indexes': True}),
)

