from django.contrib import admin
from post.models import Post, PostLike


class PostAdmin(admin.ModelAdmin):
    model = Post
    list_display = ('id', 'owner', 'post', 'created', 'modified')


class PostLikeAdmin(admin.ModelAdmin):
    model = PostLike
    list_display = ('id', 'post', 'user', 'like', 'created', 'modified')


# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(PostLike, PostLikeAdmin)
