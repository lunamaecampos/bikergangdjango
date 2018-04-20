from __future__ import unicode_literals
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
import bcrypt, re, time
from datetime import date
from bcrypt import hashpw
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
from django.db import models
from PIL import Image
from django.template.defaultfilters import slugify

# Create your models here.
class UserManager(models.Manager):
    def register(self, postData):
        error_msgs = []
        bikeradmintoken = "20$b!@krG18GN"
        try:
            if User.objects.get(username=postData['username']):
                error_msgs.append("Username is already in use")
        except:
            pass
        if not str(postData['admintoken'])  == bikeradmintoken:
            error_msgs.append("Please contact administrator for the Admin Token")
        if len(postData['username']) < 3:
            error_msgs.append("Username needs to be at least three characters long")
        if len(postData['firstname']) < 1:
            error_msgs.append("First name needs to be at least three characters long")
        if len(postData['lastname']) < 1:
            error_msgs.append(" Last name needs to be at least three characters long")
        if len(postData['password']) < 8:
            error_msgs.append("Password needs to be at least eight characters long")
        if not postData['password'] == postData['confirm']:
            error_msgs.append("Passwords do not match!")
        if error_msgs:
            return {'errors':error_msgs}
        else:
            hashed = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())
            user = User.objects.create(username=postData['username'], first_name=postData['firstname'], last_name=postData['lastname'], password=hashed)
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
            return {'theuser':user.username, 'userid':user.id, 'username':user.first_name}

class ApplicantManager(models.Manager):
    def createApplication(self, postData):
        error_msgs = []
        success_msg = []
        if len(postData['artistname']) < 1:
            error_msgs.append("Please enter artist name")
        if len(postData['musiclink']) < 1:
            error_msgs.append("Please enter link to your music")
        if len(postData['sociallink']) < 1:
            error_msgs.append("Please enter link to you social")
        if len(postData['email']) < 1:
            error_msgs.append("Please enter your email")
        if len(postData['city']) < 1:
            error_msgs.append("Please enter City")
        if len(postData['state']) < 1:
            error_msgs.append("Please enter State")
        if len(postData['about']) < 1:
            error_msgs.append("Please enter bio")
        if error_msgs:
            return {'errors':error_msgs}
        else:
            applicant = ArtistApplication.objects.create(appname=postData['artistname'], appmusiclink=postData['musiclink'], appsociallink=postData['sociallink'], appcontactemail=postData['email'], appcity=postData['city'], appstate=postData['state'], appabout=postData['about'])
            success_msg.append("Your Application was success! Be patient and we'll get in touch. Thank You!")
            return {'application':applicant.id, 'success':success_msg}
    def deleteApplication(self, id):
        ArtistApplication.objects.get(id=id).delete()

