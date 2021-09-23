from django.db.models import base
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from django.conf.urls import url
from asignaciones.viewsets import vAsignacion

router = DefaultRouter()
router.register(r'empleado', vAsignacion.EmpleadoViewSet, basename='empleado')
router.register(r'bodega', vAsignacion.BodegaViewSet, basename='bodega')
router.register(r'asignacionBodega', vAsignacion.AsignacionBodegaViewSet, basename ='asignacionbodega')


urlpatterns = [
    path('asignaciones/', include(router.urls)),
]

