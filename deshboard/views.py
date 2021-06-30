from django.shortcuts import render, redirect,get_object_or_404
from bid_app.models import Bid
# Create your views here.
def desh(request):
    if request.user.is_authenticated:
        user_bids = Bid.objects.filter(bid_by = request.user.id)
        context = {
            'bids': user_bids,
            'user': request.user
        }
        return render(request,'desh.html',context)
    else:
        return redirect('/auth/login/')
