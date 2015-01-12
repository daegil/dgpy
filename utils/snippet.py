#! /usr/bin/env python
#-*- coding:utf-8 -*-

from pprint import pprint

# sorting by dictionary's value
from operator import itemgetter

d = {'a':100, 'b':1, 'c':30}
r = sorted(d.items(), key=itemgetter(1))
#pprint(r)
r = sorted(d.items(), key=itemgetter(1), reverse=True)
#pprint(r)


