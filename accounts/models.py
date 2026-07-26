from django.db import models


# ---------------- User ----------------




# ---------------- Employee ----------------

class Employee(models.Model):

    name = models.CharField(max_length=100)

    employee_id = models.CharField(
        max_length=20,
        unique=True
    )

    department = models.CharField(max_length=100)

    designation = models.CharField(max_length=100)

    salary = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    phone = models.CharField(max_length=15)

    email = models.EmailField()

    address = models.TextField()

    photo = models.ImageField(
        upload_to='employees/',
        blank=True,
        null=True
    )

    joining_date = models.DateField()


    def __str__(self):
        return self.name



# ---------------- Company ----------------

class Company(models.Model):

    company_name = models.CharField(max_length=200)

    owner_name = models.CharField(max_length=100)

    email = models.EmailField()

    phone = models.CharField(max_length=15)

    gst = models.CharField(
        max_length=50,
        blank=True,
        null=True
    )

    pan = models.CharField(
        max_length=50,
        blank=True,
        null=True
    )

    address = models.TextField()

    logo = models.ImageField(
        upload_to='company_logo/',
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )


    def __str__(self):
        return self.company_name



# ---------------- Product ----------------

class Product(models.Model):

    name = models.CharField(max_length=100)

    unit = models.CharField(max_length=50)

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    gst = models.IntegerField(default=0)

    stock = models.IntegerField(default=0)

    image = models.ImageField(
        upload_to='products/',
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )


    def __str__(self):
        return self.name



# ---------------- Customer ----------------

class Customer(models.Model):

    name = models.CharField(
        max_length=100
    )

    phone = models.CharField(
        max_length=15
    )

    email = models.EmailField(
        blank=True,
        null=True
    )

    address = models.TextField(
        blank=True
    )


    def __str__(self):
        return self.name



# ---------------- Supplier ----------------

class Supplier(models.Model):

    name = models.CharField(
        max_length=100
    )

    phone = models.CharField(
        max_length=15
    )

    email = models.EmailField(
        blank=True,
        null=True
    )

    address = models.TextField(
        blank=True
    )


    def __str__(self):
        return self.name
    
    # ================= PURCHASE =================

class Purchase(models.Model):

    supplier = models.ForeignKey(
        Supplier,
        on_delete=models.CASCADE
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )

    quantity = models.IntegerField()

    purchase_price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    total_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    purchase_date = models.DateField(
        auto_now_add=True
    )


    def __str__(self):
        return self.product.name
    
    # ================= PAYMENTS =================

class Payment(models.Model):

    PAYMENT_TYPE = (
        ('Received','Received'),
        ('Paid','Paid'),
    )


    customer_name = models.CharField(
        max_length=100
    )

    payment_type = models.CharField(
        max_length=20,
        choices=PAYMENT_TYPE
    )

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    payment_date = models.DateField(
        auto_now_add=True
    )

    description = models.TextField(
        blank=True
    )


    def __str__(self):

        return self.customer_name
    
    # ================= BILLING =================

# ================= BILLING =================

class Billing(models.Model):

    customer_name = models.CharField(
        max_length=100
    )

    invoice_no = models.CharField(
        max_length=50,
        unique=True
    )

    product_name = models.CharField(
        max_length=100
    )

    quantity = models.IntegerField(
        default=1
    )

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    gst = models.IntegerField(
        default=0
    )

    total_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    billing_date = models.DateField(
        auto_now_add=True
    )


    def __str__(self):

        return self.invoice_no



# ================= RECEIPT =================

class Receipt(models.Model):

    customer_name = models.CharField(
        max_length=100
    )

    product_name = models.CharField(
        max_length=100
    )

    quantity = models.IntegerField(
        default=1
    )

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    date = models.DateTimeField(
        auto_now_add=True
    )


    def __str__(self):

        return self.customer_name