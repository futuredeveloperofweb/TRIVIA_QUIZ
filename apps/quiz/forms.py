from django import forms
from .models import Quiz, Question, Option


class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ['title', 'description']


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question_text', 'question_type']


class OptionForm(forms.ModelForm):
    class Meta:
        model = Option
        fields = ['text', 'is_correct']


class QuizAnswerForm(forms.Form):
    def __init__(self, *args, **kwargs):
        questions = kwargs.pop('questions')
        super().__init__(*args, **kwargs)
        for question in questions:
            options = question.options.all()
            self.fields[f'question_{question.question_id}'] = forms.ChoiceField(
                label=question.question_text,
                choices=[(option.option_id, option.text) for option in options],
                widget=forms.RadioSelect,
                required=True
            )
