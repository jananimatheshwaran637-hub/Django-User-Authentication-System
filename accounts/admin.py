from django.contrib import admin
from .models import Employee, Company, Product, Customer, Supplier, Purchase, Payment, Billing, Receipt


admin.site.register(Employee)
admin.site.register(Company)
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Supplier)
admin.site.register(Purchase)
admin.site.register(Payment)
admin.site.register(Billing)
admin.site.register(Receipt)