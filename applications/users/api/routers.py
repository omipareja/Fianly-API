from rest_framework.routers import DefaultRouter
from applications.users.api.views.UserViewSet import UserViewSet

router = DefaultRouter()

router.register(r'user',UserViewSet,basename='user')

urlpatterns = router.urls