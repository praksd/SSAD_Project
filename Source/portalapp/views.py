from django.shortcuts import render
from django.shortcuts import render_to_response,redirect,get_object_or_404
from .models import Register, PressRelease,Event,inNews,Link,Googlenews,Querynews,Twitternews #importing following model
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
from .forms import TalkForm
from django.shortcuts import redirect
from .models import Photo,Album,Link
from django.http import HttpResponse
from django.template import loader
from django.conf import settings
from django.core.mail import send_mail
import operator
from post_office import mail
#from post_office import mail, PRIORITY
from .tasks import user_send_activation_email , user_upload_activation_email
from endless_pagination.decorators import page_template
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template import RequestContext
from django.db.models import F
from .feedbuilder import *
from datetime import datetime
from django.template.loader import render_to_string, get_template
from django.core.mail import EmailMessage
from .scrapechange import *
from .scrapechange import *

# start of the functions related to the Talk page

# This function will display all the talks happened till date
def talks_list(request):
    # Register is the Model corresponing to the talks  
    talk = Register.objects.order_by('-date_and_time') # Assigning list of talks reverse ordered according to date and time to variable talk
    # pagination
    paginator = Paginator(talk, 6) # Show 6 talks per page

    page = request.GET.get('page')
    try:
        talks = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        talks = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        talks = paginator.page(paginator.num_pages)
    # Rendering talks/talk_list.html and passing talks variable to the page 
    return render(request, 'talks/talks_list.html', {'talks':talks})

# This function is corresponding to the uploading of talk by faculty 
def talk_new(request):
    if request.method == 'POST':    # checking wheather the type of request is POST
      form = TalkForm(request.POST, request.FILES)  # Assigning all the submitted data and files to variable form
      if form.is_valid():                           # Validating the submitted data 
         talk = form.save(commit=False)             # Not saving form as some fields are yet to add   
         talk.author = request.user                 # assigning value to field author
         talk.save()                                # saving                        
         user_send_activation_email.delay(user = request.user)  # delaying the task of sending mail (celery)
         #mail.send(request.user.email,settings.EMAIL_HOST_USER,subject='My email',message='Hi there!',html_message='Hi <strong>there</strong>!',)
         return redirect('talks_list')              # redirecting to function talk_list
                   
    else:                                           # if type of request is get 
      form = TalkForm()                             #  Creating new form of type TalkForm
    return render(request, 'talks/talk_edit.html', {'form': form})   # passing form to template 


def talks_detail(request):
   user = request.user
   talks = Register.objects.order_by('-date_and_time')
   news=inNews.objects.all().order_by('-date')[:5]
   return render(request, 'talks/talks_detail.html', {'talks':talks,'news':news})

def talk_edit(request,pk):
   talk = get_object_or_404(Register, pk=pk)
   if request.method == "POST":
      form = TalkForm(request.POST,request.FILES, instance=talk)
      if form.is_valid():
        form.save()
        user_upload_activation_email.delay(user = request.user)
        #send_mail('You Have Edited your talk', 'Confirmation mail', 'settings.EMAIL_HOST_USER',[request.user.email], fail_silently=False)
        #user_send_activation_email.delay(user = request.user)
        return redirect('talks_detail')
   else:
       form = TalkForm(instance=talk)
   return render(request, 'talks/talk_edit.html', {'form': form})

def talk_part(request,pk):
   talk = get_object_or_404(Register, pk=pk)
   news=inNews.objects.all().order_by('-date')[:5]
   return render(request, 'talks/talk_part.html', {'talk': talk,'news':news})

