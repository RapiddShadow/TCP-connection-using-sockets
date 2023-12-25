import socket
client_socke = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_Socket_Ip = '127.0.0.1'
Client_Socket_port = 12345
client_socke.connect((client_Socket_Ip, Client_Socket_port))
message = "Hello from client"                   #Client message that will go to server
encoded_message = message.encode('utf-8')

try:
    client_socke.send(encoded_message)

    data = client_socke.recv(1024)              #Data received by server
    
    
    print(str(data))
except:
    print("Server refused to connect because client IP is flagged") #This will print if client is blocked
    
client_socke.close()
    