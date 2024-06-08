from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from customers.models import *
from vendorPortal.models import Vendor
from customers.models import Customer
from .forms import VendorLoginForm
all_vendors = Vendor.objects.all()

# Vendor.objects.filter(Vendor_Id = "11910616").update(Feedback = "This is my feedback")

def indexVendor(request, id):
    obj = Vendor.objects.get(Vendor_Id = id)
    customers_pk = obj.Customers_Delivering.split(',')[1:]
    customers_pk = [int(i) for i in customers_pk]
    customers = []
    for i in customers_pk:
        customers.append(Customer.objects.get(pk = i))
    
    
  



    context = {'name':obj.Vendor_Name, 'customers':customers}
    return render(request,"vendorPortal/index.html", context)

def vendorLogin(request):
    form = VendorLoginForm()
    check=0
    if request.method == "POST":
        form = VendorLoginForm(request.POST)
        if form.is_valid():
            obj = form.save()
            id = obj.Vendor_ID
            
            for obj in all_vendors:
                if obj.Vendor_Id == id:
                    check=1
                    return indexVendor(request, id)
            if check==0:   
                messages.error(request,"Invalid ID. Please try again.")


    context = {'form':form}
    return render(request, "vendorPortal/login.html",context)
