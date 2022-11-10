from django import forms
from app.models import *
class NameForm(forms.Form):
    name=forms.CharField(max_length=100)
    age=forms.IntegerField()

class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'
