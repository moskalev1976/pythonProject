def int_func(txt):
    word = txt[0] .upper() + txt[1:].lower()
    return word

string = input('Введите список слов через пробел: ')
for word in string.split(' '):
    print(f'{int_func(word)} ', end=' ')
