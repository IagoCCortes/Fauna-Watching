from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from .models import Post, User
from .forms import PostForm, UserForm
# Create your views here.

def index(request):
	
	if request.method == 'POST':
		form = UserForm(request.POST)
		if form.is_valid():
			if User.objects.filter(usuario=request.POST['usuario'], senha=request.POST['senha']).exists():
				return redirect(posts)
	else:
		form = UserForm()
	return render(request, 'blog/login.html', {'form' : form})

def cadastro(request):
	return render(request, 'blog/new_user.html')

def posts(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	query = request.GET.get("q")
	if query:
		posts = posts.filter(especie__icontains=query)
	return render(request, 'blog/posts.html', {'posts' : posts})

def upvote(request, post_post_id):
	post = Post.objects.get(pk=post_post_id)
	post.votes+=1
	post.save()
	return redirect(posts)

def novo_animal(request):
	if request.method == "POST":
		form = PostForm(request.POST, request.FILES or None)
		if form.is_valid():
			post = form.save()
			#
			#Post. = MyProfileForm.cleaned_data["picture"]
			#
			post.save()
			return redirect(posts)
	else:
		form = PostForm()
	return render(request, 'blog/cadAnimais.html', {'form' : form})
	
def novo_bioma(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save()
			post.save()
			return redirect(posts)
	else:
		form = PostForm()
	return render(request, 'blog/cadBiomas.html', {'form' : form})	
	
def sobre(request):
	return render(request, 'blog/sobre.html')	