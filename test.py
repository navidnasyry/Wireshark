import pyshark
from datetime import datetime
import time
import math
import numpy as np
from matplotlib import pyplot as plt


capture = pyshark.LiveCapture(interface='lo')
capture.sniff(timeout=5)
for packet in capture.sniff_continuously(packet_count=5):
    print('Joust arrived: {}'.format(packet))

# The script analyzes directly a PCAP trace
# Remember to include the filter in display_filter
# CF - 2019


###########################################
#
# DATA Traffic (code 1)
#
###########################################
'''https://linuxhint.com/building-your-own-network-monitor-with-pyshark/'''
'''https://stackoverflow.com/questions/57099396/continuously-capture-packets-in-pyshark'''
'''https://wiki.wireshark.org/CaptureFilters'''

'''
tc qdisc add dev eth0 root netem loss 10%
iperf3 -c 127.0.0.1 -p 4040 -t 60 -u -b 5G  
iperf3 -s -p 4040 
'''


print(type(capture))

#cap = pyshark.FileCapture('./compressed-trace.pcap',
                       #   display_filter="ip.src==10.16.0.2 && tcp.srcport==60204 && ip.dst==10.0.0.11 && tcp.dstport==5001")


# COUNT RETRANSMISSION PACKETS
capture = pyshark.LiveCapture(interface='en1', bpf_filter='ip and tcp port 443', display_filter='tcp.analysis.retransmission')
capture.sniff(timeout=50)

for packet in capture.sniff_continuously(packet_count=5):
  print ('Just arrived:', packet)




def pyshark_retran_packet(inputfile):
        capture = pyshark.FileCapture(inputfile, display_filter='tcp.analysis.retransmission')
        counter = 0
        for packet in capture:
            counter = counter + 1
         
        print ("Total number of retransmitted frames found = " + str(counter))
        

##################################3
ref = float(capture[0].sniff_timestamp)
# print (ref)

# dictionary to store in form of key-value the tuple (time/amount of data in the given time)
# and compute throughput

totPkt = 0
totData = 0


thr_dict = {}
print(type(capture))

xx = 0
for pkt in capture:
    xx +=1
    if xx == 100:
        break
    totData = totData + int(pkt.tcp.len)
    totPkt = totPkt + 1
    # print (pkt.sniff_timestamp," ", pkt.tcp.len)

    # * * * *  to check the time
    inDate=pkt.sniff_time
    d=datetime.strptime(str(inDate), "%Y-%m-%d %H:%M:%S.%f")
    print(time.mktime(d.timetuple()), " ", pkt.tcp.len)

    # doing the timediff from the first element to check time progress
    timediff = float(pkt.sniff_timestamp) - ref
    i, d = divmod(timediff, 1)
    print (i,pkt.tcp.len)

    # insertion in the dictionary: if the value does not exitst,
    # then we create the new tuple, otherwise we just sum the data field
    if i not in thr_dict:
        thr_dict[i] = int(pkt.tcp.len)
    else:
        thr_dict[i] += int(pkt.tcp.len)

# printing the dictionary
for key, value in thr_dict.items():
    print(key, value)

# plot
keys = np.fromiter(thr_dict.keys(), dtype=float)
vals = np.fromiter(thr_dict.values(), dtype=float)
data = (((vals * 8) / 1024) / 1024)
timeinterval = keys / 1
plt.plot(timeinterval, data)

plt.xlabel("Time (s)", fontsize=20)
plt.ylabel("Throughput (Mbit/s)", fontsize=20)

plt.show()

# print("Tot pkt - tot data",totPkt,totData)
