from rest_framework import serializers
from .models import Table, Row, Column


class ColumnSerializer(serializers.ModelSerializer):
    class Meta:
        model = Column
        fields = ['name', 'value']


class RowSerializer(serializers.ModelSerializer):
    columns = ColumnSerializer(many=True)
    class Meta:
        model = Row
        fields = ['columns']


class TableSerializer(serializers.ModelSerializer):
    rows = RowSerializer(many=True)
    class Meta:
        model = Table
        fields = ['name', 'rows']
    def create(self, validated_data):
        rows_data = validated_data.pop('rows')
        table = Table.objects.create(**validated_data)
        for row_data in rows_data:
            row = Row.objects.create(table=table)
            columns_data = row_data.pop('columns')
            for column_data in columns_data:
                Column.objects.create(row=row, **column_data)
        return table
