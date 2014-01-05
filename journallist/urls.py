from django.conf.urls import patterns, include, url
from django.contrib.auth.models import User, Group
from django.views.generic import TemplateView
from rest_framework import viewsets, routers

from views import JLItemViewSet, JLCategoryViewSet, TodaysListView



# Routers provide an easy way of automatically determining the URL conf.
router = routers.SimpleRouter()
router.register(r'items', JLItemViewSet)
router.register(r'categories', JLCategoryViewSet)


urlpatterns = patterns('',

    url(r'^api/', include(router.urls)),
    url(r'^api/d/(?P<year>\d{4})/(?P<month>\d\d?)/(?P<day>\d\d?)/', TodaysListView.as_view()),
    url(r'^api/d/', TodaysListView.as_view()),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^$', TemplateView.as_view(template_name="index.html")),
)
