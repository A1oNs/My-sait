from .models import new
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class newForm(ModelForm):
    class Meta:
        model = new
        fields = ['name', 'number', 'comment', 'data']

        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя'
            }),
            "number": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Номер телефона'
            }),
            "data": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата записи'
            }),
            "comment": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Комментарий'
            }),
        }