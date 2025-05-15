from django.shortcuts import render,redirect
from .models import Photo, Category
from .forms import PhotoForm

def index(request):
    photos = Photo.objects.all()
    categories = Category.objects.all()
    context = {'photos': photos,'categories': categories }
    return render(request, 'photo/index.html',context)


def viewPhoto(request,pk):
    photo = Photo.objects.get(id=pk)
    categories = Category.objects.all()
    context = {'photo': photo,'categories': categories }
    return render(request, 'photo/view.html',context)


def addPhoto(request):
    form = PhotoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('index')
    context = {'form': form}
    return render(request, 'photo/add.html',context)


def deletePhoto(request,pk):
    photo = Photo.objects.get(id=pk)
    if request.method == 'POST':
        photo.delete()
        return redirect('index')
    context = {'photo': photo}
    return render(request, 'photo/delete.html',context)