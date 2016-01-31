from __future__ import unicode_literals

from django_thumbs.db.models import ImageWithThumbsField
from django.db import models

from app.settings import PIECE_TYPES, SOFTWARE_TYPES

class Piece(models.Model):
	name 		= models.CharField(null=True, blank=True, max_length=50)
	description	= models.CharField(null=True, blank=True, max_length=500)
	piece_type 	= models.CharField(null=True, blank=True, max_length=100)
	image 		= ImageWithThumbsField(upload_to='images', sizes=((200,200)))
	frontpage 	= models.NullBooleanField(default=False, null=True, blank=True)
	software 	= models.ManyToManyField('Software', related_name='software')
	date 		= models.DateField(auto_now=True)

	def __unicode__(self):
		return self.name

class Software(models.Model):
	name 		= models.CharField(null=True, blank=True, max_length=50)
	image 		= ImageWithThumbsField(null=True, blank=True, upload_to='images/software', sizes=((100,100)))
	level 		= models.DecimalField(null=True, blank=True, decimal_places=1, max_digits=3)
	sType		= models.CharField(choices=SOFTWARE_TYPES, null=True, blank=True, max_length=50)

	def __unicode__(self):
		return self.name

class Skill(models.Model):
	name 		= models.CharField(null=True, blank=True, max_length=50)
	image 		= ImageWithThumbsField(null=True, blank=True, upload_to='images/skill', sizes=((100,100)))
	level 		= models.DecimalField(null=True, blank=True, decimal_places=1, max_digits=3)

	def __unicode__(self):
		return self.name
