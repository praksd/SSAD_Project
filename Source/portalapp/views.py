from django.shortcuts import render
from .models import Register
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .forms import TalkForm
from django.shortcuts import redirect
from .models import Photo
from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template('home/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

def photo_list(request):
    queryset = Photo.objects.all()
    context = {
            "photos" : queryset,
            }
    return render(request, "talks/gallery.html", context)


def talks_list(request):
    talks = Register.objects.filter(date_and_time__gte = timezone.now()).order_by('date_and_time')
    return render(request, 'talks/talks_list.html', {'talks':talks})

def talk_new(request):
    if request.method == 'POST':
      form = TalkForm(request.POST)
      if form.is_valid():
         talk = form.save(commit=False)
         talk.author = request.user
         talk.save()
         return redirect('talks_list')

    else:
      form = TalkForm()
    return render(request, 'talks/talk_edit.html', {'form': form})

def talks_detail(request):
   user = request.user
   talks = Register.objects.filter(date_and_time__gte = timezone.now(), author = user).order_by('date_and_time')
   return render(request, 'talks/talks_detail.html', {'talks':talks})

def talk_edit(request,pk):
   talk = get_object_or_404(Register, pk=pk)
   if request.method == "POST":
      form = TalkForm(request.POST, instance=talk)
      if form.is_valid():
        form.save()
      return redirect('talks_detail')
   else:
       form = TalkForm(instance=talk)
   return render(request, 'talks/talk_edit.html', {'form': form})
