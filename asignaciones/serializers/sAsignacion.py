from django.db.models import fields
from rest_framework import serializers
from asignaciones.models import Empleado, Bodega, AsignacionBodega

class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = '__all__'

class BodegaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bodega
        fields = '__all__'

class AsignacionBodegaSerializer(serializers.ModelSerializer):
    class Meta:
        model = AsignacionBodega
        fields = '__all__'