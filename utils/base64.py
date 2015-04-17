#! /bin/env python
#-*- coding:utf-8 -*-

import base64

if __name__ == '__main__':
    print 'usage>\n  enc {str}\n  dec {str}\n  quit\n'
    while 1:
        cmd=raw_input('))) ')
        try:
            if len(cmd) == 0: continue
            c = cmd.split()[0]
            plist = cmd.split()[1:]
            if c == 'enc':
                rst = base64.b64encode(plist[0])
                print repr(rst)
                print 'length : %d' % (len(rst),)
            elif c == 'dec':
                rst = base64.b64decode(plist[0])
                print repr(rst)
                print 'length : %d' % (len(rst),)
            elif c == 'quit':
                break;
        except Exception as e:
            print e.args
            continue