import socket
server_socke = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket_Ip = '127.0.0.1'
server_socket_port = 12345
server_socke.bind((server_socket_Ip,server_socket_port))
server_socke.listen(5)

blocked_addresses = ['127.0.0.1', '192.168.0.1', '127.1.1.1']       #Blocked IP addresses
while True:
    print("Server waiting for a connection")
    client_socke,address = server_socke.accept()
    
    print("client trying to connect from: ", address)
    
    if address[0] in blocked_addresses:                             #To check if client IP is blocked
            print("Firewall blocked the flagged IP ")
            print("Client Ip was found in blocked IP addresses")
            print("Server closing connection now")
            break
            
    while True:
        
        data = client_socke.recv(1024)
        if not data : break
        print("Connection to client successful")                    #Printing Connection successful if client is not blocked
        print("received message: ",data.decode("utf-8"))
        try:
            client_socke.send(bytes("Connection to server successful ", "utf-8"))   #Send client message after successful connection
        except:
            print("Exited")
    client_socke.close()
server_socke.close()