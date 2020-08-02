from django.shortcuts import render

# Create your views here.
from django.views import generic
from django.shortcuts import get_object_or_404

from .models import Table, Row, Column
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response
from .serializers import TableSerializer, RowSerializer, ColumnSerializer


class IndexView(generic.ListView):
    model = Table
    template_name = 'tables/index.html'


class DetailView(generic.DetailView):
    model = Table
    template_name = 'tables/detail.html'


class TableViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows tables to be viewed or edited.
    """
    queryset = Table.objects.all()
    serializer_class = TableSerializer

    def retrieve(self, request, pk=None):
        queryset = Table.objects.all()
        table = get_object_or_404(queryset, name=pk)
        serializer = TableSerializer(table)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        queryset = Table.objects.all()
        table = get_object_or_404(queryset, name=pk)
        table.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class RowViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows rows to be viewed or edited.
    """
    queryset = Row.objects.all()
    serializer_class = RowSerializer


class ColumnViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows columns to be viewed or edited.
    """
    queryset = Column.objects.all()
    serializer_class = ColumnSerializer
