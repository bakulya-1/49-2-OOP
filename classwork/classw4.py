#Тема №4. Закрепление пройденного материала - Использование ООП в проекте
""" Модуль, пакеты - библиотека. Декораторы."""

# import lessons.lesson4  as mymodule
# from lessons import lesson4 as mymodule

# import random
# import math
# from json import JSONDecodeError

# mymodule.greet('Kirtito')
# print(mymodule.TEST)

#def greet(name):
#    return print(f'Привет, {name}!')

#TEST = "123"


"""""
Модуль и Пакеты
Встроенные модули и библиотеки
Внешние пакеты, модули и библиотеки
"""""

from colorama import init, Fore, Style

init()

print(Fore.BLUE + "Hello, World!")
print(Style.BRIGHT + "Hello, World!")
print(Style.RESET_ALL)

#from colorama import init, Fore, Style

#init()

#print(Fore.RED + "This text is red!")
#print(Fore.GREEN + "This text is green!")

#from requests import get, post, put, delete


from requests import  get, post, put, delete