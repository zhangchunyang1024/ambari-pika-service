#!/usr/bin/env python
"""
Licensed to the Apache Software Foundation (ASF) under one
or more contributor license agreements.  See the NOTICE file
distributed with this work for additional information
regarding copyright ownership.  The ASF licenses this file
to you under the Apache License, Version 2.0 (the
"License"); you may not use this file except in compliance
with the License.  You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE_2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

"""

from resource_management import *
import json

# server configurations
config = Script.get_config()

#conf_dir = "/etc/"
logdir = "/opt/soft/log/pika"
pika_home = "/opt/soft/pika"
conf_dir = "/opt/soft/pika/conf"
pika_user = config['configurations']['pika-env']['pika_user']
pika_group = config['configurations']['pika-env']['pika_group']
pika_slave = False

# pika configuration
port = config['configurations']['pika']['port']
thread_num = config['configurations']['pika']['thread_num']
thread_pool_size = config['configurations']['pika']['thread_pool_size']
sync_thread_num = config['configurations']['pika']['sync_thread_num']
log_path = config['configurations']['pika']['log_path']
logdir = log_path
db_path = config['configurations']['pika']['db_path']
write_buffer_size = config['configurations']['pika']['write_buffer_size']
timeout = config['configurations']['pika']['timeout']
requirepass = config['configurations']['pika']['requirepass']
masterauth = config['configurations']['pika']['masterauth']
userpass = config['configurations']['pika']['userpass']
userblacklist = config['configurations']['pika']['userblacklist']
instance_mode = config['configurations']['pika']['instance_mode']
databases = config['configurations']['pika']['databases']
default_slot_num = config['configurations']['pika']['default_slot_num']
dump_prefix = config['configurations']['pika']['dump_prefix']
daemonize = config['configurations']['pika']['daemonize']
dump_path = config['configurations']['pika']['dump_path']
dump_exipre = config['configurations']['pika']['dump_exipre']
pidfile = config['configurations']['pika']['pidfile']
maxclients = config['configurations']['pika']['maxclients']
target_file_size_base = config['configurations']['pika']['target_file_size_base']
expire_logs_days = config['configurations']['pika']['expire_logs_days']
expire_logs_nums = config['configurations']['pika']['expire_logs_nums']
root_connection_num = config['configurations']['pika']['root_connection_num']
slowlog_log_slower_than = config['configurations']['pika']['slowlog_log_slower_than']
slowlog_max_len = config['configurations']['pika']['slowlog_max_len']

slave_priority = config['configurations']['pika']['slave_priority']
slave_read_only = config['configurations']['pika']['slave_read_only']
db_sync_path = config['configurations']['pika']['db_sync_path']
db_sync_speed = config['configurations']['pika']['db_sync_speed']
network_interface = config['configurations']['pika']['network_interface']
compact_cron = config['configurations']['pika']['compact_cron']
compact_interval = config['configurations']['pika']['compact_interval']
write_binlog = config['configurations']['pika']['write_binlog']
binlog_file_size = config['configurations']['pika']['binlog_file_size']
compression = config['configurations']['pika']['compression']
mall_compaction_threshold = config['configurations']['pika']['mall_compaction_threshold']
max_write_buffer_size = config['configurations']['pika']['max_write_buffer_size']
max_background_flushes = config['configurations']['pika']['max_background_flushes']
max_background_compactions = config['configurations']['pika']['max_background_compactions']
max_cache_files = config['configurations']['pika']['max_cache_files']
max_bytes_for_level_multiplier = config['configurations']['pika']['max_bytes_for_level_multiplier']

master_ip = config['configurations']['pika']['master_ip']

# Sentinel configuration


sentinel_port = config['configurations']['pika-sentinel']['sentinel_port']
sentinel_logfile = config['configurations']['pika-sentinel']['sentinel_logfile']
quorum = config['configurations']['pika-sentinel']['quorum']
master_name = config['configurations']['pika-sentinel']['master_name']
blacklist_threshold = config['configurations']['pika-sentinel']['blacklist_threshold']
numslaves = config['configurations']['pika-sentinel']['numslaves']
sentinel_pidfile = "/opt/soft/run/pika/sentinel.pid"

if 'ganglia_server_host' in config['clusterHostInfo'] and \
        len(config['clusterHostInfo']['ganglia_server_host'])>0:
  ganglia_installed = True
  ganglia_server = config['clusterHostInfo']['ganglia_server_host'][0]
  ganglia_report_interval = 60
else:
  ganglia_installed = False
