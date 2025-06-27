from rest_framework import viewsets
from musica.models import  Instrumento, Ritmo, Departamento, Agrupacion, Cancion
from musica.serializers import RitmoSerializer, InstrumentoSerializer, DepartamentoSerializer, AgrupacionSerializer, CancionSerializer

class InstrumentoViewSet(viewsets.ModelViewSet):
    queryset = Instrumento.objects.all()
    serializer_class = InstrumentoSerializer

class RitmoViewSet(viewsets.ModelViewSet):
    queryset = Ritmo.objects.all()
    serializer_class = RitmoSerializer

class DepartamentoViewSet(viewsets.ModelViewSet):
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer

class AgrupacionViewSet(viewsets.ModelViewSet):
    queryset = Agrupacion.objects.all()
    serializer_class = AgrupacionSerializer

class CancionViewSet(viewsets.ModelViewSet):
    queryset = Cancion.objects.all()
    serializer_class = CancionSerializer
