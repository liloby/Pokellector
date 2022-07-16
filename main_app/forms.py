from django.forms import ModelForm
from .models import Interaction

class InteractionForm(ModelForm):
    class Meta:
        model = Interaction
        fields = ['date', 'interact']