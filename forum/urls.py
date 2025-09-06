from django.urls import path, include
from rest_framework import routers

from . import api
from . import views
from . import htmx


router = routers.DefaultRouter()
router.register("Comment", api.CommentViewSet)
router.register("Like", api.LikeViewSet)
router.register("Post", api.PostViewSet)
router.register("Tag", api.TagViewSet)

urlpatterns = (
    path("api/v1/", include(router.urls)),
    path("forum/Comment/", views.CommentListView.as_view(), name="forum_Comment_list"),
    path("forum/Comment/create/", views.CommentCreateView.as_view(), name="forum_Comment_create"),
    path("forum/Comment/detail/<int:pk>/", views.CommentDetailView.as_view(), name="forum_Comment_detail"),
    path("forum/Comment/update/<int:pk>/", views.CommentUpdateView.as_view(), name="forum_Comment_update"),
    path("forum/Comment/delete/<int:pk>/", views.CommentDeleteView.as_view(), name="forum_Comment_delete"),
    path("forum/Like/", views.LikeListView.as_view(), name="forum_Like_list"),
    path("forum/Like/create/", views.LikeCreateView.as_view(), name="forum_Like_create"),
    path("forum/Like/detail/<int:pk>/", views.LikeDetailView.as_view(), name="forum_Like_detail"),
    path("forum/Like/update/<int:pk>/", views.LikeUpdateView.as_view(), name="forum_Like_update"),
    path("forum/Like/delete/<int:pk>/", views.LikeDeleteView.as_view(), name="forum_Like_delete"),
    path("forum/Post/", views.PostListView.as_view(), name="forum_Post_list"),
    path("forum/Post/create/", views.PostCreateView.as_view(), name="forum_Post_create"),
    path("forum/Post/detail/<int:pk>/", views.PostDetailView.as_view(), name="forum_Post_detail"),
    path("forum/Post/update/<int:pk>/", views.PostUpdateView.as_view(), name="forum_Post_update"),
    path("forum/Post/delete/<int:pk>/", views.PostDeleteView.as_view(), name="forum_Post_delete"),
    path("forum/Tag/", views.TagListView.as_view(), name="forum_Tag_list"),
    path("forum/Tag/create/", views.TagCreateView.as_view(), name="forum_Tag_create"),
    path("forum/Tag/detail/<int:pk>/", views.TagDetailView.as_view(), name="forum_Tag_detail"),
    path("forum/Tag/update/<int:pk>/", views.TagUpdateView.as_view(), name="forum_Tag_update"),
    path("forum/Tag/delete/<int:pk>/", views.TagDeleteView.as_view(), name="forum_Tag_delete"),

    path("forum/htmx/Comment/", htmx.HTMXCommentListView.as_view(), name="forum_Comment_htmx_list"),
    path("forum/htmx/Comment/create/", htmx.HTMXCommentCreateView.as_view(), name="forum_Comment_htmx_create"),
    path("forum/htmx/Comment/delete/<int:pk>/", htmx.HTMXCommentDeleteView.as_view(), name="forum_Comment_htmx_delete"),
    path("forum/htmx/Like/", htmx.HTMXLikeListView.as_view(), name="forum_Like_htmx_list"),
    path("forum/htmx/Like/create/", htmx.HTMXLikeCreateView.as_view(), name="forum_Like_htmx_create"),
    path("forum/htmx/Like/delete/<int:pk>/", htmx.HTMXLikeDeleteView.as_view(), name="forum_Like_htmx_delete"),
    path("forum/htmx/Post/", htmx.HTMXPostListView.as_view(), name="forum_Post_htmx_list"),
    path("forum/htmx/Post/create/", htmx.HTMXPostCreateView.as_view(), name="forum_Post_htmx_create"),
    path("forum/htmx/Post/delete/<int:pk>/", htmx.HTMXPostDeleteView.as_view(), name="forum_Post_htmx_delete"),
    path("forum/htmx/Tag/", htmx.HTMXTagListView.as_view(), name="forum_Tag_htmx_list"),
    path("forum/htmx/Tag/create/", htmx.HTMXTagCreateView.as_view(), name="forum_Tag_htmx_create"),
    path("forum/htmx/Tag/delete/<int:pk>/", htmx.HTMXTagDeleteView.as_view(), name="forum_Tag_htmx_delete"),
)
