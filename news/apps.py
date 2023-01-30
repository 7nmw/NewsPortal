from django.apps import AppConfig


class NewsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'news'

    def ready(self):
        import news.signals
'''
    def ready(self):asdfasfq2f
        import news.runapscheduler
'''