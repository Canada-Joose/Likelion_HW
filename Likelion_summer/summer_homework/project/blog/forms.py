from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'realtor', 'mainphoto', 'content', 'author')

        widgets = {
            'title': forms.TextInput(attrs={
                'class': "form-control",
                'style': 'width: 400px;',
                'placeholder': '매물 종류 및 보증금/월세 금액'
            }),
            'realtor': forms.TextInput(attrs={
                'class': "form-control",
                'style': 'width: 400px;',
                'placeholder': '공인중개사 이름'
            }),
            'content': forms.EmailInput(attrs={
                'class': "form-control",
                'style': 'width: 400px; height: 100px;',
                'placeholder': '주인 측 특이사항'
            }),
        }
