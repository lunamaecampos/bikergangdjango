from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from models import User, ArtistApplication, ArtistProfile, TourDates, NewsAnnouncement, FeaturedImage
# from .models import User, ArtistApplication, ArtistProfile, TourDates, NewsAnnouncement
from datetime import date, datetime
# Create your views here.
def index (request):
    return render(request, 'bikeradmin/landing.html')

def logpage (request):
    return render(request, 'bikeradmin/login.html')

def roster (request):
    trueartist = ArtistProfile.objects.filter(currentArtist=True)
    falseartist = ArtistProfile.objects.filter(currentArtist=False)
    return render(request, 'bikeradmin/roster.html', {'trueartist':trueartist, 'falseartist':falseartist})

def tourdates (request):
    artist = ArtistProfile.objects.all()
    tour_list = TourDates.objects.order_by('tourdatetime')
    paginator = Paginator(tour_list, 50) # Show 50 Tourdates per page

    page = request.GET.get('page')
    try:
        tourdate = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        tourdate = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 999), deliver last page of results
        tourdate = paginator.page(paginator.num_pages)
    context = {'tourdate':tourdate, 'artist':artist}
    return render(request, 'bikeradmin/tourdates.html', {'artist':artist, 'tourdate':tourdate})

def news (request):
    news_list = NewsAnnouncement.objects.all()
    news_list = news_list.order_by('-newsdatetime')
    paginator = Paginator(news_list, 5) # Show 5 News Listings per page

    page = request.GET.get('page')
    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        news = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 999), deliver last page of results
        news = paginator.page(paginator.num_pages)
    return render(request, 'bikeradmin/news.html', {'news': news})

def halloffame (request):
    hofphoto = FeaturedImage.objects.order_by('created_at')
    return render(request, 'bikeradmin/halloffame.html', {'hofphoto':hofphoto})

def contact (request):
    return render(request, 'bikeradmin/contact.html')

def apply (request):
    return render(request, 'bikeradmin/apply.html')

def about (request):
    return render(request, 'bikeradmin/about.html')

def artist(request):
    return render(request, 'bikeradmin/artistpage.html')

def artistman(request):
    artist = ArtistProfile.objects.all()
    return render(request, 'bikeradmin/artistman.html', {'artist': artist})

##### Management views for windows dashboard #######

def appman(request):
    applicant_list = ArtistApplication.objects.order_by('-created_at')

    paginator = Paginator(applicant_list, 5) # Show 10 App Listings per page

    page = request.GET.get('page')
    try:
        applicant = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        applicant = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 999), deliver last page of results
        applicant = paginator.page(paginator.num_pages)
    return render(request, 'bikeradmin/appman.html', {'applicant': applicant})

def newsman(request):
    news = NewsAnnouncement.objects.all()
    return render(request, 'bikeradmin/newsman.html', {'news': news})

def hofman(request):
    image = FeaturedImage.objects.all()
    return render(request, 'bikeradmin/hofman.html', {'image': image})

def tourman(request):
    artist = ArtistProfile.objects.all()
    tour_list = TourDates.objects.all()
    paginator = Paginator(tour_list, 50) # Show 50 Tourdates per page

    page = request.GET.get('page')
    try:
        tourdate = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        tourdate = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 999), deliver last page of results
        tourdate = paginator.page(paginator.num_pages)
    return render(request, 'bikeradmin/tourman.html', {'tourdate': tourdate, 'artist': artist},)

def tourArtistSelect(request, id):
    artist = ArtistProfile.objects.all()
    tour_list = TourDates.objects.filter(artist=id)
    paginator = Paginator(tour_list, 50) # Show 50 Tourdates per page

    page = request.GET.get('page')
    try:
        tourdate = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        tourdate = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 999), deliver last page of results
        tourdate = paginator.page(paginator.num_pages)
    context = {'tourdate':tourdate, 'artist':artist}
    return render(request, 'bikeradmin/tourman.html', context)

def tourSelect(request, id):
    artist = ArtistProfile.objects.all()
    tour_list = TourDates.objects.filter(artist=id)
    tour_list = tour_list.order_by('tourdatetime')
    paginator = Paginator(tour_list, 50) # Show 50 Tourdates per page

    page = request.GET.get('page')
    try:
        tourdate = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        tourdate = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 999), deliver last page of results
        tourdate = paginator.page(paginator.num_pages)
    context = {'tourdate':tourdate, 'artist':artist}
    return render(request, 'bikeradmin/tourdates.html', context)

def newsSelect(request, id):
    thenews = NewsAnnouncement.objects.get(pk=id)
    news = NewsAnnouncement.objects.all()
    return render(request, 'bikeradmin/newsman.html', {'thenews':thenews, 'news':news})

def selectArtist(request, id):
    artist = ArtistProfile.objects.all()
    theartist = ArtistProfile.objects.get(pk=id)
    context = {'theartist':theartist, 'artist':artist}
    return render(request, 'bikeradmin/artistman.html', context)

