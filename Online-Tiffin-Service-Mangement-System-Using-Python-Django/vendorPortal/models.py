from django.db import models

# Create your models here.
class VendorLogin(models.Model):
    Vendor_ID = models.CharField(max_length=10)


class Vendor(models.Model):
    Vendor_Id = models.CharField(max_length=10)
    Vendor_Name = models.CharField(max_length=100)
    Vendor_Phone = models.CharField(max_length=10)
    # Delivery_Type = models.CharField(max_length=30)s
    Customers_Delivering = models.CharField(max_length=200, blank=True, null=True, default ="Def")
    Total_Customers = models.IntegerField(blank=True, null=True)
    # Feedback = models.CharField(max_length=200, blank=True, null=True)
    
    def __str__(self) -> str:
        return self.Vendor_Id