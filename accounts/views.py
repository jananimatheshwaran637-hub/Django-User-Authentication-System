from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

from .models import (
    Product,
    Customer,
    Supplier,
    Purchase,
    Payment,
    Billing,
    Receipt,
)

from .forms import (
    ProductForm,
    CustomerForm,
    SupplierForm,
    PurchaseForm,
    PaymentForm,
    BillingForm,
    ReceiptForm,
)


# ================= REGISTER =================

def register(request):

    if request.method == "POST":

        fullname = request.POST.get("fullname")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm = request.POST.get("confirm_password")

        if password != confirm:
            messages.error(request, "Passwords do not match")
            return redirect("register")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect("register")

        User.objects.create_user(
            username=username,
            first_name=fullname,
            email=email,
            password=password
        )

        messages.success(request, "Registration Successful")
        return redirect("login")

    return render(request, "register.html")


# ================= LOGIN =================

def login_view(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user:
            login(request, user)
            return redirect("dashboard")

        messages.error(request, "Invalid Username or Password")

    return render(request, "login.html")


# ================= LOGOUT =================

def logout_view(request):

    logout(request)
    return redirect("login")


# ================= DASHBOARD =================

@login_required
def dashboard(request):

    context = {
        "total_products": Product.objects.count(),
        "total_customers": Customer.objects.count(),
        "total_suppliers": Supplier.objects.count(),
        "total_purchase": Purchase.objects.count(),
        "total_payments": Payment.objects.count(),
        "total_billings": Billing.objects.count(),
        "total_receipts": Receipt.objects.count(),
        "total_stock": sum(
            p.stock for p in Product.objects.all()
        ),
    }

    return render(
        request,
        "dashboard.html",
        context
    )


# ================= PROFILE =================

@login_required
def profile(request):
    return render(request, "profile.html")


# ================= COMPANY PROFILE =================

@login_required
def company_profile(request):
    return render(request, "company_profile.html")


# ================= PRODUCTS =================

@login_required
def products(request):

    return render(
        request,
        "products.html",
        {
            "products": Product.objects.all()
        }
    )


@login_required
def add_product(request):

    form = ProductForm(
        request.POST or None,
        request.FILES or None
    )

    if form.is_valid():
        form.save()
        messages.success(request, "Product Added Successfully")
        return redirect("products")

    return render(
        request,
        "add_product.html",
        {"form": form}
    )


@login_required
def edit_product(request, id):

    product = get_object_or_404(Product, id=id)

    form = ProductForm(
        request.POST or None,
        request.FILES or None,
        instance=product
    )

    if form.is_valid():
        form.save()
        messages.success(request, "Product Updated Successfully")
        return redirect("products")

    return render(
        request,
        "edit_product.html",
        {"form": form}
    )


@login_required
def delete_product(request, id):

    product = get_object_or_404(Product, id=id)
    product.delete()

    messages.success(request, "Product Deleted Successfully")

    return redirect("products")


# ================= CUSTOMERS =================

@login_required
def customers(request):

    return render(
        request,
        "customers.html",
        {
            "customers": Customer.objects.all()
        }
    )


@login_required
def add_customer(request):

    form = CustomerForm(request.POST or None)

    if form.is_valid():
        form.save()
        messages.success(request, "Customer Added Successfully")
        return redirect("customers")

    return render(
        request,
        "add_customer.html",
        {"form": form}
    )


@login_required
def edit_customer(request, id):

    customer = get_object_or_404(Customer, id=id)

    form = CustomerForm(
        request.POST or None,
        instance=customer
    )

    if form.is_valid():
        form.save()
        return redirect("customers")

    return render(
        request,
        "edit_customer.html",
        {"form": form}
    )


@login_required
def delete_customer(request, id):

    customer = get_object_or_404(Customer, id=id)
    customer.delete()

    return redirect("customers")


# ================= SUPPLIERS =================

@login_required
def suppliers(request):

    return render(
        request,
        "suppliers.html",
        {
            "suppliers": Supplier.objects.all()
        }
    )


@login_required
def add_supplier(request):

    form = SupplierForm(request.POST or None)

    if form.is_valid():
        form.save()
        messages.success(request, "Supplier Added Successfully")
        return redirect("suppliers")

    return render(
        request,
        "add_supplier.html",
        {"form": form}
    )


@login_required
def edit_supplier(request, id):

    supplier = get_object_or_404(Supplier, id=id)

    form = SupplierForm(
        request.POST or None,
        instance=supplier
    )

    if form.is_valid():
        form.save()
        messages.success(request, "Supplier Updated Successfully")
        return redirect("suppliers")

    return render(
        request,
        "edit_supplier.html",
        {"form": form}
    )


@login_required
def delete_supplier(request, id):

    supplier = get_object_or_404(Supplier, id=id)
    supplier.delete()

    messages.success(request, "Supplier Deleted Successfully")

    return redirect("suppliers")


# ================= PURCHASE =================

@login_required
def purchase(request):

    return render(
        request,
        "purchase.html",
        {
            "purchases": Purchase.objects.all()
        }
    )


@login_required
def add_purchase(request):

    form = PurchaseForm(request.POST or None)

    if form.is_valid():
        form.save()
        messages.success(request, "Purchase Added Successfully")
        return redirect("purchase")

    return render(
        request,
        "add_purchase.html",
        {"form": form}
    )


@login_required
def purchase_detail(request, id):

    purchase = get_object_or_404(
        Purchase,
        id=id
    )

    return render(
        request,
        "purchase_detail.html",
        {
            "purchase": purchase
        }
    )


@login_required
def edit_purchase(request, id):

    purchase = get_object_or_404(
        Purchase,
        id=id
    )

    form = PurchaseForm(
        request.POST or None,
        instance=purchase
    )

    if form.is_valid():
        form.save()
        messages.success(request, "Purchase Updated Successfully")
        return redirect("purchase")

    return render(
        request,
        "edit_purchase.html",
        {"form": form}
    )


@login_required
def delete_purchase(request, id):

    purchase = get_object_or_404(
        Purchase,
        id=id
    )

    purchase.delete()

    messages.success(request, "Purchase Deleted Successfully")

    return redirect("purchase")

# ================= PAYMENTS =================

@login_required
def payments(request):

    payment_list = Payment.objects.all()

    return render(
        request,
        "payments.html",
        {
            "payments": payment_list
        }
    )


@login_required
def add_payment(request):

    form = PaymentForm(request.POST or None)

    if form.is_valid():
        form.save()
        messages.success(request, "Payment Added Successfully")
        return redirect("payments")

    return render(
        request,
        "add_payment.html",
        {
            "form": form
        }
    )


@login_required
def edit_payment(request, id):

    payment = get_object_or_404(
        Payment,
        id=id
    )

    form = PaymentForm(
        request.POST or None,
        instance=payment
    )

    if form.is_valid():
        form.save()
        messages.success(request, "Payment Updated Successfully")
        return redirect("payments")

    return render(
        request,
        "edit_payment.html",
        {
            "form": form
        }
    )


@login_required
def delete_payment(request, id):

    payment = get_object_or_404(
        Payment,
        id=id
    )

    payment.delete()

    messages.success(request, "Payment Deleted Successfully")

    return redirect("payments")


# ================= BILLING =================

@login_required
def billing(request):

    bill_list = Billing.objects.all()

    return render(
        request,
        "billing.html",
        {
            "billings": bill_list
        }
    )


@login_required
def add_billing(request):

    form = BillingForm(request.POST or None)

    if form.is_valid():
        form.save()
        messages.success(request, "Billing Added Successfully")
        return redirect("billing")

    return render(
        request,
        "add_billing.html",
        {
            "form": form
        }
    )


@login_required
def edit_billing(request, id):

    bill = get_object_or_404(
        Billing,
        id=id
    )

    form = BillingForm(
        request.POST or None,
        instance=bill
    )

    if form.is_valid():
        form.save()
        messages.success(request, "Billing Updated Successfully")
        return redirect("billing")

    return render(
        request,
        "edit_billing.html",
        {
            "form": form
        }
    )


@login_required
def delete_billing(request, id):

    bill = get_object_or_404(
        Billing,
        id=id
    )

    bill.delete()

    messages.success(request, "Billing Deleted Successfully")

    return redirect("billing")


# ================= RECEIPT =================

@login_required
def receipt(request):

    receipt_list = Receipt.objects.all()

    return render(
        request,
        "receipt.html",
        {
            "receipts": receipt_list
        }
    )


@login_required
def add_receipt(request):

    form = ReceiptForm(request.POST or None)

    if form.is_valid():
        form.save()
        messages.success(request, "Receipt Created Successfully")
        return redirect("receipt")

    return render(
        request,
        "add_receipt.html",
        {
            "form": form
        }
    )


@login_required
def edit_receipt(request, id):

    receipt = get_object_or_404(
        Receipt,
        id=id
    )

    form = ReceiptForm(
        request.POST or None,
        instance=receipt
    )

    if form.is_valid():
        form.save()
        messages.success(request, "Receipt Updated Successfully")
        return redirect("receipt")

    return render(
        request,
        "edit_receipt.html",
        {
            "form": form
        }
    )


@login_required
def delete_receipt(request, id):

    receipt = get_object_or_404(
        Receipt,
        id=id
    )

    receipt.delete()

    messages.success(request, "Receipt Deleted Successfully")

    return redirect("receipt")


@login_required
def print_receipt(request, id):

    receipt = get_object_or_404(
        Receipt,
        id=id
    )

    return render(
        request,
        "print_receipt.html",
        {
            "receipt": receipt
        }
    )


# ================= REPORTS =================

# ================= REPORTS =================

@login_required
def reports(request):

    context = {
        "products": Product.objects.all(),
        "customers": Customer.objects.all(),
        "suppliers": Supplier.objects.all(),
        "purchases": Purchase.objects.all(),
        "payments": Payment.objects.all(),
        "billings": Billing.objects.all(),
        "receipts": Receipt.objects.all(),

        "total_products": Product.objects.count(),
        "total_customers": Customer.objects.count(),
        "total_suppliers": Supplier.objects.count(),
        "total_purchases": Purchase.objects.count(),
        "total_payments": Payment.objects.count(),
        "total_billings": Billing.objects.count(),
        "total_receipts": Receipt.objects.count(),
    }

    return render(
        request,
        "reports.html",
        context
    )


# ================= SETTINGS =================

@login_required
def settings_page(request):
    return render(request, "settings.html")


@login_required
def profile(request):
    return render(request, "profile.html")


# ================= CHANGE PASSWORD =================

@login_required
def change_password(request):

    if request.method == "POST":

        form = PasswordChangeForm(
            request.user,
            request.POST
        )

        if form.is_valid():

            user = form.save()

            update_session_auth_hash(
                request,
                user
            )

            messages.success(
                request,
                "Password Changed Successfully"
            )

            return redirect("settings")

    else:

        form = PasswordChangeForm(
            request.user
        )

    return render(
        request,
        "change_password.html",
        {
            "form": form
        }
    )
    
