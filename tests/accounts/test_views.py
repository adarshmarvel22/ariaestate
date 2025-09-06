import pytest
import test_helpers

from django.urls import reverse


pytestmark = [pytest.mark.django_db]


def tests_Profile_list_view(client):
    instance1 = test_helpers.create_accounts_Profile()
    instance2 = test_helpers.create_accounts_Profile()
    url = reverse("accounts_Profile_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Profile_create_view(client):
    user = test_helpers.create_accounts_User()
    url = reverse("accounts_Profile_create")
    data = {
        "avatar": "anImage",
        "phone": "text",
        "bio": "text",
        "address": "text",
        "user": user.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Profile_detail_view(client):
    instance = test_helpers.create_accounts_Profile()
    url = reverse("accounts_Profile_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Profile_update_view(client):
    user = test_helpers.create_accounts_User()
    instance = test_helpers.create_accounts_Profile()
    url = reverse("accounts_Profile_update", args=[instance.pk, ])
    data = {
        "avatar": "anImage",
        "phone": "text",
        "bio": "text",
        "address": "text",
        "user": user.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Role_list_view(client):
    instance1 = test_helpers.create_accounts_Role()
    instance2 = test_helpers.create_accounts_Role()
    url = reverse("accounts_Role_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Role_create_view(client):
    url = reverse("accounts_Role_create")
    data = {
        "name": "text",
        "description": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Role_detail_view(client):
    instance = test_helpers.create_accounts_Role()
    url = reverse("accounts_Role_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Role_update_view(client):
    instance = test_helpers.create_accounts_Role()
    url = reverse("accounts_Role_update", args=[instance.pk, ])
    data = {
        "name": "text",
        "description": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_User_list_view(client):
    instance1 = test_helpers.create_accounts_User()
    instance2 = test_helpers.create_accounts_User()
    url = reverse("accounts_User_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_User_create_view(client):
    role = test_helpers.create_accounts_Role()
    url = reverse("accounts_User_create")
    data = {
        "role": role.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_User_detail_view(client):
    instance = test_helpers.create_accounts_User()
    url = reverse("accounts_User_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_User_update_view(client):
    role = test_helpers.create_accounts_Role()
    instance = test_helpers.create_accounts_User()
    url = reverse("accounts_User_update", args=[instance.pk, ])
    data = {
        "role": role.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302
