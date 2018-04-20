from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^login$', views.login),
    url(r'logpage$', views.logpage),
    url(r'logout$', views.logout),
    url(r'^dashboard$', views.dashboard),
    url(r'^tourdates$', views.tourdates),
    url(r'^tourdates/$', views.tourdates),
    url(r'^roster$', views.roster),
    url(r'^news$', views.news),
    url(r'^HoF$', views.halloffame),
    url(r'^contact$', views.contact),
    url(r'^apply$', views.apply),
    url(r'^about$', views.about),
    url(r'^artist$', views.artist),

    url(r'^tourmanager$', views.tourman),
    url(r'^artistmanager$', views.artistman),
    url(r'^newsmanager$', views.newsman),
    url(r'^appmanager$', views.appman),
    url(r'^hofmanager$', views.hofman),

    #####This route will carry the object by passing the model field "artisturlname"######
    url(r'^artist/(?P<artisturlname>[\w-]+)/$', views.artistProfile),

    #####These routes will create######
    url(r'register', views.register),
    url(r'^submitApplication', views.submitApplication),
    url(r'^addartist', views.addArtist),
    url(r'^addtourdate', views.addTourdate),
    url(r'^addnews', views.addNewsAnnouncement),
    url(r'^addimage', views.addFeaturedImage),

    #####These routes will select######
    url(r'^selectartist/(?P<id>\d+)$', views.selectArtist),
    url(r'^selectartist/$', views.artistman),
    url(r'^tourartistselect/(?P<id>\d+)$', views.tourArtistSelect),
    url(r'^tourartistselect/', views.tourman),
    url(r'^selectnews/(?P<id>\d+)$', views.newsSelect),
    url(r'^selectnews/', views.newsman),
    url(r'^tourdates/(?P<id>\d+)$', views.tourSelect),

    #####These routes will edit######
    url(r'editartist/(?P<id>\d+)$', views.editArtist),
    url(r'editnews/(?P<id>\d+)$', views.editAnnouncement),

    #####These routes will delete######
    url(r'deleteannouncement/(?P<id>\d+)$', views.deleteAnnouncement),
    url(r'deleteapplication/(?P<id>\d+)$', views.deleteApplication),
    url(r'deleteartist/(?P<id>\d+)$', views.deleteArtist),
    url(r'deletetourdate/(?P<id>\d+)$', views.deleteTourdate),
    url(r'deleteimage/(?P<id>\d+)$', views.deleteImage),
]
