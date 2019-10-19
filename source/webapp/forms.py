from django import forms
from django.forms import widgets
from webapp.models import *

class PollForm(forms.ModelForm):
    class Meta:
        model = Poll

        widgets = {
            'question':forms.Textarea
        }
        exclude = ['created_at']


class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice

        widgets = {
            'answer_option':forms.Textarea
        }
        fields = ['answer_option', 'poll']


class AnswerForPollForm(forms.ModelForm):
    class Meta:
        model = Choice

        widgets = {
            'answer_option':forms.Textarea
        }
        fields = ['answer_option']


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['choice', 'poll']