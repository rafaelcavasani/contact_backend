from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from contact.views import ContactViewSet

router = routers.DefaultRouter()
router.register(r'contacts', ContactViewSet, basename='Contact')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
