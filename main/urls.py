from django.conf.urls import url

from . import views


urlpatterns = (
    url(r'^members/$', views.get_members),
    # url(r'^events/$', views.events),
)
