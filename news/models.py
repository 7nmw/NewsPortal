from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.urls import reverse



article = 'AR'
news = 'NE'

Types = [
    (article, 'статья'),
    (news, 'новость'),
]


class Author(models.Model):  # наследуемся от класса Model
    user_name = models.OneToOneField(User, on_delete=models.CASCADE)
    user_rating = models.IntegerField(default=0)

    def update_rating(self):
        self.user_rating = 0
        for post in Post.objects.filter(author_name=self):
            self.user_rating += post.rating_post * 3
            for comment in Comment.objects.filter(post_comment=post):
                self.user_rating += comment.rating_comment
        for comment in Comment.objects.filter(user_comment=self.user_name):
            self.user_rating += comment.rating_comment
        self.save()

    def __str__(self):
        return f'{self.user_name}'


class Category(models.Model):
    name_category = models.CharField(max_length=255, unique=True)
    subscribers = models.ManyToManyField(User, through='SubscribersCategory')

    def __str__(self):
        return f'{self.name_category}'


class Post(models.Model):
    article = 'AR'
    news = 'NE'
    author_name = models.ForeignKey(Author, on_delete=models.CASCADE)  # связь «один ко многим» с моделью Author
    types_post = models.CharField(max_length=2, choices=Types, default='NE')  # поле с выбором — «статья» или «новость»;
    datetime_post = models.DateTimeField(auto_now_add=True)  # автоматически добавляемая дата и время создания;
    category_post = models.ManyToManyField(Category, through='PostCategory')  # связь «многие ко многим» с моделью Category (с дополнительной моделью PostCategory);
    header = models.CharField(max_length=255) #  заголовок статьи/новости
    content = models.TextField() #  текст статьи/новости
    rating_post = models.IntegerField(default=0) #  рейтинг статьи/новости

    def preview(self):
        self.content = self.content[0:125]+"..."
        return self.content

    def like(self, amount=0):
        self.rating_post += amount
        self.save()

    def dislike(self, amount=0):
        self.rating_post -= amount
        self.save()

    def __str__(self):
        return f'{self.header}: {self.content[:20]}...'

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE) #	связь «один ко многим» с моделью Post;
    category = models.ForeignKey(Category, on_delete=models.CASCADE) #	связь «один ко многим» с моделью Category.

    def __str__(self):
        return f'{self.post.content}: {self.category.name_category}'


class Comment(models.Model):
    post_comment = models.ForeignKey(Post, on_delete=models.CASCADE)  # связь «один ко многим» с моделью Post;
    user_comment = models.ForeignKey(User, on_delete=models.CASCADE)  #  связь «один ко многим» со встроенной моделью User ;
    text_comment = models.TextField(max_length=255)  # текст комментария;
    datetime_comment = models.DateTimeField(auto_now_add=True)  # дата и время создания комментария;
    rating_comment = models.IntegerField(default=0)  # рейтинг комментария

    def like(self, amount=0):
        self.rating_comment += amount
        self.save()

    def dislike(self, amount=0):
        self.rating_comment -= amount
        self.save()


class SubscribersCategory(models.Model):
    subscriber = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.category}: {self.subscriber}'
