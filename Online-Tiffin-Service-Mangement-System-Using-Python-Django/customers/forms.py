from django.db.models import fields
from django.forms import ModelForm
from .models import *

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['Full_Name','Address','Address_Type','Phone','Email']



