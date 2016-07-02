from django.db import models
from django.contrib import admin
# from .models import Company


class Company(models.Model):
    company_name = models.CharField(max_length=50,unique=True)
    email=models.CharField(max_length=50,unique=True)
    address = models.CharField(max_length=200,unique=True)
    mobile_number = models.CharField(max_length=200,unique=True)

    def __unicode__(self):
    	return self.company_name


class Vehicle(models.Model):
    vehicle_number = models.CharField(max_length=50,unique=True)
    rc_number = models.CharField(max_length=200,unique=True)
    company=models.ForeignKey(Company)
    loading_capacity=models.CharField(max_length=50,unique=True)

    def __unicode__(self):
    	return self.vehicle_number



