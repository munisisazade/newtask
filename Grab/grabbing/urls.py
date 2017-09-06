from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView, parser


urlpatterns = [
    url(r'^$', CreateView.as_view(), name='index'),
    url(r'^parser/$', parser, name='parser'),
    ]
urlpatterns = format_suffix_patterns(urlpatterns)