class ArtistManager(models.Manager):
    def createArtist(self, postData, fileData, filepath):
        error_msgs = []
        success_msg = []
        if len(postData['artistname']) < 1:
            error_msgs.append("Please make sure you've entered Artist Name")
        if len(postData['artistbio']) < 1:
            error_msgs.append("Please make sure you've entered Artist Bio")
        if filepath == False:
            error_msgs.append("Please upload a valid image")
            if error_msgs:
                return {'errors':error_msgs}
        else:
            image = Image.open(fileData['artistimg'])
            if image.size[0] < 480: #image.size is a 2-tuple (width, height)
                error_msgs.append("Please make sure your image is at least 480px in width")
            if error_msgs:
                return {'errors':error_msgs}
            else:
                artist = ArtistProfile(artistname=postData['artistname'], artisturlname=slugify(postData['artistname']), artistbio=postData['artistbio'], websiteLink=postData['artistweb'], facebookLink=postData['artistfb'], soundcloudLink=postData['artistsc'], bandcampLink=postData['artistbc'], instagramLink=postData['artistinsta'], twitterLink=postData['artisttwitter'], spotLink=postData['artistspot'], youtubeLink=postData['artistyt'], playersoundcloudLink=postData['artistplayer'], profileImage=fileData['artistimg'])
                artist.save()
                success_msg.append("You've successfully added this Artist in the Database!")
                return {'artist':artist.id, 'success':success_msg}
    def updateArtist(self, postData, fileData, id, filepath):
        error_msgs = []
        success_msg = []
        if len(postData['artistname']) < 1:
            error_msgs.append("Please make sure you've entered Artist Name")
        if len(postData['artistbio']) < 1:
            error_msgs.append("Please make sure you've entered Artist Bio")
        if error_msgs:
            return {'errors':error_msgs}
        else:
            if filepath == False:
                artist = ArtistProfile.objects.filter(id=id).update(artistname=postData['artistname'], artisturlname=slugify(postData['artistname']), artistbio=postData['artistbio'], websiteLink=postData['artistweb'], facebookLink=postData['artistfb'], soundcloudLink=postData['artistsc'], bandcampLink=postData['artistbc'], instagramLink=postData['artistinsta'], twitterLink=postData['artisttwitter'], spotLink=postData['artistspot'], youtubeLink=postData['artistyt'], playersoundcloudLink=postData['artistplayer'])
                success_msg.append("You've successfully updated this Artist Profile!")
                return {'artist':artist, 'success':success_msg}
            else:
                image = Image.open(fileData['artistimg'])
                if image.size[0] < 480: #image.size is a 2-tuple (width, height)
                    error_msgs.append("Please make sure your image is at least 480 in width")
                if error_msgs:
                    return {'errors':error_msgs}
                else:
                    artist = ArtistProfile.objects.get(id=id)
                    artist.artistname=postData['artistname']
                    artist.artisturlname=slugify(postData['artistname'])
                    artist.artistbio=postData['artistbio']
                    artist.websiteLink=postData['artistweb']
                    artist.facebookLink=postData['artistfb']
                    artist.soundcloudLink=postData['artistsc']
                    artist.bandcampLink=postData['artistbc']
                    artist.instagramLink=postData['artistinsta']
                    artist.twitterLink=postData['artisttwitter']
                    artist.spotLink=postData['artistspot']
                    artist.youtubeLink=postData['artistyt']
                    artist.playersoundcloudLink=postData['artistplayer']
                    artist.profileImage.delete()
                    artist.profileImage=fileData['artistimg']
                    artist.save()
                    success_msg.append("You've successfully updated this Artist Profile!")
                    return {'artist':artist, 'success':success_msg}
    def deleteArtist(self, id):
        artist = ArtistProfile.objects.get(id=id)
        artist.profileImage.delete()
        artist.delete()


class TourdatesManager(models.Manager):
    def createTourdate(self, postData):
        error_msgs = []
        success_msg = []
        if len(postData['tourcity']) < 1:
            error_msgs.append("Please make sure you've entered Tour City")
        if len(postData['tourvenue']) < 1:
            error_msgs.append("Please make sure you've entered Tour Venu")
        if len(postData['tourinfourl']) < 1:
            error_msgs.append("Please make sure you've entered Ticket/Info Link")
        if error_msgs:
            return {'errors':error_msgs}
        else:
            artistid = ArtistProfile.objects.get(id=postData['select_artist'])
            tourdateall = TourDates.objects.create(tourdatetime=postData['tourdatetime'], tourcity=postData['tourcity'], tourvenue=postData['tourvenue'], tourinfourl=postData['tourinfourl'], artist=artistid)
            success_msg.append("You've successfully added this Tour Date in the Database!")
            return {'tourdateall':tourdateall.id, 'success':success_msg}
    def deleteTourdate(self, id):
        TourDates.objects.get(id=id).delete()

class HallManager(models.Manager):
    def createImage(self, postData, fileData, filepath):
        error_msgs = []
        success_msg = []
        if len(postData['caption']) < 1:
            error_msgs.append("Please make sure you've entered a Caption")
        if len(postData['cred']) < 1:
            error_msgs.append("Please make sure you've entered a Credit for this Image")
        if filepath == False:
            error_msgs.append("Please upload a valid Image")
            if error_msgs:
                return {'errors':error_msgs}
        else:
            image = Image.open(fileData['image'])
            if image.size[0] < 480:
                error_msgs.append("Please make sure your image is at least 480px in width")
            if error_msgs:
                return {'errors':error_msgs}
            else:
                ftImage = FeaturedImage(caption=postData['caption'], credit=postData['cred'], image=fileData['image'])
                ftImage.save()
                success_msg.append("You've successfully added this image to your Hall of Fame")
                return {'ftImage':ftImage.id, 'success':success_msg}
    def deleteImage(self, id):
        ftImage = FeaturedImage.objects.get(id=id)
        ftImage.image.delete()
        ftImage.delete()

