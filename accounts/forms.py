from django import forms

from django.contrib.auth.models import User

from .models import (
    Employee,
    Product,
    Customer,
    Supplier,
    Purchase,
    Payment,
    Billing,
    Receipt
)


# ---------------- Profile Form ----------------



# ---------------- Employee Form ----------------

class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee

        fields = '__all__'

        widgets = {
            'joining_date': forms.DateInput(
                attrs={'type': 'date'}
            ),
        }



# ---------------- Product Form ----------------

class ProductForm(forms.ModelForm):

    class Meta:

        model = Product

        fields = [
            'name',
            'unit',
            'price',
            'gst',
            'stock',
            'image',
        ]

        widgets = {

            'name': forms.TextInput(
                attrs={'class':'form-control'}
            ),

            'unit': forms.TextInput(
                attrs={'class':'form-control'}
            ),

            'price': forms.NumberInput(
                attrs={'class':'form-control'}
            ),

            'gst': forms.NumberInput(
                attrs={'class':'form-control'}
            ),

            'stock': forms.NumberInput(
                attrs={'class':'form-control'}
            ),

            'image': forms.FileInput(
                attrs={'class':'form-control'}
            ),
        }



# ---------------- Customer Form ----------------

class CustomerForm(forms.ModelForm):

    class Meta:

        model = Customer

        fields = [
            'name',
            'phone',
            'email',
            'address',
        ]

        widgets = {

            'name': forms.TextInput(
                attrs={'class':'form-control'}
            ),

            'phone': forms.TextInput(
                attrs={'class':'form-control'}
            ),

            'email': forms.EmailInput(
                attrs={'class':'form-control'}
            ),

            'address': forms.Textarea(
                attrs={
                    'class':'form-control',
                    'rows':3
                }
            ),
        }



# ---------------- Supplier Form ----------------

class SupplierForm(forms.ModelForm):

    class Meta:

        model = Supplier

        fields = [
            'name',
            'phone',
            'email',
            'address',
        ]

        widgets = {

            'name': forms.TextInput(
                attrs={'class':'form-control'}
            ),

            'phone': forms.TextInput(
                attrs={'class':'form-control'}
            ),

            'email': forms.EmailInput(
                attrs={'class':'form-control'}
            ),

            'address': forms.Textarea(
                attrs={
                    'class':'form-control',
                    'rows':3
                }
            ),
        }
    


class PurchaseForm(forms.ModelForm):

    class Meta:

        model = Purchase

        fields = [
            'supplier',
            'product',
            'quantity',
            'purchase_price',
            'total_amount',
        ]
        
    


class PaymentForm(forms.ModelForm):

    class Meta:

        model = Payment

        fields = [
            'customer_name',
            'payment_type',
            'amount',
            'description'
        ]
        
       


class BillingForm(forms.ModelForm):

    class Meta:

        model = Billing

        fields = [
            'customer_name',
            'invoice_no',
            'product_name',
            'quantity',
            'amount',
            'gst',
            'total_amount'
        ]
        
    
    
  


class ReceiptForm(forms.ModelForm):

    class Meta:
        model = Receipt

        fields = [
            'customer_name',
            'product_name',
            'quantity',
            'amount',
        ]