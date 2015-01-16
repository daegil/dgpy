#! /bin/env python
#-*- coding:utf-8 -*-

import os
import filecmp


target_dir_a = '/Users/darren/pkg'
target_dir_b = '/Users/darren/pkg_test'
#target_dir_a = '/home/deploy/workspace/pj'
#target_dir_b = '/home/deploy/pkg/pjproject-1.14.2'

crcf_ignore = False
skip_words = ['.svn', '.o', 'tests', 'depend', '.a']


if __name__ == '__main__':
    target_dir_a_list = {}
    target_dir_b_list = {}
    if target_dir_a[len(target_dir_a)-1] == '/':
        target_dir_a = target_dir_a[0:len(target_dir_a)-1]
    if target_dir_b[len(target_dir_b)-1] == '/':
        target_dir_b = target_dir_b[0:len(target_dir_b)-1]
    for (dirpath, dirnames, filenames) in os.walk(target_dir_a):
        #print (dirpath, dirnames, filenames)
        skip_flag = False
        for ele in skip_words:
            if dirpath.find(ele) != -1:
                skip_flag = True
        if skip_flag:
            continue
        if len(filenames) > 0:
            for fn in filenames:
                skip_flag = False
                for ele in skip_words:
                    if fn.find(ele) != -1:
                        skip_flag = True
                if not skip_flag:
                    target_dir_a_list[dirpath.split(target_dir_a)[1]+'/'+fn] = 'file'
        elif len(dirnames) == 0 and len(filenames) == 0:
            #print (dirpath, dirnames, filenames)
            target_dir_a_list[dirpath.split(target_dir_a)[1]+'/'] = 'directory'
    for (dirpath, dirnames, filenames) in os.walk(target_dir_b):
        #print (dirpath, dirnames, filenames)
        skip_flag = False
        for ele in skip_words:
            if dirpath.find(ele) != -1:
                skip_flag = True
        if skip_flag: continue
        if len(filenames) > 0:
            for fn in filenames:
                for ele in skip_words:
                    if fn.find(ele) != -1:
                        skip_flag = True
                if skip_flag: continue
                target_dir_b_list[dirpath.split(target_dir_b)[1]+'/'+fn] = 'file'
        elif len(dirnames) == 0 and len(filenames) == 0:
            #print (dirpath, dirnames, filenames)
            target_dir_b_list[dirpath.split(target_dir_b)[1]+'/'] = 'directory'

    result = {}
    print 'Compare [{0}] with [{1}]'.format(target_dir_a, target_dir_b)
    for k in target_dir_a_list:
        if not target_dir_b_list.has_key(k):
            if target_dir_a_list[k] == 'directory':
                result[target_dir_a+k] = ['OX DIRECTORY']
            else:
                result[target_dir_a+k] = ['OX']
            continue
        if target_dir_a_list[k] == 'directory':
            continue
        target_a_crlf_term_file = False
        target_b_crlf_term_file = False
        if crcf_ignore:
            target_a_crlf_term_file = True
            os.system('tr -d "\15\32" < %s > crlf_target_a.tmp' % (target_dir_a+k,))
            target_b_crlf_term_file = True
            os.system('tr -d "\15\32" < %s > crlf_target_b.tmp' % (target_dir_b+k,))
        if target_a_crlf_term_file:
            target_a_fn = 'crlf_target_a.tmp'
        else:
            target_a_fn = target_dir_a+k
        if target_b_crlf_term_file:
            target_b_fn = 'crlf_target_b.tmp'
        else:
            target_b_fn = target_dir_b+k
        rst = filecmp.cmp(target_a_fn, target_b_fn)
        if rst:
            result[target_dir_a+k] = ['==']
        else:
            result[target_dir_a+k] = ['!=', 'vimdiff {0}{1} {2}{3}'.format(target_dir_a, k, target_dir_b, k)]
    for k in target_dir_b_list:
        if not target_dir_a_list.has_key(k):
            if target_dir_b_list[k] == 'directory':
                result[target_dir_a+k] = ['XO DIRECTORY']
            else:
                result[target_dir_a+k] = ['XO']
            continue

    vimdiff_str_list = []
    diff_file_cnt = 0
    same_file_cnt = 0
    right_only_empty_dir_cnt = 0
    right_only_file_cnt = 0
    left_only_empty_dir_cnt = 0
    left_only_file_cnt = 0
    print '\n[DIFF RESULT]'
    print '{FILE} {RESULT SIGN}'
    key_sorted = list(result)
    key_sorted.sort()
    for k in key_sorted:
        if result[k][0] == '!=':
            print k, result[k][0]
            vimdiff_str_list.append(result[k][1])
            diff_file_cnt += 1
        elif result[k][0] == '==':
            same_file_cnt += 1
        elif result[k][0].find('OX') != -1:
            print k, result[k][0]
            if result[k][0].find('DIRECTORY') != -1:
                left_only_empty_dir_cnt += 1
            else:
                left_only_file_cnt += 1
        elif result[k][0].find('XO') != -1:
            print k, result[k][0]
            if result[k][0].find('DIRECTORY') != -1:
                right_only_empty_dir_cnt += 1
            else:
                right_only_file_cnt += 1
        else:
            print k, result[k][0]
            raise StandardError
    print '\nsame file : ' + str(same_file_cnt)
    print 'not same file : ' + str(diff_file_cnt)
    print 'left only file : ' + str(left_only_file_cnt)
    print 'left only empty directory : ' + str(left_only_empty_dir_cnt)
    print 'right only file : ' + str(right_only_file_cnt)
    print 'right only empty directory : ' + str(right_only_empty_dir_cnt)
    print '\n* vimdiff string list'
    for ele in vimdiff_str_list:
        print ele
    answer = raw_input('Would you run "vimdiff string list"? [y/n]')
    if answer.lower() == 'y':
        for cmd in vimdiff_str_list:
            os.system(cmd)
