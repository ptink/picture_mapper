from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from .views import UploadPictureView, PictureAjaxView

urlpatterns = patterns('',
    # Picture upload page url
    url(r'^upload/$', login_required(UploadPictureView.as_view()), name='picture_form'),

    # Global map url
    url(r'^map/$', login_required(TemplateView.as_view(template_name='picture_app/show_map.html')), name="map"),

    # Picture data AJAX url
    url(r'^map/picture-data/$', login_required(PictureAjaxView.as_view()), name="picture_data"),

)
