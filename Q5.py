# coding=utf-8

from requests import *
import pickle

src = get('http://www.pythonchallenge.com/pc/def/banner.p').text
res = pickle.loads(src)
print res
for line in res:
    print ''.join(map(lambda pair: pair[0]*pair[1], line))

# ans is: channel
