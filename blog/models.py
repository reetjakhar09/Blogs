from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from django.db.models import CharField, Model
from django_extensions.db.fields import AutoSlugField




	



class Category(models.Model):
	created_at =models.DateTimeField(auto_now_add=True,verbose_name="created at")
	updated_at = models.DateTimeField(auto_now=True,verbose_name="Updated at")
	title = models.CharField(max_length=255, verbose_name="Title")
	text = models.TextField(blank = True)
	name = models.CharField(max_length=100, default=True)
	

	class Meta:
		verbose_name = "Category"
		verbose_name_plural = "Categories"
		ordering = ['title']

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('index')


class Post(models.Model):
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True,verbose_name="created at")
	published_date = models.DateTimeField(blank=True, null=True)
	category = models.ForeignKey(Category, on_delete=models.CASCADE, null = True, blank=True)
	updated_at = models.DateTimeField(auto_now=True,verbose_name="Updated at")
	is_published  = models.BooleanField(default=False, verbose_name="Is Published?")
	slug = AutoSlugField(populate_from='title',editable=True)
	likes = models.ManyToManyField(User, related_name='blog_posts')
	thumb = models.ImageField(default='default.png', blank=True)
	image = models.ImageField(upload_to='post_images/',blank=True)


	class Meta:
		verbose_name = "Post"
		verbose_name_plural = "Posts"
		ordering = ['-created_at']

	def publish(self):
		self.is_published =True
		self.published_at = timezone.now()
		self.save()

	def total_likes(self):
		return self.likes.count()

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('index')


	def slugify_function(self, content):
		return content.replace('_', '-').lower()

	def get_thumb(self):
		
		if host.startswith('www.'):
			host = host[4:]
		thumb = 'https://api.thumbalizr.com/?url=http://' + host + '&width=125'
		return thumb

class Tag(models.Model):
	title = models.CharField(max_length=255, verbose_name="Title")
	text = models.TextField(blank = True)
	name = models.CharField(max_length=100, default=True)
	slug = AutoSlugField(populate_from='title',editable=True)
	post = models.ForeignKey(Post, on_delete=models.CASCADE,default=True)

	def __str__(self):
		return self.title


	def get_absolute_url(self):
		return reverse('index')

	def slugify_function(self, content):
		return content.replace('_', '-').lower()


class Comment(models.Model):
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=True)
	post = models.ForeignKey(Post, on_delete=models.CASCADE,)
	slug = AutoSlugField(populate_from='name')
	name= models.CharField(max_length=80)
	email = models.EmailField()
	body = models.TextField(max_length=50)
	created_on = models.DateTimeField(auto_now_add=True)
	active = models.BooleanField(default=True)
	reply = models.ForeignKey('self',null=True, blank=True, related_name='replies',on_delete=models.CASCADE)
	content = models.TextField(max_length=100, default=True)

	class Meta:
		ordering = ['created_on']

	def __str__(self):
		return 'Comment {} by {}'.format(self.body, self.name)

class UserProfile(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, default=True)
	first_name = models.TextField()
	last_name = models.TextField()
	email = models.TextField()
	image = models.ImageField()

	def __str__(self):
		return self.user.username


class UserImage(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	image =models.ImageField()


	def __str__(self):
		return self.user.username


	


