import pyshark
from datetime import datetime
import time
import math
import os


# intrfaces : lo / eno2 / wlo1 / tun0 /
time_of_sniffing = int(input("input time of sniffing : "))

file = "./CaptureFile/file.cap"
file_output = open(file, 'w')



capture = pyshark.LiveCapture(interface='lo', 
                            bpf_filter= 'port 4040',
                            output_file= file)



print("Capture Created...")
print("Sniffing...")
#capture.sniff(timeout= time_of_sniffing) # 10 sec sniffing...:)
#capture.sniff(timeout= 10)    ://
#print("Sniff complete.\n")    


# read from file :)
#capture.close()
#capture = pyshark.FileCapture(input_file= file)
#capture.set_debug(True)

file_output.close()

def number_of_resend_files(file_path):

    cap = pyshark.FileCapture(file_path, display_filter='tcp.analysis.retransmission')
    counter = 0
    #cap.set_debug(set_to= True)
    try: 
        for i in cap :
            counter +=1
    except:
        return counter

    return counter
    




#print()
#print("\n\nnumber of packet resend : "+str (number_of_resend_files(file)))




def main():

    number_of_resend= 0
    sum_of_length= 0
    counter = 0
    flag=0
    number_of_packets = 0

    #for packet in capture.sniff_continuously(packet_count= len(capture)):
    start_time = time.time()
    for packet in capture:
        #counter +=1
        #if counter == len(capture)-1:
            #break






        localtime = time.asctime(time.localtime(time.time()))
    
        # get packet content
        protocol = packet.transport_layer   # protocol type
        src_addr = packet.ip.src            # source address
        src_port = packet[protocol].srcport   # source port
        dst_addr = packet.ip.dst            # destination address
        dst_port = packet[protocol].dstport   # destination port

        sum_of_length += int(packet.length)      # sum of packet size







        if protocol == 'TCP' :
            flag= 1
        elif protocol == 'UDP':
            pass

        else :
            pass

        print("%s IP %s:%s ==>> %s:%s (%s)" % (localtime, src_addr, src_port, dst_addr, dst_port, protocol))

        number_of_packets += 1
        time_now = time.time()
        if time_now - start_time >= time_of_sniffing:
            break


    print("\n\n=============================================summary===========================================================\n\n")

    if flag == 1:
        number_of_resend= number_of_resend_files(file)

    bit_rate = sum_of_length / time_of_sniffing

    print("Number of all packets : {}\n".format(number_of_packets))

    print("Throwghput (sum of packets size / time of sniffing) = {} bits/sec\n".format(bit_rate))

    print("Namber of Packets Resend: {}\n".format(number_of_resend))


    #find timestamp of each packet
    
    
    



try:
    main()
    os._exit(1)
except:
    pass