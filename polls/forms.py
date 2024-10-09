from django import forms
from .models import Question

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question_text', 'pub_date']
        widgets = {
            'question_text': forms.TextInput(attrs={'class': 'form-control'}),
            'pub_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }
