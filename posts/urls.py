from django.urls import path
from .views import PostList, PostDetail, UserViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('users',UserViewSet)

urlpatterns = [
    path('<int:pk>/', PostDetail.as_view()),
    path('', PostList.as_view()),
]

urlpatterns += router.urls
