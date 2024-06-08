from django.urls import path
from . import views
urlpatterns = [
  
   path("", views.PlanSelection, name="PlanSelect"),
   path("customerCredentials/",views.TwoWeekVegPlan,name="TwoWeekVeg"),
   path("thankyou/",views.LastPage,name="LastPage"),
   path("FreeTrials/",views.Free, name="Free"),
   path("OneMonthVeg/",views.OneMonthVeg, name="OneMonthVeg"),
   path("OneMonthVegNonVeg/",views.OneMonthVegNonVeg, name="OneMonthVegNonVeg"),
   path("ThreeMonthVeg/",views.ThreeMonthVeg, name="ThreeMonthVeg"),
   path("ThreeMonthVegNonveg/",views.ThreeMonthVegNonveg, name="ThreeMonthVegNonveg"),
   

]
