#!/usr/bin/python
#-*-coding: utf-8 -*-

from pylexto import LexTo


lexto = LexTo()
#text = u"อยากรู้เรื่องยาคูลท์ ถามสาวยาคูลท์สิคะ"
text = u"แมวกินปลาแมวมันชอบนอนนอนกลางวันนอนแล้วนอนอีกเป็นสัตว์ที่ขี้เกียจจริงๆเลยแมวแต่แมวมันเข้ากับคนได้ดีฉันชอบแมว"
words, types = lexto.tokenize(text)

print('|'.join(words))
print(types)
'''
for n in types:
    print(n.value,type(n.value))'''