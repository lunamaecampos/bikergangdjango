from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^login', views.login),
    url(r'logpage', views.logpage),
    url(r'logout', views.logout),
    url(r'^dashboard', views.dashboard),
    url(r'^tourdates', views.tourdates),
    url(r'^roster', views.roster),
    url(r'^news', views.news),
    url(r'^HoF', views.halloffame),
    url(r'^contact', views.contact),
    url(r'^apply', views.apply),
    url(r'^about', views.about),
    url(r'^artist', views.artist),

    #####These routes will create######
    url(r'register', views.register),
    url(r'^submitApplication', views.submitApplication),
    url(r'^addartist', views.addArtist),
    url(r'^addtourdate', views.addTourdate),
    url(r'^addnews', views.addNewsAnnouncement),

    #####These routes will edit######

    #####These routes will delete######
    url(r'deleteannouncement/(?P<id>\d+)$', views.deleteAnnouncement),
    url(r'deleteapplication/(?P<id>\d+)$', views.deleteApplication),
    url(r'deleteartist/(?P<id>\d+)$', views.deleteArtist),
    url(r'deletetourdate/(?P<id>\d+)$', views.deleteTourdate),
]
