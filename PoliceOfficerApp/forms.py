from django import forms
from records.models import Criminal as CriminalModel

# created a new form for all the fields in the Criminal Model
class EditForm(forms.ModelForm):

    class Meta:
        model = CriminalModel
        fields= "__all__"