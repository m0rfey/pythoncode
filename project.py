__author__ = 'm0rfey'
# -*- coding: utf-8 -*-
import os

symbol = (u'а', u'б', u'в', u'г', u'д', u'е', u'є', u'ж', u'з', u'и', u'і', u'ї', u'й', u'к', u'л', u'м',
          u'н', u'о', u'п', u'р', u'с', u'т', u'у', u'ф', u'х', u'ц', u'ч', u'ш', u'щ', u'ь', u'ю',
          u'я', u' ', u',', u'.', u'!', u'?', u'\n')

ks = 0

sp = []
f = open('xxx_.txt')

print('Виберіть варінт 1 або 2', '\n', u'1 - Кодувати', '\n',u'2 - Декодувати')
number = input('Варіант: ')

#encrypt
if number == '1':
    if os.stat("xxx_.txt").st_size == 0:
        for iz in symbol:
            print(iz,':')
            s = input(u' ')

            if not s:
                print(u'Не коректно! Поля не повинні бути пустими')
                s = input(u' ')
                break
            else:
                sp.append(s)
                print(sp)

        ff = open('xxx_.txt', 'w')
        for ix in sp:
            ff.write("%s\n" % ix)
        ff.close()

    else:
        global spp
        spp = []
        for ex in f.readlines():
            spp.append(ex)

    txt = input(u'Введіть текст: \n').
    k = []
    for i in txt.lower():
        for z in range(0, len(symbol)):
            for l in symbol[z]:
                if i == l:
                    k.append(spp[z])

    str_f = ''.join(k).split()
    print(''.join(str_f))

#decrypt
elif number == '2':

    print(u'Декодування')

    txt_dec = input(u'Введіть текст для декодування:\n')

    if not txt_dec:
        print('Error')
    else:
        print('Continue...')





