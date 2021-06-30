from django import forms
from market_place.models import Product

class New_Product(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
        'company_name',
        'model',
        'sub_class',
        'year',
        'fuel_type',
        'body_type',
        'color',
        'transmission_type',
        'location',
        'registration_state',
        'driven',
        'number_of_owner',
        'condition_grade',
        'expected_price',
        'img',
        'status',
        ]
