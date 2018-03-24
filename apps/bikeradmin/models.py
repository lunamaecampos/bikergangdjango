from __future__ import unicode_literals
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
import bcrypt, re, time
from datetime import date
from bcrypt import hashpw
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
from django.db import models

# Create your models here.
class UserManager(models.Manager):
    def register(self, postData):
        error_msgs = []
        bikeradmintoken = "$bikerGANG2017"
        try:
            if User.objects.get(username=postData['username']):
                error_msgs.append("Username is already in use")
        except:
            pass
        if not str(postData['admintoken'])  == bikeradmintoken:
            error_msgs.append("Please contact administrator for the Admin Token")
        if len(postData['username']) < 3:
            error_msgs.append("Username needs to be at least three characters long")
        if len(postData['password']) < 8:
            error_msgs.append("Password needs to be at least eight characters long")
        if not postData['password'] == postData['confirm']:
            error_msgs.append("Passwords do not match!")
        if error_msgs:
            return {'errors':error_msgs}
        else:
            hashed = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())
            user = User.objects.create(username=postData['username'], password=hashed)
            return {'theuser':user.username, 'userid': user.id}

    def login(self, postData):
        error_msgs = []
        password = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())
        try:
            user = User.objects.get(username=postData['username'])
        except:
            error_msgs.append("Invalid Login Credentials")
            return {'errors':error_msgs}
        if not bcrypt.hashpw(postData['password'].encode(), user.password.encode()) == user.password.encode():
            error_msgs.append("Ivalid Password")
        if error_msgs:
            return {'errors':error_msgs}
        else:
            return {'theuser':user.username, 'userid':user.id}

class ApplicantManager(models.Manager):
    def createApplication(self, postData):
        error_msgs = []
        success_msg = []
        if len(postData['artistname'] or postData['musiclink'] or postData['sociallink'] or postData['email'] or postData['city'] or postData['state'] or postData['about']) < 1:
            error_msgs.append("Please enter all the fields")
        if error_msgs:
            return {'errors':error_msgs}
        else:
            applicant = ArtistApplication.objects.create(appname=postData['artistname'], appmusiclink=postData['musiclink'], appsociallink=postData['sociallink'], appcontactemail=postData['email'], appcity=postData['city'], appstate=postData['state'], appabout=postData['about'])
            success_msg.append("Your Application was success! Be patient and we'll get in touch. Thank You!")
            return {'application':applicant.id, 'success':success_msg}
    def deleteApplication(self, id):
        ArtistApplication.objects.get(id=id).delete()

class ArtistManager(models.Manager):
    def createArtist(self, postData):
        error_msgs = []
        success_msg = []
        print "hello"
        ### checking to see if django is collecting information
        print postData['artistname']
        print "bye"
        if len(postData['artistname'] or postData['artisturlname'] or postData['artistbio']) < 1:
            error_msgs.append("Please make sure you've entered Artist Name, Urlname, and Bio ")
        if (' ' in postData['artisturlname']) == True:
            error_msgs.append("Please avoid using SPACES in your Urlname")
        ##code that uploads image to s3 bucket and gets url needs to be written here.
        if error_msgs:
            return {'errors':error_msgs}
        else:
            artist = ArtistProfile.objects.create(artistname=['artistname'], artisturlname=['artisturlname'], artistbio=['artistbio'], websiteLink=['artistweb'], facebookLink=['artistfb'], soundcloudLink=['artistsc'], bandcampLink=['artistbc'], instagramLink=postData['artistinsta'], twitterLink=postData['artisttwitter'], spotLink=postData['artistspot'], youtubeLink=postData['artistyt'], playersoundcloudLink=postData['artistplayer'])
            success_msg.append("You've successfully added this Artist in the Database!")
            print "hello"
            print artist
            ### checking to see if django is saving information in the database
            print artist.id
            print artist.artistname
            print "bye"
            return {'artist':artist.id, 'success':success_msg}
    def updateArtist(self, postData):
        error_msgs = []
        success_msg = []
        if len(postData['artistname'] or postData['artisturlname'] or postData['artistbio']) < 1:
            error_msgs.append("Please make sure you've entered Artist Name, Urlname, and Bio ")
        if (' ' in postData['artisturlname']) == True:
            error_msgs.append("Please avoid using SPACES in your Urlname")
        ##code that uploads image to s3 bucket and gets url needs to be written here.
        if error_msgs:
            return {'errors':error_msgs}
        else:
            artist = ArtistProfile.objects.save(artistname=['artistname'], artisturlname=['artisturlname'], artistbio=['artistbio'], websiteLink=['artistweb'], facebookLink=['artistfb'], soundcloudLink=['artistsc'], bandcampLink=['artistbc'], instagramLink=postData['artistinsta'], twitterLink=postData['artisttwitter'], youtubeLink=postData['artistyt'], pictureLink1=postData['artistimg'], playersoundcloudLink=postData['artistplayer'])
            success_msg.append("You've successfully updated this Artist Profile!")
            return {'artist':artist.id, 'success':success_msg}
    def deleteArtist(self, id):
        ArtistProfile.objects.get(id=id).delete()

