#! /usr/bin/python

from socket import *
 
UDP_IP = "192.168.0.38"
UDP_PORT = 50
MESSAGE = 'my message'

print "UDP target IP:", UDP_IP
print "UDP target port:", UDP_PORT

def calc_checksum(msg):
    total = 0
    for i in msg:
        total += ord(i)
    total = total % 128
    total += 128 # |0x80 -> +127
    return total

def prepare_msg(msg):
#    return msg + chr(calc_checksum(msg))
    return msg
wt_msg = prepare_msg(MESSAGE)
print wt_msg

cs = socket(AF_INET, SOCK_DGRAM)
cs.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
cs.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
cs.sendto(wt_msg, (UDP_IP, UDP_PORT))
