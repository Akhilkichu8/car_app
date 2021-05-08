from django.db import models

# Create your models here.


class Car(models.Model):
    car_company = models.CharField(max_length=200)
    car_rent = models.FloatField()
    car_kilometers = models.FloatField()
    car_last_rented = models.DateField()
    car_condition = models.CharField(max_length=200)
    car_status = models.CharField(max_length=200)

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


# Create your models here.
