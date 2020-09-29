from django import forms 
from .models import Post,User, Category
from .models import UserImage
from .models import Comment

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title','text','category',)


		widgets = {
		'title': forms.TextInput(attrs={'class':'form-control'}),
		'text': forms.TextInput(attrs={'class':'form-control'}),
		'category': forms.Select(attrs={'class':'form-control'}),
		}

class UserEdit(forms.ModelForm):
	class Meta:
		model = User
		fields = ('username','first_name', 'last_name', 'email',)

class ImageEdit(forms.ModelForm):
	class Meta:
		model=UserImage
		fields = ("image",)

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ('name','email','body')

