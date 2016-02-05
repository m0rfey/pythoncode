__author__ = 'm0rfey'
# -*- coding: utf-8 -*-
import os
import sys

class enigma:

    print(u'Виберіть варінт 1 або 2', '\n', u'1 - Кодувати', '\n',u'2 - Декодувати')
    number = input('Варіант: ')
    #name file open
    num = 2 #nput('Номер файла: ')
    strok = 'xxx-'

    def __init__(self, symbol, sp, file):
        symbol = (u'а', u'б', u'в', u'г', u'д', u'е', u'є', u'ж', u'з', u'и', u'і', u'ї', u'й', u'к', u'л', u'м',
                  u'н', u'о', u'п', u'р', u'с', u'т', u'у', u'ф', u'х', u'ц', u'ч', u'ш', u'щ', u'ь', u'ю',
                  u'я', u' ', u',', u'.', u'!', u'?', u'\n')

        sp = []
        file = open(enigma.strok+str(enigma.num)+'.txt')
        self.symbol = symbol
        self.sp = sp
        self.file = file

    #encrypt

    def encrypt(self):

        if os.stat(enigma.strok+str(enigma.num)+'.txt').st_size == 0: #
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
                        print(u'УВАГА.Робота програми перервана!')
                        break
                    else:
                        self.sp.append(s)
                        print(self.sp)

                    ffile = open(enigma.strok+str(enigma.num)+'.txt', 'w')
                    for ix in self.sp:
                        ffile.write("%s\n" % ix)
                    ffile.close()
            return enigma.encrypt(self)     #

        else:
            print(u'\nФайл шифрування існує \n')
            self.spp = []
            for ex in self.file.readlines():
                self.spp.append(ex)

        txt = input(u'Введіть текст: \n')
        k = []
        for i in txt.lower():
            for z in range(0, len(self.symbol)):
                for l in self.symbol[z]:
                    if i == l:
                        k.append(self.spp[z])

        str_f = ''.join(k).split()
        print(''.join(str_f))

    #decrypt

    def decrypt(self):
        print(u'\nДекодування\n')

        self.txt_dec = input(u'Введіть текст для декодування:\n')

        if not self.txt_dec:
            print('Error')
            return enigma.decrypt(self.txt_dec)
        else:
           enigma.blo(self)

    def blo(self):
        n = 2 #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        dec = []
        file_open = open(enigma.strok+str(enigma.num)+'.txt')
        for j in file_open.readlines():
            dec.append(j)
            self.de = ''.join(dec).split()#створюємо список з файлу

        t = []

        for i in [self.txt_dec.lower()[i:i+n] for i in range(0, len(self.txt_dec), n)]:#розбиваємо введений текст по n символів
            for z in range(len(self.symbol)):#генеруємо множину з списку символів
                for l in self.de[z:z+1]:#
                    if i == l:
                        t.append(self.symbol[z])

        print('','\n',''.join(t))



    def tobeornottobe(self):
        if enigma.number =='1':
            enigma(symbol='', sp='', file='').encrypt()
        elif enigma.number =='2':
            enigma(symbol='', sp='', file='').decrypt()

enigma(symbol='', sp='', file='').tobeornottobe()
