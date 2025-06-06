from django import forms
from .models import Article, Comment

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'category', 'entry', 'header_image']

class ArticleUpdateForm(forms.ModelForm):
    class Meta:
        model = Article
        exclude = ['created_on', 'author'] 

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['entry']
