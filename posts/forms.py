from django import forms

from posts.models import Posts


class AddPostMyForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ('title', 'content', 'image', 'is_published', 'paid_published', 'cost')


class UpdatePostMyForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ('title', 'content', 'image', 'is_published', 'paid_published', 'cost')
