from django.contrib import admin
from .models import Car, Customer


class CarAdmin(admin.ModelAdmin):
    list_display = ('car_company', 'car_rent', 'car_kilometers',
                    'car_last_rented', 'car_condition', 'car_status')


# Register your models here.
admin.site.register(Car, CarAdmin)
admin.site.register(Customer)

# Register your models here.
