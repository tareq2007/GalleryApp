from django.shortcuts import render

def index(request):
    return render(request, 'photo/index.html')


def viewPhoto(request,pk):
    return render(request, 'photo/view.html')


def addPhoto(request):
    return render(request, 'photo/add.html')
