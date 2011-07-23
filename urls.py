from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
	(r'^mediacenter/Music/$',			"Django.mediacenter.music.TitleList"),
	(r'^mediacenter/Music/AddOnlineMusic$',		"Django.mediacenter.music.AddOnlineMusic"),
	(r'^mediacenter/Music/LocalMusic$',		"Django.mediacenter.music.LocalMusic"),
	(r'^mediacenter/Music/AddLocalMusic$',		"Django.mediacenter.music.AddLocalMusic"),
	(r'^mediacenter/Music/Performers$',		"Django.mediacenter.music.PerformerList"),
	(r'^mediacenter/Music/Performer$',		"Django.mediacenter.music.Performer"),
	(r'^mediacenter/Music/PerformerIcon$',		"Django.mediacenter.music.PerformerIcon"),
	(r'^mediacenter/Movies/$',			"Django.mediacenter.movies.Listing"),
	(r'^mediacenter/Movies/Icon$',			"Django.mediacenter.movies.Icon"),
	(r'^mediacenter/Movies/Search$',		"Django.mediacenter.movies.Search"),
	(r'^mediacenter/Movies/AddMovie$',		"Django.mediacenter.movies.AddMovie"),
	(r'^mediacenter/Movies/AddStream$',		"Django.mediacenter.movies.AddStream"),
	(r'^mediacenter/static/(?P<path>.*)$',		'django.views.static.serve', {'document_root': '/var/www/Django/mediacenter/static', 'show_indexes': True}),
)

