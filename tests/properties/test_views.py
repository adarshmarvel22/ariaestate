import pytest
import test_helpers

from django.urls import reverse


pytestmark = [pytest.mark.django_db]


def tests_Category_list_view(client):
    instance1 = test_helpers.create_properties_Category()
    instance2 = test_helpers.create_properties_Category()
    url = reverse("properties_Category_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Category_create_view(client):
    url = reverse("properties_Category_create")
    data = {
        "description": "text",
        "name": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Category_detail_view(client):
    instance = test_helpers.create_properties_Category()
    url = reverse("properties_Category_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Category_update_view(client):
    instance = test_helpers.create_properties_Category()
    url = reverse("properties_Category_update", args=[instance.pk, ])
    data = {
        "description": "text",
        "name": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Lease_list_view(client):
    instance1 = test_helpers.create_properties_Lease()
    instance2 = test_helpers.create_properties_Lease()
    url = reverse("properties_Lease_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Lease_create_view(client):
    unit = test_helpers.create_properties_Unit()
    url = reverse("properties_Lease_create")
    data = {
        "monthly_rent": 1.0,
        "start_date": datetime.now(),
        "tenant_name": "text",
        "end_date": datetime.now(),
        "unit": unit.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Lease_detail_view(client):
    instance = test_helpers.create_properties_Lease()
    url = reverse("properties_Lease_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Lease_update_view(client):
    unit = test_helpers.create_properties_Unit()
    instance = test_helpers.create_properties_Lease()
    url = reverse("properties_Lease_update", args=[instance.pk, ])
    data = {
        "monthly_rent": 1.0,
        "start_date": datetime.now(),
        "tenant_name": "text",
        "end_date": datetime.now(),
        "unit": unit.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Project_list_view(client):
    instance1 = test_helpers.create_properties_Project()
    instance2 = test_helpers.create_properties_Project()
    url = reverse("properties_Project_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Project_create_view(client):
    category = test_helpers.create_properties_Category()
    url = reverse("properties_Project_create")
    data = {
        "launch_date": datetime.now(),
        "price_range": "text",
        "title": "text",
        "description": "text",
        "location": "text",
        "category": category.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Project_detail_view(client):
    instance = test_helpers.create_properties_Project()
    url = reverse("properties_Project_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Project_update_view(client):
    category = test_helpers.create_properties_Category()
    instance = test_helpers.create_properties_Project()
    url = reverse("properties_Project_update", args=[instance.pk, ])
    data = {
        "launch_date": datetime.now(),
        "price_range": "text",
        "title": "text",
        "description": "text",
        "location": "text",
        "category": category.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Unit_list_view(client):
    instance1 = test_helpers.create_properties_Unit()
    instance2 = test_helpers.create_properties_Unit()
    url = reverse("properties_Unit_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Unit_create_view(client):
    project = test_helpers.create_properties_Project()
    url = reverse("properties_Unit_create")
    data = {
        "size_sqft": 1.0,
        "unit_number": "text",
        "is_available": True,
        "price": 1.0,
        "project": project.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Unit_detail_view(client):
    instance = test_helpers.create_properties_Unit()
    url = reverse("properties_Unit_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Unit_update_view(client):
    project = test_helpers.create_properties_Project()
    instance = test_helpers.create_properties_Unit()
    url = reverse("properties_Unit_update", args=[instance.pk, ])
    data = {
        "size_sqft": 1.0,
        "unit_number": "text",
        "is_available": True,
        "price": 1.0,
        "project": project.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302
