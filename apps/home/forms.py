from django import forms
from .models import *


class UpdatePromptForm(forms.ModelForm):
    class Meta:
        model = Prompt
        fields = ['instructions']  # Make sure that instructions field is included

    instructions = forms.CharField(widget=forms.Textarea, required=True)

