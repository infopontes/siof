from rest_framework import serializers

from tipoDespesa.models import TipoDespesa


class TipodespesaSerializer(serializers.ModelSerializer):

    class Meta:
        model = TipoDespesa
        fields = '__all__'