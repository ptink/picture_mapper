import json
from django.core.exceptions import ImproperlyConfigured
from django.contrib import messages
from django.http import HttpResponse

from registration.backends.simple.views import RegistrationView


class AjaxableResponseMixin(object):
    """
    Mixin to add AJAX support to a form.
    Must be used with an object-based FormView (e.g. CreateView)
    """
    def render_to_json_response(self, context, **response_kwargs):
        data = json.dumps(context)
        response_kwargs['content_type'] = 'application/json'
        return HttpResponse(data, **response_kwargs)

    def form_invalid(self, form):
        response = super(AjaxableResponseMixin, self).form_invalid(form)
        if self.request.is_ajax():
            return self.render_to_json_response(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        # We make sure to call the parent's form_valid() method because
        # it might do some processing (in the case of CreateView, it will
        # call form.save() for example).
        response = super(AjaxableResponseMixin, self).form_valid(form)
        if self.request.is_ajax():
            data = {
                'pk': self.object.pk,
            }
            return self.render_to_json_response(data)
        else:
            return response


class MessagesMixin(object):
    """
    Mixin to add message support to a form for the creation
    or updating of objects.
    """

    @property
    def form_valid_msg(self):
        raise ImproperlyConfigured("you're missing the 'form_valid_msg' property")

    def get_form_valid_msg(self):
        return self.form_valid_msg

    def form_invalid(self, form):
        # Create an error message
        response = super(MessagesMixin, self).form_invalid(form)
        if self.model:
            message = 'Could not add %s' % self.model._meta.verbose_name
        else:
            message = 'Creation failed'
        messages.add_message(self.request,
                             messages.ERROR,
                             message)
        return response

    def form_valid(self, form):
        # Create a success message
        response = super(MessagesMixin, self).form_valid(form)
        msg = 'Successfully {form_valid_msg} {form}'.format(
            form_valid_msg=self.get_form_valid_msg(),
            form=self.object)
        messages.success(self.request, msg)
        return response


class RedirectRegistrationView(RegistrationView):
    """
    Subclassing django-registration RegistrationView so
    that it re-directs to the user's profile page after
    successful registration.
    """

    def get_success_url(self, request, user):
        return "/accounts/profile/"
