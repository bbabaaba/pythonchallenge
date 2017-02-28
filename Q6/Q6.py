# coding=utf-8

# get channel.zip
#'''
from zipfile import *

zfile = ZipFile('/Users/nali/Code/pythonchallenge/Q6/channel.zip', mode='r')
zfile_comments = []
name = '90052.txt'
while True:
    with open(name) as fp:
        number = fp.read().split(' ')[-1]
        # print number
    comment = zfile.getinfo(name).comment
    zfile_comments.append(comment)
    if number.isdigit():
        name = number + '.txt'
    else:
        break
print ''.join(zfile_comments)
'''
from zipfile import *


zfile = ZipFile('/Users/nali/Code/pythonchallenge/Q6/channel.zip', mode='r')
name = '90052.txt'

while True:
    with open(name) as fp:
        words = fp.read()
        number = words.split(' ')[-1]
        # print number
    if number.isdigit():
        name = number + '.txt'
    else:
        print words
        break

'''
# ans is oxygen
