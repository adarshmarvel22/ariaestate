from django.urls import path, include
from rest_framework import routers

from . import api
from . import views
from . import htmx


router = routers.DefaultRouter()
router.register("Category", api.CategoryViewSet)
router.register("Lease", api.LeaseViewSet)
router.register("Project", api.ProjectViewSet)
router.register("Unit", api.UnitViewSet)

urlpatterns = (
    path("api/v1/", include(router.urls)),
    path("properties/Category/", views.CategoryListView.as_view(), name="properties_Category_list"),
    path("properties/Category/create/", views.CategoryCreateView.as_view(), name="properties_Category_create"),
    path("properties/Category/detail/<int:pk>/", views.CategoryDetailView.as_view(), name="properties_Category_detail"),
    path("properties/Category/update/<int:pk>/", views.CategoryUpdateView.as_view(), name="properties_Category_update"),
    path("properties/Category/delete/<int:pk>/", views.CategoryDeleteView.as_view(), name="properties_Category_delete"),
    path("properties/Lease/", views.LeaseListView.as_view(), name="properties_Lease_list"),
    path("properties/Lease/create/", views.LeaseCreateView.as_view(), name="properties_Lease_create"),
    path("properties/Lease/detail/<int:pk>/", views.LeaseDetailView.as_view(), name="properties_Lease_detail"),
    path("properties/Lease/update/<int:pk>/", views.LeaseUpdateView.as_view(), name="properties_Lease_update"),
    path("properties/Lease/delete/<int:pk>/", views.LeaseDeleteView.as_view(), name="properties_Lease_delete"),
    path("properties/Project/", views.ProjectListView.as_view(), name="properties_Project_list"),
    path("properties/Project/create/", views.ProjectCreateView.as_view(), name="properties_Project_create"),
    path("properties/Project/detail/<int:pk>/", views.ProjectDetailView.as_view(), name="properties_Project_detail"),
    path("properties/Project/update/<int:pk>/", views.ProjectUpdateView.as_view(), name="properties_Project_update"),
    path("properties/Project/delete/<int:pk>/", views.ProjectDeleteView.as_view(), name="properties_Project_delete"),
    path("properties/Unit/", views.UnitListView.as_view(), name="properties_Unit_list"),
    path("properties/Unit/create/", views.UnitCreateView.as_view(), name="properties_Unit_create"),
    path("properties/Unit/detail/<int:pk>/", views.UnitDetailView.as_view(), name="properties_Unit_detail"),
    path("properties/Unit/update/<int:pk>/", views.UnitUpdateView.as_view(), name="properties_Unit_update"),
    path("properties/Unit/delete/<int:pk>/", views.UnitDeleteView.as_view(), name="properties_Unit_delete"),

    path("properties/htmx/Category/", htmx.HTMXCategoryListView.as_view(), name="properties_Category_htmx_list"),
    path("properties/htmx/Category/create/", htmx.HTMXCategoryCreateView.as_view(), name="properties_Category_htmx_create"),
    path("properties/htmx/Category/delete/<int:pk>/", htmx.HTMXCategoryDeleteView.as_view(), name="properties_Category_htmx_delete"),
    path("properties/htmx/Lease/", htmx.HTMXLeaseListView.as_view(), name="properties_Lease_htmx_list"),
    path("properties/htmx/Lease/create/", htmx.HTMXLeaseCreateView.as_view(), name="properties_Lease_htmx_create"),
    path("properties/htmx/Lease/delete/<int:pk>/", htmx.HTMXLeaseDeleteView.as_view(), name="properties_Lease_htmx_delete"),
    path("properties/htmx/Project/", htmx.HTMXProjectListView.as_view(), name="properties_Project_htmx_list"),
    path("properties/htmx/Project/create/", htmx.HTMXProjectCreateView.as_view(), name="properties_Project_htmx_create"),
    path("properties/htmx/Project/delete/<int:pk>/", htmx.HTMXProjectDeleteView.as_view(), name="properties_Project_htmx_delete"),
    path("properties/htmx/Unit/", htmx.HTMXUnitListView.as_view(), name="properties_Unit_htmx_list"),
    path("properties/htmx/Unit/create/", htmx.HTMXUnitCreateView.as_view(), name="properties_Unit_htmx_create"),
    path("properties/htmx/Unit/delete/<int:pk>/", htmx.HTMXUnitDeleteView.as_view(), name="properties_Unit_htmx_delete"),
)
