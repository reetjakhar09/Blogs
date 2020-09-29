from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Post, Category,Tag, Comment,UserImage
from .forms import PostForm
from django.contrib.auth.models import User, auth
from .forms import UserEdit,ImageEdit
from .forms import CommentForm



# Create your views here.
def post_list(request):
	
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	
	return render(request, 'blog/post_list.html', {'posts':posts, } )

def post_detail(request,pk):
	post = get_object_or_404(Post, pk=pk)
	comment = Comment.objects.filter(active=True, post=post,reply=None).order_by('-created_on')
	tag= Tag.objects.filter(post=post)
	stuff = get_object_or_404(Post,pk=pk)
	total_likes = stuff.total_likes()


	liked = False
	if stuff.likes.filter(id=request.user.id).exists():
		liked = True 

	if request.method =='POST':
		comment_form = CommentForm(data=request.POST)
		if comment_form.is_valid():
			
			reply_id = request.POST.get('comment_id')
			comment_qs = None
			if reply_id:
				comment_qs = Comment.objects.get(id=reply_id)
			

			new_comment = comment_form.save(commit=False)
			new_comment.post = post
			new_comment.reply = comment_qs
			new_comment.save()
			return redirect('post_detail',pk=post.pk)
	else:
		comment_form = CommentForm()
	return render(request, 'blog/post_detail.html', {'comment_form':comment_form,'post':post,'comment':comment,'tag':tag, 'total_likes':total_likes,'liked':liked})

	

def post_new(request):
	if request.method =="POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('post_detail', pk=post.pk)

	else:
		form = PostForm()
	return render(request, 'blog/post_edit.html',{'form':form})

def post_edit(request, pk):
	post = get_object_or_404(Post, pk=pk)
	if request.method == "POST":
		form = PostForm(request.POST, instance=post)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('post_detail', pk=post.pk)
	else:
		form = PostForm(instance=post)
	return render(request, 'blog/post_edit.html', {'form': form})

def edit_profile(request,pk):
	user= get_object_or_404(User ,pk=pk)
	# imguser = UserImage.objects.filter(user = user)
	# print(imguser)
	if request.method =="POST":
		form = UserEdit(request.POST,instance=user)
		form_image= ImageEdit(request.POST, request.FILES)
		if form.is_valid() and form_image.is_valid():
			img = UserImage.objects.get(user=request.user)
			if img:
				img.image = form_image.cleaned_data.get('image')
				# img.user = request.user
				img.save()
			else:
				form = form(commit=False)
				form_image= form_image(commit=False)
				form.user = request.user
				form_image = request.user
				img.save()
				form.save()
				form_image.save()
			
			return redirect('/')
	else:
		form = UserEdit(instance=user)
		form_image= ImageEdit(instance=user)
	return render(request, 'edit_profile.html', {'form': form,  'form_image':form_image})

def register(request):
		
		if request.method =="POST":
			first_name = request.POST.get('first_name')
			last_name = request.POST.get('last_name')
			username = request.POST.get('username')
			password1 = request.POST.get('password1')
			password2 = request.POST.get('password2')
			email = request.POST.get('email')

			if password1 == password2:
				if User.objects.filter(username=username).exists():
					messages.info(request,'Username Taken')
					return redirect('register')
				elif User.objects.filter(email=email).exists():
					messages.info(request, 'Email Taken')
					return redirect('register')
				else:
					user = User.objects.create_user(username=username, password=password1, email=email,first_name=first_name,last_name=last_name)
					user.save();
					
					print('user created')	
		   
			else:
				print('password not matching..')
			return redirect('login')

		else:		
			return render(request, 'register.html')


def login(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		print(username, password)
		user = auth.authenticate(username=username,password=password)

		if user is not None:
			auth.login(request, user)
			return redirect("/")
		else:
			messages.info(request, 'invalid credentials')
			return redirect('login')

	else:
		return render(request, 'login.html')

def logout(request):
	auth.logout(request)
	return redirect('/')

def profile(request,):
	imgg = UserImage.objects.filter(user = request.user).first()
	print(imgg)

	return render(request,'profile.html',{'imgg':imgg})



def category_detail(request,pk):
	category = get_object_or_404(Category, pk=pk)
	category = Category.objects.filter(pk=pk).first()
	print(category)
	posts = Post.objects.filter(category=category).all()
	print(posts)
	post = get_object_or_404(Post, pk=pk)
	return render (request, 'category_detail.html',{'category':category,'posts':posts, 'post':post})

def category_list(request):
	category = Category.objects.all()
	print(category)
	
	return render(request,'category_list.html',{'category': category})

def tag_list(request):
	tag = Tag.objects.all()
	print(tag)
	return render(request, 'tag_list.html', {'tag':tag})

def tag_detail(request,slug,):
	tag = get_object_or_404(Tag, slug=slug)
	
	print(tag)
	posts = Post.objects.filter(tag=tag).all()
	print(posts)
	
	return render (request, 'tag_detail.html',{'tag':tag, 'posts':posts })

def like_post(request,pk):
	post = get_object_or_404(Post, id=request.POST.get('post_id'))
	liked = False
	if post.likes.filter(id=request.user.id).exists():
		post.likes.remove(request.user)
		liked = False
	else:
		post.likes.add(request.user)
		liked = True

	return redirect('post_detail',pk=pk)

