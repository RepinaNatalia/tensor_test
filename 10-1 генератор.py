# Напишите генератор generate_random_name(), используя модуль random,
# который генерирует два слова из латинских букв от 1 до 15 символов, разделенных пробелами
# Например при исполнении следующего кода:
# gen = generate_random_name()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
#
# Выводится:
# tahxmckzexgdyt ocapwy
# dxqebbukr jg
# aym jpvezfqexlv
# iuy qnikkgxvxfxtxv
import random
import string
def generate_random_name():
    n1 = random.randint(1, 15)
    word1 = ''.join(random.choices(string.ascii_lowercase, k=n1))
    # print(word1)
    n2 = random.randint(1, 15)
    word2 = ''.join(random.choices(string.ascii_lowercase, k=n2))
    # print(word1)
    gen = word1 + " " + word2
    yield gen 
gen = generate_random_name()
print(next(gen))
