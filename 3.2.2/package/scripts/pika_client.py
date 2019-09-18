# -*- coding: utf-8 -*-

import sys, os, pwd, signal, time
from resource_management import *
from subprocess import call
from pika_sentinel import pika_sentinel

class pika_client(Script):
  def install(self, env):
    # Install packages listed in metainfo.xml
    import params
    self.install_packages(env)
    self.configure(env)
    # Execute(('chmod', '755', '/etc/init.d/pika-cli') , user=params.pika_user ,sudo = True)
    #if any other install steps were needed they can be added here
    
  def configure(self, env):
    import params
    env.set_params(params)
    # pika_sentinel() TODO

  

  #To get status of the, use the linux service status command
  def status(self, env):
    raise ClientComponentHasNoStatus()

if __name__ == "__main__":
    pika_client().execute()
