from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView, ListView
from django.contrib.auth.decorators import login_required
from core.views import RedirectRegistrationView
from picture_app.views import ProfileView
from picture_app.models import Picture

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', ListView.as_view(template_name='home.html',
                                queryset=Picture.objects.all().order_by('-created')[:10]), name="home"),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # django-registration urls
    url(r'^register/$', RedirectRegistrationView.as_view(), name='registration_register'),
    url(r'^register/closed/$',
        TemplateView.as_view(template_name='registration/registration_closed.html'),
        name='registration_disallowed'),
    (r'^accounts/', include('registration.auth_urls')),
    url(r'^accounts/profile/', login_required(ProfileView.as_view()), name="profile"),

    # picture app urls
    (r'^pictures/', include('picture_app.urls')),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
