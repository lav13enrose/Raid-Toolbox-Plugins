# Plugin Author: lav13enrose
# Plugin Name: Random Pick Line from File
# Date: 69/69/2069

import subprocess
import time
import sys
import os

pyprefix = sys.argv[1]
SERVER = input("Server ID: ")
chan = input("Channel ID: ")
fileinput = input("File For Spammed: ")
tokenlist = open("tokens.txt").read().splitlines()
for token in tokenlist:
    p = subprocess.Popen([pyprefix,'plugins/Spam From Text/spamfromtext.py',token,SERVER,chan,fileinput],stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT)
    time.sleep(0.1)
    with open('pluginpids', 'a+') as handle:
        handle.write(str(p.pid)+'\n')
input("Press enter to return to raid toolbox.")
