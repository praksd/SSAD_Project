from django.shortcuts import render
from django.shortcuts import render_to_response,redirect,get_object_or_404
from .models import Register, PressRelease,Event,inNews,Link,Googlenews,Querynews
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


def add_in_news(request):
    in_news = Googlenews.objects.order_by('-pubdate')[:4]
    return {
        'in_news':in_news
    }


