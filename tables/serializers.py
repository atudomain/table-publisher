from rest_framework import serializers
from .models import Table, Row, Column


class ColumnSerializer(serializers.ModelSerializer):
    class Meta:
        model = Column
        fields = ['id', 'name', 'value']


class RowSerializer(serializers.ModelSerializer):
    columns = serializers.SerializerMethodField()
    class Meta:
        model = Row
        fields = ['id', 'columns']
    def get_columns(self, obj):
        return ColumnSerializer(obj.columns.all(), many=True, read_only=True).data


class TableSerializer(serializers.ModelSerializer):
    rows = serializers.SerializerMethodField()
    class Meta:
        model = Table
        fields = ['id', 'name', 'rows']
    def get_rows(self, obj):
        return RowSerializer(obj.rows.all(), many=True, read_only=True).data
