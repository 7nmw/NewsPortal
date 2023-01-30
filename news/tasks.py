from celery import shared_task
from django.core.mail import send_mail, EmailMultiAlternatives
from django.core.mail import EmailMessage, EmailMultiAlternatives
from .models import Post, Category
from django.template.loader import render_to_string, get_template
from datetime import datetime, timedelta

#Реализовать рассылку уведомлений подписчикам после создания новости.

@shared_task
def send_news_after_post(post_id):
    post = Post.objects.get(pk=post_id)
    recipient_list = []
    for category in post.category_post.all():
        for subscriber in category.subscribers.all():
            recipient_list.append(subscriber.email)
            recipient_list = list(set(recipient_list))
    html_content = render_to_string('mail_subscribers.html', {'post': post})
    msg = EmailMultiAlternatives(
        subject=f'{post.header}',
        from_email='win.c4ester@yandex.ru',
        to=recipient_list
    )
    msg.attach_alternative(html_content, 'text/html')
    msg.send()


#Реализовать еженедельную рассылку с последними новостями (каждый понедельник в 8:00 утра).
@shared_task
def send_week_news_at8am():
    context = {}
    recipient_list = []
    for category in Category.objects.all():
        context['posts'] = category.post_set.filter(datetime_post__gte=datetime.utcnow() - timedelta(hours=10))
#        print(category)
        for subscriber in category.subscribers.all():
#            print(subscriber)
            recipient_list.append(subscriber.email)
            recipient_list = list(set(recipient_list))
            message = get_template('week_mail_subscribers.html').render(context | {'user': subscriber})
            msg = EmailMessage('Новости за неделю', message, 'win.c4ester@yandex.ru', recipient_list)
            msg.content_subtype = 'html'
            msg.send()
            
