from django.conf.urls import patterns, include, url
from django.contrib.auth.models import User, Group
from django.views.generic import TemplateView
from rest_framework import viewsets, routers

import views



# Routers provide an easy way of automatically determining the URL conf.
router = routers.SimpleRouter()
router.register(r'items', views.JLItemViewSet)
router.register(r'categories', views.JLCategoryViewSet)


urlpatterns = patterns('',

    url(r'^api/d/', views.TodaysListView.as_view()),
    url(r'^api/', include(router.urls)),

    url(r'^(?P<category_slug>[^\s]+)/', views.category_detail, name="journallist_category" ),

    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^$', TemplateView.as_view(template_name="journallist/index.html"), name="journallist_home"),
)