class TourdatesManager(models.Manager):
    def createTourdate(self, postData):
        error_msgs = []
        success_msg = []
        if len(postData['tourcity'] or postData['tourvenue'] or postData['tourinfourl'] or postData['select_artist']) < 1:
            error_msgs.append("Please make sure you've entered Tour City, Tour Venue and Tickets/Info Url")
        if error_msgs:
            return {'errors':error_msgs}
        else:
            tourdateall = TourDates.objects.create(tourdatetime=postData['tourdatetime'], tourcity=postData['tourcity'], tourvenue=postData['tourvenue'], tourinfourl=postData['tourinfourl'], artist_id=postData['select_artist'])
            success_msg.append("You've successfully added this Tour Date in the Database!")
            return {'tourdateall':tourdateall.id, 'success':success_msg}
    def deleteTourdate(self, id):
        TourDates.objects.get(id=id).delete()


class AnnouncementManager(models.Manager):
    def createAnnouncement(self, postData):
        error_msgs = []
        success_msg = []
        if len(postData['newsheadline'] or postData['newsstory']) < 1:
            error_msgs.append("Please make you've entered a News Headline and Story")
        if error_msgs:
            return {'errors':error_msgs}
        else:
            announcement = NewsAnnouncement.objects.create(newsdatetime=postData['newsdatetime'], newsheadline=postData['newsheadline'], newsstory=postData['newsstory'], newsimglink=postData['newsimg'], newsimgcred=postData['newsimgcred'])
            success_msg.append("You've successfully added this News Announcement in the Database!")

            return {'announcement':announcement.id, 'success':success_msg}
    def deleteAnnouncement(self, id):
        NewsAnnouncement.objects.get(id=id).delete()

class NewsAnnouncement(models.Model):
    newsdatetime = models.DateTimeField()
    newsheadline = models.CharField(max_length=255)
    newsstory = models.CharField(max_length=2000)
    newsimglink = models.CharField(max_length=255)
    newsimgcred = models.CharField(max_length=255)
    objects = AnnouncementManager()

class ArtistApplication(models.Model):
    appname = models.CharField(max_length=255)
    appmusiclink = models.CharField(max_length=255)
    appsociallink = models.CharField(max_length=255)
    appcontactemail = models.CharField(max_length=255)
    appcity = models.CharField(max_length=255)
    appstate = models.CharField(max_length=255)
    appabout = models.CharField(max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True)
    objects = ApplicantManager()

class ArtistProfile(models.Model):
    artistname = models.CharField(max_length=255)
    artistbio = models.CharField(max_length=2000)
    artisturlname = models.CharField(max_length=255)
    websiteLink = models.CharField(max_length=255)
    facebookLink = models.CharField(max_length=255)
    soundcloudLink = models.CharField(max_length=255)
    bandcampLink = models.CharField(max_length=255)
    instagramLink = models.CharField(max_length=255)
    twitterLink = models.CharField(max_length=255)
    spotLink = models.CharField(max_length=255)
    youtubeLink = models.CharField(max_length=255)
    playersoundcloudLink = models.CharField(max_length=255)
    # pictureLink1 = models.CharField(max_length=255)
    objects = ArtistManager()

class TourDates(models.Model):
    artist_id = models.ForeignKey(ArtistProfile)
    tourdatetime = models.DateTimeField()
    tourcity = models.CharField(max_length=50)
    tourvenue = models.CharField(max_length=50)
    tourinfourl = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = TourdatesManager()

class User(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    udpated_at = models.DateTimeField(auto_now=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    objects = UserManager()
