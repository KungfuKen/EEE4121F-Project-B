import socket
import time

if __name__ == "__main__":
    ip2 = "92.10.10.20"
    mac2 = "10:AF:CB:EF:19:CF"
    #port = 1234

    router =("localhost", 8200)
    
    client2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    time.sleep(1)
    client2.connect(router)

    while True:
        received_message = client2.recv(1024)    
        received_message = received_message.decode("utf-8")    
        source_mac = received_message[0:17]    
        destination_mac = received_message[17:34]    
        source_ip = received_message[34:45]    
        destination_ip =  received_message[45:56]    
        transmittion_rate = int(received_message[56:58])  
        message = received_message[58:] 
        print("\nPacket integrity:\ndestination MAC address matches client 1 MAC address: {mac}".format(mac=(mac2 == destination_mac)))    
        print("\ndestination IP address matches client 1 IP address: {mac}".format(mac=(ip2 == destination_ip)))    
        print("\nThe packed received:\n Source MAC address: {source_mac}, Destination MAC address: {destination_mac}".format(source_mac=source_mac, destination_mac=destination_mac))
        print("\nSource IP address: {source_ip}, Destination IP address: {destination_ip}".format(source_ip=source_ip, destination_ip=destination_ip))
        print("\nMessage: " + message)
