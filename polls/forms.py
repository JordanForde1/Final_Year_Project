from django.forms import ModelForm
from polls.models import Constituency


class MyModelForm(ModelForm):
    class Meta:
        model = Constituency
        fields = ['constituency_text']