from django.shortcuts import render, redirect
from .models import bhagtan

# Create your views here.
def home(request):
    myteam = bhagtan.objects.all()
    return render(request,'home.html', {'myteam': myteam})


def add_members(request):
    if request.method == "GET":
        return render(request, 'add.html')
    else:
        bhagtan (
            firstname = request.POST.get('fname'),
            lastname = request.POST.get('lname'),
            age = request.POST.get('age'),
            singer = request.POST.get('singer'),
        ) .save()
        return redirect('home')
    
def update_members(request, pk):
    team = bhagtan.objects.get(pk=pk)    
    if request.method == "GET":
        return render(request, 'update.html', {'team': team})
    else:
        team.firstname = request.POST.get('fname')
        team.lastname = request.POST.get('lname')
        team.age = request.POST.get('age')
        team.singer = request.POST.get('singer')
        team.save()
        return redirect('home')
    
def delete_members(request, pk):   
    teams = bhagtan.objects.get(pk=pk)
    if request.method == "POST":
        teams.delete()
        return redirect('home')
    return render(request, 'delete.html', {'teams': teams})
    
    
    
    