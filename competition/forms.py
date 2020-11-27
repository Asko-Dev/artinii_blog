from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import AmateurCompetition

class AmateurCompetitionForm(ModelForm):

    class Meta:
        model = AmateurCompetition
        fields = ['title', 'link', 'plot', 'poster', 'letter']
