from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from core.views import CustomersViewSet, ProfessionViewSet, DocumentiewSet, DataSheetViewSet

router = routers.DefaultRouter()
router.register('Customer', CustomersViewSet)
router.register('Profession', ProfessionViewSet)
router.register('Datasheet', DataSheetViewSet)
router.register('Document', DocumentiewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls'))
]
