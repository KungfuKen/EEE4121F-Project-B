import socket
import time

router = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
router.bind(("localhost", 8100))
router_send = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
router_send.bind(("localhost", 8200))
router_mac = "05:10:0A:CB:24:EF"

server = ("localhost", 8000)

ip1 = "92.10.10.15"
mac1 = "32:04:0A:EF:19:CF"
ip2 = "92.10.10.20"
mac2 = "10:AF:CB:EF:19:CF"

router_send.listen(4)
client1 = None
client2 = None

transmission_threshold = 60
new_transmission_rate = 0

while (client1 == None or client2 == None ):
    client, address = router_send.accept()

    if(client1 == None):
        client1 = client
        print("Client 1 is online")
    
    elif(client2 == None):
        client2 = client
        print("Client 2 is online")
    
    
arp_table_socket = {ip1 : client1, ip2 : client2}
arp_table_mac = {ip1 : mac1, ip2 : mac2}

router.connect(server) 

while True:
    received_message = router.recv(1024)
    received_message =  received_message.decode("utf-8")
    source_mac = received_message[0:17]    
    destination_mac = received_message[17:34]    
    source_ip = received_message[34:45]    
    destination_ip =  received_message[45:56]    
    message = received_message[56:60]
    transmission_rate = int(received_message[60:])

    print("The packed received:\n Source MAC address: {source_mac}, Destination MAC address: {destination_mac}".format(source_mac=source_mac, destination_mac=destination_mac))    
    print("\nSource IP address: {source_ip}, Destination IP address: {destination_ip}".format(source_ip=source_ip, destination_ip=destination_ip))    
    print("\nMessage: " + message)

    if transmission_rate >= transmission_threshold:
        new_transmission_rate = transmission_rate//1.25
        new_transmission_rate = int(new_transmission_rate)
    else: 
        new_transmission_rate = 0

    ethernet_header = router_mac + arp_table_mac[destination_ip]    
    IP_header = source_ip + destination_ip 
    packet = ethernet_header + IP_header + message + str(new_transmission_rate) 
    destination_socket = arp_table_socket[destination_ip]
    destination_socket.send(bytes(packet, "utf-8"))

    time.sleep(2)