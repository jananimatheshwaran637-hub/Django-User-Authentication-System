from django.urls import path
from django.shortcuts import redirect
from . import views


urlpatterns = [

    # Home
    path(
        '',
        lambda request: redirect('dashboard')
    ),


    # Authentication

    path(
        'register/',
        views.register,
        name='register'
    ),

    path(
        'login/',
        views.login_view,
        name='login'
    ),

    path(
        'logout/',
        views.logout_view,
        name='logout'
    ),



    # Dashboard

    path(
        'dashboard/',
        views.dashboard,
        name='dashboard'
    ),



    # Profile

    path(
        'profile/',
        views.profile,
        name='profile'
    ),


    # Company Profile

    path(
        'company-profile/',
        views.company_profile,
        name='company_profile'
    ),



    # Products CRUD

    path(
        'products/',
        views.products,
        name='products'
    ),

    path(
        'add-product/',
        views.add_product,
        name='add_product'
    ),

    path(
        'edit-product/<int:id>/',
        views.edit_product,
        name='edit_product'
    ),

    path(
        'delete-product/<int:id>/',
        views.delete_product,
        name='delete_product'
    ),



    # Customers CRUD

    path(
        'customers/',
        views.customers,
        name='customers'
    ),

    path(
        'add-customer/',
        views.add_customer,
        name='add_customer'
    ),

    path(
        'edit-customer/<int:id>/',
        views.edit_customer,
        name='edit_customer'
    ),

    path(
        'delete-customer/<int:id>/',
        views.delete_customer,
        name='delete_customer'
    ),



    # Suppliers CRUD

    path(
        'suppliers/',
        views.suppliers,
        name='suppliers'
    ),

    path(
        'add-supplier/',
        views.add_supplier,
        name='add_supplier'
    ),

    path(
        'edit-supplier/<int:id>/',
        views.edit_supplier,
        name='edit_supplier'
    ),

    path(
        'delete-supplier/<int:id>/',
        views.delete_supplier,
        name='delete_supplier'
    ),



    # Purchase CRUD

    path(
        'purchase/',
        views.purchase,
        name='purchase'
    ),

    path(
        'add-purchase/',
        views.add_purchase,
        name='add_purchase'
    ),

    path(
        'purchase-detail/<int:id>/',
        views.purchase_detail,
        name='purchase_detail'
    ),

    path(
        'edit-purchase/<int:id>/',
        views.edit_purchase,
        name='edit_purchase'
    ),

    path(
        'delete-purchase/<int:id>/',
        views.delete_purchase,
        name='delete_purchase'
    ),



    # Payment CRUD

    path(
        'payments/',
        views.payments,
        name='payments'
    ),

    path(
        'add-payment/',
        views.add_payment,
        name='add_payment'
    ),

    path(
        'edit-payment/<int:id>/',
        views.edit_payment,
        name='edit_payment'
    ),

    path(
        'delete-payment/<int:id>/',
         views.delete_payment,
        name='delete_payment'
    ),



    # Billing CRUD

    path(
        'billing/',
        views.billing,
        name='billing'
    ),

    path(
        'add-billing/',
        views.add_billing,
        name='add_billing'
    ),

    path(
        'edit-billing/<int:id>/',
        views.edit_billing,
        name='edit_billing'
    ),

    path(
        'delete-billing/<int:id>/',
        views.delete_billing,
        name='delete_billing'
    ),



    # Receipt CRUD

    path(
        'receipt/',
        views.receipt,
        name='receipt'
    ),

    path(
        'add-receipt/',
        views.add_receipt,
        name='add_receipt'
    ),

    path(
        'edit-receipt/<int:id>/',
        views.edit_receipt,
        name='edit_receipt'
    ),

    path(
        'delete-receipt/<int:id>/',
        views.delete_receipt,
        name='delete_receipt'
    ),

    path(
        'print-receipt/<int:id>/',
        views.print_receipt,
        name='print_receipt'
    ),



    # Reports

    path(
        'reports/',
        views.reports,
        name='reports'
    ),



    # Settings

path(
    'settings/',
    views.settings_page,
    name='settings'
),



path(
    'change-password/',
    views.change_password,
    name='change_password'
),


]