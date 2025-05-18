from django.shortcuts import render,redirect ,get_object_or_404
from .models import Photo, Category

def index(request):
    categories = Category.objects.all()
    category = request.GET.get('category')
    
    if category == None:
        photos = Photo.objects.all()
    else:
        photos = Photo.objects.filter(category__name=category)
    
    context = {'photos': photos,'categories': categories }
    return render(request, 'photo/index.html',context)


def viewPhoto(request,pk):
    photo = Photo.objects.get(id=pk)
    categories = Category.objects.all()
    context = {'photo': photo,'categories': categories }
    return render(request, 'photo/view.html',context)


def addPhoto(request):
    categories = Category.objects.all()
    if request.method == "POST":
        data = request.POST
        images = request.FILES.getlist('images')
        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data['new_category'] != '':
            category, created = Category.objects.get_or_create(name=data['new_category'])
        else:
            category = None
        for image in images:
            photo = Photo.objects.create(
                description=data['description'],
                image=image,
                category=category
            )
        return redirect('index')
    context = {'categories': categories }
    return render(request, 'photo/add.html',context)


def deletePhoto(request,pk):
    photo = Photo.objects.get(id=pk)
    if request.method == 'POST':
        photo.delete()
        return redirect('index')
    context = {'photo': photo}
    return render(request, 'photo/delete.html',context)


