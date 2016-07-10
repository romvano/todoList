from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from datetime import date, timedelta, datetime
from models import *

def todo( request ):
    note_list = Note.objects.filter( user__pk = request.user.id ).order_by( '-is_overtimed' ).order_by( 'deadline' )
    context = {
        'note_list': note_list,
    }
    for n in note_list:
        print n.is_overtimed()
    return render( request, 'content.html', context )

def perform( action ):
    def improved_action( request ):
        try:
            if not request.user.is_authenticated():
                raise PermissionDenied
            note = Note.objects.get( pk = request.POST.get( 'pk' ) )
            if note.user.username != request.user.username:
                raise PermissionDenied
            action( request, note )
        except PermissionDenied:
            return HttpResponse( 'Permission denied!' )
        except:
            return HttpResponse( 'Something gone wrong!' )
        else:
            return HttpResponse( 0 )
    return improved_action

@login_required
def add( request ):
    try:
        text = request.POST[ 'note_text' ]
        if text == '':
            return HttpResponse( 'The note is empty' )
        deadline = datetime( 1, 1, 1 )
        try:
            deadline = datetime( request.POST[ 'deadline' ] )
        except:
            deadline = None
        note = Note( text=text, deadline=dealine, user = request.user )
        note.save()
    except:
        return HttpResponse( 'Error!' )
    else:
        return HttpResponse( { 'code': 0, 'text': text, 'deadline': deadline } )

def add_nojs( request ):
    add( request )
    return redirect( 'todo' )

@perform
def delete( request, note ):
    note.delete()

def delete_nojs( request ):
    delete( request )
    return redirect( 'todo' )

@perform
def do_undo( request, note ):
    if 'done' in request.POST.keys():
        note.is_done = True
    else:
        note.is_done = False
    note.save()

def do_undo_nojs( request ):
    do_undo( request )
    return redirect( 'todo' )