class AnnouncementManager(models.Manager):
    def createAnnouncement(self, postData, fileData, filepath):
        error_msgs = []
        success_msg = []
        if len(postData['newsheadline']) < 1:
            error_msgs.append("Please make you've entered a News Headline")
        if len(postData['newsstory']) < 1:
            error_msgs.append("Please make you've entered a News Story")
        if filepath == False:
            error_msgs.append("Please upload a valid image")
            if error_msgs:
                return {'errors':error_msgs}
        else:
            image = Image.open(fileData['newsimg'])
            if image.size[0] < 480: #image.size is a 2-tuple (width, height)
                error_msgs.append("Please make sure your image is at least 480px in width")
            if error_msgs:
                return {'errors':error_msgs}
            else:
                announcement = NewsAnnouncement(newsheadline=postData['newsheadline'], newsstory=postData['newsstory'], newsimgcred=postData['newsimgcred'], newsimg=fileData['newsimg'])
                announcement.save()
                success_msg.append("You've successfully added this News Announcement in the Database!")
                return {'announcement':announcement.id, 'success':success_msg}
    def updateNewsAnnouncement(self, postData, fileData, id, filepath):
        error_msgs = []
        success_msg = []
        if len(postData['newsheadline']) < 1:
            error_msgs.append("Please make you've entered a News Headline")
        if len(postData['newsstory']) < 1:
            error_msgs.append("Please make you've entered a News Story")
        if error_msgs:
            return {'errors':error_msgs}
        else:
            if filepath == False:
                announcement = NewsAnnouncement.objects.filter(id=id).update(newsheadline=postData['newsheadline'], newsstory=postData['newsstory'], newsimgcred=postData['newsimgcred'])
                return {'announcement':announcement, 'success':success_msg}
            else:
                image = Image.open(fileData['newsimg'])
                if image.size[0] < 480: #image.size is a 2-tuple (width, height)
                    error_msgs.append("Please make sure your image is at least 480px in width")
                if error_msgs:
                    return {'errors':error_msgs}
                else:
                    announcement = NewsAnnouncement.objects.get(id=id)
                    announcement.newsheadline=postData['newsheadline']
                    announcement.newsstory=postData['newsstory']
                    announcement.newsimgcred=postData['newsimgcred']
                    announcement.newsimg.delete()
                    announcement.newsimg=fileData['newsimg']
                    announcement.save()
                    success_msg.append("You've successfully updated this News Announcement!")
                    return {'announcement':announcement, 'success':success_msg}
    def deleteAnnouncement(self, id):
        announcement = NewsAnnouncement.objects.get(id=id)
        announcement.newsimg.delete()
        announcement.delete()

class NewsAnnouncement(models.Model):
    newsdatetime = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    newsheadline = models.CharField(max_length=255)
    newsstory = models.CharField(max_length=2000)
    newsimgcred = models.CharField(max_length=255)
    newsimg = models.FileField()
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
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    artistname = models.CharField(max_length=255)
    artistbio = models.CharField(max_length=2000)
    artisturlname = models.SlugField(max_length=255)
    websiteLink = models.CharField(max_length=255)
    facebookLink = models.CharField(max_length=255)
    soundcloudLink = models.CharField(max_length=255)
    bandcampLink = models.CharField(max_length=255)
    instagramLink = models.CharField(max_length=255)
    twitterLink = models.CharField(max_length=255)
    spotLink = models.CharField(max_length=255)
    youtubeLink = models.CharField(max_length=255)
    playersoundcloudLink = models.CharField(max_length=255)
    profileImage = models.ImageField()
    objects = ArtistManager()

class TourDates(models.Model):
    artist = models.ForeignKey(ArtistProfile)
    tourdatetime = models.DateTimeField()
    tourcity = models.CharField(max_length=50)
    tourvenue = models.CharField(max_length=50)
    tourinfourl = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = TourdatesManager()

class FeaturedImage(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    caption = models.CharField(max_length=150)
    credit = models.CharField(max_length=50)
    image = models.ImageField()
    objects = HallManager()

class User(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    udpated_at = models.DateTimeField(auto_now=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    objects = UserManager()
