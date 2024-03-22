import django.utils.datastructures
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Mod


# Create your views here.

def index_view(request):
    mods = list(Mod.objects.all().values())
    return render(request, 'index.html', {'mods': mods})

def info_view(request,id):
    Mobj = Mod.objects
    mod = list(Mobj.filter(id=id).values())
    if len(mod) == 0:
        return HttpResponse('<script>window.alert("未找到此mod！");window.location.replace("../../")</script>',
                            status=404)
    else:
        mod = mod[0]
    return render(request, 'info.html', {'mod': mod})

def info_404(request):
    return HttpResponse('<script>window.alert("请输入mod编号！");window.location.replace("../")</script>', status=404)

def api(request):
    mods = str(list(Mod.objects.all().values()))
    return HttpResponse(mods)