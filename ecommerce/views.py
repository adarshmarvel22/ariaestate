from django.views import generic
from django.urls import reverse_lazy
from . import models
from . import forms


class CartListView(generic.ListView):
    model = models.Cart
    form_class = forms.CartForm


class CartCreateView(generic.CreateView):
    model = models.Cart
    form_class = forms.CartForm


class CartDetailView(generic.DetailView):
    model = models.Cart
    form_class = forms.CartForm


class CartUpdateView(generic.UpdateView):
    model = models.Cart
    form_class = forms.CartForm
    pk_url_kwarg = "pk"


class CartDeleteView(generic.DeleteView):
    model = models.Cart
    success_url = reverse_lazy("ecommerce_Cart_list")


class CartItemListView(generic.ListView):
    model = models.CartItem
    form_class = forms.CartItemForm


class CartItemCreateView(generic.CreateView):
    model = models.CartItem
    form_class = forms.CartItemForm


class CartItemDetailView(generic.DetailView):
    model = models.CartItem
    form_class = forms.CartItemForm


class CartItemUpdateView(generic.UpdateView):
    model = models.CartItem
    form_class = forms.CartItemForm
    pk_url_kwarg = "pk"


class CartItemDeleteView(generic.DeleteView):
    model = models.CartItem
    success_url = reverse_lazy("ecommerce_CartItem_list")


class OrderListView(generic.ListView):
    model = models.Order
    form_class = forms.OrderForm


class OrderCreateView(generic.CreateView):
    model = models.Order
    form_class = forms.OrderForm


class OrderDetailView(generic.DetailView):
    model = models.Order
    form_class = forms.OrderForm


class OrderUpdateView(generic.UpdateView):
    model = models.Order
    form_class = forms.OrderForm
    pk_url_kwarg = "pk"


class OrderDeleteView(generic.DeleteView):
    model = models.Order
    success_url = reverse_lazy("ecommerce_Order_list")


class PaymentListView(generic.ListView):
    model = models.Payment
    form_class = forms.PaymentForm


class PaymentCreateView(generic.CreateView):
    model = models.Payment
    form_class = forms.PaymentForm


class PaymentDetailView(generic.DetailView):
    model = models.Payment
    form_class = forms.PaymentForm


class PaymentUpdateView(generic.UpdateView):
    model = models.Payment
    form_class = forms.PaymentForm
    pk_url_kwarg = "pk"


class PaymentDeleteView(generic.DeleteView):
    model = models.Payment
    success_url = reverse_lazy("ecommerce_Payment_list")


class ProductListView(generic.ListView):
    model = models.Product
    form_class = forms.ProductForm


class ProductCreateView(generic.CreateView):
    model = models.Product
    form_class = forms.ProductForm


class ProductDetailView(generic.DetailView):
    model = models.Product
    form_class = forms.ProductForm


class ProductUpdateView(generic.UpdateView):
    model = models.Product
    form_class = forms.ProductForm
    pk_url_kwarg = "pk"


class ProductDeleteView(generic.DeleteView):
    model = models.Product
    success_url = reverse_lazy("ecommerce_Product_list")
