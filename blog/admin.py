from django.contrib import admin
from blog.models import Blog, Category
#imported the models created

class BlogAdmin(admin.ModelAdmin):
    #exclude = ['posted']
    #automatically filled
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title']

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    #both slugs are created automatically from the title

admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CategoryAdmin)
#registers models with admin
