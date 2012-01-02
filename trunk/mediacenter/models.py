# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models

class Albums(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    name = models.CharField(max_length=300, db_column='Name') # Field name made lowercase.
    icon = models.TextField(db_column='Icon', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'Albums'

class Composers(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    name = models.CharField(max_length=300, db_column='Name') # Field name made lowercase.
    icon = models.TextField(db_column='Icon', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'Composers'

class Movies(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    original = models.CharField(max_length=300, db_column='Original') # Field name made lowercase.
    german = models.CharField(max_length=300, db_column='German') # Field name made lowercase.
    year = models.IntegerField(null=True, db_column='Year', blank=True) # Field name made lowercase.
    icon = models.TextField(db_column='Icon', blank=True) # Field name made lowercase.
    rating = models.CharField(max_length=300, db_column='Rating', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'Movies'

class Online(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    title = models.IntegerField(null=True, db_column='Title', blank=True) # Field name made lowercase.
    link = models.CharField(max_length=900, db_column='Link') # Field name made lowercase.
    class Meta:
        db_table = u'Online'

class Performers(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    name = models.CharField(max_length=300, db_column='Name') # Field name made lowercase.
    icon = models.TextField(db_column='Icon', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'Performers'

class Radio(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    name = models.CharField(max_length=90, db_column='Name') # Field name made lowercase.
    logo = models.TextField(db_column='Logo', blank=True) # Field name made lowercase.
    frequency = models.DecimalField(decimal_places=1, null=True, max_digits=5, db_column='Frequency', blank=True) # Field name made lowercase.
    stream = models.CharField(max_length=900, db_column='Stream', blank=True) # Field name made lowercase.
    playlist = models.CharField(max_length=900, db_column='Playlist', blank=True) # Field name made lowercase.
    homepage = models.CharField(max_length=900, db_column='Homepage', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'Radio'

class Titles(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    composer = models.CharField(max_length=300, db_column='Composer') # Field name made lowercase.
    performer = models.CharField(max_length=300, db_column='Performer') # Field name made lowercase.
    album = models.CharField(max_length=300, db_column='Album') # Field name made lowercase.
    track = models.IntegerField(db_column='Track') # Field name made lowercase.
    title = models.CharField(max_length=300, db_column='Title') # Field name made lowercase.
    class Meta:
        db_table = u'Titles'

