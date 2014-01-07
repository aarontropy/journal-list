from django.shortcuts import render
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from datetime import datetime, date
from rest_framework import viewsets, generics, filters

from serializers import JLItemSerializer, JLCategorySerializer, JLCategoryFullSerializer, JLItemFullSerializer, DailyItemsSerializer
from models import JLCategory, JLItem



class ExactSearchFilter(filters.SearchFilter):

    def filter_queryset(self, request, queryset, view):
        """ Overrides the filter_queryset in order to cancel the filter
            if there is no search parameter """
        if request.QUERY_PARAMS.get(self.search_param, None) is not None:
            return super(ExactSearchFilter, self).filter_queryset(request, queryset, view)
        else:
            return queryset

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
        print "wtf"
        query_date = self.request.QUERY_PARAMS.get('d', None)
        if query_date is not None:
            self.date = datetime.strptime(query_date, "%Y%m%d").date()
        else:
            self.date = date.today()

        return JLCategory.objects.filter(items__pub_date=self.date).distinct()



def category_detail(request, category_slug=None):
    category = get_object_or_404(JLCategory, slug=category_slug)

    return render_to_response('journallist/category.html',
        {'category': category,},
        context_instance=RequestContext(request))
