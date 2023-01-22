# django_1.6HW-03

## Создана структура базы данных
Была использована база данных db.sqlite3

Установим Django:
pip install django

Запускаем приложение:
python manage.py runserver

## В данной ветке было добавлено следующее:
*Создана новая страница с адресом /news/, на которой выводиться список всех новостей.

*Выводятся все статьи в виде заголовка, даты публикации и первых 20 символов текста.

*Новости выводяться в порядке от более свежей к самой старой.

*Сделана отдельная страница для полной информации о статье /news/<id новости>.

*На этой странице показана вся информация о статье. Название, текст и дата загрузки в формате день.месяц.год.

*Есть собственный фильтр censor, который заменяет буквы нежелательных слов в заголовках и текстах статей на символ «*».

*Все новые страницы используют шаблон default.html как основу.


## В базу данные были добавленые данные с помощью python shell

#Создать двух пользователей
Sam = User.objects.create_user('Sam')
Din = User.objects.create_user('Din')

#Создать два объекта модели Author, связанные с пользователями
Sam_author=Author.objects.create(user_name=Sam)
Din_author=Author.objects.create(user_name=Din)

#Добавить 4 категории в модель Category.
Category.objects.create(name_category = 'Hockey')
Category.objects.create(name_category = 'Basketball')
Category.objects.create(name_category = 'Football')
Category.objects.create(name_category = 'WC2022')


#Добавить 2 статьи и 1 новость
post_1 = Post.objects.create(author_name = Sam_author, types_post = 'AR', header='У Малкина уже 450 шайб в НХЛ! Больше в истории «Питтсбурга» забивали только Кросби и Лемье',
content = 'Всю первую половину 2022 года Евгений Малкин выбивал новый контракт у «Питтсбурга» – и весьма успешно. Четырехлетнее соглашение на 24,4 млн в итоге подписано – и пока нападающий полностью оправдывает его: до матча с «Торонто» он лишь в трех играх регулярки не набирал очков.')

post_2 = Post.objects.create(author_name = Sam_author, types_post = 'AR', header = 'Леброн тратит 1,5 млн в год на тело, чтобы подобраться к вечному рекорду Абдул-Джаббара. А у великого центрового была только йога',
content = 'Невнятный старт «Лейкерс» еще больше убедил в том, что основные приоритеты клуба разнятся с претензиями на что-либо весомое. В отсутствии перспектив командного успеха все сводится к успеху индивидуальному, то есть к единственному вопросу: где и как Леброн Джеймс побьет достижение Карима Абдул-Джаббара, который пока еще остается самым результативным игроком в истории НБА.')

post_3 = Post.objects.create(author_name = Din_author, types_post = 'NE', header='Что стало с немецкими центрфорвардами? В заявку на ЧМ попали лишь двое – с 0 матчей за сборную',
content = 'В заявке Германии на ЧМ-2022 только два профильных центфорварда: Никлас Фюллькруг и Юссуфа Мукоко. У обоих 0 матчей за сборную. Один этот факт подсвечивает нехватку сильных игроков на важную позицию – после ухода Мирослава Клозе только Марио Гомес получал стабильные шансы. Отсутствие нападающих – точно проблема? Почему такое случилось с топ-сборной? Германия пытается выправить ситуацию? ')

#присвоение категориий

PostCategory.objects.create(post_id=1, category_id = 1)
PostCategory.objects.create(post_id=2, category_id = 2)
PostCategory.objects.create(post_id=3, category_id = 3)
PostCategory.objects.create(post_id=3, category_id = 4)



#6. Создать как минимум 4 комментария к разным объектам модели Post (в каждом объекте должен быть как минимум один комментарий)
Comment.objects.create(post_comment_id = 1, user_comment = Sam, text_comment = 'Малкин обрел второе дыхание+')
Comment.objects.create(post_comment_id = 2, user_comment = Sam, text_comment = 'Без денег бы не добился такого -')
Comment.objects.create(post_comment_id = 3, user_comment = Din, text_comment = 'Кай Хавертц затащит сборную +')
Comment.objects.create(post_comment_id = 3, user_comment = Din, text_comment = 'Они все игры проиграют. Фуфло - а не сборная-')


#7. Применяя функции like() и dislike() к статьям/новостям скорректировать рейтинги этих объектов.
Post.like(Post.objects.get(id=1),1)
Post.like(Post.objects.get(id=1),1)

Post.like(Post.objects.get(id=2),1)
Post.like(Post.objects.get(id=2),1)

Post.like(Post.objects.get(id=3),1)
Post.like(Post.objects.get(id=3),1)


Post.dislike(Post.objects.get(id=1),1)

Post.dislike(Post.objects.get(id=2),1)
Post.dislike(Post.objects.get(id=2),1)

#Применяя функции like() и dislike() к комментариям
Comment.like(Comment.objects.get(id=1),1)
Comment.like(Comment.objects.get(id=2),1)
Comment.like(Comment.objects.get(id=3),1)
Comment.like(Comment.objects.get(id=3),1)
Comment.like(Comment.objects.get(id=4),1)

Comment.dislike(Comment.objects.get(id=2),1)



#8.	Обновить рейтинги пользователей.
author1=Author.objects.last()
author1.update_rating()

author2=Author.objects.first()
author2.update_rating()



#9.	Вывести username и рейтинг лучшего пользователя
best_autor = Author.objects.all().order_by('-user_rating')[0]
print("Лучший автор:", best_autor.user_name)
print("Рейтинг автора:", best_autor.user_rating)



#10.	Вывести дату добавления, username автора, рейтинг,
заголовок и превью лучшей статьи, основываясь на лайках/дислайках к этой статье.
best_post=Post.objects.all().order_by('-rating_post')[0]
print("Дата:", best_post.datetime_post)
print("Автор:", best_post.author_name.user_name)
print("Рейтинг:", best_post.rating_post)
print("Заголовок:", best_post.header)
print("Превью:", best_post.preview())

#11.	Вывести все комментарии (дата, пользователь, рейтинг, текст) к этой статье
for comment in Comment.objects.filter(post_comment=best_post):
    print("Дата:", comment.datetime_comment)
    print("Автор:", comment.user_comment)
    print("Рейтинг:", comment.rating_comment)
    print("Комментариии:", comment.text_comment)
