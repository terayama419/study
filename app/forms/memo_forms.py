from django import forms
from app.models import Memo

class MemoForm(forms.ModelForm):
    class Meta:
        model = Memo
        fields = ['title', 'content', 'category']
        labels = {
            'title': 'タイトル',
            'content': '内容',
        }
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'タイトルを入力',
                'class': 'form-control',
            }),
            'content': forms.Textarea(attrs={
                'placeholder': '本文を入力',
                'rows': 5,
                'class': 'form-control',
            }),
        }
        error_messages = {
            'title': {
                'required': 'タイトルは必須です',
                'max_length': 'タイトルは50文字以内です',
            },
        }