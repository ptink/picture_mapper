from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

from core.views import RedirectRegistrationView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='base.html'), name="home"),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # django-registration urls
    url(r'^register/$', RedirectRegistrationView.as_view(), name='registration_register'),
    url(r'^register/closed/$',
        TemplateView.as_view(template_name='registration/registration_closed.html'),
        name='registration_disallowed'),
    (r'^accounts/', include('registration.auth_urls')),
    url(r'^accounts/profile/', login_required(TemplateView.as_view(template_name='core/profile.html')), name="profile"),

    # map url
    url(r'^map/', login_required(TemplateView.as_view(template_name='easy_maps/map.html')), name="map"),

    # picture app urls
    (r'^pictures/', include('picture_app.urls')),

)
