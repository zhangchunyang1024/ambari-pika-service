# -*- coding: utf-8 -*-

import sys, os, pwd, signal, time
from resource_management import *
from subprocess import call
from pika import pika

class pika_service(Script):
  def install(self, env):
    # Install packages listed in metainfo.xml
    import params
    self.install_packages(env)
    Execute(('chmod', '-R' , '755', '/opt/soft/pika') , user=params.pika_user ,sudo = True)
    Execute(('chmod', '755', '/etc/init.d/pika') , user=params.pika_user ,sudo = True)
    #if any other install steps were needed they can be added here
  
  def configure(self, env):
    import params
    env.set_params(params)
    pika()

  #To stop the service, use the linux service stop command and pipe output to log file
  def stop(self, env):
    import params
    env.set_params(params)
    stop_cmd = format("service pika stop")
    Execute(stop_cmd , user=params.pika_user)

  #To start the service, use the linux service start command and pipe output to log file
  def start(self, env):
    import params
    env.set_params(params)
    self.configure(env)
    start_cmd = format("service pika start")
    Execute(start_cmd, user=params.pika_user)

  #To get status of the, use the linux service status command
  def status(self, env):
    import status_params
    env.set_params(status_params)
    check_process_status(status_params.pika_pid_file)
    
if __name__ == "__main__":
    pika_service().execute()
