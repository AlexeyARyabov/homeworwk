def int_func(text):
    counter = 0
    for letter in text:
        if 96 < ord(letter) < 123:
            counter += 1
    if counter == len(text):
        return text[0].upper() + text[1:]
    else:
        return 'не все символы являются маленькими латинскими буквами'


print(int_func(input('введите слово ')))
