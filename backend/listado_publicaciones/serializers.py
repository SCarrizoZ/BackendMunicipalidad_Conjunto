from rest_framework import serializers
from .models import (
    Usuario,
    Categoria,
    DepartamentoMunicipal,
    Evidencia,
    JuntaVecinal,
    Publicacion,
    RespuestaMunicipal,
    SituacionPublicacion,
)


# Serializer para Usuario
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = [
            "rut",
            "numero_telefonico_movil",
            "nombre",
            "contrasena",
            "es_administrador",
            "email",
            "fecha_registro",
            "esta_activo",
        ]


# Serializer para Departamento Municipal
class DepartamentoMunicipalSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepartamentoMunicipal
        fields = ["id", "nombre", "descripcion"]


# Serializer para Categoria
class CategoriaSerializer(serializers.ModelSerializer):
    departamento = DepartamentoMunicipalSerializer()

    class Meta:
        model = Categoria
        fields = ["id", "departamento", "nombre", "descripcion"]


# Serializer para Junta Vecinal
class JuntaVecinalSerializer(serializers.ModelSerializer):
    class Meta:
        model = JuntaVecinal
        fields = [
            "id",
            "nombre_calle",
            "numero_calle",
            "departamento",
            "villa",
            "comuna",
            "latitud",
            "longitud",
        ]


# Serializer para Situacion de Publicacion
class SituacionPublicacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SituacionPublicacion
        fields = ["id", "nombre", "descripcion"]


# Serializer para Publicacion
class PublicacionSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer()
    junta_vecinal = JuntaVecinalSerializer()
    categoria = CategoriaSerializer()
    departamento = DepartamentoMunicipalSerializer()
    situacion = SituacionPublicacionSerializer()

    class Meta:
        model = Publicacion
        fields = [
            "id",
            "usuario",
            "junta_vecinal",
            "categoria",
            "departamento",
            "descripcion",
            "situacion",
            "fecha_publicacion",
            "titulo",
            "latitud",
            "longitud",
        ]


# Serializer para Evidencia
class EvidenciaSerializer(serializers.ModelSerializer):
    publicacion = PublicacionSerializer()

    class Meta:
        model = Evidencia
        fields = ["id", "publicacion", "url", "fecha", "extension"]


# Serializer para Respuesta Municipal
class RespuestaMunicipalSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer()
    publicacion = PublicacionSerializer()

    class Meta:
        model = RespuestaMunicipal
        fields = [
            "id",
            "usuario",
            "publicacion",
            "fecha",
            "descripcion",
            "acciones",
            "situacion_inicial",
            "situacion_posterior",
        ]
