from django.contrib import admin
from .models import Vehicle,Company
# Register your models here.
class DesignVehicle(admin.ModelAdmin):
    list_display=['id','vehicle_number','rc_number','company','loading_capacity']
    # prepopulated_fields = {"slug": ("tag_name",)}
    # class Met

class DesignCompany(admin.ModelAdmin):
    list_display=['id','company_name','email','address','mobile_number']
    # prepopulated_fields = {"slug": ("tag_name",)}
    # class Met

admin.site.register(Vehicle,DesignVehicle)
admin.site.register(Company,DesignCompany)
