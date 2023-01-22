from django import template

register = template.Library()


#CENSOR_SYMBOLS = [
#   'нападающих',
#   'отсутствии',
#   'оправдывает',
#   'заявку',
#]

#text = 'Всю первую половину 2022 года'
#word = header.split()
#stopwords = ['нападающих', 'отсутствии', 'оправдывает', 'заявку']

@register.filter(name='censors')
def censor(value):
   """
   value: header
   """

   stopwords = ['стало', 'истории', 'заявку', 'заявке', 'первую', 'стабильные', 'старт', 'чтобы', 'бяка']
   word = value.replace(',', "")
   word = word.replace('-', "")
   word = word.split()
#   word = value.lower()
   if type(value) is str:
      for word in stopwords:
         value = value.replace(word, word[0] + "*" * (len(word) - 1))
         value = value.replace(word.capitalize(), word[0] + "*" * (len(word) - 1))
   else:
      raise ValueError('Ошибка, это не переменная строкого типа')

   return f'{value}'