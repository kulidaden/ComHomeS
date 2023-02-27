from .models import Task
from django.forms import ModelForm, TextInput, Textarea
class TaskForm(ModelForm):
    class Meta:
        model=Task
        fields=["title","task"]
        widgets={
            "title": TextInput(attrs={
                'class':'form-control',
                'placeholder':"Введіть ім'я та контактий номер телефону!",
                'style':"width: 500px;font-size: 20px;height: 50px;"

            }),
            "task": Textarea(attrs={
                'class':'form-control',
                'placeholder':'Який пункт Вас зацікавив?',
                'style': "width: 500px; font-size: 20px;margin-top:10px; height: 50px;"
            }),
        }