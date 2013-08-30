from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView
from .forms import PictureForm
from core.views import MessagesMixin
from .models import Picture


class UploadPicture(MessagesMixin, CreateView):
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

    @property
    def form_valid_msg(self):
        return 'uploaded'