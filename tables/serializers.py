from rest_framework import serializers
from .models import Table, Row, Column


class TableSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Table
        fields = ['name']
