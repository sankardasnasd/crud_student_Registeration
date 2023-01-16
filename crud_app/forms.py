from django import forms
from crud_app.models import Students

class Studentform(forms.ModelForm):
    class Meta:
        model = Students
        fields = '__all__'