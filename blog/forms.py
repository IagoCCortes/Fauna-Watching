from django import forms
from .models import Post, User

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('especie', 'descricao', 'bioma', 'autor', 'imagem', 'local')

class UserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('usuario', 'senha')
		
		