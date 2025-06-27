from musica.models import Ritmo, Instrumento, Departamento, Agrupacion, Cancion
from rest_framework import serializers


class InstrumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instrumento
        fields = '__all__'

class DepartamentoSerializer(serializers.ModelSerializer):


    class Meta:
        model = Departamento
        fields = '__all__'

class AgrupacionSerializer(serializers.ModelSerializer):


    class Meta:
        model = Agrupacion
        fields = '__all__'

class CancionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cancion
        fields = '__all__'

class RitmoSerializer(serializers.ModelSerializer):
    instrumentos = InstrumentoSerializer(many=True, read_only=True)

    class Meta:
        model = Ritmo
        fields = '__all__'
        depth = 1
