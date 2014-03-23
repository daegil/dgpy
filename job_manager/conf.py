job_info = {}

# type : daily/weekly/monthly/duration
# at :
#  - daily type, ex) '13:15:00'
#  - weekly type, ex) 'SUNDAY 13:15:00'
#  - monthly type, ex) '3 13:15:00'
#  - duration type, ex) '60'

#job_info['JOB_TEST_1'] = {
#    'cmd' : 'echo "job_test_1"',
#    'type' : 'daily',
#    'at' : '18:08:00',
#    'timeout' : 300
#}

#job_info['JOB_TEST_2'] = {
#    'cmd' : 'echo "job_test_2"',
#    'type' : 'weekly',
#    'at' : 'MONDAY 18:08:00',
#    'timeout' : 300
#}

#job_info['JOB_TEST_3'] = {
#    'cmd' : 'echo "job_test_3"',
#    'type' : 'monthly',
#    'at' : '3 18:08:00',
#    'timeout' : 300
#}

job_info['JOB_TEST_4'] = {
    'cmd' : 'touch /tmp/job_test_4.tmp',
    'type' : 'duration',
    'at' : 1,
    'iteration' : 'infinite',
    'timeout' : 5
}
