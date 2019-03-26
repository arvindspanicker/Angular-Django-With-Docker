from django.urls import path,re_path, include
from testapp.api.v1.views import ListTestEntries

urlpatterns = [
    re_path(r'^(?P<tenant_name>[\w\-]+)/$', ListTestEntries.as_view(), name='api_view'),
]
