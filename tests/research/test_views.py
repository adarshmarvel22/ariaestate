import pytest
import test_helpers

from django.urls import reverse


pytestmark = [pytest.mark.django_db]


def tests_Document_list_view(client):
    instance1 = test_helpers.create_research_Document()
    instance2 = test_helpers.create_research_Document()
    url = reverse("research_Document_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Document_create_view(client):
    project = test_helpers.create_research_ResearchProject()
    url = reverse("research_Document_create")
    data = {
        "uploaded_at": datetime.now(),
        "file": "aFile",
        "project": project.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Document_detail_view(client):
    instance = test_helpers.create_research_Document()
    url = reverse("research_Document_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Document_update_view(client):
    project = test_helpers.create_research_ResearchProject()
    instance = test_helpers.create_research_Document()
    url = reverse("research_Document_update", args=[instance.pk, ])
    data = {
        "uploaded_at": datetime.now(),
        "file": "aFile",
        "project": project.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_ResearchProject_list_view(client):
    instance1 = test_helpers.create_research_ResearchProject()
    instance2 = test_helpers.create_research_ResearchProject()
    url = reverse("research_ResearchProject_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_ResearchProject_create_view(client):
    lead = test_helpers.create_accounts_User()
    url = reverse("research_ResearchProject_create")
    data = {
        "end_date": datetime.now(),
        "title": "text",
        "description": "text",
        "start_date": datetime.now(),
        "lead": lead.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_ResearchProject_detail_view(client):
    instance = test_helpers.create_research_ResearchProject()
    url = reverse("research_ResearchProject_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_ResearchProject_update_view(client):
    lead = test_helpers.create_accounts_User()
    instance = test_helpers.create_research_ResearchProject()
    url = reverse("research_ResearchProject_update", args=[instance.pk, ])
    data = {
        "end_date": datetime.now(),
        "title": "text",
        "description": "text",
        "start_date": datetime.now(),
        "lead": lead.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Team_list_view(client):
    instance1 = test_helpers.create_research_Team()
    instance2 = test_helpers.create_research_Team()
    url = reverse("research_Team_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Team_create_view(client):
    project = test_helpers.create_research_ResearchProject()
    member = test_helpers.create_accounts_User()
    url = reverse("research_Team_create")
    data = {
        "role": "text",
        "project": project.pk,
        "member": member.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Team_detail_view(client):
    instance = test_helpers.create_research_Team()
    url = reverse("research_Team_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Team_update_view(client):
    project = test_helpers.create_research_ResearchProject()
    member = test_helpers.create_accounts_User()
    instance = test_helpers.create_research_Team()
    url = reverse("research_Team_update", args=[instance.pk, ])
    data = {
        "role": "text",
        "project": project.pk,
        "member": member.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302
