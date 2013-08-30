from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

from .views import UploadPictureView, MapView

urlpatterns = patterns('',

    # Picture upload page
    url(r'^upload/$', login_required(UploadPictureView.as_view()), name='picture_form'),

    # Global map url
    url(r'^map/$', login_required(MapView.as_view()), name="map"),

)
