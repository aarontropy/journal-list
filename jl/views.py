from django.shortcuts import render
from rest_framework import viewsets, generics
from jl.serializers import JLItemSerializer, JLCategorySerializer, JLCategoryFullSerializer, JLItemFullSerializer
from jl.models import JLCategory, JLItem

from datetime import date


class JLCategoryViewSet(viewsets.ModelViewSet):
    queryset = JLCategory.objects.all()
    serializer_class = JLCategorySerializer


class JLItemViewSet(viewsets.ModelViewSet):
    queryset = JLItem.objects.all()
    serializer_class = JLItemFullSerializer


class TodaysListView(generics.ListAPIView):
    serializer_class = JLCategoryFullSerializer


    def get_queryset(self):
        year = self.kwargs.get('year', None)
        month = self.kwargs.get('month', None)
        day = self.kwargs.get('day', None)

        if year is None or month is None or day is None:
            thedate = date.today()
        else:
            thedate = date(int(year), int(month), int(day))

        return JLCategory.objects.filter(items__pub_date=thedate)
