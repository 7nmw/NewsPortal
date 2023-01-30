from django import template

register = template.Library()


@register.filter(name='censors')
def censor(value):
   """
   value: header
   """

   stopwords = ['урод', 'бяка', 'гопник']
   word = value.replace(',', "")
   word = word.replace('-', "")
   word = word.split()
   if type(value) is str:
      for word in stopwords:
         value = value.replace(word, word[0] + "*" * (len(word) - 1))
         value = value.replace(word.capitalize(), word[0] + "*" * (len(word) - 1))
   else:
      raise ValueError('Ошибка, это не переменная строкого типа')

   return f'{value}'