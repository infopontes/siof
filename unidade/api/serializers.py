from rest_framework import serializers

from unidade.models import ComandoMilitarArea, RegiaoMilitar, Unidade


class ComandomilitarareaSerializer(serializers.ModelSerializer):

    class Meta:
        model = ComandoMilitarArea
        fields = '__all__'


class RegiaomilitarSerializer(serializers.ModelSerializer):

    class Meta:
        model = RegiaoMilitar
        fields = '__all__'


class UnidadeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Unidade
        fields = '__all__'