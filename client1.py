import socket
import time

if __name__ == "__main__":
    ip1 = "92.10.10.15"
    mac1 = "32:04:0A:EF:19:CF"
    #port = 1234

    router =("localhost", 8200)
    
    client1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(("localhost", 8080))
    time.sleep(1)
    client1.connect(router)

    while True:
        received_message = client1.recv(1024)    
        received_message = received_message.decode("utf-8")    
        source_mac = received_message[0:17]    
        destination_mac = received_message[17:34]    
        source_ip = received_message[34:45]    
        destination_ip =  received_message[45:56]
        message = received_message[56:60]
        transmission_rate = int(received_message[60:])
        transmission_rate = str(transmission_rate)

        sock.send(bytes(transmission_rate, "utf-8")) 
        print("\nPacket integrity:\ndestination MAC address matches client 1 MAC address: {mac}".format(mac=(mac1 == destination_mac)))    
        print("\ndestination IP address matches client 1 IP address: {mac}".format(mac=(ip1 == destination_ip)))    
        print("\nThe packed received:\n Source MAC address: {source_mac}, Destination MAC address: {destination_mac}".format(source_mac=source_mac, destination_mac=destination_mac))
        print("\nSource IP address: {source_ip}, Destination IP address: {destination_ip}".format(source_ip=source_ip, destination_ip=destination_ip))
        if transmission_rate == 0:
            print("\nNew transmission rate: Null")
        else:
            print("\nNew transmission rate: " + transmission_rate)
        print("\nMessage: " + message )

    #server.connect((ip1, port))