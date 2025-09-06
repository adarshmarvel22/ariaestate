from django.urls import path, include
from rest_framework import routers

from . import api
from . import views
from . import htmx


router = routers.DefaultRouter()
router.register("Profile", api.ProfileViewSet)
router.register("Role", api.RoleViewSet)
router.register("User", api.UserViewSet)

urlpatterns = (
    path("api/v1/", include(router.urls)),
    path("accounts/Profile/", views.ProfileListView.as_view(), name="accounts_Profile_list"),
    path("accounts/Profile/create/", views.ProfileCreateView.as_view(), name="accounts_Profile_create"),
    path("accounts/Profile/detail/<int:pk>/", views.ProfileDetailView.as_view(), name="accounts_Profile_detail"),
    path("accounts/Profile/update/<int:pk>/", views.ProfileUpdateView.as_view(), name="accounts_Profile_update"),
    path("accounts/Profile/delete/<int:pk>/", views.ProfileDeleteView.as_view(), name="accounts_Profile_delete"),
    path("accounts/Role/", views.RoleListView.as_view(), name="accounts_Role_list"),
    path("accounts/Role/create/", views.RoleCreateView.as_view(), name="accounts_Role_create"),
    path("accounts/Role/detail/<int:pk>/", views.RoleDetailView.as_view(), name="accounts_Role_detail"),
    path("accounts/Role/update/<int:pk>/", views.RoleUpdateView.as_view(), name="accounts_Role_update"),
    path("accounts/Role/delete/<int:pk>/", views.RoleDeleteView.as_view(), name="accounts_Role_delete"),
    path("accounts/User/", views.UserListView.as_view(), name="accounts_User_list"),
    path("accounts/User/create/", views.UserCreateView.as_view(), name="accounts_User_create"),
    path("accounts/User/detail/<int:pk>/", views.UserDetailView.as_view(), name="accounts_User_detail"),
    path("accounts/User/update/<int:pk>/", views.UserUpdateView.as_view(), name="accounts_User_update"),
    path("accounts/User/delete/<int:pk>/", views.UserDeleteView.as_view(), name="accounts_User_delete"),

    path("accounts/htmx/Profile/", htmx.HTMXProfileListView.as_view(), name="accounts_Profile_htmx_list"),
    path("accounts/htmx/Profile/create/", htmx.HTMXProfileCreateView.as_view(), name="accounts_Profile_htmx_create"),
    path("accounts/htmx/Profile/delete/<int:pk>/", htmx.HTMXProfileDeleteView.as_view(), name="accounts_Profile_htmx_delete"),
    path("accounts/htmx/Role/", htmx.HTMXRoleListView.as_view(), name="accounts_Role_htmx_list"),
    path("accounts/htmx/Role/create/", htmx.HTMXRoleCreateView.as_view(), name="accounts_Role_htmx_create"),
    path("accounts/htmx/Role/delete/<int:pk>/", htmx.HTMXRoleDeleteView.as_view(), name="accounts_Role_htmx_delete"),
    path("accounts/htmx/User/", htmx.HTMXUserListView.as_view(), name="accounts_User_htmx_list"),
    path("accounts/htmx/User/create/", htmx.HTMXUserCreateView.as_view(), name="accounts_User_htmx_create"),
    path("accounts/htmx/User/delete/<int:pk>/", htmx.HTMXUserDeleteView.as_view(), name="accounts_User_htmx_delete"),
)
