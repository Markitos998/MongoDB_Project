from django import forms
from datetime import datetime

class ToDoItemForm(forms.Form):
    text = forms.CharField(max_length=100)
    due_date = forms.DateField(initial=datetime.now())