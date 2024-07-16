from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from myapp.views import PersonViewSet, CompanyViewSet

router = DefaultRouter()
router.register(r'persons', PersonViewSet)
router.register(r'companies', CompanyViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
