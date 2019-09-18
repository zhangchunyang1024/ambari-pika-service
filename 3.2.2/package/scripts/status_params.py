#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Redis service params

"""

from resource_management import *

config = Script.get_config()

pika_pid_file = format("/opt/soft/run/pika/pika.pid")
sentinel_pid_file = format("/opt/soft/run/pika/sentinel.pid")