from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, View
from braces.views import FormMessagesMixin, JSONResponseMixin
from .forms import PictureForm
from .models import Picture


class UploadPictureView(FormMessagesMixin, CreateView):
    model = Picture
    template_name = 'picture_app/forms/picture_form.html'
    form_class = PictureForm
    success_url = reverse_lazy('profile')

    def get_form_kwargs(self):
        """
        Returns the keyword arguments for instanciating the form.
        """
        kwargs = {'initial': self.get_initial()}
        if self.request.method in ('POST', 'PUT'):
            kwargs.update({
                'data': self.request.POST,
                'files': self.request.FILES,
                'request': self.request})
        return kwargs

    def get_form_invalid_message(self):
        return 'Failed to save {0}'.format(self.model._meta.verbose_name)

    def get_form_valid_message(self):
        return '{0} uploaded'.format(self.object.title)


class PictureAjaxView(JSONResponseMixin, View):
    content_type = 'application/json'

    def get_queryset(self):
        queryset = Picture.objects.all() \
                          .values('title', 'image', 'author__username',
                                  'created', 'description', 'latitude', 'longitude',)
        return list(queryset)

    def get(self, request, *args, **kwargs):
        context_dict = {
            'pictures': self.get_queryset(),
        }
        return self.render_json_response(context_dict)
