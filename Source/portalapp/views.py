from django.shortcuts import render
from .models import Register, PressRelease ,Event
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .forms import TalkForm
from django.shortcuts import redirect
from .models import Photo
from django.http import HttpResponse
from django.template import loader
import operator

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


"""def talks_list(request):
    talks = Register.objects.filter(date_and_time__gte = timezone.now()).order_by('date_and_time')
      form = TalkForm(request.POST, request.FILES)

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
  talk = get_object_or_404(Register, pk=pk)
  return render(request, 'talks/talk_part.html', {'talk': talk})
"""
def talks_list(request):
    talks = Register.objects.filter(date_and_time__gte = timezone.now()).order_by('date_and_time')
    return render(request, 'talks/talks_list.html', {'talks':talks})

def talk_new(request):
    if request.method == 'POST':
      form = TalkForm(request.POST, request.FILES)
      if form.is_valid():
         talk = form.save(commit=False)
         talk.author = request.user
         talk.save()
         print redirect('talks_list')
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
      form = TalkForm(request.POST,request.FILES, instance=talk)
      if form.is_valid():
        form.save()
      return redirect('talks_detail')
   else:
       form = TalkForm(instance=talk)
   return render(request, 'talks/talk_edit.html', {'form': form})

def talk_part(request,pk):
   talk = get_object_or_404(Register, pk=pk)
   return render(request, 'talks/talk_part.html', {'talk': talk})


def pressrelease(request):
    presreleases = PressRelease.objects.order_by('date')
    return render(request, 'pressrelease/pressrelease.html', {'pressrelease':pressrelease})

def pressrelease_short(request):
    pressreleases = PressRelease.objects.order_by('date')
    slider_photo= Photo.objects.all().order_by('id')[:4]
    talks = Register.objects.filter(date_and_time__gte = timezone.now()).order_by('date_and_time')[:2]
    events=Event.objects.all().order_by('date')
    return render(request, 'pressrelease/slider.html', {'events':events,'pressrelease':pressrelease ,'talks':talks, 'slider_photo':slider_photo})

'''def eventline(request):
    events=Event.objects.all().order_by('date')
    return render(request,'pressrelease/slider.html',{'events':events})
'''
#adding different choices for photographs

def all_photo(request):
    all_photos = Photo.objects.all
    return render(request, 'talks/all_photo.html', {'all_photos':all_photos})


def campus(request):
    campus_photos = Photo.objects.filter( album = 'CAMPUS')
    return render(request, 'talks/campus.html', {'campus_photos':campus_photos})

def cult(request):
    cult_photos = Photo.objects.filter( album = 'CULT')
    return render(request, 'talks/cult.html', {'cult_photos':cult_photos})


def acads(request):
    acad_photos = Photo.objects.filter( album = 'ACADS')
    return render(request, 'talks/acads.html', {'acad_photos':acad_photos})



#def albumchoice(request):
#    all_photos =
