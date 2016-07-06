from django.shortcuts import render
from django.contrib.auth.models import User
from models import *

def todo( request ):
    note_list = Note.objects.filter( user__pk = request.user.id ).order_by( '-is_overtimed' ).order_by( 'deadline' )
    context = {
        'note_list': note_list,
    }
    return render( request, 'content.html', context )

def delete( request ):
    try:
        note = Note.objects.get( pk = request.POST[ 'to_delete' ] )
        note.delete()
    except:
        return 1
    return 0

def add( request ):
    return
