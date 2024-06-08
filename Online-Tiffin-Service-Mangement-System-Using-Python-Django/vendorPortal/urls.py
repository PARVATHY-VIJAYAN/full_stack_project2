from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    # path('',views.indexVendor, name="VendorIndex"),
    path('',views.vendorLogin, name="VendorLogin"),
    path('vendorDeliveries/',views.indexVendor, name="IndexVendor")
    ]