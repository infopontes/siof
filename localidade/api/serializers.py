from rest_framework import serializers

from localidade.models import Estado, Cidade


class EstadoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Estado
        fields = '__all__'
        #depth = 1


class CidadeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cidade
        fields = '__all__'
        #depth = 1