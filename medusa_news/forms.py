from django import forms
from .models import News


class DateInput(forms.DateInput):
    input_type = 'date'


class NewsForm(forms.ModelForm):

    class Meta:
        model = News
        widgets = {'date': DateInput()}
        fields = "__all__"