from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from models import User, ArtistApplication, ArtistProfile, TourDates, NewsAnnouncement
from .models import User, ArtistApplication, ArtistProfile, TourDates, NewsAnnouncement
from datetime import date, datetime
# Create your views here.
def index (request):
    return render(request, 'bikeradmin/landing.html')

def logpage (request):
    return render(request, 'bikeradmin/login.html')

def roster (request):
    return render(request, 'bikeradmin/roster.html')

def tourdates (request):
    return render(request, 'bikeradmin/tourdates.html')

def news (request):
    return render(request, 'bikeradmin/news.html')

def halloffame (request):
    return render(request, 'bikeradmin/halloffame.html')

def contact (request):
    return render(request, 'bikeradmin/contact.html')

def apply (request):
    return render(request, 'bikeradmin/apply.html')

def about (request):
    return render(request, 'bikeradmin/about.html')

def artist(request):
    return render(request, 'bikeradmin/artistpage.html')

def register (request):
    if request.method=="POST":
        user = User.objects.register(request.POST)
    if 'errors' in user:
        for error in user['errors']:
            messages.error(request, error)
        return redirect('/logpage')
    if 'theuser' in user:
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
            return redirect('/dashboard')

def submitApplication(request):
    if request.method == "POST":
        applicant = ArtistApplication.objects.createApplication(request.POST)
        if 'errors' in applicant:
            for error in applicant['errors']:
                messages.error(request, error)
            return redirect('/apply')
        if 'application' in applicant:
            messages.success(request, success)
            return redirect('/apply')

def addArtist(request):
    if request.method == "POST":
        artist = ArtistProfile.objects.createArtist(request.POST)
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
        announcement = NewsAnnouncement.objects.createAnnouncement(request.POST)
        if 'errors' in announcement:
            for error in announcement['errors']:
                messages.error(request, error)
            return redirect('/dashboard')
        if 'announcement' in announcement:
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
            messages.success(request, success)
            return redirect('/dashboard')

def deleteAnnouncement(request, id):
    NewsAnnouncement.objects.deleteAnnouncement(id=id)
    return redirect('/dashboard')

def deleteApplication(request, id):
    ArtistApplication.objects.deleteApplication(id=id)
    return redirect('/dashboard')

def deleteArtist(request, id):
    ArtistProfile.objects.deleteArtist(id=id)
    return redirect('/dashboard')

def deleteTourdate(request, id):
    TourDates.objects.deleteTourdate(id=id)
    return redirect('/dashboard')

def logout(request):
    del request.session['theuser']
    del request.session['userid']
    return redirect('/logpage')

def dashboard(request):
    try:
        request.session['theuser']
    except KeyError:
        return redirect('/')
    print "what it do what it do"
    artist = ArtistProfile.id
    print ArtistProfile.objects.order_by('artistname')
    print artist
    context={
        'artist':artist
    }
    return render(request, "bikeradmin/dashboard.html", context)
