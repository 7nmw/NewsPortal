# Generated by Django 4.1.3 on 2022-12-22 18:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0002_subscriberscategory_category_subscribers'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'verbose_name_plural': 'Авторы'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name_plural': 'Комментарии'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name_plural': 'Посты'},
        ),
        migrations.AlterModelOptions(
            name='postcategory',
            options={'verbose_name_plural': 'Категории постов'},
        ),
        migrations.AlterModelOptions(
            name='subscriberscategory',
            options={'verbose_name_plural': 'Категории подписчиков'},
        ),
        migrations.AddField(
            model_name='category',
            name='name_category_en_us',
            field=models.CharField(max_length=255, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_category_ru',
            field=models.CharField(max_length=255, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='datetime_comment',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата и время комментария'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='rating_comment',
            field=models.IntegerField(default=0, verbose_name='Рейтинг комментария'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='text_comment',
            field=models.TextField(max_length=255, verbose_name='Текст комментария'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='user_comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор комментария'),
        ),
        migrations.AlterField(
            model_name='post',
            name='author_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.author', verbose_name='Имя автора'),
        ),
        migrations.AlterField(
            model_name='post',
            name='datetime_post',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата и время поста'),
        ),
        migrations.AlterField(
            model_name='post',
            name='header',
            field=models.CharField(max_length=255, verbose_name='Заголовок'),
        ),
        migrations.AlterField(
            model_name='post',
            name='types_post',
            field=models.CharField(choices=[('AR', 'статья'), ('NE', 'новость')], default='NE', max_length=2, verbose_name='Тип поста'),
        ),
    ]
