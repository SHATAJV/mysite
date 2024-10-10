
from django import forms
from .models import Question, Choice


class QuestionForm(forms.ModelForm):
    choice1 = forms.CharField(max_length=200, required=True)
    choice2 = forms.CharField(max_length=200, required=True)
    choice3 = forms.CharField(max_length=200, required=False)
    choice4 = forms.CharField(max_length=200, required=False)
    choice5 = forms.CharField(max_length=200, required=False)

    class Meta:
        model = Question
        fields = ['question_text', 'pub_date']
        widgets = {
            'question_text': forms.TextInput(attrs={'class': 'form-control'}),
            'pub_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

    def save(self, commit=True):
        question = super().save(commit)

        if commit:
            choices = [
                self.cleaned_data['choice1'],
                self.cleaned_data['choice2'],
                self.cleaned_data['choice3'],
                self.cleaned_data['choice4'],
                self.cleaned_data['choice5'],
            ]
            for choice in choices:
                if choice:
                    Choice.objects.create(question=question, choice_text=choice)
        return question
