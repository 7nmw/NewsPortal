from django.urls import path
# Импортируем созданное нами представление
from .views import PostList, PostDetail, PostCreate, PostUpdate, PostDelete, SubscriberView


urlpatterns = [
   # path — означает путь.
   # В данном случае путь ко всем товарам у нас останется пустым,
   # чуть позже станет ясно почему.
   # Т.к. наше объявленное представление является классом,
   # а Django ожидает функцию, нам надо представить этот класс в виде view.
   # Для этого вызываем метод as_view.
   path('', PostList.as_view(), name='post_list'), #http://127.0.0.1:8000/news/
   path('<int:pk>', PostDetail.as_view(), name='post_detail'), #http://127.0.0.1:8000/1
   path('create/', PostCreate.as_view(), name='post_create'), #http://127.0.0.1:8000/news/create/
   path('<int:pk>/update/', PostUpdate.as_view(), name='post_update'), #http://127.0.0.1:8000/news/pk/update/
   path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'), #http://127.0.0.1:8000/news/pk/delete/
   path('post/', SubscriberView.as_view(), name='subscribe'), #http://127.0.0.1:8000/
]