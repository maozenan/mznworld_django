from django.conf.urls import url, include
from . import views
from api_test.views import Contract

urlpatterns = [
    url(r'Contract', views.Contract.as_view(),name='Contract' )
]