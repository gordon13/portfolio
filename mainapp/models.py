from __future__ import unicode_literals

from django_thumbs.db.models import ImageWithThumbsField
from django.db import models

from app.settings import PIECE_TYPES

class Piece(models.Model):
	piece_type 	= models.CharField(null=True, blank=True, max_length=100)
	image 		= ImageWithThumbsField(upload_to='images', sizes=((200,200)))
	frontpage 	= models.NullBooleanField(default=False, null=True, blank=True)
	date 		= models.DateField(auto_now=True)

class Software(models.Model):
	name 		= models.CharField(null=True, blank=True, max_length=50)
	level 		= models.DecimalField(null=True, blank=True, decimal_places=1, max_digits=3)

