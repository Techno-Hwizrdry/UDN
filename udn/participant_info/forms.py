#  Let's make a form directly based on the Participant model,
#  by using a django ModelForm.

from django.utils.translation import gettext_lazy as _
from django.forms import ModelForm
from .models      import Participant

class ParticipantForm(ModelForm):
    required_css_class = 'required'

    class Meta:
        model  = Participant
        fields = '__all__'
        labels = {
            'num_siblings': _('Number of Siblings'),
            'env_exposures': _('Known environmental exposures'),
            'genetic_mutations': _('Known genetic mutations'),
        }
