from django.db.models import fields
from django.forms import ModelForm
from .models import *

class VendorLoginForm(ModelForm):
    class Meta:
        model = VendorLogin
        fields = "__all__"

