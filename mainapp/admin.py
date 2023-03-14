from django.contrib import admin
from .models import Contact


# Register your models here.


# class PostAdmin(admin.ModelAdmin):
#     list_display = ('title', 'content_post', 'author_post', 'date_creation')
#     search_fields = ('title', 'content')
#
#
# admin.site.register(Post, PostAdmin)
#
#
#


class AdminCont(admin.ModelAdmin):
    list_display = ('name', 'email', 'mes')


admin.site.register(Contact, AdminCont)
