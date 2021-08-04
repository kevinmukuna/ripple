from django import forms
from .models import Post


class UserdataModelForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['headline']
        ordering = ['-date', ]

    def clean(self):
        """cleans all the form data"""
        return self.clean()

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(UserdataModelForm, self).__init__(*args, **kwargs)
