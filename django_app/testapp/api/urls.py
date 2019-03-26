from django.urls import path,re_path, include

urlpatterns = [
    re_path(r'^v1/', include('testapp.api.v1.urls'), name='test_app_v1'),
]