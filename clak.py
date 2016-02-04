__author__ = 'm0rfey'
# -*- coding: utf-8 -*-

class Enigma:
    txt = input('Enter teext: ')
    symbol = (u'а', u'б', u'в', u'г', u'д', u'е', u'є', u'ж', u'з', u'и', u'і', u'ї', u'й', u'к', u'л', u'м',
          u'н', u'о', u'п', u'р', u'с', u'т', u'у', u'ф', u'х', u'ц', u'ч', u'ш', u'щ', u'ь', u'ю',
          u'я', u' ', u',', u'.', u'!', u'?')
    def __init__(self, txt, symbol):
        self.txt = txt
        self.symbol = symbol

    def load(self):
        open_file = open('xxx.txt', 'w')
        self.open_file = open_file

    def coding(self):
        for i in self.txt:
            for k in self.symbol:
                if i == k:
                   print(i, k)
                else:
                    print(None)

    print(txt)

