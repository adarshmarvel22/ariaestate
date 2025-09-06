from django.urls import path, include
from rest_framework import routers

from . import api
from . import views
from . import htmx


router = routers.DefaultRouter()
router.register("Cart", api.CartViewSet)
router.register("CartItem", api.CartItemViewSet)
router.register("Order", api.OrderViewSet)
router.register("Payment", api.PaymentViewSet)
router.register("Product", api.ProductViewSet)

urlpatterns = (
    path("api/v1/", include(router.urls)),
    path("ecommerce/Cart/", views.CartListView.as_view(), name="ecommerce_Cart_list"),
    path("ecommerce/Cart/create/", views.CartCreateView.as_view(), name="ecommerce_Cart_create"),
    path("ecommerce/Cart/detail/<int:pk>/", views.CartDetailView.as_view(), name="ecommerce_Cart_detail"),
    path("ecommerce/Cart/update/<int:pk>/", views.CartUpdateView.as_view(), name="ecommerce_Cart_update"),
    path("ecommerce/Cart/delete/<int:pk>/", views.CartDeleteView.as_view(), name="ecommerce_Cart_delete"),
    path("ecommerce/CartItem/", views.CartItemListView.as_view(), name="ecommerce_CartItem_list"),
    path("ecommerce/CartItem/create/", views.CartItemCreateView.as_view(), name="ecommerce_CartItem_create"),
    path("ecommerce/CartItem/detail/<int:pk>/", views.CartItemDetailView.as_view(), name="ecommerce_CartItem_detail"),
    path("ecommerce/CartItem/update/<int:pk>/", views.CartItemUpdateView.as_view(), name="ecommerce_CartItem_update"),
    path("ecommerce/CartItem/delete/<int:pk>/", views.CartItemDeleteView.as_view(), name="ecommerce_CartItem_delete"),
    path("ecommerce/Order/", views.OrderListView.as_view(), name="ecommerce_Order_list"),
    path("ecommerce/Order/create/", views.OrderCreateView.as_view(), name="ecommerce_Order_create"),
    path("ecommerce/Order/detail/<int:pk>/", views.OrderDetailView.as_view(), name="ecommerce_Order_detail"),
    path("ecommerce/Order/update/<int:pk>/", views.OrderUpdateView.as_view(), name="ecommerce_Order_update"),
    path("ecommerce/Order/delete/<int:pk>/", views.OrderDeleteView.as_view(), name="ecommerce_Order_delete"),
    path("ecommerce/Payment/", views.PaymentListView.as_view(), name="ecommerce_Payment_list"),
    path("ecommerce/Payment/create/", views.PaymentCreateView.as_view(), name="ecommerce_Payment_create"),
    path("ecommerce/Payment/detail/<int:pk>/", views.PaymentDetailView.as_view(), name="ecommerce_Payment_detail"),
    path("ecommerce/Payment/update/<int:pk>/", views.PaymentUpdateView.as_view(), name="ecommerce_Payment_update"),
    path("ecommerce/Payment/delete/<int:pk>/", views.PaymentDeleteView.as_view(), name="ecommerce_Payment_delete"),
    path("ecommerce/Product/", views.ProductListView.as_view(), name="ecommerce_Product_list"),
    path("ecommerce/Product/create/", views.ProductCreateView.as_view(), name="ecommerce_Product_create"),
    path("ecommerce/Product/detail/<int:pk>/", views.ProductDetailView.as_view(), name="ecommerce_Product_detail"),
    path("ecommerce/Product/update/<int:pk>/", views.ProductUpdateView.as_view(), name="ecommerce_Product_update"),
    path("ecommerce/Product/delete/<int:pk>/", views.ProductDeleteView.as_view(), name="ecommerce_Product_delete"),

    path("ecommerce/htmx/Cart/", htmx.HTMXCartListView.as_view(), name="ecommerce_Cart_htmx_list"),
    path("ecommerce/htmx/Cart/create/", htmx.HTMXCartCreateView.as_view(), name="ecommerce_Cart_htmx_create"),
    path("ecommerce/htmx/Cart/delete/<int:pk>/", htmx.HTMXCartDeleteView.as_view(), name="ecommerce_Cart_htmx_delete"),
    path("ecommerce/htmx/CartItem/", htmx.HTMXCartItemListView.as_view(), name="ecommerce_CartItem_htmx_list"),
    path("ecommerce/htmx/CartItem/create/", htmx.HTMXCartItemCreateView.as_view(), name="ecommerce_CartItem_htmx_create"),
    path("ecommerce/htmx/CartItem/delete/<int:pk>/", htmx.HTMXCartItemDeleteView.as_view(), name="ecommerce_CartItem_htmx_delete"),
    path("ecommerce/htmx/Order/", htmx.HTMXOrderListView.as_view(), name="ecommerce_Order_htmx_list"),
    path("ecommerce/htmx/Order/create/", htmx.HTMXOrderCreateView.as_view(), name="ecommerce_Order_htmx_create"),
    path("ecommerce/htmx/Order/delete/<int:pk>/", htmx.HTMXOrderDeleteView.as_view(), name="ecommerce_Order_htmx_delete"),
    path("ecommerce/htmx/Payment/", htmx.HTMXPaymentListView.as_view(), name="ecommerce_Payment_htmx_list"),
    path("ecommerce/htmx/Payment/create/", htmx.HTMXPaymentCreateView.as_view(), name="ecommerce_Payment_htmx_create"),
    path("ecommerce/htmx/Payment/delete/<int:pk>/", htmx.HTMXPaymentDeleteView.as_view(), name="ecommerce_Payment_htmx_delete"),
    path("ecommerce/htmx/Product/", htmx.HTMXProductListView.as_view(), name="ecommerce_Product_htmx_list"),
    path("ecommerce/htmx/Product/create/", htmx.HTMXProductCreateView.as_view(), name="ecommerce_Product_htmx_create"),
    path("ecommerce/htmx/Product/delete/<int:pk>/", htmx.HTMXProductDeleteView.as_view(), name="ecommerce_Product_htmx_delete"),
)
