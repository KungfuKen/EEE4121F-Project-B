import socket
import time

if __name__ == "__main__":

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("localhost", 8000))
    server.listen(2)

    serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serv.bind(('localhost', 8080))
    serv.listen(2)

    server_ip = "92.10.10.10"
    server_mac = "00:00:0A:BB:28:FC"
    #port = 1234
    router_mac = "05:10:0A:CB:24:EF"
    
    while True:
        client, addr = serv.accept()

        routerConnection, address = server.accept()
        if(routerConnection != None):
            print(routerConnection)
            break

    while True:
        ethernet_header = ""
        IP_header = ""

        
        #message = input("\nEnter the text message to send: ")
        destination_ip = input("Enter the IP of the client to send the message to:\n1. 92.10.10.15\n2. 92.10.10.20 \n")

        if(destination_ip == "92.10.10.15" or destination_ip == "92.10.10.20"):
            source_ip = server_ip
            IP_header = IP_header + source_ip + destination_ip
            source_mac = server_mac
            destination_mac = router_mac 
            ethernet_header = ethernet_header + source_mac + destination_mac

            starttime = time.time()
            transmission_rate = 10
            i = 0
            while i<15:
                time.sleep(100//transmission_rate)    
                packet = ethernet_header + IP_header + "byte" + str(transmission_rate)
                routerConnection.send(bytes(packet, "utf-8")) 
                print("\nTransmission rate = " + str(transmission_rate))
                transmission_rate = transmission_rate + 10 
                i = 1+i
                new_transmission_rate = client.recv(1024)
                new_transmission_rate = new_transmission_rate.decode("utf-8")
                new_transmission_rate = int(new_transmission_rate)
                #new_transmission_rate = new_transmission_rate[0:2]
                
                if new_transmission_rate > 0:
                    transmission_rate = new_transmission_rate
                    
        else:
            print("Wrong client IP inputted")    