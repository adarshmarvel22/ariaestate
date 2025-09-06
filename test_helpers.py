import random
import string

from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType
from datetime import datetime

from ecommerce import models as ecommerce_models
from forum import models as forum_models
from properties import models as properties_models
from research import models as research_models
from accounts import models as accounts_models


def random_string(length=10):
    # Create a random string of length length
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for i in range(length))


def create_User(**kwargs):
    defaults = {
        "username": "%s_username" % random_string(5),
        "email": "%s_username@tempurl.com" % random_string(5),
    }
    defaults.update(**kwargs)
    return User.objects.create(**defaults)


def create_AbstractUser(**kwargs):
    defaults = {
        "username": "%s_username" % random_string(5),
        "email": "%s_username@tempurl.com" % random_string(5),
    }
    defaults.update(**kwargs)
    return AbstractUser.objects.create(**defaults)


def create_AbstractBaseUser(**kwargs):
    defaults = {
        "username": "%s_username" % random_string(5),
        "email": "%s_username@tempurl.com" % random_string(5),
    }
    defaults.update(**kwargs)
    return AbstractBaseUser.objects.create(**defaults)


def create_Group(**kwargs):
    defaults = {
        "name": "%s_group" % random_string(5),
    }
    defaults.update(**kwargs)
    return Group.objects.create(**defaults)


def create_ContentType(**kwargs):
    defaults = {
    }
    defaults.update(**kwargs)
    return ContentType.objects.create(**defaults)


def create_ecommerce_Cart(**kwargs):
    defaults = {}
    if "user" not in kwargs:
        defaults["user"] = create_accounts_User()
    defaults.update(**kwargs)
    return ecommerce_models.Cart.objects.create(**defaults)
def create_ecommerce_CartItem(**kwargs):
    defaults = {}
    defaults["quantity"] = ""
    if "cart" not in kwargs:
        defaults["cart"] = create_ecommerce_Cart()
    if "product" not in kwargs:
        defaults["product"] = create_ecommerce_Product()
    defaults.update(**kwargs)
    return ecommerce_models.CartItem.objects.create(**defaults)
def create_ecommerce_Order(**kwargs):
    defaults = {}
    defaults["total_amount"] = ""
    defaults["status"] = ""
    if "user" not in kwargs:
        defaults["user"] = create_accounts_User()
    defaults.update(**kwargs)
    return ecommerce_models.Order.objects.create(**defaults)
def create_ecommerce_Payment(**kwargs):
    defaults = {}
    defaults["status"] = ""
    defaults["transaction_id"] = ""
    defaults["amount"] = ""
    if "order" not in kwargs:
        defaults["order"] = create_ecommerce_Order()
    defaults.update(**kwargs)
    return ecommerce_models.Payment.objects.create(**defaults)
def create_ecommerce_Product(**kwargs):
    defaults = {}
    defaults["name"] = ""
    defaults["image"] = ""
    defaults["price"] = ""
    defaults["stock"] = ""
    defaults["description"] = ""
    defaults.update(**kwargs)
    return ecommerce_models.Product.objects.create(**defaults)
def create_forum_Comment(**kwargs):
    defaults = {}
    defaults["content"] = ""
    if "post" not in kwargs:
        defaults["post"] = create_forum_Post()
    if "author" not in kwargs:
        defaults["author"] = create_accounts_User()
    defaults.update(**kwargs)
    return forum_models.Comment.objects.create(**defaults)
def create_forum_Like(**kwargs):
    defaults = {}
    if "post" not in kwargs:
        defaults["post"] = create_forum_Post()
    if "user" not in kwargs:
        defaults["user"] = create_accounts_User()
    defaults.update(**kwargs)
    return forum_models.Like.objects.create(**defaults)
def create_forum_Post(**kwargs):
    defaults = {}
    defaults["content"] = ""
    if "author" not in kwargs:
        defaults["author"] = create_accounts_User()
    if "tags" not in kwargs:
        defaults["tags"] = create_forum_Tag()
    defaults.update(**kwargs)
    return forum_models.Post.objects.create(**defaults)
def create_forum_Tag(**kwargs):
    defaults = {}
    defaults["name"] = ""
    defaults.update(**kwargs)
    return forum_models.Tag.objects.create(**defaults)
def create_properties_Category(**kwargs):
    defaults = {}
    defaults["description"] = ""
    defaults["name"] = ""
    defaults.update(**kwargs)
    return properties_models.Category.objects.create(**defaults)
def create_properties_Lease(**kwargs):
    defaults = {}
    defaults["monthly_rent"] = ""
    defaults["start_date"] = datetime.now()
    defaults["tenant_name"] = ""
    defaults["end_date"] = datetime.now()
    if "unit" not in kwargs:
        defaults["unit"] = create_properties_Unit()
    defaults.update(**kwargs)
    return properties_models.Lease.objects.create(**defaults)
def create_properties_Project(**kwargs):
    defaults = {}
    defaults["launch_date"] = datetime.now()
    defaults["price_range"] = ""
    defaults["title"] = ""
    defaults["description"] = ""
    defaults["location"] = ""
    if "category" not in kwargs:
        defaults["category"] = create_properties_Category()
    defaults.update(**kwargs)
    return properties_models.Project.objects.create(**defaults)
def create_properties_Unit(**kwargs):
    defaults = {}
    defaults["size_sqft"] = ""
    defaults["unit_number"] = ""
    defaults["is_available"] = ""
    defaults["price"] = ""
    if "project" not in kwargs:
        defaults["project"] = create_properties_Project()
    defaults.update(**kwargs)
    return properties_models.Unit.objects.create(**defaults)
def create_research_Document(**kwargs):
    defaults = {}
    defaults["uploaded_at"] = datetime.now()
    defaults["file"] = ""
    if "project" not in kwargs:
        defaults["project"] = create_research_ResearchProject()
    defaults.update(**kwargs)
    return research_models.Document.objects.create(**defaults)
def create_research_ResearchProject(**kwargs):
    defaults = {}
    defaults["end_date"] = datetime.now()
    defaults["title"] = ""
    defaults["description"] = ""
    defaults["start_date"] = datetime.now()
    if "lead" not in kwargs:
        defaults["lead"] = create_accounts_User()
    defaults.update(**kwargs)
    return research_models.ResearchProject.objects.create(**defaults)
def create_research_Team(**kwargs):
    defaults = {}
    defaults["role"] = ""
    if "project" not in kwargs:
        defaults["project"] = create_research_ResearchProject()
    if "member" not in kwargs:
        defaults["member"] = create_accounts_User()
    defaults.update(**kwargs)
    return research_models.Team.objects.create(**defaults)
def create_accounts_Profile(**kwargs):
    defaults = {}
    defaults["avatar"] = ""
    defaults["phone"] = ""
    defaults["bio"] = ""
    defaults["address"] = ""
    if "user" not in kwargs:
        defaults["user"] = create_accounts_User()
    defaults.update(**kwargs)
    return accounts_models.Profile.objects.create(**defaults)
def create_accounts_Role(**kwargs):
    defaults = {}
    defaults["name"] = ""
    defaults["description"] = ""
    defaults.update(**kwargs)
    return accounts_models.Role.objects.create(**defaults)
def create_accounts_User(**kwargs):
    defaults = {}
    defaults["username"] = "username"
    defaults["email"] = "username@tempurl.com"
    if "role" not in kwargs:
        defaults["role"] = create_accounts_Role()
    defaults.update(**kwargs)
    return accounts_models.User.objects.create(**defaults)
