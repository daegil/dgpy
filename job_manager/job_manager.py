#! /usr/bin/env python
#-*- coding:utf-8 -*-

"""
 AUTHOR     : Daegil Kim 
 CREATED    : 2014/03/16 21:14

 [DESCRIPTION]
"""

import os
from optparse import OptionParser
from threading import Thread
import subprocess
import select
import time

class JobThread(Thread):
    def __init__(self, job_name, job_info):
        Thread.__init__(self)
        self.stop_received = False
        self.job_name = job_name
        self.job_info = job_info
        self.prev_time = int(time.time())
        self.job_cnt = 0

    def do_job(self):
        text = ''
        p = subprocess.Popen(self.job_info['cmd'], shell=True, stdout=subprocess.PIPE)
        r, w, x = select.select([p.stdout.fileno()], [], [], self.job_info['timeout'])
        if r:
            text = p.stdout.read()
        else:
            os.system('kill -9 %d' % (p.pid))
            text = 'JOB TIMEOUT[%d sec]' % (self.job_info['timeout'])
        text = text.strip()
        return text

    def run(self):
        while not self.stop_received:
            if self.job_info['type'] == 'duration':
                ctime = int(time.time())
                ttime = self.prev_time + int(self.job_info['at'])
                if ctime == ttime:
                    text = self.do_job()
                    self.job_cnt += 1
                    if len(text):
                        print text
                    if self.job_info['iteration'] != 'infinite' and self.job_cnt >= int(self.job_info['iteration']):
                        break
                    self.prev_time = int(time.time())
            time.sleep(0.5)


class JobManager():
    def __init__(self, conf_file, log_file):
        self.conf_file = conf_file
        self.log_file = log_file
        self.conf = None
        self.thread_list = []

    def start(self):
        mn = self.conf_file.split('.py')[0]
        self.conf = __import__(mn)
        self.createThread()
        self.joinThread()

    def createThread(self):
        for job in self.conf.job_info:
            print 'JOB[%s] LOAD' % (job)
            th = JobThread(job, self.conf.job_info[job])
            self.thread_list.append(th)
            th.start()

    def joinThread(self):
        while len(self.thread_list) > 0:
            try:
                for th in self.thread_list:
                    th.join(1)
                    if not th.isAlive():
                        self.thread_list.remove(th)
            except KeyboardInterrupt:
                for th in self.thread_list:
                    th.stop_received = True


if __name__ == '__main__':
    usage_str = '%prog -c {CONF_FILE} -l {LOG_FILE} (See More : %prog -h)'
    parser = OptionParser(usage=usage_str)
    parser.add_option('-c', '--conf', dest='conf_file', default='',  help='Describe a configuration file for Job Manager.\n')
    parser.add_option('-l', '--logfile', dest="log_file", default="/dev/null", help="Describe a log file for Job Manager.\n")
    (options, args) = parser.parse_args()
    if options.conf_file == '':
        parser.error('No Configuration File')
    if options.log_file[0] == '/':
        log_file = options.log_file
    else:
        log_file = os.getcwd() + "/" + options.log_file
    jm = JobManager(options.conf_file, log_file)
    jm.start()
