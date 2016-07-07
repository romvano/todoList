from django.conf.urls import patterns, include, url
from . import views

urlpatterns = [
    url( r'^$', views.todo, name = 'todo' ),
    url( r'^do_undo/?$', views.do_undo, name = 'do_undo'),
]
