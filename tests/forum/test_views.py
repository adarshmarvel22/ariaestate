import pytest
import test_helpers

from django.urls import reverse


pytestmark = [pytest.mark.django_db]


def tests_Comment_list_view(client):
    instance1 = test_helpers.create_forum_Comment()
    instance2 = test_helpers.create_forum_Comment()
    url = reverse("forum_Comment_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Comment_create_view(client):
    post = test_helpers.create_forum_Post()
    author = test_helpers.create_accounts_User()
    url = reverse("forum_Comment_create")
    data = {
        "content": "text",
        "post": post.pk,
        "author": author.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Comment_detail_view(client):
    instance = test_helpers.create_forum_Comment()
    url = reverse("forum_Comment_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Comment_update_view(client):
    post = test_helpers.create_forum_Post()
    author = test_helpers.create_accounts_User()
    instance = test_helpers.create_forum_Comment()
    url = reverse("forum_Comment_update", args=[instance.pk, ])
    data = {
        "content": "text",
        "post": post.pk,
        "author": author.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Like_list_view(client):
    instance1 = test_helpers.create_forum_Like()
    instance2 = test_helpers.create_forum_Like()
    url = reverse("forum_Like_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Like_create_view(client):
    post = test_helpers.create_forum_Post()
    user = test_helpers.create_accounts_User()
    url = reverse("forum_Like_create")
    data = {
        "post": post.pk,
        "user": user.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Like_detail_view(client):
    instance = test_helpers.create_forum_Like()
    url = reverse("forum_Like_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Like_update_view(client):
    post = test_helpers.create_forum_Post()
    user = test_helpers.create_accounts_User()
    instance = test_helpers.create_forum_Like()
    url = reverse("forum_Like_update", args=[instance.pk, ])
    data = {
        "post": post.pk,
        "user": user.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Post_list_view(client):
    instance1 = test_helpers.create_forum_Post()
    instance2 = test_helpers.create_forum_Post()
    url = reverse("forum_Post_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Post_create_view(client):
    author = test_helpers.create_accounts_User()
    tags = test_helpers.create_forum_Tag()
    url = reverse("forum_Post_create")
    data = {
        "content": "text",
        "author": author.pk,
        "tags": tags.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Post_detail_view(client):
    instance = test_helpers.create_forum_Post()
    url = reverse("forum_Post_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Post_update_view(client):
    author = test_helpers.create_accounts_User()
    tags = test_helpers.create_forum_Tag()
    instance = test_helpers.create_forum_Post()
    url = reverse("forum_Post_update", args=[instance.pk, ])
    data = {
        "content": "text",
        "author": author.pk,
        "tags": tags.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Tag_list_view(client):
    instance1 = test_helpers.create_forum_Tag()
    instance2 = test_helpers.create_forum_Tag()
    url = reverse("forum_Tag_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Tag_create_view(client):
    url = reverse("forum_Tag_create")
    data = {
        "name": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Tag_detail_view(client):
    instance = test_helpers.create_forum_Tag()
    url = reverse("forum_Tag_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Tag_update_view(client):
    instance = test_helpers.create_forum_Tag()
    url = reverse("forum_Tag_update", args=[instance.pk, ])
    data = {
        "name": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302
