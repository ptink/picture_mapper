from registration.backends.simple.views import RegistrationView


class RedirectRegistrationView(RegistrationView):
    """
    Subclassing django-registration RegistrationView so
    that it re-directs us to the user's profile page after
    successful registration.
    """

    def get_success_url(self, request, user):
        return "/accounts/profile/"
