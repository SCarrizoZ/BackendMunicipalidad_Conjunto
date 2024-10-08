from .models import Publicacion
from .serializers import PublicacionSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
@api_view(["GET", "POST"])
def gestionPublicaciones(request):
    if request.method == "GET":
        paginator = PageNumberPagination()
        paginator.page_size = 3
        publicacion = Publicacion.objects.all().order_by("-fecha_publicacion")
        result_page = paginator.paginate_queryset(publicacion, request)
        ser = PublicacionSerializer(result_page, many=True)
        return paginator.get_paginated_response(ser.data)

    if request.method == "POST":
        ser = PublicacionSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)

        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
