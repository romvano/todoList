from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import date, timedelta, datetime

class Profile( models.Model ):
    user = models.OneToOneField( User )
    def __str__( self ):
        return self.user.username

class Note( models.Model ):
    user = models.ForeignKey( User, null = False )
    text = models.TextField( 'Text', null = False, blank = False )
    deadline = models.DateTimeField( 'Deadline', default=timezone.now() )#+ timedelta( 1 ) )
    is_done = models.BooleanField( 'Is Done', default = False )
    def is_overtimed( self ):
        return self.deadline >= timezone.make_aware( datetime.now(), timezone.get_default_timezone() )
    def __str__( self ):
        return self.text