# end
def index(request):
    template = loader.get_template('home/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

def album_list(request):
    album_choice = Album.objects.all()
    events_recent=Event.objects.all().filter(date__gte = timezone.now()).order_by('date')[:5]
    news=inNews.objects.all().order_by('-date')[:5]
    return render(request, "talks/gallery.html", {'album_choice':album_choice,'news':news,'events_recent':events_recent})

def photo_list(request,pk):

    album = get_object_or_404(Album, pk=pk)
    events_recent=Event.objects.all().filter(date__gte = timezone.now()).order_by('date')[:5]
    pic = Photo.objects.filter(album = album)

    paginator = Paginator(pic, 8) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        pics = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        pics = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        pics = paginator.page(paginator.num_pages)

    context = {
            "album" : album,
            "pics"  : pics,
            'events_recent':events_recent
            }
    return render(request, "talks/album_view.html", context)

def release_unique(request,pk):
   pressrelease  = get_object_or_404(PressRelease, pk=pk)
   events_recent=Event.objects.all().filter(date__gte = timezone.now()).order_by('date')[:5]
   news=inNews.objects.all().order_by('-date')[:5]
   return render(request, 'pressrelease/release_unique.html', {'events_recent':events_recent,'news':news,'pressrelease': pressrelease})

def event_unique(request,pk):
   event = get_object_or_404(Event, pk=pk)
   events_recent=Event.objects.all().filter(date__gte = timezone.now()).order_by('date')[:5]
   news=inNews.objects.all().order_by('-date')[:5]
   return render(request, 'pressrelease/event_unique.html', {'events_recent':events_recent,'news':news,'event': event})


def pressrelease(request):
    pressreleases = PressRelease.objects.all().order_by('-date')
    events_recent=Event.objects.all().filter(date__gte = timezone.now()).order_by('date')[:5]
    news=inNews.objects.all().order_by('-date')[:5]
    paginator = Paginator(pressreleases, 2) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        pressreleases_page = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        pressreleases_page = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        pressreleases_page = paginator.page(paginator.num_pages)

    return render(request, 'pressrelease/pressrelease.html', {'pressreleases':pressreleases,'news':news,'events_recent':events_recent,'pressreleases_page':pressreleases_page})

def pressrelease_short(request):
    pressreleases = PressRelease.objects.order_by('-date')[:1]
    slider_photo= Photo.objects.all().order_by('id')[:4]
    talks = Register.objects.filter(date_and_time__gte = timezone.now()).order_by('date_and_time')[:2]
    events=Event.objects.all().filter(date__gte = timezone.now()).order_by('date')
    events_recent=Event.objects.all().filter(date__gte = timezone.now()).order_by('date')[:5]
    news=inNews.objects.all().order_by('-date')[:5]
    return render(request, 'pressrelease/slider.html', {'events_recent':events_recent,'news':news,'events':events,'pressreleases':pressreleases ,'talks':talks, 'slider_photo':slider_photo})

def event(request):
    events=Event.objects.all().order_by('-date')
    events_recent=Event.objects.all().filter(date__gte = timezone.now()).order_by('date')[:5]
    news=inNews.objects.all().order_by('-date')[:5]
    paginator = Paginator(events, 6) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        events_page = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        events_page = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        events_page = paginator.page(paginator.num_pages)

    return render(request,'pressrelease/event.html',{'events':events,'events_recent':events_recent,'news':news,'events_page':events_page})

def contact(request):
    events_recent=Event.objects.all().filter(date__gte = timezone.now()).order_by('date')[:5]
    news=inNews.objects.all().order_by('-date')[:5]
    return render(request,'pressrelease/contact.html',{'events_recent':events_recent,'news':news})

def base_footer(request):
    events_recent=Event.objects.all().filter(date__gte = timezone.now()).order_by('date')[:5]
    return render(request,'talks/base.html', {'events_recent':events_recent})


def home(request):
   short_url = None
   if request.method == "POST":
      link_db = models.Link()
      link_db.link = request.POST.get("url")
      link_db.save()
      short_url = request.build_absolute_uri(link_db.get_short_id())
   return render_to_response("tinyurl/tinify.html",
                             {"short_url":short_url},
                             context_instance=RequestContext(request))

def link(request, id):
   db_id = models.Link.deocde_id(id)
   link_db = get_object_or_404(models.Link, id=db_id)
   models.Link.objects.filter(id=db_id).update(hits=F('hits')+1)
   return redirect(link_db.link)



