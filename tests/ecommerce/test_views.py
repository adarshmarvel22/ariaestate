import pytest
import test_helpers

from django.urls import reverse


pytestmark = [pytest.mark.django_db]


def tests_Cart_list_view(client):
    instance1 = test_helpers.create_ecommerce_Cart()
    instance2 = test_helpers.create_ecommerce_Cart()
    url = reverse("ecommerce_Cart_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Cart_create_view(client):
    user = test_helpers.create_accounts_User()
    url = reverse("ecommerce_Cart_create")
    data = {
        "user": user.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Cart_detail_view(client):
    instance = test_helpers.create_ecommerce_Cart()
    url = reverse("ecommerce_Cart_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Cart_update_view(client):
    user = test_helpers.create_accounts_User()
    instance = test_helpers.create_ecommerce_Cart()
    url = reverse("ecommerce_Cart_update", args=[instance.pk, ])
    data = {
        "user": user.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_CartItem_list_view(client):
    instance1 = test_helpers.create_ecommerce_CartItem()
    instance2 = test_helpers.create_ecommerce_CartItem()
    url = reverse("ecommerce_CartItem_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_CartItem_create_view(client):
    cart = test_helpers.create_ecommerce_Cart()
    product = test_helpers.create_ecommerce_Product()
    url = reverse("ecommerce_CartItem_create")
    data = {
        "quantity": 1,
        "cart": cart.pk,
        "product": product.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_CartItem_detail_view(client):
    instance = test_helpers.create_ecommerce_CartItem()
    url = reverse("ecommerce_CartItem_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_CartItem_update_view(client):
    cart = test_helpers.create_ecommerce_Cart()
    product = test_helpers.create_ecommerce_Product()
    instance = test_helpers.create_ecommerce_CartItem()
    url = reverse("ecommerce_CartItem_update", args=[instance.pk, ])
    data = {
        "quantity": 1,
        "cart": cart.pk,
        "product": product.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Order_list_view(client):
    instance1 = test_helpers.create_ecommerce_Order()
    instance2 = test_helpers.create_ecommerce_Order()
    url = reverse("ecommerce_Order_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Order_create_view(client):
    user = test_helpers.create_accounts_User()
    url = reverse("ecommerce_Order_create")
    data = {
        "total_amount": 1.0,
        "status": "text",
        "user": user.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Order_detail_view(client):
    instance = test_helpers.create_ecommerce_Order()
    url = reverse("ecommerce_Order_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Order_update_view(client):
    user = test_helpers.create_accounts_User()
    instance = test_helpers.create_ecommerce_Order()
    url = reverse("ecommerce_Order_update", args=[instance.pk, ])
    data = {
        "total_amount": 1.0,
        "status": "text",
        "user": user.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Payment_list_view(client):
    instance1 = test_helpers.create_ecommerce_Payment()
    instance2 = test_helpers.create_ecommerce_Payment()
    url = reverse("ecommerce_Payment_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Payment_create_view(client):
    order = test_helpers.create_ecommerce_Order()
    url = reverse("ecommerce_Payment_create")
    data = {
        "status": "text",
        "transaction_id": "text",
        "amount": 1.0,
        "order": order.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Payment_detail_view(client):
    instance = test_helpers.create_ecommerce_Payment()
    url = reverse("ecommerce_Payment_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Payment_update_view(client):
    order = test_helpers.create_ecommerce_Order()
    instance = test_helpers.create_ecommerce_Payment()
    url = reverse("ecommerce_Payment_update", args=[instance.pk, ])
    data = {
        "status": "text",
        "transaction_id": "text",
        "amount": 1.0,
        "order": order.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Product_list_view(client):
    instance1 = test_helpers.create_ecommerce_Product()
    instance2 = test_helpers.create_ecommerce_Product()
    url = reverse("ecommerce_Product_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Product_create_view(client):
    url = reverse("ecommerce_Product_create")
    data = {
        "name": "text",
        "image": "anImage",
        "price": 1.0,
        "stock": 1,
        "description": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Product_detail_view(client):
    instance = test_helpers.create_ecommerce_Product()
    url = reverse("ecommerce_Product_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Product_update_view(client):
    instance = test_helpers.create_ecommerce_Product()
    url = reverse("ecommerce_Product_update", args=[instance.pk, ])
    data = {
        "name": "text",
        "image": "anImage",
        "price": 1.0,
        "stock": 1,
        "description": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302
