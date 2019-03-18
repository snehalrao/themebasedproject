from django import forms
from loginapp.models import Login_details

class Insurance_form(forms.ModelForm):
    class Meta:
        model = Login_details
        fields = "__all__"
