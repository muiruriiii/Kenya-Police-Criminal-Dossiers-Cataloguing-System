from django import forms
from records.models import Criminal as CriminalModel


class EditForm(forms.ModelForm):

    class Meta:
        model = CriminalModel
        fields= "__all__"