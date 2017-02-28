# coding=utf-8

from urllib import *

page_source = urlopen('http://www.pythonchallenge.com/pc/def/ocr.html')

for i in range(37):
    page_source.readline()
chars = []
src_left = page_source.read()
for i in src_left:
    if i.isalpha():
        chars.append(i)
print ''.join(chars)
page_source.close()

