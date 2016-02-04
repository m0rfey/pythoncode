__author__ = 'm0rfey'
# -*- coding: utf-8 -*-
import os

class enigma:

    print('Виберіть варінт 1 або 2', '\n', u'1 - Кодувати', '\n',u'2 - Декодувати')
    number = input('Варіант: ')

    def __init__(self, symbol, sp, file):
        symbol = (u'а', u'б', u'в', u'г', u'д', u'е', u'є', u'ж', u'з', u'и', u'і', u'ї', u'й', u'к', u'л', u'м',
                  u'н', u'о', u'п', u'р', u'с', u'т', u'у', u'ф', u'х', u'ц', u'ч', u'ш', u'щ', u'ь', u'ю',
                  u'я', u' ', u',', u'.', u'!', u'?', u'\n')

        sp = []
        file = open('xxx.txt')
        self.symbol = symbol
        self.sp = sp
        self.file = file

    #encrypt

    def encrypt(self):

        if os.stat("xxx.txt").st_size == 0: #
            for iz in self.symbol:
                self.iz = iz
                print(u'Для виходу введіть exit\n' ,iz,':')
                s = input(u' ')
                self.s = s
                if not self.s:
                    print(u'Не коректно! Поля не повинні бути пустими')
                    return enigma.encrypt(self)
                else:
                    if s == 'exit':
                        break
                    else:
                        self.sp.append(s)
                        print(self.sp)

            ffile = open('xxx.txt', 'w')
            for ix in self.sp:
                ffile.write("%s\n" % ix)
            ffile.close()

        else:
            print(u'\nФайл шифрування існує \n')
            global spp
            spp = []
            for ex in self.file.readlines():
                spp.append(ex)

        txt = input(u'Введіть текст: \n')
        k = []
        for i in txt.lower():
            for z in range(0, len(self.symbol)):
                for l in self.symbol[z]:
                    if i == l:
                            k.append(spp[z])

            str_f = ''.join(k).split()
            print(''.join(str_f))

    #decrypt
    def decrypt(self):
        print(u'Декодування')

        txt_dec = input(u'Введіть текст для декодування:\n')

        if not txt_dec:
            print('Error')
        else:
            print('Continue...')

    def pool(self):
        if enigma.number =='1':
            enigma(symbol='', sp='', file='').encrypt()
        elif enigma.number =='2':
            enigma(symbol='', sp='', file='').decrypt()

enigma(symbol='', sp='', file='').pool()
