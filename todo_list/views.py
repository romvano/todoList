from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from todo.models import *

def not_authed_yet( func ):
    def improved_func( request ):
        if request.user.is_authenticated():
            return redirect( 'todo' )
        return func( request )
    return improved_func

@not_authed_yet
def login_view( request ):
    context = {}
    if request.method == "POST":
        if "login" and "password" in request.POST.keys():
            try:
                username = User.objects.get( email = request.POST[ 'login' ] )
                user = authenticate( username = username, password = request.POST[ "password" ] )
                if( user is not None ):
                    login( request, user )
                    return redirect( 'todo' )
                else:
                    raise ObjectDoesNotExist
            except ObjectDoesNotExist:
                context[ 'error' ] = "Invalid credentials!"
    return render( request, 'login.html', context )

def logout_view( request ):
    if( request.method == 'POST' ):
        if( "log_out" in request.POST.keys() and request.user.is_authenticated() ):
            logout(request)
    return redirect( 'todo' )

@not_authed_yet
def registration( request ):
    context = { 'error': '' }
    if ( request.method == 'POST' ) and ( 'login' and 'password1' and 'password2' in request.POST.keys() ):
        # email
        try:
            User.objects.get( email = request.POST[ 'login' ] )
            context[ 'error' ] = 'There is a user with this e-mail already.'
            return render( request, 'registration.html', context )
        except ObjectDoesNotExist:
            # passwords
            if request.POST[ 'password1' ] != request.POST[ 'password2' ]:
                context[ 'error' ] = 'Please check your passwords.'
                return render( request, 'registration.html', context )
            user = User.objects.create_user( request.POST[ 'login' ], request.POST[ 'login' ], request.POST[ 'password1' ] )
            p = Profile(user = user)
            p.save()
            return redirect( 'todo' )
        except:
            context[ 'error' ] = 'Sorry, sth is wrong. Please try again!'
    return render( request, 'registration.html', context )
