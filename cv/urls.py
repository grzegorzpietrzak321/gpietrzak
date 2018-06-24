from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'home$', home, name="cv_home"),
    url(r'^$', home, name="cv_home"),
    url(r'home_authenticated$', home_authenticated, name="cv_home_authenticated")
]
