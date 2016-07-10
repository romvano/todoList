from django.conf.urls import patterns, include, url
from . import views

urlpatterns = [
    url( r'^$', views.todo, name = 'todo' ),
    url( r'^do_undo/?$', views.do_undo, name = 'do_undo' ),
    url( r'^do_undo-nojs/?$', views.do_undo_nojs, name = 'do_undo-nojs' ),
    url( r'^delete/?$', views.delete, name = 'delete' ),
    url( r'^delete-nojs/?$', views.delete_nojs, name = 'delete-nojs' ),
    url( r'^add/?$', views.add, name = 'add' ),
    url( r'^add-nojs/?$', views.add_nojs, name = 'add-nojs' ),
]
