from django.shortcuts import render, redirect, get_object_or_404
from .forms import New_Product
from market_place.models import Product
from bid_app.models import Bid
# Create your views here.
def home(request):
    if request.user.is_authenticated:
        return render(request,'superuser_home.html',{})
    else:
        return redirect('/auth/login/')


def add_product(request):
    if request.user.is_authenticated:
        form = New_Product(request.POST or None, request.FILES or None)
        if form.is_valid():
            new = form.save(commit=False)
            new.username = request.user
            new.save()

        form = New_Product()
        context = {
            'form':form
        }
        return render(request,'add_product.html',context)
    else:
        return redirect('/auth/login/')


def products(request):
    if request.user.is_authenticated:
        active_list = Product.objects.filter(status='0').order_by('-id')
        short_term = Product.objects.filter(status='1').order_by('-id')
        close_list = Product.objects.filter(status='2').order_by('-id')
        context = {
            'active_list':active_list,
            'close':close_list,
            'short':short_term
        }
        return render(request,'super_products.html',context)
    else:
        return redirect('/auth/login/')


def view_all_bid(request,id=None):
    if request.user.is_authenticated:
        bid_list = Bid.objects.filter(product_id=id)
        product = Product.objects.get(id=id)
        context = {
            'bids':bid_list,
            'product':product
        }
        return render(request,'superuser_bid.html',context)
    else:
        return redirect('/auth/login/')



def accept_bid(request,id,p_id):
    if request.user.is_authenticated:
        instance = get_object_or_404(Bid, id=id)
        instance.status = '1'
        instance.save()

        product = get_object_or_404(Product,id=p_id)
        product.status = '2'
        product.save()

        return redirect('/superuser/products/')
    else:
        return redirect('/auth/login/')



def accepted_bids(request):
    if request.user.is_authenticated:
        list = Bid.objects.filter(status='1')
        context = {
            'list':list
        }
        return render(request,'accepted_bid.html',context)
    else:
        return redirect('/auth/login/')
