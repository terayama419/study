# app/forms.py
from django import forms
from .models import Memo
from django.contrib.auth.models import User

class MemoForm(forms.ModelForm):
    class Meta:
        model = Memo
        fields = ['title', 'content']
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

class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')

        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError('パスワードが一致しません')

        return cleaned_data