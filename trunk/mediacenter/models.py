# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models

class ComposerIcons(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    name = models.CharField(max_length=300, db_column='Name') # Field name made lowercase.
    icon = models.TextField(db_column='Icon', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'Composer_Icons'

class Movies(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    imdb_id = models.IntegerField(null=True, db_column='IMDB_ID', blank=True) # Field name made lowercase.
    original_title = models.CharField(max_length=300, db_column='Original_Title') # Field name made lowercase.
    german_title = models.CharField(max_length=300, db_column='German_Title') # Field name made lowercase.
    year = models.IntegerField(null=True, db_column='Year', blank=True) # Field name made lowercase.
    icon = models.TextField(db_column='Icon', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'Movies'

class PerformerIcons(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    name = models.CharField(max_length=300, db_column='Name') # Field name made lowercase.
    icon = models.TextField(db_column='Icon', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'Performer_Icons'

class Playlists(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    name = models.CharField(max_length=300, db_column='Name') # Field name made lowercase.
    is_album = models.IntegerField(db_column='Is_Album') # Field name made lowercase.
    icon = models.TextField(db_column='Icon', blank=True) # Field name made lowercase.
    titles = models.TextField(db_column='Titles', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'Playlists'

class RadioStreams(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    name = models.CharField(max_length=90, db_column='Name') # Field name made lowercase.
    logo = models.TextField(db_column='Logo', blank=True) # Field name made lowercase.
    frequency = models.DecimalField(decimal_places=1, null=True, max_digits=6, db_column='Frequency', blank=True) # Field name made lowercase.
    stream = models.CharField(max_length=900, db_column='Stream', blank=True) # Field name made lowercase.
    playlist = models.CharField(max_length=900, db_column='Playlist', blank=True) # Field name made lowercase.
    homepage = models.CharField(max_length=900, db_column='Homepage', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'Radio_Streams'

class TitleStreams(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    title = models.IntegerField(null=True, db_column='Title', blank=True) # Field name made lowercase.
    link = models.CharField(max_length=900, db_column='Link') # Field name made lowercase.
    heading = models.CharField(max_length=300, db_column='Heading') # Field name made lowercase.
    preview = models.TextField(db_column='Preview', blank=True) # Field name made lowercase.
    played = models.IntegerField(db_column='Played') # Field name made lowercase.
    class Meta:
        db_table = u'Title_Streams'

class Titles(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    composer = models.CharField(max_length=300, db_column='Composer') # Field name made lowercase.
    performer = models.CharField(max_length=300, db_column='Performer') # Field name made lowercase.
    title = models.CharField(max_length=300, db_column='Title') # Field name made lowercase.
    played = models.IntegerField(db_column='Played') # Field name made lowercase.
    class Meta:
        db_table = u'Titles'

