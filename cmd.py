#! /usr/bin/env python
#-*- coding:utf-8 -*-
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

"""
 AUTHOR     : Daegil Kim 
 CREATED    : 2014/01/31 02:03 

 [DESCRIPTION]
"""

import os

_dgpy_home = ''

def main():
    global _dgpy_home
    tmp = os.getenv('DGPY_HOME')
    if tmp:
        _dgpy_home = tmp
    else:
        _dgpy_home = os.popen('pwd').read()
    while 1:
        cmd = raw_input('DGPY CMD >>> ')
        if cmd in ('help', '?', 'h'):
            do_help()
            continue
        elif cmd in ('quit', 'q', 'exit'):
            break
        elif cmd in ('tplcp',):
            do_tplcp()
            continue
        elif len(cmd) == 0:
            continue
        else:
            print_error('Unknown Command!')
    return

def do_help():
    print '''
Command List)
 - help, ?, h
 - quit, q, exit
 - tplcp
'''

def print_error(msg):
    print '\n%s\n' % (msg,)

def do_tplcp():
    t = raw_input(' Template Type [0:basic][1:class]? ')
    if t not in ('0', '1'):
        print_error('Unknown Type!')
        return
    fn = raw_input(' Target File Name? ')
    if fn[-3:] != '.py':
        fn += '.py'
    if t == '0':
        if fn == 'tpl_basic.py':
            print_error('Filename Error!')
            return
        os.system('cp %s/tpl_basic.py %s' % (_dgpy_home, fn,))
    elif t == '1':
        if fn == 'tpl_class.py':
            print_error('Filename Error!')
            return
        os.system('cp %s/tpl_class.py %s' % (_dgpy_home, fn,))

if __name__ == '__main__':
    main()
