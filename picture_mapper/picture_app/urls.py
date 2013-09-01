from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from .views import UploadPictureView, EditPictureView, PictureAjaxView, DeletePictureView

urlpatterns = patterns('',
    # Picture model urls
    url(r'^upload/$', login_required(UploadPictureView.as_view()), name='upload_picture'),
    url(r'^edit/(?P<pk>\d+)/$', login_required(EditPictureView.as_view()), name='edit_picture'),
    url(r'^delete/(?P<pk>\d+)/$', login_required(DeletePictureView.as_view()), name='delete_picture'),

    # Global map url
    url(r'^map/$', login_required(TemplateView.as_view(template_name='picture_app/show_map.html')), name="map"),

    # Picture data AJAX url
    url(r'^map/picture-data/$', login_required(PictureAjaxView.as_view()), name="picture_data"),

)
