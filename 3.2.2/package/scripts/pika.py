#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Licensed to the Apache Software Foundation (ASF) under one
or more contributor license agreements.  See the NOTICE file
distributed with this work for additional information
regarding copyright ownership.  The ASF licenses this file
to you under the Apache License, Version 2.0 (the
"License"); you may not use this file except in compliance
with the License.  You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

"""

from resource_management import *
#from yaml_config import yaml_config
import sys


def pika():
    import params

    Directory( params.db_path,
           mode=0755,
           owner = params.pika_user,
           group = params.pika_group,
           create_parents = True
    )

    Directory( params.db_sync_path,
           mode=0755,
           owner = params.pika_user,
           group = params.pika_group,
           create_parents = True
    )

    Directory( params.logdir,
        mode=0755,
        owner = params.pika_user,
        group = params.pika_group,
        create_parents = True
    )

    File(format("{conf_dir}/pika.conf"),
        content=Template("pika.conf.j2"),
        owner=params.pika_user,
        group=params.pika_group
    )


    Directory("/opt/soft/run/pika",
        mode=0755,
        owner = params.pika_user,
        group = params.pika_group,
        create_parents = True
    )

    File(format("/etc/init.d/pika"),
         content=Template("pika.j2"),
         owner=params.pika_user,
         group=params.pika_group
    )
