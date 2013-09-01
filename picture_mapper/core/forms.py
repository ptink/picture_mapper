from django import forms


class AuthorModelForm(forms.ModelForm):
    """
    Custom ModelForm that automatically adds the currently
    logged in user as the author of the model record
    """
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        return super(AuthorModelForm, self).__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        kwargs['commit'] = False
        obj = super(AuthorModelForm, self).save(*args, **kwargs)
        if self.request:
            obj.author = self.request.user
        obj.save()
        return obj
