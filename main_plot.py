
import numpy as np
import matplotlib.pyplot as plt
import json




def use_json_file():

    #open client file 
    with open('capture_client.json','r') as json_file_client:
        capture_client_dic = json.load(json_file_client)

    #open server file
    with open('capture_server.json','r') as json_file_server:
        capture_server_dic = json.load(json_file_server)




    sender_bitrate_list = []
    receiver_bitrate_list= []
    sender_timestamp_list= []
    receiver_timestamp_list= []
    sum_of_client_bitrate = 0
    sum_of_server_bitrate = 0

    #client is sender
    #server is client
    for packet in capture_client_dic['intervals']:
        bitrate = packet['streams'][0]['bits_per_second']
        time_bitrate = packet['streams'][0]['end']
        print("(Client) Bitrate : {}    End : {}".format(bitrate, time_bitrate))
        sender_bitrate_list.append(bitrate)
        sender_timestamp_list.append(time_bitrate)
        sum_of_client_bitrate += bitrate


    for packet in capture_server_dic['intervals']:
        bitrate = packet['streams'][0]['bits_per_second']
        time_bitrate = packet['streams'][0]['end']
        print("(Server) Bitrate : {}    End : {}".format(bitrate, time_bitrate))
        receiver_bitrate_list.append(bitrate)
        receiver_timestamp_list.append(time_bitrate)
        sum_of_server_bitrate += bitrate


    plt.plot(sender_timestamp_list, sender_bitrate_list, color= 'r', label= 'Client')
    #plt.plot([1,2,3,4,4,4,5], [10,20,30,40,40,40,50], color= 'r', label= 'Client')
    plt.ylabel('Bit Rates')
    plt.xlabel('Time')
    #plt.title('Client')
    

    plt.plot(receiver_timestamp_list, receiver_bitrate_list, color= 'g', label= 'Server')
    #plt.plot([1.5,2.5,3.5,4.5,4.5,4.5,5.5], [100,200,300,400,400,400,500], color= 'g', label= 'Server')

    plt.ylabel('Bit Rates')
    plt.xlabel('Time')
    #plt.title('Server')
    plt.legend()
    plt.show()







  

    ###########################################CLIENT
    
    protocol = capture_client_dic['start']['test_start']['protocol']
    intervals_list = capture_client_dic['intervals']
    number_of_packets = len(capture_client_dic)
    local_host = capture_client_dic['start']['connected'][0]['local_host']
    local_port = capture_client_dic['start']['connected'][0]['local_port']
    remote_host = capture_client_dic['start']['connected'][0]['remote_host']
    remote_port = capture_client_dic['start']['connected'][0]['remote_port']
    local_time = capture_client_dic['start']['timestamp']['time']
    #find average of speeds:)
    client_bitrate_avg = sum_of_client_bitrate / number_of_packets


    print(local_time)
    print("\n\n\nClient ===========================================================")
    print("({})  local host : {} , local port : {}  ==>> remote host : {} , remote port : {}\n".format(protocol, local_host, local_port, remote_host, remote_port))

    print("Number Of Packets : {}\n".format(len(intervals_list)))
    print("Average of Server BitRate : " + str(client_bitrate_avg))

    #############################################SERVER

    protocol = capture_server_dic['start']['test_start']['protocol']
    intervals_list = capture_server_dic['intervals']
    number_of_packets = len(capture_server_dic)
    local_host = capture_server_dic['start']['connected'][0]['local_host']
    local_port = capture_server_dic['start']['connected'][0]['local_port']
    remote_host = capture_server_dic['start']['connected'][0]['remote_host']
    remote_port = capture_server_dic['start']['connected'][0]['remote_port']
    local_time = capture_server_dic['start']['timestamp']['time']
    #find average of speeds:)
    server_bitrate_avg = sum_of_server_bitrate / number_of_packets


    print(local_time)
    print("\n\n\nServer ===========================================================")
    print("({})  local host : {} , local port : {}  ==>> remote host : {} , remote port : {}\n".format(protocol, local_host, local_port, remote_host, remote_port))

    print("Number Of Packets : {}\n".format(len(intervals_list)))
    print("Average of Server BitRate : " + str(server_bitrate_avg))


  




use_json_file()

