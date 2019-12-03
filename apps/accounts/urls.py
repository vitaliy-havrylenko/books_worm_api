from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.accounts.views import UserViewSet

app_name = 'accounts'

router = DefaultRouter()
router.register(r'accounts', UserViewSet)


urlpatterns = [
    path('', include(router.urls)),

]


