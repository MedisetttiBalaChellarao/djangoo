from django import forms


from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
   class Meta:
        model = Feedback
        fields = ['name', 'email', 'phone', 'comments']
