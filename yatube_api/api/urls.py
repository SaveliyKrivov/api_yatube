from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework import routers
from .views import PostView, GroupViewSet, CommentViewSet

router = routers.DefaultRouter()
router.register(r'api/v1/posts', PostView)
router.register(r'api/v1/groups', GroupViewSet)

comment_list = CommentViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

comment_detail = CommentViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = [
    path('api/v1/api-token-auth/', views.obtain_auth_token),
    path('', include(router.urls)),
    path('api/v1/posts/<int:post_id>/comments/',
         comment_list, name='comment-list'),
    path('api/v1/posts/<int:post_id>/comments/<int:pk>/',
         comment_detail, name='comment-detail'),
]
