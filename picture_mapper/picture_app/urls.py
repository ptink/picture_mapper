from django.conf.urls import patterns, url

from .views import UploadPicture

urlpatterns = patterns('',

    # Picture upload page
    url(r'^upload/$', UploadPicture.as_view(), name='picture_form'),


)
