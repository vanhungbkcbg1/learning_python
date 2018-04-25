# -*- coding: utf-8 -*-
import codecs

file=codecs.open('unicode.txt','w','sjis')

file.write(u'先に表示するテーブルを指定して下さい。')

file.close()