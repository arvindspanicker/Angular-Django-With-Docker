from django import forms

from api.models import TestModel

class TestForm(forms.ModelForm):
    class Meta:
        model = TestModel
        fields = ('title',)