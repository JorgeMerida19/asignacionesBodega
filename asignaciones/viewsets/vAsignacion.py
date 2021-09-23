from asignaciones.serializers.sAsignacion import BodegaSerializer
from asignaciones.serializers.sAsignacion import AsignacionBodegaSerializer, EmpleadoSerializer, BodegaSerializer
import json
from django.core.files import File
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, filters, viewsets
from django.contrib.auth.models import User
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.settings import api_settings
from asignaciones.models import Empleado, AsignacionBodega, Bodega
from datetime import datetime, timedelta
import datetime
import calendar

class EmpleadoViewSet(viewsets.ModelViewSet):
    queryset = Empleado.objects.all()
    filter_backends = ( filters.SearchFilter, filters.OrderingFilter)
    filter_fields = ("nombre", )
    search_fields = ("nombre",)
    ordering_fields = ("nombre", )

    def get_serializer_class(self):
        """Define serializer for API"""
        if self.action == 'list' or self.action == 'retrieve':
            return EmpleadoSerializer
        else:
            return EmpleadoSerializer

class BodegaViewSet(viewsets.ModelViewSet):
    queryset = Bodega.objects.all()
    filter_backends = ( filters.SearchFilter, filters.OrderingFilter)
    filter_fields = ("nombreBodega", )
    search_fields = ("nombreBodega",)
    ordering_fields = ("nombreBodega", )

    def get_serializer_class(self):
        """Define serializer for API"""
        if self.action == 'list' or self.action == 'retrieve':
            return BodegaSerializer
        else:
            return BodegaSerializer

class AsignacionBodegaViewSet(viewsets.ModelViewSet):
    queryset = AsignacionBodega.objects.all()
    filter_backends = ( filters.SearchFilter, filters.OrderingFilter)
    filter_fields = ("nombreAsignacion", )
    search_fields = ("nombreAsginacion",)
    ordering_fields = ("nombreAsignacion", )

    def get_serializer_class(self):
        """Define serializer for API"""
        if self.action == 'list' or self.action == 'retrieve':
            return AsignacionBodegaSerializer
        else:
            return AsignacionBodegaSerializer

