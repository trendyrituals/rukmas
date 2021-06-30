from django import forms

class BidForm(forms.Form):
    bid_amt = forms.CharField()
    
