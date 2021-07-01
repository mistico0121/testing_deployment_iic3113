from django.shortcuts import render, get_object_or_404, redirect
from .models import Videocall, Survey
from .forms import SurveyForm
import requests
import environ
from time import sleep
from threading import Thread

#VIDEOLLAMADAS

def videocall_index_view(request):
    queryset = Videocall.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, "videocall/index.html", context)

def videocall_create():
    env = environ.Env()
    environ.Env.read_env()
    videocall_url = env('VIDEOCALL_URL')
    sleep(1)
    req = requests.get(f'{videocall_url}/API')
    link = f'{videocall_url}/' + str(req.content).replace("b", "", 1).strip("'")
    new_call = Videocall(url=link)
    new_call.save()

def videocall_middleware(request):
    create = Thread(target=videocall_create)
    create.start()
    return redirect('http://localhost:3000')

def videocall_delete(request, data):
    obj = Videocall.objects.get(pk=data)
    url = obj.url
    obj.delete()
    return redirect(url)

#ENCUESTAS

def surveys(request):
    queryset = Survey.objects.all()[::-1][:10]
    suma_calidad = 0
    suma_utilidad = 0
    for i in queryset:
        suma_calidad += i.quality_rating
        suma_utilidad += i.usefullness_rating
    context = {
        'object_list': queryset,
        'mean_quality_rating': round(suma_calidad/len(queryset), 2),
        'mean_usefullness_rating': round(suma_utilidad/len(queryset), 2)
    }
    return render(request, "videocall/surveys.html", context)

def survey_create(request):
    form = SurveyForm(request.POST or None)
    if form.is_valid():
        fcc_form = form.save(commit=True)
        return render(request, "home.html", {})
    context = {
        'form': form
    }
    return render(request, "videocall/new.html", context)