def editArtist(request, id):
    if request.method=="POST":
        filepath = request.FILES.get('artistimg', False)
        artist = ArtistProfile.objects.updateArtist(request.POST, request.FILES, id, filepath)
        if 'errors' in artist:
            for error in artist['errors']:
                messages.error(request, error)
            return redirect('/artistmanager')
        if 'artist' in artist:
            for success in artist['success']:
                messages.success(request, success)
            return redirect('/artistmanager')
def editAnnouncement(request, id):
    if request.method == "POST":
        filepath = request.FILES.get('newsimg', False)
        announcement = NewsAnnouncement.objects.updateNewsAnnouncement(request.POST, request.FILES, id, filepath)
        if 'errors' in announcement:
            for error in announcement['errors']:
                messages.error(request, error)
            return redirect('/newsmanager')
        if 'announcement' in announcement:
            for success in announcement['success']:
                messages.success(request, success)
            return redirect('/newsmanager')

#####updated version for when we have artists in our database
def artistProfile(request, artisturlname):
    artist = ArtistProfile.objects.get(artisturlname=artisturlname)

    tourdate = TourDates.objects.filter(artist = artist.id)
    tourdate = tourdate.order_by('tourdatetime')
    return render(request, 'bikeradmin/artistpage.html', {'artist':artist, 'tourdate':tourdate})

def register (request):
    if request.method=="POST":
        user = User.objects.register(request.POST)
    if 'errors' in user:
        for error in user['errors']:
            messages.error(request, error)
        return redirect('/logpage')
    if 'theuser' in user:
	request.session['username'] = user['username']
        request.session['theuser'] = user['theuser']
        request.session['userid'] = user['userid']
        return redirect('/dashboard')

def login(request):
    if request.method == "POST":
        user = User.objects.login(request.POST)
        if 'errors' in user:
            for error in user ['errors']:
                messages.error(request, error)
                return redirect('/login')
        if 'theuser' in user:
            request.session['theuser'] = user['theuser']
            request.session['userid'] = user['userid']
            request.session['username'] = user['username']
            return redirect('/dashboard')

def submitApplication(request):
    if request.method == "POST":
        applicant = ArtistApplication.objects.createApplication(request.POST)
        if 'errors' in applicant:
            for error in applicant['errors']:
                messages.error(request, error)
            return redirect('/apply')
        if 'application' in applicant:
            for success in applicant['success']:
                messages.success(request, success)
            return redirect('/apply')

def addArtist(request):
    if request.method == "POST":
        filepath = request.FILES.get('artistimg', False)
        artist = ArtistProfile.objects.createArtist(request.POST, request.FILES, filepath)
        if 'errors' in artist:
            for error in artist['errors']:
                messages.error(request, error)
            return redirect('/dashboard')
        if 'artist' in artist:
            for success in artist['success']:
                messages.success(request, success)
            return redirect('/dashboard')

def addNewsAnnouncement(request):
    if request.method == "POST":
        filepath = request.FILES.get('newsimg', False)
        announcement = NewsAnnouncement.objects.createAnnouncement(request.POST, request.FILES, filepath)
        if 'errors' in announcement:
            for error in announcement['errors']:
                messages.error(request, error)
            return redirect('/dashboard')
        if 'announcement' in announcement:
            for success in announcement['success']:
                messages.success(request, success)
            return redirect('/dashboard')

def addFeaturedImage(request):
    if request.method == "POST":
        filepath = request.FILES.get('image', False)
        ftImage = FeaturedImage.objects.createImage(request.POST, request.FILES, filepath)
        if 'errors' in ftImage:
            for error in ftImage['errors']:
                messages.error(request, error)
            return redirect('/dashboard')
        if 'ftImage' in ftImage:
            for success in ftImage['success']:
                messages.success(request, success)
            return redirect('/dashboard')

def addTourdate(request):
    if request.method == "POST":
        tourdateall = TourDates.objects.createTourdate(request.POST)
        if 'errors' in tourdateall:
            for error in tourdateall['errors']:
                messages.error(request, error)
            return redirect('/dashboard')
        if 'tourdateall' in tourdateall:
            for success in tourdateall['success']:
                messages.success(request, success)
            return redirect('/dashboard')

def deleteAnnouncement(request, id):
    NewsAnnouncement.objects.deleteAnnouncement(id=id)
    return redirect('/newsmanager')

def deleteApplication(request, id):
    ArtistApplication.objects.deleteApplication(id=id)
    return redirect('/appmanager')

def deleteArtist(request, id):
    ArtistProfile.objects.deleteArtist(id=id)
    return redirect('/artistmanager')

def deleteTourdate(request, id):
    TourDates.objects.deleteTourdate(id=id)
    return redirect('/tourmanager')

def deleteImage(request, id):
    FeaturedImage.objects.deleteImage(id=id)
    return redirect('/hofmanager')

def logout(request):
    del request.session['theuser']
    del request.session['userid']
    del request.session['username']
    return redirect('/logpage')

def dashboard(request):
    try:
        request.session['username']
    except KeyError:
        return redirect('/')
    artist = ArtistProfile.objects.all()
    context={
        'artist': artist
    }
    return render(request, "bikeradmin/dashboard.html", context)
