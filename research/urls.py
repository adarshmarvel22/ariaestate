from django.urls import path, include
from rest_framework import routers

from . import api
from . import views
from . import htmx


router = routers.DefaultRouter()
router.register("Document", api.DocumentViewSet)
router.register("ResearchProject", api.ResearchProjectViewSet)
router.register("Team", api.TeamViewSet)

urlpatterns = (
    path("api/v1/", include(router.urls)),
    path("research/Document/", views.DocumentListView.as_view(), name="research_Document_list"),
    path("research/Document/create/", views.DocumentCreateView.as_view(), name="research_Document_create"),
    path("research/Document/detail/<int:pk>/", views.DocumentDetailView.as_view(), name="research_Document_detail"),
    path("research/Document/update/<int:pk>/", views.DocumentUpdateView.as_view(), name="research_Document_update"),
    path("research/Document/delete/<int:pk>/", views.DocumentDeleteView.as_view(), name="research_Document_delete"),
    path("research/ResearchProject/", views.ResearchProjectListView.as_view(), name="research_ResearchProject_list"),
    path("research/ResearchProject/create/", views.ResearchProjectCreateView.as_view(), name="research_ResearchProject_create"),
    path("research/ResearchProject/detail/<int:pk>/", views.ResearchProjectDetailView.as_view(), name="research_ResearchProject_detail"),
    path("research/ResearchProject/update/<int:pk>/", views.ResearchProjectUpdateView.as_view(), name="research_ResearchProject_update"),
    path("research/ResearchProject/delete/<int:pk>/", views.ResearchProjectDeleteView.as_view(), name="research_ResearchProject_delete"),
    path("research/Team/", views.TeamListView.as_view(), name="research_Team_list"),
    path("research/Team/create/", views.TeamCreateView.as_view(), name="research_Team_create"),
    path("research/Team/detail/<int:pk>/", views.TeamDetailView.as_view(), name="research_Team_detail"),
    path("research/Team/update/<int:pk>/", views.TeamUpdateView.as_view(), name="research_Team_update"),
    path("research/Team/delete/<int:pk>/", views.TeamDeleteView.as_view(), name="research_Team_delete"),

    path("research/htmx/Document/", htmx.HTMXDocumentListView.as_view(), name="research_Document_htmx_list"),
    path("research/htmx/Document/create/", htmx.HTMXDocumentCreateView.as_view(), name="research_Document_htmx_create"),
    path("research/htmx/Document/delete/<int:pk>/", htmx.HTMXDocumentDeleteView.as_view(), name="research_Document_htmx_delete"),
    path("research/htmx/ResearchProject/", htmx.HTMXResearchProjectListView.as_view(), name="research_ResearchProject_htmx_list"),
    path("research/htmx/ResearchProject/create/", htmx.HTMXResearchProjectCreateView.as_view(), name="research_ResearchProject_htmx_create"),
    path("research/htmx/ResearchProject/delete/<int:pk>/", htmx.HTMXResearchProjectDeleteView.as_view(), name="research_ResearchProject_htmx_delete"),
    path("research/htmx/Team/", htmx.HTMXTeamListView.as_view(), name="research_Team_htmx_list"),
    path("research/htmx/Team/create/", htmx.HTMXTeamCreateView.as_view(), name="research_Team_htmx_create"),
    path("research/htmx/Team/delete/<int:pk>/", htmx.HTMXTeamDeleteView.as_view(), name="research_Team_htmx_delete"),
)
