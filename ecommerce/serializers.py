from rest_framework import serializers

from . import models


class CartSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Cart
        fields = [
            "id",
            "created",
            "last_updated",
            "user",
        ]

class CartItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.CartItem
        fields = [
            "last_updated",
            "quantity",
            "created",
            "id",
            "cart",
            "product",
        ]

class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Order
        fields = [
            "created",
            "id",
            "total_amount",
            "last_updated",
            "status",
            "user",
        ]

class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Payment
        fields = [
            "status",
            "transaction_id",
            "last_updated",
            "payment_date",
            "amount",
            "id",
            "created",
            "order",
        ]

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Product
        fields = [
            "name",
            "image",
            "last_updated",
            "price",
            "created",
            "stock",
            "description",
            "id",
        ]
