from django.contrib import admin
from .models import Author, Category, Post, PostCategory, Comment, SubscribersCategory
from modeltranslation.admin import TranslationAdmin

# создаём новый класс для представления товаров в админке
class PostAdmin(admin.ModelAdmin):
    # list_display — это список или кортеж со всеми полями, которые вы хотите видеть в таблице с товарами
    list_display = ('id', 'header', 'types_post', 'author_name', 'datetime_post')
    list_filter = ('types_post', 'author_name')  # добавляем примитивные фильтры в нашу админку
    search_fields = ('header', 'content') # тут всё очень похоже на фильтры из запросов в базу

class CommentAdmin(admin.ModelAdmin):
    # list_display — это список или кортеж со всеми полями, которые вы хотите видеть в таблице с товарами
    list_display = ('id', 'user_comment', 'text_comment', 'datetime_comment', 'rating_comment')
    search_fields = ('post_comment', 'user_comment') # тут всё очень похоже на фильтры из запросов в базу


class CategoryAdmin(TranslationAdmin):
    model = Category

admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(PostCategory)
admin.site.register(Comment, CommentAdmin)
admin.site.register(SubscribersCategory)
