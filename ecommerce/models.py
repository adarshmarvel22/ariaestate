from django.db import models
from django.urls import reverse


class Cart(models.Model):

    # Relationships
    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE)

    # Fields
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("ecommerce_Cart_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("ecommerce_Cart_update", args=(self.pk,))

    @staticmethod
    def get_htmx_create_url():
        return reverse("ecommerce_Cart_htmx_create")

    def get_htmx_delete_url(self):
        return reverse("ecommerce_Cart_htmx_delete", args=(self.pk,))


class CartItem(models.Model):

    # Relationships
    cart = models.ForeignKey("ecommerce.Cart", on_delete=models.CASCADE)
    product = models.ForeignKey("ecommerce.Product", on_delete=models.CASCADE)

    # Fields
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    quantity = models.PositiveIntegerField()
    created = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("ecommerce_CartItem_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("ecommerce_CartItem_update", args=(self.pk,))

    @staticmethod
    def get_htmx_create_url():
        return reverse("ecommerce_CartItem_htmx_create")

    def get_htmx_delete_url(self):
        return reverse("ecommerce_CartItem_htmx_delete", args=(self.pk,))


class Order(models.Model):

    # Relationships
    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE)

    # Fields
    created = models.DateTimeField(auto_now_add=True, editable=False)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    status = models.CharField(max_length=30, default="Pending")

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("ecommerce_Order_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("ecommerce_Order_update", args=(self.pk,))

    @staticmethod
    def get_htmx_create_url():
        return reverse("ecommerce_Order_htmx_create")

    def get_htmx_delete_url(self):
        return reverse("ecommerce_Order_htmx_delete", args=(self.pk,))


class Payment(models.Model):

    # Relationships
    order = models.ForeignKey("ecommerce.Order", on_delete=models.CASCADE)

    # Fields
    status = models.CharField(max_length=30)
    transaction_id = models.CharField(max_length=30)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    payment_date = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("ecommerce_Payment_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("ecommerce_Payment_update", args=(self.pk,))

    @staticmethod
    def get_htmx_create_url():
        return reverse("ecommerce_Payment_htmx_create")

    def get_htmx_delete_url(self):
        return reverse("ecommerce_Payment_htmx_delete", args=(self.pk,))


class Product(models.Model):

    # Fields
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to="images/")
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    stock = models.PositiveIntegerField()
    description = models.TextField(max_length=100)

    class Meta:
        pass

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("ecommerce_Product_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("ecommerce_Product_update", args=(self.pk,))

    @staticmethod
    def get_htmx_create_url():
        return reverse("ecommerce_Product_htmx_create")

    def get_htmx_delete_url(self):
        return reverse("ecommerce_Product_htmx_delete", args=(self.pk,))
