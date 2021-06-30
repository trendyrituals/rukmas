from django.shortcuts import render,redirect,get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Product
# Create your views here.
def product_list(request):
    # if request.user.is_authenticated:
    user = request.user
    product_list = Product.objects.all().exclude(status='2').order_by('-id')
    paginator = Paginator(product_list, 30) # Show 30 contacts per page

    page = request.GET.get('page')
    try:
    	list = paginator.page(page)
    except PageNotAnInteger:
    # If page is not an integer, deliver first page.
    	list = paginator.page(1)
    except EmptyPage:
    # If page is out of range (e.g. 9999), deliver last page of results.
    	list = paginator.page(paginator.num_pages)

    context = {
        'user':user,
        'list':list
    }
    return render(request,'product_list.html',context)
    # else:
        # return redirect('/auth/login')

def product_view(request,id=None):
    # if request.user.is_authenticated:
    item = get_object_or_404(Product,id=id)
    context={
        'item':item
    }
    return render(request,'product_view.html',context)
    # else:
        # return redirect('/auth/login')
