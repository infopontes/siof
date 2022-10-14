from rest_framework import serializers

from tipoPtrab.models import TipoPtrab


class TipoPtrabSerializer(serializers.ModelSerializer):

    class Meta:
        model = TipoPtrab
        fields = '__all__'