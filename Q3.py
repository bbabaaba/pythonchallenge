# coding = utf-8

from urllib import *
import re


page_source = urlopen('http://www.pythonchallenge.com/pc/def/equality.html')
for i in range(21):
    page_source.readline()
new_page_source = page_source.read()
pattern = re.compile(r'[^A-Z][A-Z]{3}[a-z][A-Z]{3}[^A-Z]')
result = re.findall(pattern, new_page_source)
ans_list = []
for em in result:
    ans_list.append(em[4])
page_source.close()
ans = ''.join(ans_list)
print ans
# ans is: linkedlist


