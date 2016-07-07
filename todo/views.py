from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse
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

def do_undo( request ):
    if not request.user.is_authenticated():
        return HttpResponse( 'Please log in to perform this action' )
    try:
        note = Note.objects.get( pk = request.POST.get( 'do_undo' ) )
        if 'done' in request.POST.keys():
            note.is_done = True
            note.save()
        elif 'done' not in request.POST.keys():
            note.is_done = False
            note.save()
    except:
        return HttpResponse( 'Something gone wrong!' )
    else:
        return HttpResponse( 0 )
