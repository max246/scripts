#!/usr/bin/env python
'''
Very helpful script to reset your usb port if you dont want to unplug it or from remote.

How to use it:
sudo python reset_usb.py <name device>
The name of the device is the one displayed by running the commnad lsusb


Source: http://askubuntu.com/a/591979

'''

import os
import sys
from subprocess import Popen, PIPE
import fcntl
driver = sys.argv[-1]
print "resetting driver:", driver
USBDEVFS_RESET= 21780

try:
    lsusb_out = Popen("lsusb | grep -i %s"%driver, shell=True, bufsize=64, stdin=PIPE, stdout=PIPE, close_fds=True).stdout.read().strip().split()
    bus = lsusb_out[1]
    device = lsusb_out[3][:-1]
    f = open("/dev/bus/usb/%s/%s"%(bus, device), 'w', os.O_WRONLY)
    fcntl.ioctl(f, USBDEVFS_RESET, 0)
except Exception, msg:
    print "failed to reset device:", msg
