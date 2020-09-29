from django.contrib import admin
from .models import Post,Category, Tag, Comment,UserImage

class CommentAdmin(admin.ModelAdmin):
	list_display = ('name', 'post','created_on','active')
	list_filter = ('active','created_on')
	search_fields = ('name','email','body')
	actions = ['approve_comments']


	def approve_comments(self,request,queryset):
		queryset.update(active=True)

class PostsAdmin(admin.ModelAdmin):
	list_display = ('title','updated_at','published_date','author',)



	
class CategoryAdmin(admin.ModelAdmin):
	list_display = ('title','created_at','updated_at',)

class TagAdmin(admin.ModelAdmin):
	list_display = ('title','text', 'post',)


admin.site.register(Post,PostsAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Comment,CommentAdmin)
admin.site.register(UserImage)

# Register your models here.
