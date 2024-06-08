from django.db import models

# Create your models here.
class Customer(models.Model):
    Full_Name = models.CharField(max_length=200)
    Address = models.CharField(max_length=400)
    CHOICES=[('Work','Work'),
         ('Home','Home'),('Other','Other')]
    Address_Type = models.CharField(max_length=20,choices=CHOICES, default = 'Work')
    Phone = models.CharField(max_length=10)
    Email = models.EmailField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)  
    Plan_Type = models.CharField(max_length=200,null=True,blank=True)
    # Feedback = models.CharField(max_length=600, null=True,blank=True)

    def __str__(self):
        return self.Full_Name
    


