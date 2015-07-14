#! /usr/bin/env python
#-*- coding:utf-8 -*-

"""
 AUTHOR     : Daegil Kim 
 CREATED    : 2014/05/22 11:31

 [DESCRIPTION]
"""

from datetime import datetime
import time

def timestamp_to_datetime(ts):
    return datetime(*time.localtime(ts)[:6])

def datetime_to_timestamp(dt):
    return int(time.mktime(dt.timetuple()))

# func. for 'Decode early' (ref : http://farmdev.com/talks/unicode/)
def to_unicode_or_bust(obj, encoding='utf-8'):
    if isinstance(obj, basestring):
        if not isinstance(obj, unicode):
            obj = unicode(obj, encoding)
    return obj

def enum(*sequential, **named):
    enums = dict(zip(sequential, range(len(sequential))), **named)
    reverse = dict((value, key) for key, value in enums.iteritems())
    enums['reverse_mapping'] = reverse
    return type('Enum', (), enums)

if __name__ == '__main__':
    dt = datetime.now()
    ts = datetime_to_timestamp(dt)
    print ts, timestamp_to_datetime(1433755745)
    obj = to_unicode_or_bust('가나다')
    print obj
    print type(obj)
    num = enum('zero', 'one', 'two')
    print num.zero
    print num.reverse_mapping[0]
