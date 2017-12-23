from django.conf.urls import url
from django.views.generic import RedirectView
from first import views
from django.conf.urls import handler404


urlpatterns = [

    url(r'^(?P<g>[0-9]{1})/(?P<new>[0-9]{3})/$', views.main),
    url(r'^$', RedirectView.as_view(url='https://djbook.ru/rel1.9/topics/http/urls.html'))

]
