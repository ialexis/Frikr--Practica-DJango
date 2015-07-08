from django.http import HttpResponse, HttpResponseNotFound
from photos.models import Photo, PUBLIC
from django.shortcuts import render

# Create your views here.
def home(request):
    ###photos = Photo.objects.all().order_by('-createdAt')
    photos = Photo.objects.filter(visibility=PUBLIC).order_by('-createdAt')
    context = {
       'photos_list': photos[:5]

    }

    return render(request,'photos/home.html',context)


def detail(request, pk):

    possible_photos = Photo.objects.filter(pk=pk)
    photo=possible_photos[0] if len(possible_photos) == 1 else None
    if photo is not None:
        #cargar plantilla detalle
        context = {
            'photo': photo
        }
        return render(request,'photos/detail.html',context)
    else:
        return HttpResponseNotFound('No existe la foto')
