from django.shortcuts import render
from market_place.models import Product
from .models import Detail,Team_member, Working_process
# Create your views here.
def home(request):
    short = Product.objects.filter(status=1)
    process = Working_process.objects.all()
    context = {
        'product': short,
        'process': process
    }
    return render(request,'landing.html',context)

def about(request):
    about = Detail.objects.get()
    team = Team_member.objects.all()
    context = {
        'about':about,
        'team':team
    }
    return render(request,'about.html',context)
