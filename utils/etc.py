#! /usr/bin/env python
#-*- coding:utf-8 -*-
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

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

if __name__ == '__main__':
    dt = datetime.now()
    ts = datetime_to_timestamp(dt)
    print ts, timestamp_to_datetime(ts)
