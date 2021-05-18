from django.contrib import messages
from django.shortcuts import render , redirect

from frontoffice.models import *
from frontoffice.forms import materielForm


def login(request):
    if request.method=="POST":
        try:
            Userdetails=user.objects.get(Email=request.POST['Email'],Pwd=request.POST['pwd'])
            print("lastname=",Userdetails)
            request.session["Email"]=Userdetails.Email
            return render(request,"authentification/index.html")
        except user.DoesNotExist as e:
            messages.success(request,"Username OR password Invalid ..!")
    return render(request, "authentification/login.html")

def register(request):
    if request.method == 'POST':
        Firstname = request.POST['firstname']
        Lastname = request.POST['lastname']
        Email = request.POST['mail']
        Pwd = request.POST['pwd']


        user(Firstname=Firstname, Lastname=Lastname,Email=Email, Pwd=Pwd).save()
        messages.success(request, "The new user is added successfully")
        return render(request, "authentification/register.html")
    else:
        return render(request,"authentification/register.html")

def index(request):
    return render(request,"authentification/index.html")

def updateMateriel(request, id=0):
    if id == 0 :
        form=materielForm()
    else:
        m=materiel.objects.get(id=id)
        form = materielForm(instance=m)
    if request.method== 'POST':
        form=materielForm(request.POST)
        if form.is_valid():
           form.save()
           return  redirect('Materiels')
        else:
            messages.error(request, 'Error !!')
    return render(request,"UpdateMateriel.html",locals())

def ajouter(request):

    return render(request,"UpdateMateriel.html")

def getMateriels(request):
    materiels = materiel.objects.all()
    return render(request,'listMateriel.html', {'mate':materiels})

def deleteMat(request, id):
    materiel.objects.get(id=id).delete()
    return redirect('/Materiels')
# Create your views here.
