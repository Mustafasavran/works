#!/usr/bin/python
import socket
import binascii
import struct
s=socket.socket(socket.PF_PACKET,socket.SOCK_RAW,socket.htons(0x0800))
while 1:
    eth=s.recvfrom(2048)
    eth1=eth[0][0:14]
    eth1=struct.unpack("!6s4s4s",eth1)
    print binascii.hexlify(eth1[0])+"--->"+binascii.hexlify(eth1[1])+"type: "+binascii.hexlify(eth1[2])
    eth2=eth[0][14:34]
    eth3=struct.unpack("!12s4s4s",eth2)
    print socket.inet_ntoa(eth3[1])+"---->"+socket.inet_ntoa(eth3[2])+"\n"
    
