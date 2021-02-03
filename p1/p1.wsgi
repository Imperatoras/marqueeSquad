#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/marqueeSquad/p1/")

from app import app as application
application.secret_key = 'Add your secret key'