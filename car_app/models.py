from datetime import datetime

from django.db import models

# Create your models here.


class Car(models.Model):
    car_company = models.CharField(max_length=200)
    car_rent = models.FloatField()
    car_kilometers = models.FloatField()
    car_last_rented = models.DateField()
    car_condition = models.CharField(max_length=200)
    car_status = models.CharField(max_length=200)
    image = models.ImageField(upload_to='uploads/products/')

    def __str__(self):
        return self.car_company


class Customer(models.Model):
    cus_name = models.CharField(max_length=200)
    cus_phone = models.IntegerField(default=0)
    rented_car = models.ForeignKey(Car, on_delete=models.CASCADE)
    date_rented = models.DateField()
    date_returned = models.DateField()
    cus_status = models.CharField(max_length=200)

    def __str__(self):
        return self.cus_name

class logs(models.Model):
    userid = models.FloatField()
    carid = models.FloatField()
    rentedDate = models.DateField(default=datetime.now(), blank=True)
    returnDate = models.DateField(auto_now_add=True, blank=True)

    #def register(self):
       # self.save()



# Create your models here.
