from django.shortcuts import render
from datetime import datetime, date
from rest_framework import viewsets, generics, filters

from serializers import JLItemSerializer, JLCategorySerializer, JLCategoryFullSerializer, JLItemFullSerializer, DailyItemsSerializer
from models import JLCategory, JLItem



class ExactSearchFilter(filters.SearchFilter):
    def get_search_terms(self, request):
        """
        Search terms are set by a ?search=... query parameter,
        and may be comma and/or whitespace delimited.
        """
        params = request.QUERY_PARAMS.get(self.search_param, '')
        return [params] #.replace(',', ' ').split()


class JLCategoryViewSet(viewsets.ModelViewSet):
    queryset = JLCategory.objects.all()
    serializer_class = JLCategorySerializer
    filter_backends = (ExactSearchFilter,)
    search_fields = ('=category_text',)


class JLItemViewSet(viewsets.ModelViewSet):
    queryset = JLItem.objects.all()
    serializer_class = JLItemSerializer


class TodaysListView(generics.ListAPIView):
    serializer_class = DailyItemsSerializer


    def get_queryset(self):
        # Querystring Date is formatted as yyyymmdd
        query_date = self.request.QUERY_PARAMS.get('d', None)
        if query_date is not None:
            self.date = datetime.strptime(query_date, "%Y%m%d").date()
        else:
            self.date = date.today()

        return JLCategory.objects.filter(items__pub_date=self.date).distinct()
