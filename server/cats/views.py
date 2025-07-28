from django.shortcuts import render
from .models import Owner, Cat

from django.shortcuts import get_object_or_404

from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("<h1>Welcome to the Cat Tracker!</h1>")

def author(request):
    return HttpResponse("<h1>By wilker</h1>")

def detail(request, owner_id):
   
    #owner = Owner.objects.get(id=owner_id)
    owner = get_object_or_404(Owner, id=owner_id)
    cats = owner.cat_set.all()

    #call the template 
    context = {
        "owner": owner,
        "cats": cats
    }
    
    return render(request, "detail.html", context)

def name(request, owner_name):
   
    owner =  get_object_or_404(Owner, name = owner_name)

    return detail(request, owner.id)
  #  return HttpResponse("<h1>Owner David</h1>")

def owners(request):
   
   #collect all owners but not sally.
    owners = Owner.objects.exclude(name="sally") 

    #call the template 
    context = {
        "owners": owners,
    }
    
    return render(request, "owners.html", context)


def owner_name(request):
    print(request.GET)

    owner_name = request.GET["ownername"]

    return HttpResponse("<h1>By wilker</h1>")










def catsdetail(request, cat_id):
   
    #cats = Cat.objects.get(id=cat_id)
    cats = get_object_or_404(Cat, id=cat_id)
    #call the template 
    context = {
        "cats": cats
    }
    
    return render(request, "catdetail.html", context)
