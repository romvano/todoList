from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from datetime import date, timedelta, datetime
from dateutil import parser
import json
from models import *

@login_required
def todo( request ):
    note_list = Note.objects.filter( user__pk = request.user.id ).order_by( '-is_overtimed' ).order_by( 'deadline' )
    context = {
        'note_list': note_list,
    }
    if request.user.is_authenticated():
        context[ 'useremail' ] = request.user.email
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
        try:
            deadline = parser.parse( request.POST[ 'deadline' ] )
            note = Note( text=text, deadline=deadline, user=request.user )
        except:
            note = Note( text=text, user=request.user )
        finally:
            note.save()
    except:
        return HttpResponse( 'Error!' )
    else:
        return HttpResponse( json.dumps( { 'code': 0, 'pk': note.pk, 'text': note.text, 'deadline': str( note.deadline )[ 0:16 ] } ) )

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

