from django.shortcuts import render
from rest_framework import viewsets, generics, filters
from jl.serializers import JLItemSerializer, JLCategorySerializer, JLCategoryFullSerializer, JLItemFullSerializer
from jl.models import JLCategory, JLItem

from datetime import datetime, date


class JLCategoryViewSet(viewsets.ModelViewSet):
    queryset = JLCategory.objects.all()
    serializer_class = JLCategorySerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('=category_text',)


class JLItemViewSet(viewsets.ModelViewSet):
    queryset = JLItem.objects.all()
    serializer_class = JLItemSerializer


class TodaysListView(generics.ListAPIView):
    serializer_class = JLCategoryFullSerializer


    def get_queryset(self):
        # Querystring Date is formatted as yyyymmdd
        query_date = self.request.QUERY_PARAMS.get('d', None)
        if query_date is not None:
            thedate = datetime.strptime(query_date, "%Y%m%d").date()
        else:
            thedate = date.today()

        return JLCategory.objects.filter(items__pub_date=thedate)
