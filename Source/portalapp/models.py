from __future__ import unicode_literals
import datetime, os, sys
from PIL import Image
from django.db import models
from django.core.files import File
from django.conf import settings
#from markdown import markdown
from django.utils import timezone
from datetime import datetime
from tinymce.models import HTMLField
from django import forms
#from django.contrib.flatpages.models import FlatPage
from tinymce.widgets import TinyMCE
#from image_cropping import ImageRatioField

class Album(models.Model):
	title = models.CharField(max_length=250)
	date = models.DateTimeField(default=datetime.now)
	image = models.ImageField(upload_to='photos')

	class Meta:
                ordering = ['-date']

	def __str__(self):
		return self.title


class Photo(models.Model):
        title = models.CharField(max_length=250,
                help_text='Maximum 250 characters.', blank=True)
        slug = models.SlugField(unique = True,
                help_text='Suggested value automatically generated from title. Must be unique.', null=True)
        caption = models.TextField(blank=True, max_length=250,
                help_text='An optional summary.')
        date = models.DateTimeField(default=datetime.now)
        image = models.ImageField(upload_to='photos',
                help_text='Maximum resolution 800x600. Larger images will be resized.')
	album = models.ForeignKey(Album)

        class Meta:
                ordering = ['-date']
        def __unicode__(self):
                return self.title


        def get_absolute_url(self):
                return ('thaddeus_photo_detail', (),
                                { 'slug': self.slug })
        get_absolute_url = models.permalink(get_absolute_url)

class Register(models.Model):
    author = models.ForeignKey('auth.User')
    topic = models.CharField(max_length=200)
    abstract = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    speaker = models.CharField(max_length=200)
    venue = models.CharField(max_length=200)
    date_and_time = models.DateTimeField(blank = False,default=datetime.now)
    bio = models.TextField()
    coordinator = models.CharField(max_length=200)
    image = models.ImageField(upload_to='photos',
                help_text='Maximum resolution 800x600. Larger images will be resized.')

    def __str__(self):
        return self.speaker

class PressRelease(models.Model):
	Title = models.CharField(max_length=256)
	summary = models.TextField(blank=True, help_text='A summary for the archive.')
	slug = models.SlugField(unique = True, help_text='Suggested value automatically generated from title. Must be unique.', null=True)
	content = HTMLField()
	#timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	date = models.DateTimeField(default=datetime.now)
	image = models.ImageField(upload_to='coverphotos')

'''    def get_absolute_url(self):
        return ('release_detail', (),
                        { 'slug': self.slug })
    get_absolute_url = models.permalink(get_absolute_url)

    class Meta:
            ordering = ['-date']
    def __unicode__(self):
            return self.Title
'''
class Event(models.Model):
    Title=models.CharField(max_length=256)
    date=models.DateTimeField(default=datetime.now,blank=False)
    venue=models.CharField(max_length=512)
    content=models.TextField()
    image = models.ImageField(upload_to='eventphotos',
            help_text='Can also use garbage images')
	#cropping = ImageRatioField('image', '430x360')
"""class FlatPageForm(forms.ModelForm):
    #fields
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))

    class Meta:
        model = FlatPage
        fields="__all__"
"""
