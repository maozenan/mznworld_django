from django.urls import re_path as url
from . import views
from api_test.views import Contract
from api_test.views import Login

urlpatterns = [
    url(r'Contract', views.Contract.as_view(),name='Contract' ),
    url(r'Login', views.Login.as_view(),name='Login' ),
]