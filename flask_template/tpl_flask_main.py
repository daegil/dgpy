#! /usr/bin/env python
#-*- coding:utf-8 -*-

"""
 AUTHOR     : Daegil Kim 
 CREATED    : 2014/01/28 02:08 

 [DESCRIPTION]
"""

import os
import sys
import logging
from logging.handlers import RotatingFileHandler
from logging import Formatter
from flask import Flask, render_template, url_for

app = Flask(__name__)
app.secret_key = os.urandom(24)

_listen_port = 5000
_flask_debug = True
_flask_threaded = True

_log_file_name = '/tmp/flask_test.log'
_log_level = logging.DEBUG
_log_max_bytes = 100 * 1024 * 1024
_log_backup_count = 10

# alias for Log
log_debug = app.logger.debug
log_info = app.logger.info
log_warning = app.logger.warning
log_error = app.logger.error
log_critical = app.logger.critical

@app.before_request
def before_request():
    pass

@app.teardown_request
def teardown_request(exception):
    pass

@app.route('/')
def main():
    return render_template('main.html')

@app.errorhandler(404)
def page_not_founde(error):
    log_error('page not found')
    return (render_template('page_not_found.html'), 404)


if __name__ == '__main__':
    file_handler = RotatingFileHandler(_log_file_name, maxBytes=_log_max_bytes, backupCount=_log_backup_count)
    file_handler.setLevel(_log_level)
    file_handler.setFormatter(Formatter('%(asctime)s [%(levelname)s] [%(pathname)s:%(lineno)d] %(message)s'))
    app.logger.addHandler(file_handler)

    reload(sys)
    sys.setdefaultencoding('utf-8')

    if len(sys.argv) == 2:
        _listen_port = int(sys.argv[1])

    app.run(host='0.0.0.0', port=_listen_port, debug=_flask_debug, threaded=_flask_threaded)
