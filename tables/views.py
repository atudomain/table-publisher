from django.shortcuts import render

# Create your views here.
from django.views import generic
from .models import Table, Row, Column
from rest_framework import viewsets
from rest_framework import permissions
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
