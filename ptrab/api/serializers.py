from rest_framework import serializers

from ptrab.models import Ptrab


class PtrabSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ptrab
        fields = '__all__'