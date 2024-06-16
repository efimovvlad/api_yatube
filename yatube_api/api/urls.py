from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter
from .views import GroupViewSet, PostViewSet, CommentViewSet

app_name = 'api'

router = DefaultRouter()
router.register('groups', GroupViewSet)
router.register('posts', PostViewSet)
router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)

urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token),
]
