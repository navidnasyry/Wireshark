import pyshark
from datetime import datetime
import time
import math
import numpy as np
from matplotlib import pyplot as plt

# intrfaces : lo / eno2 / wlo1 / tun0 /

file = "./CaptureFile/file.cap"
#file_output = open(file, 'w')


def number_of_resend_files(file_path):
    cap = pyshark.FileCapture(file_path)

    print("debug--- in function")
    
    for i in cap:

        print(len(cap))
        print(i)

    return (len(cap), cap)

a = number_of_resend_files(file)
print(a[1])

'''
capture = pyshark.LiveCapture(interface='lo', 
                            bpf_filter= 'port 4040',
                            output_file= file)
                    


print("Capture Created...")
print("Sniffing...")
capture.sniff(timeout= 5) # 5 sec sniffing...:)
print("Sniff complete.\n")



for packet in capture.sniff_continuously(packet_count= 50):
#for packet in capture:
    print("arrived:")
    #print(packet)
       # adjusted output
    try:
        # get timestamp
        localtime = time.asctime(time.localtime(time.time()))
     
        # get packet content
        protocol = packet.transport_layer   # protocol type
        src_addr = packet.ip.src            # source address
        src_port = packet[protocol].srcport   # source port
        dst_addr = packet.ip.dst            # destination address
        dst_port = packet[protocol].dstport   # destination port


        if protocol == 'TCP' :
            pass

        elif protocol == 'UDP':
            pass

        else :
            pass


        print ("%s IP %s:%s <-> %s:%s (%s)" % (localtime, src_addr, src_port, dst_addr, dst_port, protocol))
    except :
        print("\nError ---------------------------------!!!\n")

        '''

'''

def number_of_resend_files(file_path):
    cap = pyshark.FileCapture(file_path, display_filter='tcp.analysis.retransmission')
    print("debug--- in function")
    
    return len(cap)
'''
    
