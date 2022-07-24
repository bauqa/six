from .models import Task
from django.forms import ModelForm, TextInput, Textarea

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title","description"]
        widgets = {
        "title": TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите имя таска'
        }),
        "description":Textarea(attrs={
            'class': 'mt-5 form-control',
            'placeholder': 'Введите описание таска',})
        }