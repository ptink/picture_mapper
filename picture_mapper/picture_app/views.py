from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, View, ListView, UpdateView, DeleteView
from braces.views import FormMessagesMixin, JSONResponseMixin
from .forms import PictureForm
from .models import Picture


class ProfileView(ListView):
    template_name = 'profile.html'
    queryset = Picture.objects.all()

    def get_queryset(self):
        return self.request.user.picture_set.all()


class PictureView(FormMessagesMixin):
    model = Picture
    template_name = 'forms/picture_form.html'
    form_class = PictureForm
    success_url = reverse_lazy('profile')

    def get_form_kwargs(self):
        """
        Returns the keyword arguments for instanciating the form.
        Need this to replace request kwarg (AuthorForm popped it)
        """
        kwargs = {
            'initial': self.get_initial(),
            'instance': self.object}
        if self.request.method in ('POST', 'PUT'):
            kwargs.update({
                'data': self.request.POST,
                'files': self.request.FILES,
                'request': self.request})
        return kwargs


class UploadPictureView(PictureView, CreateView):

    def get_form_invalid_message(self):
        return 'Failed to save {0}'.format(self.model._meta.verbose_name)

    def get_form_valid_message(self):
        return '{0} uploaded'.format(self.object.title)


class EditPictureView(PictureView, UpdateView):

    def get_queryset(self):
        # Make sure user can only edit their own pictures
        return self.request.user.picture_set.all()

    def get_form_invalid_message(self):
        return 'Failed to save {0}'.format(self.model._meta.verbose_name)

    def get_form_valid_message(self):
        return '{0} updated'.format(self.object.title)


class DeletePictureView(DeleteView):
    template_name = None
    success_url = reverse_lazy('profile')
    model = Picture

    def get_queryset(self):
        # Make sure user can only delete their own pictures
        return self.request.user.picture_set.all()


class PictureAjaxView(JSONResponseMixin, View):
    content_type = 'application/json'

    def get_queryset(self):
        queryset = Picture.objects.all() \
                          .values('title', 'image', 'author__username',
                                  'created', 'description', 'latitude', 'longitude',)
        # If the request has "user" parameter we want to filter the queryset on the user id
        if "user" in self.request.GET:
            return list(queryset.filter(author=self.request.GET["user"]))
        else:
            return list(queryset)

    def get(self, request, *args, **kwargs):
        context_dict = {
            'pictures': self.get_queryset(),
        }
        return self.render_json_response(context_dict)
