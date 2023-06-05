from django import forms
from .models import Post, Comment, Profile


class ProfilePageForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['location', 'facebook', 'twitter', 'instagram', 'tiktok', 'description', 'profile_image']
        widgets = {
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Location'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'style': 'min-height: 100%'}),
            'facebook': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Facebook'}),
            'instagram': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Instagram'}),
            'twitter': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Twitter'}),
            'tiktok': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tiktok'}),
            'profile_image': forms.FileInput(attrs={'class': 'form-control'}),
        }


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'category', 'body', 'header_image', 'requires_permission', 'password']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'style': 'min-height: 100%'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'requires_permission': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
            'header_image': forms.FileInput(attrs={'class': 'form-control'}),
        }


class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'style': 'min-height: 100%'}),
        }
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control', 'style': 'min-height: 5rem; max-height: 8rem;'}),
        }

class UpdateCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control', 'style': 'min-height: 100%'}),
        }
