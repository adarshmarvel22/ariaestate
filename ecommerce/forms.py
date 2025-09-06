from django import forms
from accounts.models import User
from ecommerce.models import Cart
from ecommerce.models import Product
from accounts.models import User
from ecommerce.models import Order
from . import models


class CartForm(forms.ModelForm):
    class Meta:
        model = models.Cart
        fields = [
            "user",
        ]

    def __init__(self, *args, **kwargs):
        super(CartForm, self).__init__(*args, **kwargs)
        self.fields["user"].queryset = User.objects.all()



class CartItemForm(forms.ModelForm):
    class Meta:
        model = models.CartItem
        fields = [
            "quantity",
            "cart",
            "product",
        ]

    def __init__(self, *args, **kwargs):
        super(CartItemForm, self).__init__(*args, **kwargs)
        self.fields["cart"].queryset = Cart.objects.all()
        self.fields["product"].queryset = Product.objects.all()



class OrderForm(forms.ModelForm):
    class Meta:
        model = models.Order
        fields = [
            "total_amount",
            "status",
            "user",
        ]

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields["user"].queryset = User.objects.all()



class PaymentForm(forms.ModelForm):
    class Meta:
        model = models.Payment
        fields = [
            "status",
            "transaction_id",
            "amount",
            "order",
        ]

    def __init__(self, *args, **kwargs):
        super(PaymentForm, self).__init__(*args, **kwargs)
        self.fields["order"].queryset = Order.objects.all()



class ProductForm(forms.ModelForm):
    class Meta:
        model = models.Product
        fields = [
            "name",
            "image",
            "price",
            "stock",
            "description",
        ]
