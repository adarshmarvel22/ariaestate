from django.contrib import admin
from django import forms

from . import models


class CartAdminForm(forms.ModelForm):

    class Meta:
        model = models.Cart
        fields = "__all__"


class CartAdmin(admin.ModelAdmin):
    form = CartAdminForm
    list_display = [
        "id",
        "created",
        "last_updated",
    ]
    readonly_fields = [
        "id",
        "created",
        "last_updated",
    ]


class CartItemAdminForm(forms.ModelForm):

    class Meta:
        model = models.CartItem
        fields = "__all__"


class CartItemAdmin(admin.ModelAdmin):
    form = CartItemAdminForm
    list_display = [
        "last_updated",
        "quantity",
        "created",
        "id",
    ]
    readonly_fields = [
        "last_updated",
        "quantity",
        "created",
        "id",
    ]


class OrderAdminForm(forms.ModelForm):

    class Meta:
        model = models.Order
        fields = "__all__"


class OrderAdmin(admin.ModelAdmin):
    form = OrderAdminForm
    list_display = [
        "created",
        "id",
        "total_amount",
        "last_updated",
        "status",
    ]
    readonly_fields = [
        "created",
        "id",
        "total_amount",
        "last_updated",
        "status",
    ]


class PaymentAdminForm(forms.ModelForm):

    class Meta:
        model = models.Payment
        fields = "__all__"


class PaymentAdmin(admin.ModelAdmin):
    form = PaymentAdminForm
    list_display = [
        "status",
        "transaction_id",
        "last_updated",
        "payment_date",
        "amount",
        "id",
        "created",
    ]
    readonly_fields = [
        "status",
        "transaction_id",
        "last_updated",
        "payment_date",
        "amount",
        "id",
        "created",
    ]


class ProductAdminForm(forms.ModelForm):

    class Meta:
        model = models.Product
        fields = "__all__"


class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm
    list_display = [
        "name",
        "image",
        "last_updated",
        "price",
        "created",
        "stock",
        "description",
        "id",
    ]
    readonly_fields = [
        "name",
        "image",
        "last_updated",
        "price",
        "created",
        "stock",
        "description",
        "id",
    ]


admin.site.register(models.Cart, CartAdmin)
admin.site.register(models.CartItem, CartItemAdmin)
admin.site.register(models.Order, OrderAdmin)
admin.site.register(models.Payment, PaymentAdmin)
admin.site.register(models.Product, ProductAdmin)
