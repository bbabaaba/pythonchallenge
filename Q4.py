# coding=utf-8

from requests import get

first_url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345'
next_url = None
url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
last_url = 'http://www.pythonchallenge.com/pc/def/'
old_id = 16044
src = get(first_url).text
nextid = src.split(' ')[-1]
# '''
while True:
    try:
        nextid = int(nextid)
    except:
        if 'Divide by two' in src:
            nextid = old_id/2
        else:
            next_url = last_url + str(nextid)
            print next_url
            break
    old_id = nextid
    next_url = url + str(nextid)
    src = get(next_url).text
    nextid = src.split(' ')[-1]
    # print nextid
# '''
# ans is: http://www.pythonchallenge.com/pc/def/peak.html


