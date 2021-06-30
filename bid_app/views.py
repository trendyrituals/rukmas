from django.shortcuts import render,get_object_or_404, redirect
from market_place.models import Product
from .forms import BidForm
from .models import Bid
# Create your views here.
def entry_bid(request,product_id=None):
    if request.user.is_authenticated:
        product = get_object_or_404(Product, id = product_id)
        form = BidForm(request.POST or None)
        if form.is_valid():
            amt = form.cleaned_data.get('bid_amt')
            if int(amt) > int(product.expected_price):
                instance = Bid()
                instance.bid_by = request.user.id
                instance.product_id = product.id
                instance.bid_amt = amt
                instance.status = '0'
                instance.save()
                return redirect('/market_place/')
            else:
                return redirect('/bid/'+str(product.id))
        form = BidForm()
        context ={
            'product':product,
            'form':form
        }
        return render(request,'entry_bid.html',context)
    else:
        return redirect('/auth/login')
