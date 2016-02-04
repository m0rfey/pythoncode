__author__ = 'm0rfey'
# -*- coding: utf-8 -*-
import os

symbol = (u'а', u'б', u'в', u'г', u'д', u'е', u'є', u'ж', u'з', u'и', u'і', u'ї', u'й', u'к', u'л', u'м',
          u'н', u'о', u'п', u'р', u'с', u'т', u'у', u'ф', u'х', u'ц', u'ч', u'ш', u'щ', u'ь', u'ю',
          u'я', u' ', u',', u'.', u'!', u'?')

ks = 0

sp = []
f = open('xxx.txt')

if os.stat("xxx.txt").st_size == 0: 
    for iz in symbol:
        print(iz,':')
        s = input(u' ')
        try:
            if not s:
                print(u'Не коректно! Поля не повинні бути пустими')
                break
            else:
                sp.append(s)
                print(sp)
        except (ValueError, TypeError):
            print(u'-')

    f = open('xxx.txt', 'w')
    for ix in sp:
        f.write("%s\n" % ix)
    f.close()

else:
    global spp
    spp = []
    for ex in f.readlines():
        spp.append(ex)
        #print(spp)


txt = input(u'Введіть текст: \n')
k = []
for i in txt.lower():
    for z in range(0, len(symbol)):
        for l in symbol[z]:
            if i == l:
                k.append(spp[z])
                #print(spp[z])

                #print(spp, '=====')

str_f = ''.join(k).split()
print(''.join(str_f))




